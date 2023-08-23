from random import randrange

def merge(left, right):
    temp = []
    while left and right:
        if left[0] < right[0]:
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
    if left:
        temp.extend(left)

    if right:
        temp.extend(right)
    return temp



def merge_sort(arr): 
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[0:mid]
    right= arr[mid:len(arr)]
    return merge(merge_sort(left), merge_sort(right))

if __name__ == '__main__':

    arr = [randrange(25) for x in range(12)]
    print(arr)
    print(merge_sort(arr))
