


animals = ["penguin", "ant", "canary", "dog",
           "python", "donkey", "cat","anaconda"]


if __name__ == '__main__':
    print(animals)

    #bad 
    sort = animals.sort()
    print(sort)

    #good
    animals.sort()
    print(animals)
