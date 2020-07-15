'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # sort array
    # loop through array swapping elements from current position to last
    # if the current position value is 0 
    # append element to arr and remove element
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.append(arr[i])
            arr.remove(arr[i])
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
