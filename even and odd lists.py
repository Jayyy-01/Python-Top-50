li = []
even_list = []
odd_list = []
for i in range(5):
    num = int(input("enter the numbers to be in the list: "))
    li.append(num)
for i in li:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(li)
print("even list: ",even_list)
print("odd list: ",odd_list)
