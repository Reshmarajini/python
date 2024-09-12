#count the numbers even and odd numbers between 1 to 100
e_count=0
o_count=0
for i in range(1,100):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)
        
