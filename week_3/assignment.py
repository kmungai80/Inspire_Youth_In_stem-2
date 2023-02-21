

favourite_musicians = ["dababy", "polo g", "drake", "21 savage", "rema"]
list_1 = favourite_musicians
for musician in favourite_musicians:
    print(musician)

favourite_musicians.append("cardi b")
favourite_musicians.append("dax")
favourite_musicians.append("j cole")
favourite_musicians.append("playboy carti")
favourite_musicians.append("lil tjay")
for musician in favourite_musicians:

    print(musician)

celebs = favourite_musicians.copy()
print(celebs)
celebs.sort()
print(celebs)

celebs.pop()
celebs.pop()
print(celebs)


print(len(celebs))

for celeb in list_1:
    list_1.append(celeb)
    print(list_1)
