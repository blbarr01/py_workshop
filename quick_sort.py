from random import randrange
from typing import List 
import sys


#the most elegant implementaion of quicksort i've seen 
def quick_sort(arr:List[int])->List[int]:
    if len(arr) <= 1:
        return arr
    else:
       return quick_sort([x for x in arr[1:] if x < arr[0]]) \
            + [arr[0]]\
            + quick_sort([x for x in arr[1:] if x >= arr[0]])

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    arr = [randrange(25) for x in range(n)]
    print(arr)
    s = quick_sort(arr)
    print(s)
    print(arr)
'''
take note of the multiline statement deliminated with \
watch out for white space after the \ 
'''

