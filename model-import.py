from transformers import pipeline
classifier = pipeline('question-answering', model='xlm-roberta-base')
result = classifier(question="What is the purpose of the transformers library?", context="  The transformers library provides state-of-the-art general-purpose architectures for natural language understanding and generation.")
print(result)