import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
	language_counter.update(response.split(";"))

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])


languages.reverse()						# reverse() => tersine çevirmek için.
popularity.reverse()

plt.barh(languages, popularity)			# plt.barh => sütunları yatay hale getirmek için kullanılır.

plt.title("Most Popular Languages")
plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()