# Example of using map function
# Get L and R from the input

L, R = map(int, input().split())

# Write here the logic to print all integers between L and R

for i in range(L,R+1):
    print(i, end=" ") 
print("")
