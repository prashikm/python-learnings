# ----------------------- Arithmetic Operators ------------------------------
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
print('\n')                        # adds new line below

# ----------------------- Assignment Operators ------------------------------
x = 5
print('x =', x)

x += 4
print('x += 4: ', x)

x -= 2
print('x -= 2: ', x)

x *= 3
print('x *= 3: ', x)

x //= 6
print('x //= 6: ', x)

x %= 3
print('x %= 3: ', x)

x **= 2
print('x **= 2: ', x)
print('2 **= 2: ', 2**2)
print('\n')


# ----------------------- Comparison Operators ------------------------------
print('4 == 2: ', 4 == 2)
print('8 == 8: ', 8 == 8)

print('6 != 4: ', 6 != 4)
print('45 != 45: ', 45 != 45)

print('5 > 2: ', 5 > 2)
print('8 < 2: ', 8 < 2)
print('7 >= 2: ', 7 >= 2)
print('2 <= 2: ', 2 <= 2)
print('\n')


# ----------------------- Logical Operators ------------------------------
bool1 = True
bool2 = False

print("The value of bool1 AND bool2 is: ", bool1 and bool2)
print("The value of bool1 OR bool2 is: ", bool1 or bool2)
print("The value of NOT bool1 is: ", not bool1)
print("The value of NOT bool2 is: ", not bool2)
print('\n')


# ----------------------- Identity Operators ------------------------------
obj1 = [2, 4, 6, 8]
obj2 = [2, 4, 6, 8]
obj3 = obj2

print('obj1 is obj2: ', obj1 is obj2)
print('obj1 is obj3: ', obj1 is obj3)
print('obj2 is obj3: ', obj2 is obj3)
print('\n')
