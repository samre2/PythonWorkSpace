#Day8.py


x = 2

if x %2 == 0:

    print("Even")

else:
    print("Odd")



#For loop


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruits}")

nums = [2, 4, 5]

nums_sql = []
for num in nums:
    print(num ** 2)
    nums_sql.append(num ** 2)

print(nums_sql)
list_sqr = []
for item in range(3):   #3 -> 3
    input_num = int(input("Enter the number to square: "))

    input_num_sqr = input_num ** 2
    list_sqr.append(input_num_sqr)
    print(list_sqr)



input("Enter")
print(type (x))


#while loop

num = 2
while num <5:
    print(f"number: {num}")
    num +=1


