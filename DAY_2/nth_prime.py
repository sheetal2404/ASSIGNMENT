import numpy as np
# n = int(input())
# flag = 0
# ans = 0
# count = 1
# j = 2
# while flag == 0:
#     for i in range(2, n):
#         if(j%i == 0):
#             continue
#         else:
#             count=count+1
#             if(count == n):
#                 ans = j
#                 flag = 1
#                 break
#     j=j+1
# print(ans)

n=int(input())
count=0
prime=1
while(count!=n+1):
    prime+=1
    flag = 0
    for j in range(2, prime//2):
        if (prime% j == 0):
            flag = 1
            break
    if (flag == 0):
        count+=1
        if(count==0):
            break
print(prime)
