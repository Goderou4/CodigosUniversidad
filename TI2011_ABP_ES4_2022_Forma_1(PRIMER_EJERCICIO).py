#a)
videojuegos = []
#b)
for i in range(0,5):
  name = input("ingrese un videojuego: ").upper()
  videojuegos.append(name)

#c)
#print(videojuegos)
#d)
print("{}, {}".format(videojuegos[0],videojuegos[4]))
#e)
for name in videojuegos:
  print(name)
#f)
videojuegos.insert(2, ["NBA2K"])
#g)
print(videojuegos)
#h)
name = input("ingrese un nuevo videojuego: ")
videojuegos.insert(0, name)
for name in videojuegos:
  print(name)
#i)
print(videojuegos)
#j)
videojuegos.pop([-10])
