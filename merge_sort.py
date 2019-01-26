#LAB 13
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name: Daniel Melo Cruz
# Collaboration Statement:  I asked for help in the recursive function mergeSort.                
#
########################################

def merge(list1, list2):
	#write your code here

	index1 = 0
	index2 = 0
	merged = []
	counter = 0

	while counter < len(list1) + len(list2): #limits the number of iterations.

		if index1 < len(list1) and index2 < len(list2):

			if list1[index1]< list2[index2]: #compares list elements and appends the smaller one.
				merged.append(list1[index1])
				counter += 1

				index1 += 1
			else:

				merged.append(list2[index2])
				counter += 1

				index2 += 1
		else:

			if index1 >= len(list1): #if passed through whole list1, add rest of list2
				for x in range(index2, len(list2)):
					merged.append(list2[x])
					counter += 1

			elif index2 >= len(list2): #if passed through whole list2, add rest of list1
				for x in range(index1, len(list1)):
					merged.append(list1[x])
					counter +=1

	return merged

def mergeSort(numList):
	#write your code here
	mid = 0

	if len(numList) <=1: #base case
		return numList

	mid = len(numList) // 2 #get middle of list

	left = mergeSort(numList[:mid]) #recursive part for left
	right = mergeSort(numList[mid:]) #recursive part for right

	return merge(left, right)


	
