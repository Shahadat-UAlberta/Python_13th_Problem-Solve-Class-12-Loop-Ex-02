
lst=[1, 2, 3, 4]

start = 4
end = len(lst)

while start <= end:
    j=1
    sum = 0
    while j <= end:
        sum+=j
        j+=1
        print(sum)
    start+=1

print("-----")

