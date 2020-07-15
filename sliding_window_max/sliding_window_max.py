'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # iterate through list and work with a chunk of k elements at each iteration
    # for each iteration sort the splice and append largest number to new array
    start = 0
    window = k
    array = []
    while window <= len(nums):
        chunk = nums[start:window]
        chunk.sort(reverse=True)
        array.append(chunk[0])
        window +=1
        start +=1
    return array



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
