import json
import csv

"""
Задание 1. Декодировать в строку байтовое значение.
Затем результат преорбразовать в байтовый вид в кодировке Latin1.
Затем результат снова декодировать в строку.
"""
text = b'r\xc3\xa9sum\xc3\xa9'
decoded_string = text.decode()
print(type(decoded_string))
print(decoded_string)

new_text = decoded_string.encode("latin1")
print(new_text)

new_decoded_string = new_text.decode("latin1")
print(type(new_decoded_string))
print(new_decoded_string)

"""
Задание 2. Ввести 4 строки и сохранить их в 4 разные переменные.
Создать файл, записать в него первые 2 строки и закрыть файл.
Открыть файл на редактирование и дописать оставшиеся 2 строки.
"""
str_1 = "Здравствуйте!"
str_2 = "\nДавайте познакомимся."
str_3 = "\nМеня зовут Александр."
str_4 = "\nА как зовут Вас?"

with open("../my_file.txt", "w", encoding="utf-8") as file:
    print(file.write(str_1 + str_2))

with open("../my_file.txt", "a", encoding="utf-8") as file:
    print(file.write(str_3 + str_4))

"""
Задание 3. Создать словарь, в котором ключ - 6-ти значное число (id),
значение - кортеж из 3-х элементов - имя (str), возраст(int), телефон(int).
Сделать 5-6 элементов словаря и записать в json-файл.
"""
dict_a = {
    187406: ("Alena", 45, 80295647986),
    194830: ("Vitalya", 38, 80336242257),
    142858: ("Alejandro", 42, 80297880975),
    194735: ("Katerina", 31, 80442569856),
    174376: ("Maria", 35, 80256429684),
    135793: ("Oleg", 30, 80297324975)
}
print(dict_a)

with open("../data.json", "w") as file:
    json.dump(dict_a, file)

with open("../data.json", "r") as file:
    dict_a = file.readline()

"""
Задание 4. Прочитать вышеуказанный json-файл и записать в csv-файл,
первой строкой озаглавив каждый столбец и добавив столбец "телефон".
"""
columns = ["id", "name", "age", "telephone"]
dict_a = json.loads(dict_a)
with open("../csv_data.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=columns, restval="ignore")
    writer.writeheader()
    writer.writerow(dict_a)


