print("Task 1")
num_1 = 10897
num_2 = num_1
num_3 = num_2
print("id(num_1): ", id(num_1),
      "\nid(num_2): ", id(num_2),
      "\nid(num_3): ", id(num_3)
      )

print("Task 2")
list_1 = ["abc", 45]
list_2 = ["abc", 45]
print("id(list_1): ", id(list_1), "\nid(list_2): ", id(list_2))

print("Task 3")
num_2 = str
num_3 = float
print("id(num_1): ", id(num_1),
      "\nid(num_2): ", id(num_2),
      "\nid(num_3): ", id(num_3)
      )
num_4 = bool(489)
num_5 = bool(247)
print("id(num_4): ", id(num_4), "\nid(num_5): ", id(num_5))
list_1 = list_2
print("id(list_1): ", id(list_1), "\nid(list_1): ", id(list_1))

print("Task 4")
s = str(input("Enter any string: "))
print(s, "\n\n")
a = s[1::2]
b = s[::2]
print(a, "     ", b, "\n!!!")
