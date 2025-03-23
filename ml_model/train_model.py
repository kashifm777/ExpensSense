import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample data (replace with real dataset or expand)
data = {
    'text': ['milk bread eggs', 'electricity bill', 'train ticket', 'movie popcorn', 'miscellaneous'],
    'category': ['groceries', 'utilities', 'travel', 'entertainment', 'other']
}
df = pd.DataFrame(data)

# Train model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df['text'], df['category'])

# Save model
joblib.dump(model, 'ml_model/expense_model.pkl')
print("Model trained and saved!")