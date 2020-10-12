# program to add natural num
n = 20

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
print("\n")

counter = 0

# else with while loop
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")