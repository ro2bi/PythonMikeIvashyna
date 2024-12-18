#################################################
#1. Дано ціле число (int). Порахувати скільки нулів в цьому числі.
n = int(input("Введіть ціле число: "))
orign = n
count = 0;

while n != 0:
    num = n % 10;
    if num == 0:
        count += 1;
    n //= 10;
print (f"У числі {orign}, {count} нулів")
#####################################################
#2. Дано ціле число (int). Порахувати скільки нулів в кінці цього числа. Наприклад для числа 1002000 - три нулі
n = int(input("Введіть ціле число: "))
orign = n
count = 0;

for num in str(n):
    if num == "0":
        count += 1
    else:
        count = 0
    n //= 10
print (f"У числі {orign}, в кінці {count} нулів")
###############################################################################
#3. Дан список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший элемент з my_list
#стоїть на останньому месці в new_list. Якщо my_list [1,2,3,4], то new_list [2,3,4,1]
list1 = []
while (True):
    num = input("Введіть значення, які ви хтіли б побачити в списку (або Exit для виходу): ")
    if num.lower() == "exit":
        break
    list1.append(num)

list2 = list1[1:]
list2.append(list1[0])

print ("")
print (f"Початковий писок: {list1}")
print (f"Кінцевий писок: {list2}")
#################################################################################
#4. Дана строка в якій є числа (разділяються пробілами).
#Наприклад "43 більше за 34, але меньше за 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) в цій строкі.
#Для даного прикладу відповідь - 133. (використайте split и перевірку isdigit)
print("Введіть строку з будь якими числами.")
str = input()
digit = 0
allsum = 0

for num in str:
    if num.isdigit():
        digit = digit * 10 + int(num)
    else:
        allsum += digit
        digit = 0
allsum += digit

print(f"Сума всіх чисел у рядку = {allsum}")
##############################################################################################
# 5. Дана строка my_str. Разділіть цю строку на пари з двох символів и поместіть ці пари в список.
# Якщо строка має непарну кількість символів, останній символ останньої пари має
# бути підкресленням ('_'). Приклади: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (використовуйте зрізи довжиною 2 символи)
print ("Введіть строку з букв без пробілів.")
str1 = input()
str2 = ""

length = len(str1)
if length % 2 != 0:
    str1 += "_"

idx1 = -2
idx2 = 0

while idx2 != len(str1):
    idx1 += 2
    idx2 += 2
    str2 += f"{str1[idx1:idx2]} "

print(f"Пари з символів: {str2}")
# ###############################################################################################################
# 6. Дан список чисел. Порахуйте, скольки в цьому списку елементів,
# які більше за суму двох своїх сусідів (зліва и справа), и НАДРУКУЙТЕ КІЛЬКІСТЬ таких елементів.
# Крайні елементи списку не враховувати, оскільки в них недостньо сусідів.
# Для списка [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4 > 2+1, 5 > 1+3, 9>3+0.
list1 = []
while (True):
    num = input("Введіть значення, які ви хтіли б побачити в списку (або Exit для виходу): ")
    if num.lower() == "exit":
        break
    list1.append(int(num))

count = 0
for i in range(1, len(list1) - 1):
    if list1[i] > list1[i-1] + list1[i+1]:
        count += 1

print(f"Чисел які більші за суму своїх сусідів: {count}")