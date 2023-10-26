# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"


# ---------my approach---------------

def SqEl(numbers):
    ans=[]
    for i in range(0,len(numbers)):
        ans.append(numbers[i]*numbers[i])
    return ans


numbers = list(range(1, 11))
res=SqEl(numbers)
print(res)


# ----------gpt-------------

# def SqEl(numbers):
#     ans=[]
#     for num in numbers:
#         ans.append(num * num)
#     return ans

# numbers = list(range(1, 11))
# res = SqEl(numbers)
# print(res)
