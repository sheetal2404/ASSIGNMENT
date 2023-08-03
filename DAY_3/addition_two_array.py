

def addArrays(a1, a2):
    num1 = 0
    num2 = 0
    for i in range(n1):
        num1 = num1 * 10 + a1[i]

    for i in range(n2):
        num2 = num2 * 10 + a2[i]

    x=num1 + num2
    ans = []
    while(x!=0):
        d = x%10
        ans.append(d)
        x=x//10

    return ans

n1 = int(input())
n2 = int(input())

a1 = []
a2 = []

print("array1")
for i in range(n1):
    a1.append(int(input()))

print("array2")
for i in range(n2):
    a2.append(int(input()))

ans = addArrays(a1, a2, n1, n2)

print(ans[::-1])
