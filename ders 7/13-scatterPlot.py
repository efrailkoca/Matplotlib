import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')



data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']


plt.scatter(view_count, likes, c=ratio, cmap="summer", edgecolor="black", linewidth=1, alpha=0.5)

cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")

plt.xscale("log")	# on üssü şeklinde gösteriyor. 
plt.yscale("log")

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')


plt.tight_layout()

plt.show()