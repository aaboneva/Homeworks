n = int(input("Ënter a number: "))

print(1)
print(2)
digits = []

while n > 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10
print(digits)

n = 0
for digit in digits:
    n = n * 10 + digit
print(n)
