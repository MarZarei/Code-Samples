#quick sort function
def quickSort(inputList):
   quickSortStep(inputList,0,len(inputList)-1)

#calls quick sort step recursively on subarrays
def quickSortStep(inputList,startIndex,endIndex):
   #recursion ending condition
   if startIndex<endIndex:

       splitpoint = partition(inputList,startIndex,endIndex)

       quickSortStep(inputList,startIndex,splitpoint-1)
       quickSortStep(inputList,splitpoint+1,endIndex)


#locating the right spot for one index at a time
#returns the index of the right place for the pivot value
def partition(inputList,startIndex,endIndex):
   
#middle=(startIndex+endIndex)/2
   pivotvalue = inputList[startIndex]

   leftmark = startIndex+1
   rightmark = endIndex

   done = False
   while not done:

       while leftmark <= rightmark and inputList[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while inputList[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = inputList[leftmark]
           inputList[leftmark] = inputList[rightmark]
           inputList[rightmark] = temp

   temp = inputList[startIndex]
   inputList[startIndex] = inputList[rightmark]
   inputList[rightmark] = temp

   return rightmark


#testing the algorithm

#Arrays
FirstList = [39.8,111,-3,12,12,76,95,-14,62,9,14.3,25,-7.35,134,0,89]
SecondList = [17,1,-0.45,314,17,34,-15,80.55,202,100,80.50,100.029,111,235.5]

print ("Array List 1 before sorting:")
print (FirstList)
print ("Array List 1 after sorting:")
quickSort(FirstList)
print(FirstList)

print ("Array List 2 before sorting:")
print (SecondList)
print ("Array List 2 after sorting:")
quickSort(SecondList)
print(SecondList)
