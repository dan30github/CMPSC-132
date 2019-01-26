#LAB 12
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name:Daniel Melo Cruz
# Collaboration Statement: I did not ask for help to do this lab.            
#
########################################


def bubbleSort(numList):
	'''
		Takes a list and returns 2 values
		1st returned value: a dictionary with the state of the list after each complete pass of bubble sort
		2nd returned value: the sorted list

		>>> bubbleSort([2,3,5,4,1])
		({1: [2, 3, 4, 1, 5], 2: [2, 3, 1, 4, 5], 3: [2, 1, 3, 4, 5], 4: [1, 2, 3, 4, 5]}, [1, 2, 3, 4, 5])
	'''
	# Your code starts here

	swap = 0
	runs = {}
	counter = 0
	li = []

	while True:
		swap = 0
		li = [] #list that will be used in dictionary

		for x in range(len(numList) - 1): #pass through list
			if numList[x] > numList[x+1]: 
				numList[x], numList[x+1] = numList[x+1], numList[x] #swaps elements
				swap += 1

		for x in numList: #get list to put in dictionary
			li.append(x)

		counter += 1 #counter for dictionary element
		runs[counter] = li #add list to dictionary

		if swap == 0:
			return (runs, numList)

