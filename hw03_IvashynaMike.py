#Задача 1.
#Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 10.
#Користувач намагається вгадати число.
#Програма може давати підказки тільки "More", "Less", "You won!"
import math
import random

rndm = random.randint(1, 10)

print ("Перша задача")
print ("")

print("Вгадайте загадане число у проміжку від 1 до 10!")
vvod = int(input("Число: "))

while vvod != rndm:
    if vvod < rndm:
                print("Більше!")
    elif vvod > rndm:
                print("Менше!")
    vvod = int(input("Спробуйте ще раз: "))

print("Молодець! Ти вгадав загадане число!")

######################################################################################

#Задача 2.
#Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 12.
#Програма виводить на екран число, яке створено і назву місяця, який відповідає цьому числу.

print ("")
print ("Друга задача")
print ("")

rndm = random.randint(1, 12)
mnth = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
print (rndm, "-", mnth[rndm-1])

##########################################################################################
#Задача 3.
#Написати програму в якій користувач вводить два цілих числа.
#Програма виводить результат піднесення першого числа у степінь відповідний другому числу.
#Зробити обробку всіх можливих помилок.
#В разі неможливості виконання дії - вивести відповідне повідомлення. ("Введено не число", тощо ... )

print ("")
print ("Третя задача")
print ("")

integer = 0
num1 = int(input("Перше число: "))
num2 = int(input("Друге число: "))

if type(num1) != type(integer):
    print("Перше число записано невірно.")
if type(num2) != type(integer):
    print("Друге число записано невірно.")

res = math.pow(num1, num2)
print(num1, "у степені", num2, " = ", res)