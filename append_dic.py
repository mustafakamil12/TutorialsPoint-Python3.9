my_dic = {"mustfa":[1,2,3],"Mena":[4,5,6]}
print("my_dic = %s" % my_dic)
#new_dic = {"yousif":[7,8,9]}
new_list = [7,8,9]

#build new dictionary
new_dic = {}
new_dic['yousif'] = new_list

print(new_dic)


for name in my_dic:
    print(name)
    for mynumber in my_dic[name]:
        print(mynumber)
my_dic.update(new_dic)
print(my_dic)
