
nums = [ 1,2,3,4,5,6,7,8] 

if __name__ == '__main__':

    #the "convetional" way to filter the list
    alt_evens = []
    for num in nums:
        if num % 2 == 0:
            alt_evens.append(num) 

    #list comprehension syntax 
    evens = [num for num in nums if num % 2 == 0]
    print(f"alt_evens, {evens}")
    print("evens", evens) 
