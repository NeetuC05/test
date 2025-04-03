!pip install transformers torch
!pip install keras
from transformers import pipeline

#INTIALIZE THE QA PIPELINE
qa_pipeline= pipeline('question-answering')

#define the context(the doc where the answer will be extracetd from)
context="""
Mount Everest is the highest mountain on Earth, with a peak that reaches 8,848.86 meters(29,031.7 feet) above sea level.
It is located in the Himalayas on the border between Nepal and the Tibet Autonomous Region of China
"""

#define the question
question='What is the height of Mount Everest?'

#use pipeline to extract the answer
result=qa_pipeline(context=context,question=question)

#print the extracted answer
print(f'Answer: {result["answer"]}')
