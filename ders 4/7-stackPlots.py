from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]			# kaçıncı dakikada kaç puanda olduklarını göstermek için.
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ["player1", "player2", "player3"]
colors = ["#6d904f", "#fc4f30", "#008fd5"]

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)


plt.legend(loc="upper left")				# loc(location) => label ın yerini belirlemek için.
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f