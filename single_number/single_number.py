'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # sort array 
    # the loop will start at the third position
    # and track the previous two elements in the array
    # because the array is sorted all duplicate values will be adjacent
    # if the middle element doesn't equal the element to either side
    # it is the single number
    # if at the last iteration single is still equal to None
    # the last element is the single number
    arr.sort()
    print(arr)
    single = None
    first = arr[0]
    i = 2
    while i < len(arr):
        print(f'{arr[i-2]} {arr[i-1]} {arr[i]}')
        if arr[i-1] != arr[i-2]  and arr[i-1] != arr[i]:
            single = arr[i-1]
            return single
        elif i == len(arr)-1 and single == None:
            return arr[i]
        i += 1



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")