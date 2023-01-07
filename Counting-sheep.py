# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

def count_sheeps(sheep):
    total = 0
    for i in sheep:
        if i == True:
            total += 1
        else:
            pass
    return total

# Another soultion:
# def count_sheeps(arrayOfSheeps):
# return arrayOfSheeps.count(True)