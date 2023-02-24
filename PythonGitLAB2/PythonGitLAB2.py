import random

def generate_list(n):
    return [random.randint(5, 8 * 100) for i in range(n)]

mylist = generate_list(18)
print(mylist)
