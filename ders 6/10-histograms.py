import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10,20,30,40,50,60]
# kutuların hangi değerler arasında olacağını belirledik => 10-20 , 20-30 ...

plt.hist(ages, bins=bins, edgecolor="black")


# plt.hist(ages, bins=5, edgecolor="black")				# bins için diğer bir yol.
# plt.hist => histogram oluşturmak için. 	bins => kaç tane. farklı sütun olmasını istiyorsak onu belirtmek için. 	  edgecolor => kenar rengi için.

# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# ages = data['Age']

# median_age = 29
# color = '#fc4f30'

# plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()