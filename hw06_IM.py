# ############################################################
# 1. Дан словник виду {str: int} (ключи - строки, значення - цілі числа).
# - Створити список ключів цього словнику
# - Створити список значень цього словнику
# - Порахувати суму числових значень цього словнику
print("1ST TASK")

robot = {
    "model": 14,
    "age": 52,
    "number":88
        }

keys = []
for key in robot:
    keys.append(key)

print("Ключі: ", keys)

sum = 0
vals = []
for val in robot.values():
    vals.append(val)
    sum += int(val)

print("Значення: ", vals)
print("Сума значеннь: ", sum)
# ########################################################################################
# 2. Дан словник виду {str: str} (ключи - строки, значення - строки)
# - Створити список з унікальних значень цього словнику
# - Створити строку з унікальних значень цього словнику. У якості роздільника взяти символ ___
print("2ND TASK")

robot1 = {
    "model": "r0261",
    "age": "fifty five",
    "index": "r0261",
    "language": "english"
        }

newvals = ""
uniques = []
for val in robot1.values():
    if val not in uniques:
        uniques.append(val)

newvals = "___".join(uniques)

print("Список значеннь: ", uniques)
print("Строка значеннь: ", newvals)
# ###################################################################################
# 3. Дано два списка строк однакової довжини. Створити словник з ключами із першого списка і значеннями із другого.
print("3RD TASK")

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
robot3 = {}

for i in range(len(list1)):
    robot3[list1[i]] = list2[i]

print(robot3)
# ########################################################################################
# 4. Дано два списка строк однакової довжини. Строки в першому списку строки можуть бути однакові.
# Створити словник з ключами із першого списка і значеннями із другого.
# У разі повторення ключа - створити ключ з додатковим числовим суфіксом, що  відповідає номеру ключа.
# Приклад:
# Дано: ["a", "b", "c", "a", "a", "c"] та [1, 2, 3, 4, 5, 6]
# Очікуванний результат: {"a": 1, "b": 2, "c": 3, "a2": 4, "a3": 5, "c2": 6}
print("4TH TASK")

list1 = ["a", "b", "c", "a", "a", "c"]
list11 = []
list2 = [1, 2, 3, 4, 5, 6]
robot4 = {}
counts = {}

for i in range(len(list1)):
    if list1[i] in robot4.keys():
        if list1[i] in counts:
            counts[list1[i]] += 1
        else:
            counts[list1[i]] = 1
        list1[i] = f"{list1[i]}{counts[list1[i]]}"
        robot4[list1[i]] = list2[i]
    else:
        robot4[list1[i]] = list2[i]
        if list1[i] in counts:
            counts[list1[i]] += 1
        else:
            counts[list1[i]] = 1

print(robot4)