print("1ST TASK")

list1 = [12, 432, 664, 79, 101]

for val in list1:
    if val > 100:
        print (val)
#############################################################################
print("")
print("2ND TASK")

list2 = []
newlist2 = []

while True:
    print("Введіть будь яке число:")
    print("(Або Exit для виходу)")
    list1val = input("Відповідь: ")
    if list1val.lower() == "exit":
        break
    list2.append(int(list1val))
print(f"Ваші числа: {list2}")

for val in list2:
    if val > 100:
        newlist2.append(val)
print(f"З них більше 100: {newlist2}")
################################################################################
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
################################################################################
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