## Probleme 03: LINKED LIST
lst = []
  

n = int(input("Enter number of elements :"))
  

for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) 
      

lst.sort()

print(lst)

lst = list(dict.fromkeys(lst))
print(lst)
