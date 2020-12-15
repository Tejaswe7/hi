n=int(input())
li=[]
product=1
for i in range(n):
    x=float(input())
    li.append(x)
lowest=li[0]
largest=li[0]
for i in li:
    if i<lowest:
        lowest=i
    if i>largest:
        largest=i
for j in li:
    if j!=largest and j!=lowest:
        product *= j
print(product)
