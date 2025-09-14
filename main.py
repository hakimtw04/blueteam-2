"""
name: str = "Abdulhakim"
#city: str = "Misurata"
#print(f"My name is {name}, and I live in {city}")
#sentence = "apple,banana,orange,mango"
#parts = sentence.split(",")
#print(parts[0], parts[1])
#print(parts[-1])   
#print(parts)
"""
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        even.append(mylist[i])
    else:
        odd.append(mylist[i])


print(even)
print(odd)