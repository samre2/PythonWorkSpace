#FizzBuxx
print("\n--- Fizz Buzz ---")
for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")

    else:
        print(i)

# List Comprehension

print("\n--- List Comprehension ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_evens = [x**2 for x in numbers if x % 2 == 0]

print(squared_evens)

#Unique Words
print("\n--- Unique Words ---")
sentence = input("Enter a Sentence: ")

words = sentence.lower().split() #Convert to lowercase and split into a list of words

unique_words  = set(words)

sorted_words = sorted(unique_words)

print("\nUnique words (sorted alphabetically): ")
print(sorted_words)


#Dict Frequency
print("\n--- Count Character ---")
text = input("Enter a string: ")

frequencies = {}
for char in text:
    frequencies[char] = frequencies.get(char, 0)+1
    sorted_chars = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    print("\nTop 3 most frequencies charactes: ")
    for char, count in sorted_chars[:3]:
        print(f"'{char}': {count} times")


#Function Factorial

print("\n--- Function Factorial Frequency ---")