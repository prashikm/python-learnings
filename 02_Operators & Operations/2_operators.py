# ----------------------- Arthemetic Operators ------------------------------
Addition = 4 + 2
Subtraction = 6 - 4
Multiplication = 5 * 2
Division = 8 // 2
Modulus = 7 % 2
Exponential = 2 ** 2

print('4 + 2: ', Addition)         # 6
print('6 - 4: ', Subtraction)      # 2
print('5 * 2: ', Multiplication)   # 10
print('8 // 2: ', Division)        # 4.0
print('7 % 2: ', Modulus)          # 1
print('2 ** 2: ', Exponential)     # 4


# ----------------------- Assignment Operators ------------------------------
x = 5
print('x =', x)

x += 4
print('x += 4: ', x)

x -= 2
print('x -= 2', x)

x *= 3
print('x *= 3', x)

x //= 6
print('x //= 6', x)

x %= 3
print('x %= 3', x)

x **= 2
print('x **= 2', x)


# ----------------------- Comparision Operators ------------------------------
a = 14
b = 100

print('a == b', a == b)
print('8 == 8', 8 == 8)

print('a != b', a != b)
print('45 != 45', 45 != 45)

print('a > b', a > b)
print('a < b', a < b)
print('a >= b', a >= b)
print('a <= b', a <= b)


# ----------------------- Logical Operators ------------------------------
bool1 = True
bool2 = False

print("The value of bool1 AND bool2 is", bool1 and bool2)
print("The value of bool1 OR bool2 is", bool1 or bool2)
print("The value of NOT bool1 is", not bool1)
print("The value of NOT bool2 is", not bool2)


# ----------------------- Identity Operators ------------------------------
print('64 is 23', 64 is 23)
print('22 is 22', 22 is 22)

print('64 is 23', 64 is 23)
print('22 is not 22', 22 is not 22)
