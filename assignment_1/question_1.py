n=int(input())
lst=[]
for i in range(n):
    a=input()
    lst.append(a)

sort= sorted(lst)

temp=sort.pop(1)
sort.insert(0,temp)
print(sort)
