# 2. Operators

## Data Types

There are mainly 5 data type in Python which are used most frequently:

- Integer
- String
- Float
- Boolean (it can either be True or False)
- None (there's no null in Python, only None)

Apart from this there are some other built-in data types which Python provides such as list, dictionary, etc.

```python
print(12, type(12))                 # int
print('Python', type('Python'))     # str
print(34.7, type(34.7))             # float
print(True, type(True))             # bool
print(None, type(None))             # NoneType
```

## Operators

The operators are used to perform the operations on given values or variables. There mare many operators in Python which are used to carry off arithmetic or logical operations.

Some of the most commonly used operators:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators

### Arithmetic Operators

Arithmetic operators are just like the mathematical operations like addition, subtraction, multiplication, division, etc.

| Name | Operator | Example |
| ---- | -------- | ------- |
| Addition | + | 4 + 2 |
| Subtraction | + | 6 - 4 |
| Multiplication | * | 5 * 2 |
| Division | // | 8 // 2 |
| Modulus | % | 7 % 2 |
| Exponential | ** | 2 ** 2|

**Note:** Python has two type of division operators `/` which returns the floating number and `//` which returns floor value of the division.

```python
print('4 + 2: ', 4 + 2)     # 6
print('6 - 4: ', 6 - 4)     # 2
print('5 * 2: ', 5 * 2)     # 10
print('8 / 2: ', 8 / 2)     # 4.0
print('8 // 2: ', 8 // 2)   # 4
print('7 % 2: ', 7 % 2)     # 1
print('2 ** 2: ', 2 ** 2)   # 4
```

### Assignment Operators

Assignment operators are used to assign the values to given variables.

| Operator | Example |
| ---- | ------- |
| = | x = 5 |
| += | x += 4 |
| -= | x -= 2 |
| //= | x *= 3 |
| %= | x //= 6 |
| **= | x %= 3 |

```python
x = 5

print('x =', x)             # x = 5
print('x += 4: ', x)        # 9
print('x -= 2: ', x)        # 7
print('x *= 3: ', x)        # 21
print('x //= 6: ', x)       # 3
print('x %= 3: ', x)        # 0
print('x **= 2: ', x)       # 0
print('2 **= 2: ', 2**2)    # 4 
```

### Comparison Operators

Comparison operators as the name suggests is used to compare the two values.

| Name | Operator | Example |
| ---- | -------- | ------- |
| Equal | == | 4 == 2 |
| Not equal | != | 6 != 4 |
| Greater than | > | 5 > 2 |
| Less than | < | 8 < 2 |
| Greater than or equal to | >= | 7 >= 2 |
| Less than or equal to | <= | 2 <= 2 |

```python
print('4 == 2: ', 4 == 2)       # False
print('8 == 8: ', 8 == 8)       # True

print('6 != 4: ', 6 != 4)       # True
print('45 != 45: ', 45 != 45)   # False

print('5 > 2: ', 5 > 8)         # False
print('8 < 2: ', 8 < 2)         # True
print('7 >= 2: ', 7 >= 2)       # True
print('2 <= 2: ', 2 <= 2)       # True
```

### Logical Operators

Logical operator is used to perform logical operations on two statements or values. There are basically three main types of logical operators in Python.

| Operator | Description | Example |
| ---- | -------- | ------- |
| `and` | Compare both the statements and return True if both are true else False | 4 < 6 and 8 > 2 |
| `or` | Compare both the statements and return True if any one is true else False | 4 > 6 or 8 < 2 |
| `not` | Returns the reverse of given boolean value i.e. True to False and vice versa | not True |

```python
print("The value of True AND False is: ", True and False)
print("The value of True OR False is: ", True or False)
print("The value of NOT True is: ", not True)
print("The value of NOT False is: ", not False)
```
