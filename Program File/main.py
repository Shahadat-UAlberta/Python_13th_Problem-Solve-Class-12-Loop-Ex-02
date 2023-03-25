
num_lst = input("Enter a list of numbers separated by spaces:").split() # 10 20 30 40
print(num_lst)

start = 0
while start < len(num_lst):
    # Type Casting - String to Integer
    num_lst[start] = int(num_lst[start])
    start += 1

print(num_lst)

start = 0

while start < len(num_lst):
    num = int(num_lst[start])

    if num > 120:
       break

    if num % 10 == 0 :
      print(num)

    start += 1
"""

"""
