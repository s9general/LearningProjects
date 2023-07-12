''' Convert miles to kilometers
'''

#Prompt the user for the number of miles
miles = input("How many miles? ")
#convert miles to kilometers, convert it to a float first
kilometers = float(miles) * 1.609
#Concatonate then print the answer
print(str(miles) + " miles equals "+ str(kilometers) + " kilometers." )
