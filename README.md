## good-will-hunting

**(A Work in Progress Project)** <br/>
A tool that is more like your assistant in examinations, the goal is to create a program in which you can upload previous year papers of your university, your syllabus and the program can help you find the recurring questions and topics they are from.

But this shit will take time, so have patience, I'll try to complete this before my semester examination.

This stuff's harder than I thought.

## Files- and what they do (for now)
- _model-import.py_ - importing and testing different models from hugging face, and trying what different pipelines do, to select the definitive one
- _text-scanner.py_ - prompts you to select a file and reads text from it, no matter the format, img or pdf.
- _prediction.py_ - predicts a masked word in ypur given sentence.
- **(Removed)**  _img-to-text.py_ - reading text from .jpg or .png file (so that we can extract text from images in the program as well)
- **(Removed)** _pdf-to-text.py_ - reading text from .pdf file.


## Features list

1. Analyse questions, that are being repeated.
2. Even questions that are paraphrased, but are the same.
3. Analyse the syllabus, and tells what topic the questions belong to.
4. Tell you what questions are being repeated, and what topic they are from.

## Maybe possible features

1. Trained on certain subjects and tells the answers to that questions.
2. Maybe pulls the answers to that particular questions from the internet.
3. So a complete guide.

## Brainstorming

Instead of training the model with language and stuff just have an inbuilt that is pre trained and does all the work by itself, and try to make it offline.

HEY THERE! if you're reading this and have some suggestions or want to help, feel free to contact me through mail.<br/>
[![Gmail Badge](https://img.shields.io/badge/-shankhdhar.madhav@gmail.com-c14438?style=social&logo=Gmail&logoColor=red&link=mailto:shankhdhar.madhav@gmail.com)](mailto:shankhdhar.madhav@gmail.com)
