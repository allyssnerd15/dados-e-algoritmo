'''There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):'''

#code
def sockMerchant(n, ar):
    # Write your code here
    sock_counts = {}
    pairs = 0
    
    # Count the number of socks of each color
    for color in ar:
        if color in sock_counts:
            sock_counts[color] += 1
        else:
            sock_counts[color] = 1
    
    # Calculate the number of pairs for each color
    for count in sock_counts.values():
        pairs += count // 2
    
    return pairs



'''Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .'''

#code
def hourglassSum(arr):
    max_sum = float('-inf')  # Initialize the maximum sum to negative infinity
    
    # Iterate through the array, excluding the border elements
    for i in range(1, 5):
        for j in range(1, 5):
            # Calculate the sum of the current hourglass
            current_sum = (
                arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +
                arr[i][j] +
                arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            )
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
    
    return max_sum




'''It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.'''
#code
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)
    

'''You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

Example
arr = [7, 1, 3, 2, 4, 5, 6]

'''
#code
def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            temp = arr[i]
            arr[i], arr[temp - 1] = arr[temp - 1], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps


'''Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example
n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
'''

#code
def arrayManipulation(n, queries):
    # Initialize array with zeros
    arr = [0] * (n + 1)
    
    # Perform queries and update prefix sum array
    for a, b, k in queries:
        arr[a - 1] += k
        arr[b] -= k
    
    # Calculate prefix sum
    max_value = 0
    prefix_sum = 0
    for i in range(n):
        prefix_sum += arr[i]
        max_value = max(max_value, prefix_sum)
    
    return max_value


'''An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .

Reverse an array of integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Example

Return .'''

#code
def reverseArray(a):
    # Write your code here
    # return a[::-1]
    b = []
    for i in a:
        b.insert(0, i)
    return b
