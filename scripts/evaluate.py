from rouge_score import rouge_scorer
import json
import os

# Function to evaluate using ROUGE
def evaluate_summaries(generated_summaries, reference_summaries):
    # Initialize the ROUGE scorer
    scorer = rouge_scorer.RougeScorer(
        metrics=['rouge1', 'rouge2', 'rougeL'], # We use ROUGE-1, ROUGE-2, and ROUGE-L
        use_stemmer=True
    )
    
    # List to store ROUGE scores for each pair of generated and reference summaries
    rouge_scores = []

    for gen_summary, ref_summary in zip(generated_summaries, reference_summaries):
        scores = scorer.score(ref_summary, gen_summary)
        rouge_scores.append(scores)
    
    return rouge_scores

# Function to compute combined ROUGE F1 score
def compute_combined_rouge(rouge_scores):
    rouge_1_f1 = 0
    rouge_2_f1 = 0
    rouge_l_f1 = 0
    num_scores = len(rouge_scores)

    for score in rouge_scores:
        rouge_1_f1 += score['rouge1'].fmeasure
        rouge_2_f1 += score['rouge2'].fmeasure
        rouge_l_f1 += score['rougeL'].fmeasure

    # Compute combined ROUGE F1 score based on the paper's weighted formula
    combined_rouge_f1 = rouge_1_f1 + 2 * rouge_2_f1 + rouge_l_f1
    combined_rouge_f1 = (combined_rouge_f1 / (num_scores)) * 100  # Scaling the score for readability
    
    return combined_rouge_f1

# Main function to load generated and reference summaries and evaluate
def main():
    # Path to the directories where summaries are stored
    generated_summaries_path = './generated_summaries.json'  # Modify as needed
    reference_summaries_path = './reference_summaries.json'  # Modify as needed

    # Load the generated and reference summaries from JSON files
    with open(generated_summaries_path, 'r') as f:
        generated_summaries = json.load(f)
    
    with open(reference_summaries_path, 'r') as f:
        reference_summaries = json.load(f)

    # Evaluate the generated summaries using ROUGE
    rouge_scores = evaluate_summaries(generated_summaries, reference_summaries)

    # Compute combined ROUGE F1 score
    combined_rouge_f1 = compute_combined_rouge(rouge_scores)

    # Print the results
    print(f"Combined ROUGE F1 score: {combined_rouge_f1:.2f}")

if __name__ == "__main__":
    main()
