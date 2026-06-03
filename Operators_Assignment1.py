#Assignment name: day 1 – Operator Precedence & Associativity



print("Demonstrating operator precedence and associativity in Python")  
# Example 1: * and / are evaluated before + and -
result1 = 3 + 4 * 2  
print(f"3+4*2 = {result1}")  # Expected result: 11, because multiplication is evaluated before addition

print(f"(3 + 4) * 2 = { (3 + 4) * 2 }")  # Expected result: 14, because parentheses override operator precedence

# Example 2: ** is right-associative and binds tighter than unary minus
result2 = 2 ** 3 ** 2  # Expected result: 512, because 3 ** 2 is evaluated first, then 2 ** 9
print(f"2 ** 3 ** 2 = {result2}")  # Expected result: 512

print(f"-3 ** 2 = { -3 ** 2 }")  # Expected result: -9, because ** binds tighter than unary minus, so it's evaluated as -(3 ** 2)


# Example 3: Left-to-right associativity for same-precedence operators  
result3 = 100 / 5 * 2  # Expected result: 40.0, because division and multiplication are evaluated left to right
print(f"100 / 5 * 2 = {result3}")
result4 = 10 - 5 - 2  # Expected result: 3, because subtraction is evaluated left to right
print(f"10 - 5 - 2 = {result4}")

# Example 4: Mixing arithmetic, comparison, and logical operators
result5 = (3 + 4) > 5 and (2 * 3)   < 10  # Expected result: True, because (3 + 4) > 5 is True and (2 * 3) < 10 is also True, so the overall expression is True
print(f"(3 + 4) > 5 and (2 * 3) < 10 = {result5}")

print("End of demonstration")

print("Demonstrating assignment operators in Python")
# Example 1: Basic assignment
a = 10
print(f"a=10, a={a}")  # Expected output: 10 

# Example 2: Using augmented assignment operators
a += 5  # Equivalent to a = a + 5
print(f"a += 5, a={a}")  # Expected output: 15
a *= 2  # Equivalent to a = a * 2
print(f"a *= 2, a={a}")  # Expected output: 30
a /= 3  # Equivalent to a = a / 3
print(f"a /= 3, a={a}")  # Expected output: 10.0
a -= 4  # Equivalent to a = a - 4
print(f"a -= 4, a={a}")  # Expected output: 6.0
a **= 2  # Equivalent to a = a ** 2
print(f"a **= 2, a={a}")  # Expected output: 36.0
a //= 5  # Equivalent to a = a // 5
print(f"a //= 5, a={a}" )  # Expected output: 7.0


print("End of demonstration")   