from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]


plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct="%1.1f%%", wedgeprops={"edgecolor": "black"})
# explode => bir dilimi diğerlerine göre çıkıntılı göstermek için.
# shadow=True => dilimler, 3 boyutlu gibi gösteriyor.
# strartangle => grafiği derece cinsinden döndürmek için.
# autopct => dilim büyüklüklerini ondalıklı olarak daha detaylı gösterir.



plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()