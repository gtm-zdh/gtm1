#1、1分钟之内ip访问次数超过200次的，就给他的ip加入黑名单，不让他
#x需求分析：
    #1、读日志，1分钟读一次
    #2、获取这1分钟之内所有访问的ip
    #3、判断ip出现的次数，如果出现200次，那么就加入黑名单
    #4、因为每次读文件的时候，都是从文件开头开始读的，所以导致重复读了以前已经读过的
    #5、要记录每次读完之后的，文件指针，再用seek移动到那个位置  tell()
def agent_log():
    import time
    pin=0
    while True:
        ips = []
        fr = open('access.log')
        fr.seek(pin)
        for line in fr:
            ip = line.split()[0]
            ips.append(ip)
        new_ips = set(ips)
        for new_ip in new_ips:
            if ips.count(new_ip)>200:
                print('加入黑名单的ip是：%s'%new_ip)
        pin = fr.tell() #记录读完的指针位置
        time.sleep(60)






# line = '178.210.90.90 - - [04/Jun/2017:03:44:13 +0800] "GET /wp-includes/logo_img.php HTTP/1.0" 302 161 "http://nnzhp.cn/wp-includes/logo_img.php" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4" "10.3.152.221"'
# print(line.split()[0])
# import time
# pin = 0#存的文件指针
# while True:
#     with open('access.log') as fr:
#         ips = []
#         fr.seek(pin)#移动指针
#         for line in fr:
#             ip = line.split()[0] #取ip地址
#             ips.append(ip)
#         new_ips = set(ips)#ip去重
#         for new_ip in new_ips:
#             if ips.count(new_ip)>200:
#                 print('要把这个ip加入黑名单：%s' % new_ip)
#         pin = fr.tell()#记录已经读到了什么位置
#     time.sleep(2)
#
#     #要判断每个ip出现的次数是不是超过200
# # 天生就会去重




