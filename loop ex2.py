# print the output of the numbers which is divisble by 3 and 5 in the range of 1 to 100
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1

print(count)
