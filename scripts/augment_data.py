# augment_data.py
import random
from nltk.corpus import wordnet
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Synonym Replacement (SR) for data augmentation
def synonym_replacement(sentence):
    words = nltk.word_tokenize(sentence)
    new_words = words.copy()
    
    for i, word in enumerate(words):
        synonyms = wordnet.synsets(word)
        if synonyms:
            synonym = random.choice(synonyms).lemmas()[0].name()
            new_words[i] = synonym if synonym != word else word
    return " ".join(new_words)

# Example usage
sentence = "This is a simple sentence for testing."
augmented_sentence = synonym_replacement(sentence)
print(f"Original: {sentence}")
print(f"Augmented: {augmented_sentence}")
