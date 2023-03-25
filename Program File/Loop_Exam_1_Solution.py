num_of_input = int(input())
nums_list = []
start = 0

while start < num_of_input:

    number = int(input()) # User Input
    nums_list.append(number) # Add into List

    start += 1

index = 0

while index < num_of_input:

    if nums_list[index] > 120 :
        break

    elif nums_list[index] % 10 == 0:
        print(nums_list[index])

    index += 1

"""
1. Ajay Ghosh [4178225] 
2. Rasheduzzaman Biddut [4175891] 
3. Md Sabbir Khan [4176945]
4. Md.Mahedi hasan [4172396] 
5. Azad Hossan [4170669] 
6. Rahul Borma [4174857] 
7. Nargis Sultana [4175497]
8. Md.Arafat Rahman [4175878]
9.Soumik Riyan Madhu [4178224]
"""