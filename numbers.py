numbers = list(range(1,12))

print (numbers)
def num(old_list,num):
    return [x ** num for x in old_list]

print (num(numbers,2))
