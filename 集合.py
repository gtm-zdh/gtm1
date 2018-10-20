
xn=['ggy','agr','ssj','hyf']
python=['ggy','agr','ssj','zy','hxm','cz']
s_xn = set(xn)
s_python = set(python)

#并集 把两个集合合并到一起，然后把重复的去掉
# print(s_xn.union(s_python))
# print(s_xn|s_python)

#交集 把两个集合相同元素取出来
# print(s_xn.intersection(s_python))
# print(s_xn & s_python)

# print(s_xn.difference(s_python))  # 取差集 在list中存在，在list2中没有的
# print(s_xn - s_python)
# print(s_xn.issubset(s_python))  # 判断前面这个集合是不是在后面这个里头
# print(s_xn.issuperset(s_python))  # 判断前面这个集合是不是包含后面这个集合
# print(s_xn.isdisjoint(s_xn))  # 判断list1和list3是否有交集，没有交集才返回true

s_xn.add(888)#添加元素
s_xn.update([777,666,666]) #添加值
s_xn.remove(777)#删除元素，如果元素不存在会报错
s_xn.pop()#删除一个随机的元素，并返回删除的元素
s_xn.discard('dddd')#如果删除的元素存在，删除，不存在不做处理

print(s_xn)
#取对称差集
# print(s_python.symmetric_difference(s_xn)) #也就是把两个集合中相同的去掉
# print(s_python ^ s_xn)#也就是把两个集合中相同的去掉

#集合也是无序的


# import string
# upper_set = set(string.ascii_uppercase)
# lower_set = set(string.ascii_lowercase)
# num_set = set(string.digits)
# pwd ='abc123'
# set1 = set(pwd).intersection(upper_set)
# print(set1)
# set2 = set(pwd).intersection(lower_set)
# set3 = set(pwd).intersection(num_set)
# if set1 and set2 and set3:
#     print('密码是符合要求的')
# else:
#     print('不符合要求')
#非空即真 非0即真
# names = []
# dic = {}
# s = set()
# # talk = input('说：').strip()
# if s:
#     print('走if')
# else:
#     print('走else')