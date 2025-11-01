from transformers import pipeline
classifier = pipeline('sentiment-analysis', model='xlm-roberta-base')
result = classifier("I love using transformers library!")
print(result)