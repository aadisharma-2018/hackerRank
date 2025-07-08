###
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
###

def diagonalDifference(arr):
    left_total = 0
    right_total = 0
    
    for i in range (len(arr)):
        left_total += arr[i][i]
        right_total += arr[i][len(arr) - i - 1]
    
    return abs(left_total - right_total)