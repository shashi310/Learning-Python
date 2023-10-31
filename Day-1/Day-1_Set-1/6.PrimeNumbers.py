# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."


# ----------------my apporoach with right ans------

# def CheckPrimeNumber(number):
#     count=0
#     for i in range(1,number+1):
#         print(i)
#         if number%i==0:
#             count+=1
#     return count

# ans=CheckPrimeNumber(13)
# if ans==2:
#     print("Prime number")


# -----------------new0-----------------



def is_prime(number):
    
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        # print((number**0.5) + 1)
        print(i)
        if number % i == 0:
            return False
    return True

# Test the function
num = 13
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
