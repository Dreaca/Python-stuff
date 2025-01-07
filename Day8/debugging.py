import pdb

def multiplication(a,b):
    answer = (a*b)
    return answer

# pdb.set_trace()
breakpoint()

x = input("Enter first number to multiply : ")

y = input("Enter second number to multiply : ")

mul = multiplication(x,y)

print(mul)