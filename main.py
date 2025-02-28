from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("Give me a pseudo folder structure")

print(res)