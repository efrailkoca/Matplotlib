import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

'''plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries>overall_median), interpolate=True, alpha=0.25)     
# 2. yazılanın altındaki alanı boyuyor. alpha => boyamanın kalınlığını değiştiriyor.
# overall_median ile birlikte boyanacak kısmın yerini 57287 olarak belirledik.
# where => bunu kullanarak py_salaries ' in overall_median dan büyük olduğu kısmı boyattık. interpolate ile daha doğru bir boyama oldu. eğer anlamazsan interpolate olmadan çalıştır anlarsın.

plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries<=overall_median), interpolate=True, color="red", alpha=0.25)
# bununla da overall_media nın altında kalan kısmı boyattık ve rengini değiştirdik.'''

# üstteki yorum satırı doğru ile istediğimiz kısmın arasını boyuyordu.

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries>dev_salaries), interpolate=True, alpha=0.25, label="Above Average")

plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries<=dev_salaries), interpolate=True, color="red", alpha=0.25, label="Below Average")
# bu iki satır ile iki doğrunun arasındaki kısımları boyadık.


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()