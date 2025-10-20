# scripts/evaluate.py
from rouge_score import rouge_scorer

def evaluate_summary(reference, generated):
    """
    Evaluates the model's summary using ROUGE F1 score.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, generated)
    return scores

# Example usage
reference = "This is a reference summary."
generated = "This is a generated summary."
scores = evaluate_summary(reference, generated)
print(f"ROUGE-1: {scores['rouge1']}, ROUGE-2: {scores['rouge2']}, ROUGE-L: {scores['rougeL']}")
