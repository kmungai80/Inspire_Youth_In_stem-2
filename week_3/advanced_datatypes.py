#advanced datatypes

#mutable vs immutable

#mutable are datatypes thatcan change/edited during program life cycle
#add/remove element

#immutable --> datatypes that cannot be editedduring program lifecycle

#1 list(mutable)

friends = ["ken","melloz","sharon","strange master"]
# or friends =[] empty list
#add elements --> append(), extend()

students = ["ezekiel","gabriel","erick"]

friends.extend(students)
friends.append("benjamin")
friends.sort()
friends.reverse()
#remove elements --> pop(),del()
friends.pop()

#2 tuples(immutable)
stationaries = ("pens","ink","sharpener","steplar","rubber")

#you can replace the whole tuple
stationaries = ("ruler","clipboard","pins")

for stationary in stationaries:
    print(stationary)
#3 dictionaries aka dict

#use key and value pair to store data

student = {"name": "Ken", "age" : 24 ,"gender": "male"}

print(student["name"])
print(student["age"])
print(student["gender"])
print(student.values())
print(student.keys())

friend = {"fav_colour": "black", "hobby": "swimming", "course": "clinical med", "weight": "56kg", "height": "75cm"}

print(friend["fav_colour"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])
print(friend.values())
print(friend.keys())





#name(key) ken(value)

#sets