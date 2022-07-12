list_1 = []
i = 0
y = int(input("Enter the range: "))
for x in range(y):
    i += 1
    list_1.append(i)
    list_2 = str(list_1)
    list_2 = list_2.replace("[","")
    list_2 = list_2.replace("]","")
    list_2 = list_2.replace(",","")
    print(list_2)