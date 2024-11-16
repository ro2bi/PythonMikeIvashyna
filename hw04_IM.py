print("1ST TASK")

list1 = [12, 432, 664, 79, 101]

for val in list1:
    if val > 100:
        print (val)
##############################################################################
print("2ND TASK")

myres = []
list2 = [33, 98, 3561, 6574, 100, 102]

for val in list2:
    if val > 100:
        myres.append(val)

print (myres)
################################################################################
print("3RD TASK")

list3 = ["i", "love", "OGSC", "so", "hcum"]
newlist3 = []

for idx, val in enumerate(list3, start = 1):
    if idx % 2 != 0:
        newlist3.append(val[::-1])
    else:
        newlist3.append(val)
print (newlist3)
################################################################################
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