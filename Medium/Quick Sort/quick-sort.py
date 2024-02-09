#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            # Find the partition index such that elements smaller than
            # arr[pivot_index] are on the left, and elements greater are on the right.
            pivot_index = self.partition(arr, low, high)

            # Recursively sort the sub-arrays on the left and right of the pivot.
            self.quickSort(arr, low, pivot_index - 1)
            self.quickSort(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
        # Choosing the rightmost element as the pivot
        pivot = arr[high]
        # Index of the smaller element
        i = low - 1

        # Traverse through the array and rearrange elements such that
        # elements smaller than the pivot are on the left, and greater on the right.
        for j in range(low, high):
            if arr[j] <= pivot:
                # Swap arr[i+1] and arr[j]
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        # Swap arr[i+1] and arr[high] to place the pivot in its correct position.
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # Return the index where the pivot element is now located.
        return i + 1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends