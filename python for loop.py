# List of numbers
num = [6, 2, 3, 8, 4, 2, 5, 4, 9]

# variable to store the sum
sum = 0

# iterate over the list
for val in num:
    sum = sum + val

print("The sum is", sum)

# range function
print(range(6))

# for loop with else
digi = [1,3,5]

for i in digi:
    print(i)
else:
    print("No items left.")

# program to print student marks from record
student_name = 'asha'

marks = {'vani': 70, 'krupal': 65, 'deeksha': 90}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')