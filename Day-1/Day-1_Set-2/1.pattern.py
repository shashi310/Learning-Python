# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5



n = 5  # Set the number of rows

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()



# def pat(numbers):
#     ans = ""
#     for i in range(len(numbers)):
#         ans += str(numbers[i])
#         print(ans)
#     return ans
# # list(range(1, 6))
# numbers = list(range(1, 6))
# res = pat(numbers)
# print(res)
