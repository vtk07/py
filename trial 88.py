t1= eval(input("enter the tuple:"))

#maximum
i=0
max=t1[i]
for i in range(len(t1)):
    if max<t1[i]:
        max=t1[i]
print ("the maximum :",max)

i=0
min=t1[i]
for i in range(len(t1)):
    if min>=t1[i]:
        min=t1[i]
print("the minimum element is :",min)
sum=0
for i in t1:
    sum+=i
print(sum)

t=0
l1=list(t1)
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            t=l1[i]
            l1[i]=l1[j]
            l1[j]=t
t2=tuple(l1)
print ("the sorted tuple is :",t2)
    
    

    
