my_list = []
n = int(input("Enter no of elements for list :- "))
for i in range(0,n):
    elements = int(input("Enter the Elements:- "))
    my_list.append(elements)

print(my_list)
List2 = []
for i in my_list:
    if i >=0:
        List2.append(i)
print("Positive no. from list are :-",List2)       
