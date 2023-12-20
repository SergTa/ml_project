!usr/bin/python3

from transformers import pipeline
classifier = pipeline ("sentiment-analysis", blanchefort/rybert-base-cased-sentiment")

classifier ("    программную инженерию")
