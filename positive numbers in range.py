list1=[]
list2=[]
n=int(input("number of elements:"))
for i in range(0,n):
    element=int(input())
    list1.append(element)
print("input",list1)
for positive_num in list1:
    if(positive_num>0):
        list2.append(positive_num)
print("output",list2)