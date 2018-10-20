def sayHello(name,sex='男',*wjx,**jmy):
    #name必填参数，位置参数
    #默认值参数，不是必填的
    #可变参数，也不是必填的 *args
    #关键字参数，也不是必填的  **kwargs  kwargs他是一个字典
    # 如果这四种参数类型，你要连起来用的话，必须按照 必填参数、默认值参数、可变参数、关键字参数

    #可变参数和关键字参数在参数比较多的情况下和参数不确定是多少个的情况下，可以用
    print('*args的值是',wjx)
    print('*kwargs的值是',jmy)
    print('名字是%s ，性别是 %s'%(name,sex))
# def run_case(kwargs):
#     print(kwargs)
# name = 'name'
# sex = 'sex'
# sayHello(name,sex,186152323232,'回龙观','hahahah','sdfsdfs','sdfsdfsdf','ggsgsdf',a=1,b=2)

def say1(name,addr,money,age=28):
    print(name,age,addr,money)
# say1('wjx','addr',1000)
# say1(addr='addr',money=100,name='wjx',age=19) #
say1('wjx','beijing',age=399,money=10000)  #这种写法不行
#在调用函数的时候，位置传参这种方式是要写在关键字传参的前面的
#关键字参数肯定要在位置参数后面

#局部变量和全局变量

#局部变量就是在函数内部定义的变量，在函数内可以随便用，一但出了函数，那么就不能用了
#全局变量是大家都可以用的变量
#全局变量是list和字典的话，不需要用global声明，就可以直接修改
#       其他的类型，（str，元组，集合。。）如果要修改值，那么必须使用global声明
#尽量不要全局变量，因为不安全

ljt=['水瓶']
# def jmy():
#     money = 200
#     shuichi=[]
#     ljt.append('扔了2000')
#     print('贾梦缘的垃圾桶',ljt)
#     print(money-100)
# def wjx():
#     ljt.append('扔1000')
#     money = 10000
#     print(money-5000)
# jmy()
# wjx()
# print('外面的垃圾桶',ljt)

#
# res = None
# def calc(a,b):
#     global res
#     res = a*b
# calc(1,2)
# print(res)

# money = 0
# def chuzhang():
#     global money
#     money = 100000
#
# def lsx():
#     global money
#     money = money - 5000
#     print(money)
# chuzhang()
# lsx()
# print('lsx花完之后还有%s'%money)




qianbao ={'redbag':90000}
def ls():
    qianbao['redbag']=qianbao['redbag']+100
# def pdj():
#     qianbao['qian']=2000
# ls()
# print(qianbao)
# pdj()
# print(d)


#递归
 #说白了就函数自己调用自己
# 递归调用的特性：
#


# 1. 必须有一个明确的结束条件
#
# 2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
#
# 3. 递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
def aaa():
    while True:
        num = int(input('请输入一个数字：'))
        if num%2==0:
            print('是整数')
            return
        else:
            print('奇数')
# aaa()
def new_aa():
    num = int(input('请输入一个数字：'))
    if num % 2 == 0:
        print('是整数')
        return
    else:
        print('奇数')
        new_aa()
new_aa()