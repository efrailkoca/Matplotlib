
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]		# her bir sembole farklı bir renk vermek için.
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
		 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]				# her bir sembole farklı bir boyut vermek için.

plt.scatter(x, y, s=sizes, c=colors, cmap="Greens", marker="X", edgecolor="black", linewidth=1, alpha=0.5)	# cmap => bir rengin farklı tonlarını vermek için.
# s => sembolün boyutunu değiştirmek için.		c => color 		marker => sembolü değiştirmek için.		alpha => sembolün renginin baskınlığını belirlemek için
# linewidth => kenar çizgisinin büyüklüğünü değiştirmek için.

cbar = plt.colorbar()			# renk tonlarının kalınlığını göstermek için.
cbar.set_label("satisfaction")



# data = pd.read_csv('2019-05-31-data.csv')
# view_count = data['view_count']
# likes = data['likes']
# ratio = data['ratio']

# plt.title('Trending YouTube Videos')
# plt.xlabel('View Count')
# plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()