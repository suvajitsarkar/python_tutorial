str = input()
n = len(str)
max = 1
index = 0
temp = 1
for i in range(0,n-1):
    if str[i]<=str[i+1]:
        temp+=1
    else:
        if max < temp:
            index = i
            max = temp
        temp = 1
if max < temp:
    index = i+1
    max = temp
print(index,max)
print(str[index-max+1:index+1])
