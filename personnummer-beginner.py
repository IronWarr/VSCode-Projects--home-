#Start

person_1 = input("Roger: ")
person_2 = input("Rasmus: ")
person_3 = input("Birgitta: ")

my_list = [person_1, person_2, person_3]
my_list.sort()
print(my_list)

if person_1 < person_2:
  if person_1 < person_3:
    print("Roger är äldst")
  else:
    print("Birgitta är äldst")
elif person_2 < person_3:
  print("Rasmus är äldst")
else:
  print("Birgitta är äldst")