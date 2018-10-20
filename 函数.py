#函数、方法
#函数就是实现一个功能一段代码。
#为了帮你节省代码的
def hello():
    print('hello')
#函数必须调用他才会执行
#函数名加上()才是调用函数
# def sayName(name,age,sex):  #形式参数
#     #位置参数、必填参数
#     print('say %s'%name)
#     print('say %s'%age)
#     print('say %s'%sex)
#     #函数体
#
# sayName('蓝夏',18,'男')  #实际参数
# sayName('俊熹')  #实际参数
# sayName('国茹')  #实际参数

#你定义函数的时候，写的入参叫做形参，你调用函数的时候，传的值叫做实参

# s='jmy'
# new_s = s.replace('jmy','lanxia')
# print(new_s)

def calc(a,b):
    return a*b

#函数如果要有返回值的话，就写rerurn，函数里面遇到return函数立即结束
#函数不是必须有返回值的，如果不写return，默认返回None
#函数里不return，你是获取不到运算结果的
# res= calc(10,20)
# print('a*b=%s'%res)
#1、写一个能判断输入的字符串是不是小数类型的

#1、判断小数的个数是否是1  count
#2、's.23'，判断小数点右边是否为整数 isdigit
#3、判断小数点左边的，1、为整数 isdigit
                      #2、如果是负整数的话，取负号右边的， 为整数的 isdigit
# def is_float(s):
#     s =str(s)
#     if s.count('.')==1:
#         new_s = s.split('.')
#         left_num = new_s[0]
#         right_num = new_s[-1]
#         if right_num.isdigit():
#             if  left_num.isdigit():
#                 return True
#             elif left_num.count('-')==1 and left_num.startswith('-'):
#                 tmp_num = left_num.split('-')[-1]
#                 if tmp_num.isdigit():
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False

# print(is_float('5.6'))
# print(is_float('3-3.8888'))
# print(is_float('-.5'))
def is_float(s):
    s =str(s)
    if s.count('.')==1:
        new_s = s.split('.')
        left_num = new_s[0]
        right_num = new_s[-1]
        if right_num.isdigit():
            if  left_num.isdigit():
                return True
            elif left_num.count('-')==1 and left_num.startswith('-'):
                tmp_num = left_num.split('-')[-1]
                if tmp_num.isdigit():
                    return True
    return False

#函数即变量
wjx = is_float
# print(wjx('-2.'))
def weclome():
    print('欢迎光临购物系统')
def buy():
    print('选择你要买啥：')
def exit_sys():
    exit('退出程序')
choice = input('请输入你的选择：1欢迎 2退出 3买东西')
name = 'wyf'
menu ={
    "1":weclome,
    "2":exit_sys,
    "3":buy,
    "4":name
}
menu[choice]()


# if choice=='1':
#     weclome()
# elif choice=='2':
#     exit_sys()
# elif choice=='3':
#     buy()
# else:
#     print('输入错误')
