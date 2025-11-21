
from transformers import pipeline

def answer_question(question, context):
    """
    Answers a question based on a given context using the xlm-roberta-base model.

    Args:
        question (str): The question to answer.
        context (str): The context to find the answer in.

    Returns:
        dict: The result from the question-answering pipeline.
    """
    try:
        classifier = pipeline('question-answering', model='xlm-roberta-base')
        result = classifier(question=question, context=context)
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    # Example usage
    question = "What is the capital of France?"
    context = "Paris is the capital and most populous city of France."
    result = answer_question(question, context)
    print(result)
