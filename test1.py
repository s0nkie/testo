
def slice_less(my_list, less):
    b = [i for i in my_list if i > less]
    return sorted(b, reverse=True)

print(slice_less([2,3,4,5,6,7], 3))