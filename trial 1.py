n = int ( input ("enter the number:"))
fact = sum = 0
for i in range (0,n+1):
    fact = 1
    for j in range (1,i+1):
        fact*=j
    sum += 1/fact
print (sum )
    
