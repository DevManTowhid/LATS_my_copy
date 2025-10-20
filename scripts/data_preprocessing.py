# data_preprocessing.py
import nltk
from nltk.tokenize import word_tokenize

# Example of text preprocessing (tokenization)
nltk.download('punkt')

def preprocess_data(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    return tokens

# Example usage
text = "This is a sample text to preprocess."
processed_text = preprocess_data(text)
print(f"Processed text: {processed_text}")
