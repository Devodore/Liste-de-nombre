import random

debut = 0
fin = 20
limite = 50

Table = [random.randint(debut, fin) for iter in range(limite)]
Table.sort()
for i in range(21):
  Table.count(i)
  nombre = Table.count(i)
  phrase = "Il y a {} éléments pour la note {}".format(nombre, i)
  print (phrase)