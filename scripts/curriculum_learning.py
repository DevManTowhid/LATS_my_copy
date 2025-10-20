# scripts/curriculum_learning.py

import random

def sort_samples_by_complexity(samples):
    """
    Sorts the text-summary pairs based on their calculated complexity score.
    """
    return sorted(samples, key=lambda x: x['complexity'])

def create_buckets(samples, num_buckets=5):
    """
    Divides the sorted data into k buckets for curriculum learning.
    """
    bucket_size = len(samples) // num_buckets
    buckets = [samples[i:i + bucket_size] for i in range(0, len(samples), bucket_size)]
    return buckets

# Example usage
samples = [{"text": "Sample text", "summary": "Sample summary", "complexity": 0.8}, 
           {"text": "Another sample", "summary": "Another summary", "complexity": 0.4}]

sorted_samples = sort_samples_by_complexity(samples)
buckets = create_buckets(sorted_samples)
print(f"Buckets: {buckets}")
