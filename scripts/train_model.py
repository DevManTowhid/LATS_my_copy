from transformers import PegasusForConditionalGeneration, PegasusTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load pre-trained PEGASUS model and tokenizer
model_name = "google/pegasus-large"  # Use the PEGASUS model from Hugging Face
model = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer = PegasusTokenizer.from_pretrained(model_name)

# Load the dataset (you can replace with your custom dataset if needed)
dataset = load_dataset("cnn_dailymail", "3.0.0")

# Tokenize the dataset (adapt the input format for PEGASUS)
def tokenize_function(examples):
    return tokenizer(examples['article'], padding="max_length", truncation=True, max_length=1024)

# Apply tokenization to both the training and validation datasets
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set up the training arguments based on the paper (e.g., learning rate, batch size)
training_args = TrainingArguments(
    output_dir='./results',             # Directory to save model and logs
    evaluation_strategy="epoch",        # Evaluate after each epoch
    per_device_train_batch_size=2,      # As per the paper
    num_train_epochs=3,                 # Number of epochs to fine-tune
    logging_dir='./logs',               # Directory for logs
    learning_rate=5e-4,                 # Learning rate from the paper
    save_steps=500,                     # Save checkpoint every 500 steps
    max_steps=50000,                    # Total fine-tuning steps
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
)

# Start the training process
trainer.train()
