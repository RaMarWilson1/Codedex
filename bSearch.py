
arr = [ 1, 3, 5, 6, 8, 10, 15, 18 ]

def bsearch(arr, target_value):
    mid = int(len(arr) / 2)
    if len(arr) == 0: 
        return None
    if arr[mid] == target_value:
        return arr[mid]
    elif target_value > arr[mid]:
        return bsearch(arr[mid+1:], target_value)

    elif target_value < arr[mid]:
        return bsearch(arr[:mid], target_value)

    else: return None    


print(bsearch(arr, 8))


# Given a binary tree, determine (boolean) if that tree is a binary SEARCH tree
#       9
#     /   \ 
#    6     12
#   / \    / \
#  5   7  10  15 

#       9
#     /   \ 
#    6     12
#   / \
#  5   11 