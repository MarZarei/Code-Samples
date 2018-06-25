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

#Array
unorderedList = [39.8,111,12,12,76,95,62,9,14.3,25,134,0,89]

#testing the algorithm
print ("Array before sorting:")
print (unorderedList)
print ("Array after sorting:")
quickSort(unorderedList)
print(unorderedList)
