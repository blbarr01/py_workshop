from math import floor 
from random import randrange
from typing import List 



def insert_sort(arr:List[int]):
    n = len(arr)
    for l in range(n):
        for r in range(n):
            if arr[r] >= arr[l]:
                arr[r], arr[l] = arr[l], arr[r]
    return arr

if __name__ == '__main__':

    arr = [randrange(75) for i in range(12)]
    print(arr)
    insert_sort(arr)
    print(arr)
