# 1) У вас є список my_list із значеннями типу int.
# Роздрукувати значення, які більше 100.
# Завдання виконати за допомогою циклу for.
print("1ST TASK")

list1 = [12, 432, 664, 79, 101]

for val in list1:
    if val > 100:
        print (val)
#############################################################################
# 2) У вас є список my_list зі значеннями типу int і порожній список my_results.
# Додати my_results ті значення, які більше 100.
# Роздрукувати список my_results.
# Завдання виконати за допомогою циклу for.
print("")
print("2ND TASK")

list2 = []
newlist2 = []

while True:
    try:
        print("Введіть будь яке число:")
        print("(Або Exit для виходу)")
        list1val = input("Відповідь: ")
        if list1val.lower() == "exit":
            break
        list2.append(int(list1val))
    except ValueError:
        print("Ви ввели не число.")
print(f"Ваші числа: {list2}")

for val in list2:
    if val > 100:
        newlist2.append(val)
print(f"З них більше 100: {newlist2}")
# ################################################################################
# 3) У вас є список my_list із значеннями типу str. Створити новий список до якого помістити
# елементи з my_list за таким правилом:
# Якщо строка стоїть на непарному місці my_list, то її замінити на обернену строку (Наприклад "qwe" на "ewq")
# Якщо на парному – залишити без зміни.
# Завдання зробити за допомогою циклу for та функції enumerate.
print("")
print("3RD TASK")

list3 = []
newlist3 = []

while True:
    print("Введіть будь що:")
    print("Exit - для виходу")
    list1val = input("Відповідь: ")
    if list1val.lower() == "exit":
        break
    list3.append(str(list1val))
print(f"Ваші введення: {list3}")

for idx, val in enumerate(list3, start = 1):
    if idx % 2 != 0:
        newlist3.append(val[::-1])
    else:
        newlist3.append(val)
print ("Отримана строка (всі непарні слова перевернуті): ")
print (newlist3)
# ################################################################################
# 4) У вас є рядок my_string = '0123456789'.
# Згенерувати цілі числа (тип int) від 0 до 99 і помістити в список.
# Завдання потрібно виконати ТІЛЬКИ через цикл у циклі (Див. Приклад вище) і зведення типів !!!
# Генерування через range або інші "фішки" я не зараховуватиму ))
print("")
print("4TH TASK")

list4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist4 = []
res = ""

for symb1 in list4:
    for symb2 in list4:
        if symb1 == 0:
            res = str(symb2)
        else:
            res = str(symb1) + str(symb2)
        newlist4.append(int(res))

print(newlist4)