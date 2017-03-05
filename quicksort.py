# #include <stdio.h>
# #include <stdbool.h>
# #define MAX 7

# int intArray[MAX] = {4,6,3,2,1,9,7};

# void printline(int count) {
#    int i;
  
#    for(i = 0;i <count-1;i++) {
#       printf("=");
#    }
  
#    printf("=\n");
# }

# void display() {
#    int i;
#    printf("[");
  
#    // navigate through all items 
#    for(i = 0;i<MAX;i++) {
#       printf("%d ",intArray[i]);
#    }
  
#    printf("]\n");
# }

# void swap(int num1, int num2) {
#    int temp = intArray[num1];
#    intArray[num1] = intArray[num2];
#    intArray[num2] = temp;
# }

# int partition(int left, int right, int pivot) {
#    int leftPointer = left -1;
#    int rightPointer = right;

#    while(true) {
#       while(intArray[++leftPointer] < pivot) {
#          //do nothing
#       }
    
#       while(rightPointer > 0 && intArray[--rightPointer] > pivot) {
#          //do nothing
#       }

#       if(leftPointer >= rightPointer) {
#          break;
#       } else {
#          printf(" item swapped :%d,%d\n", intArray[leftPointer],intArray[rightPointer]);
#          swap(leftPointer,rightPointer);
#       }
#    }
  
#    printf(" pivot swapped :%d,%d\n", intArray[leftPointer],intArray[right]);
#    swap(leftPointer,right);
#    printf("Updated Array: "); 
#    display();
#    return leftPointer;
# }

# void quickSort(int left, int right) {
#    if(right-left <= 0) {
#       return;   
#    } else {
#       int pivot = intArray[right];
#       int partitionPoint = partition(left, right, pivot);
#       quickSort(left,partitionPoint-1);
#       quickSort(partitionPoint+1,right);
#    }        
# }

# main() {
#    printf("Input Array: ");
#    display();
#    printline(50);
#    quickSort(0,MAX-1);
#    printf("Output Array: ");
#    display();
#    printline(50);
# }
def quickSortHelper(alist,first,last):
   # print 'hit!'
   if first<last:
       splitpoint = partition(alist,first,last)
       # print splitpoint
       quickSortHelper(alist,first,splitpoint-1) #before pivot
       quickSortHelper(alist,splitpoint+1,last) #after pivot



def partition(alist,first,last):
   pivotvalue = alist[first]
   print pivotvalue
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSortHelper(alist, 0, len(alist)-1)
print(alist)