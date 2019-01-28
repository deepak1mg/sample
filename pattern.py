def combiner(args):
    ls=''
    num=0
    for item in args:
        if type(item)==type("s"):
            ls+=item
       	else:
            num+=item
    return "{}{}".format(ls,num)
print(combiner(['ss',10.55,'bb',15]))