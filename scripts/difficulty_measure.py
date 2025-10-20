# scripts/difficulty_measure.py
from collections import Counter

def calculate_deletion(text, summary):
    """
    Computes the deletion complexity (words present in text but not in summary).
    """
    text_words = Counter(text.split())
    summary_words = Counter(summary.split())
    deletions = sum((text_words[word] - summary_words.get(word, 0)) for word in text_words)
    return deletions

def calculate_reordering(text, summary):
    """
    Computes the reordering complexity based on consecutive word sequences.
    """
    # This can be extended to compare word orderings in the text and summary
    return 0  # Placeholder for reordering complexity logic

def calculate_substitution(text, summary):
    """
    Computes the substitution complexity (words that are replaced by synonyms).
    """
    return 0  # Placeholder for substitution complexity logic

def calculate_addition(text, summary):
    """
    Computes the addition complexity (words added to the summary but not in the text).
    """
    return 0  # Placeholder for addition complexity logic

# Example usage
text = "This is a simple text."
summary = "This simple text."
deletions = calculate_deletion(text, summary)
print(f"Deletions: {deletions}")
