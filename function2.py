def mult_list(lst):
    if len(lst) == 0:
        return 0
    
    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod

print(mult_list([1,2,2]))
print(mult_list([]))
print(mult_list([15]))