import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")



with open("data.csv") as csv_file:
	csv_reader = csv.DictReader(csv_file)

	language_counter = Counter()

	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(";"))		# kullanılan dilleri saymak için kullandık.

'''	row = next(csv_reader)
	print(row['LanguagesWorkedWith'].split(";"))			# 'LanguagesWorkedWith' bu bir (anahtar)key ' dir.
	# ilk önce anahtar olmadan çalıştırıp anahtarı çıktıdan öğrenebiliyoruz.
'''	# split ile birlikte ayırma işareti noktalı virgülden değiştirdik. split kullanmadan önce noktalı virgül ile ayrılmışlardı.

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

print(languages)
print(popularity)



print(language_counter.most_common(15))			# most_common metodu => en fazla olan 15 tanesini yazdırmak için kullandık.

# plt.title("Median Salary (USD) by Age")
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")

# plt.tight_layout()

# plt.show()