from transformers import pipeline
classifier = pipeline ("sentiment-analysis", blanchefort/rybert-base-cased-sentiment")
classifier ("I like engeneering of machine learning")
