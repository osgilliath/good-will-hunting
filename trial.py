from transformers import pipeline

# Load the fill-mask pipeline with XLM-RoBERTa base
nlp_fill_mask = pipeline(
    "fill-mask",
    model="xlm-roberta-base"
)

# Give an input sentence with the <mask> token
result = nlp_fill_mask("Engineering is a <mask> career choice.")

# Display the top predictions for the masked word
for pred in result:
    print(f"Prediction: {pred['sequence']} (score: {pred['score']:.3f})")
