from matplotlib import pyplot as plt

plt.xkcd()                                     # çizgi roman grafiği gibi yapar.

print(plt.style.available)                     # bu bir method değil, bu bir özellik. uygun style ları gösterir.
plt.style.use("fivethirtyeight")               # grafiğin stilini değiştiriyor. uygun stilleri üstteki satır ile görebiliyoruz.
# fivethirtyeight => bu bir style örneği

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color="k", linestyle="--", marker=".", label="All Devs")                      # grafik oluşturmak için kullanılır. 1. yazılan x ekseni, 2. yazılan y ekseni
# label ile doğrunun ismini belirledik.     color ve linestyle doğrunun rengini ve şeklini değiştirir. bu yol diğer yola göre daha okunabilir.
# marker doğru üzerinde işaretlemeler yapmak için kullanılır.
# siyah için hex gösterimi => #444444      mavi için hex gösterimi => #5a7d9a       yeşil için => #adad3b

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, "b", linewidth=3, marker="o", label="Python")                  # bir grafiğe bu şekilde birden fazla plot kullanarak birden fazla doğru çizgisi ekleyebiliriz.
# label ile doğrunun ismini belirledik.         doğrunun rengini ve şeklini değiştirmenin diğer yolu.
# linewidth doğrunun kalınlığını ayarlıyor.

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color="#adad3b", linewidth=3, label="JavaScript")

plt.xlabel("Ages")                          # x ekseni için başlık.
plt.ylabel("Median Salary (USD)")           # y ekseni için başlık.
plt.title("Median Salary (USD) by Age")     # grafiğe başlık olması için.
plt.legend()                                # label kullansak da çalışması için bu şekilde legend eklenmeli.

#plt.legend(["All Devs", "Python"])          # doğru çizgilerini belirlemek için. 1. yazılan birinci değerleri gösterir, 2. yazılan ikinci değerleri gösterir.
# bu yolu kullanmaktansa label olanı kullanmak daha iyi.

plt.grid(True)                              # grafiği ızgaralı şekle getirmek için kullanılır.
plt.tight_layout()                          # linewidth ile kalınlığı değiştirdiğimizde dolguyu daha da netleştirme işine yarıyor.

plt.savefig("plot.png")                     # oluşturduğumuz grafiği olduğum klasörün içine ekler, parantez içindeki kısım fotoğrafın ismi.

plt.show()                                  # oluşturulan grafiği göstermek için.