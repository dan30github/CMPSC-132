#LAB 14
#Due Date: 12/07/2018, 11:59PM
########################################
#                                      
# Name:Daniel Melo Cruz
# Collaboration Statement: Did not ask for any help.             
#
########################################

def makingSound(n,sound):
	#Write your code here
	def aList(k):
		li = []

		for x in range(k):
			if x%n == 0:
				li.append(sound)
			else:
				li.append(x)

		return li
	return aList

def vectorizing(term):
	#Write your code here
	def list_func(aList):
		return list(map(term,aList))

	return list_func