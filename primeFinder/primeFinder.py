#########
#Obijah
#find prime numbers
###########



##################
##Vars
#primeList[]
#1) Ask for a range (integer>0) 
#2) From 1 to range do
#		check if number can be divided by any number in prime list
#			if yes, proceed to next
#			if no, add that number to prime list, go to next
#	When range is reached, write the prime list out to a file.


#primeList returns a list of integers from 1 up to a user selected input

def findPrimes(range):
	#initialize the prime list by adding the value 2.
	primeList=[2]
	currentNumber = 3
	
	#for every integer between 3 and user input(range)
	while currentNumber <= range:
		#start at the first prime number in prime list
		primeListIndex = 0
		
		#Test the current number against every known prime in the primeList. 
		#If currentNumber is evenly divisible by any number in prime list, skip ahead
		#If the number isn't divisible (currentNumber modulus prime number is anything other than 0), 
		#	then keep testing until no more primes in list.
		
		while primeListIndex < len(primeList):
			if (currentNumber % primeList[primeListIndex])!=0:
				primeListIndex = primeListIndex+1
			else:
				break;
		#At this point, either the number was divisible, or prime numbers were exhausted. 
		#If no more primes, then currentNumber is a prime number, add to list, and go to the next.
		#other wise, just go to the next number until we reach the end of the range
		if primeListIndex == len(primeList):
			primeList.append(currentNumber)
		
		currentNumber = currentNumber + 1
	
	#the value 1 is troublesome for testing, so add to list after testing completes
	primeList.insert(0,1)
	return primeList
	
				
#Main program
			
print("Input an integer between 1 and 250: ")

while True:
	#try to catch bad input (non integer, less than 0, etc)
	try:
		userArg = int(input())
	except ValueError:
		print("Invalid input: Please enter a valid integer. ")
		continue
	if userArg < 0:
		print("Integer must be greater than 0. ")
		continue
	else:
		break
	
#write some output
print(f"Here is a list of prime numbers up to {userArg}:")
print(findPrimes(int(userArg)))	

		
		
		