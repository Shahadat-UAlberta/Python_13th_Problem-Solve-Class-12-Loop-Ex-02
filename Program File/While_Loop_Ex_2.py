"""

[10, 20, 31, 35]

"""

lst = [10, 20, 31, 35, 40]

start = 0
end = len(lst)

while start < end:
    
    value = lst[start]
    start += 1

    if value % 2 == 1:
        # odd
        continue # used to skip the remaining code inside loop

    print(value)
