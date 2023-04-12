all_Numbers = [11,34,42,3,4,44,23,21,66,33,22]

def printlist(numbers):
    for num in numbers:
        print(num)

def result(numbers):
    for num in numbers:
        if num > 12:
         print(num)

# calling function
print("All the numbers in the list - ")
printlist(all_Numbers)

print("\n\nNumbers greater than 12 - ")
result(all_Numbers)