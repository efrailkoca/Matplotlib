from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


slices = [60,40,30,20]																			# yüzdeleri gösterdik.
labels = ["sixty", "forty", "extra1", "extra2"]													# dilimlere isim vermek için.
colors = ["blue", "red", "yellow", "green"]														# dilimlerin renklerini belirlemek için.

plt.pie(slices, labels=labels, colors=colors, wedgeprops={"edgecolor": "black"})				# dairenin içine aldık.
# wedgeprops => kenar rengini belirlemek için.


# plt.pie([50,50])			# diğer bir yol

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f