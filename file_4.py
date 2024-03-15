'''
# ----> while loop
# ----> break using while loop


s1 = "hello world to all"

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1

# Eg:2
i = 20
while i<31:
    print(i)
    i+=1
    if i==27:
        break

# Eg:3
i = 20
while i<31:
    print(i)
    if i==27:
        break
    i+=1


# Eg:4
i = 20
while i<31:
    if i==27:
        print(i)
        break
    i+=1



# ! ----> continue
i = 20
while i<31:
    if i ==27:
        continue
    print(i)
    i=i+1

# Eg:2
i = 20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

i = 12
sum=0
while i<23:
    sum=sum+1
    i+=1
    print(sum)

# ! Eg:6
# find the average of value from 20 to 25


i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    count+=1
    i+=1
print(sum/count)


# -----> Nested for loop

# Eg:1
for i in range(1,3+1):
    for j in range(1,4+1):
        print(i, j)
'''
# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *    

for row in range(4):
    for col in range(4):
        print("*",end=" ")
    print()
    

    
