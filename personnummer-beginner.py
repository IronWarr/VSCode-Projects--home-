#Start

person1 = input("Personnummer ")
person2 = input("Personnummer ")
person3 = input("Personnummer ")

person1 = person1.strip()
person2 = person2.strip()
person3 = person3.strip()

if len(person1) > 6:
    person1 = person1[2:8]

print(person1)

if len(person2) > 6:
    person2 = person2[2:8]

print(person2)

if len(person3) > 6:
    person3 = person3[2:8]

print(person3)