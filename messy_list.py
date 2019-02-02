messy_list = ["a", 2, True, 3, 1, False, [1, 2, 3]]
i=0
while i<len(messy_list):
    if isinstance(messy_list[i],bool):
        del messy_list[i]

    else:
        if isinstance(messy_list[i],int):
            i+=1
        else:
            del messy_list[i]
        print('i = {}, in ELSE'.format(i))
        
print(messy_list)     