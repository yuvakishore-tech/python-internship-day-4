for i in range(1, 101):
    print(i)

count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1

for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)

text = "Python"
for ch in text:
    print(ch)

num = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

for i in range(0, 21, 2):
    print(i)

    
print("Real world example")

for second in range(5, 0, -1):
    print("Timer:", second)
