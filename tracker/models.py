from django.db import models

class Expense(models.Model):
    CATEGORIES = (
        ('groceries', 'Groceries'),
        ('utilities', 'Utilities'),
        ('travel', 'Travel'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    )
    image = models.ImageField(upload_to='receipts/')
    text = models.TextField(blank=True)  # OCR-extracted text
    amount = models.FloatField(null=True)  # Extracted amount
    category = models.CharField(max_length=20, choices=CATEGORIES, default='other')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
