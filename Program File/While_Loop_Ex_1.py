"""
name = ?
print -> name

OK
"""

"""
1. start 
*2. End 
*3. Step 
4. Condition -> True 
"""

isLooping = True

while isLooping:
    name = input()

    if name == "OK":
        break

    print(name)