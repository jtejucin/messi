from pickle import APPENDS


numbers = [10, 5 , 7 , 2 ,1 ]
print (numbers)

numbers [0] = 111
print (numbers) 

numbers [4] = numbers[0]
print (numbers)


print (numbers[2])

print(len(numbers))

numbers.append(8.9)
print (numbers)

deportesx =[]
deportesx.append(input("deporte favorito"))

del numbers[1]
print (numbers)