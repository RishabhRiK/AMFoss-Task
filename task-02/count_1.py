iter = int(input())

for j in range(iter):
    Digit = int(input())
    binary = input()
    ones = 0
    for i in range(Digit):
        if binary[i] == "1":
            ones = ones + 1
    zeros = Digit-ones
    output = ones*(ones-1)+zeros*(ones+1)
    print(output)
