
from transformers import pipeline

def fill_mask(text_with_mask):
    """
    Fills a mask in a sentence using the xlm-roberta-base model.

    Args:
        text_with_mask (str): The text with a <mask> token.

    Returns:
        list: A list of predictions for the masked word.
    """
    try:
        nlp_fill_mask = pipeline("fill-mask", model="xlm-roberta-base")
        result = nlp_fill_mask(text_with_mask)
        return result
    except Exception as e:
        return [{"error": str(e)}]

if __name__ == '__main__':
    # Example usage
    text = "The capital of France is <mask>."
    result = fill_mask(text)
    for pred in result:
        print(f"Prediction: {pred['sequence']} (score: {pred['score']:.3f})")
