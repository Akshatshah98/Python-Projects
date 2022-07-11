list1 = []
y = int(input("Enter the range: "))
for x in range(y):
    list1.append("*")
    list2 = str(list1)
    list3 = list2.replace("[","") 
    list3 = list3.replace("]","")
    list3 = list3.replace("'","")
    print(list3.replace(",",""))
    