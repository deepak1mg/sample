import operator
s =input()
my_dict={}
for x in s:
    my_dict[x]=0
for x in s:
    my_dict[x]+=1
print(sorted(my_dict.items(), key=operator.itemgetter(0)))
