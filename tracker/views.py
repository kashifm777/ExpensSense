from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Expense
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image
import joblib
import re

# Load ML model
model = joblib.load('ml_model/expense_model.pkl')

def upload_receipt(request):
    if request.method == 'POST' and request.FILES['receipt']:
        receipt = request.FILES['receipt']
        fs = FileSystemStorage()
        filename = fs.save(receipt.name, receipt)
        file_path = fs.path(filename)

        # OCR extraction
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

        # Extract amount (basic regex for demo)
        amount_match = re.search(r'\$\d+\.\d{2}', text) or re.search(r'\d+\.\d{2}', text)
        amount = float(amount_match.group().replace('$', '')) if amount_match else 0.0

        # Predict category
        category = model.predict([text])[0]

        # Save to database
        expense = Expense(image=filename, text=text, amount=amount, category=category)
        expense.save()
        return redirect('dashboard')
    
    return render(request, 'tracker/upload.html')

def dashboard(request):
    expenses = Expense.objects.all()
    category_totals = expenses.values('category').annotate(total=models.Sum('amount'))
    context = {
        'expenses': expenses,
        'category_totals': category_totals,
    }
    return render(request, 'tracker/dashboard.html', context)
