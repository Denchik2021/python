new_list = [57.8, 46.51, 97, 1, 65.5, 102, 178, 205, 590, 654.3]
price = []

for el in new_list:
    roubles = int(el)
    kop = round((el - roubles) * 100)
    price.append(f"{roubles} руб {kop:02d} коп")
print(", ".join(price))
id1 = id(new_list)
new_list.sort()
print(new_list)
print(id(new_list) == id1)
my_list = sorted(new_list, reverse=True)
print(sorted(my_list[:5]))



