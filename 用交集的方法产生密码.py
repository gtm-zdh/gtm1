import random,string
num = input('请输入一个数字：').strip()
pwds = set()
if num.isdigit():
    while len(pwds)<int(num):
        passwd = set(random.sample(string.ascii_letters+string.digits,8))
        set1 = set(string.ascii_uppercase).intersection(passwd)
        set2 = set(string.ascii_lowercase).intersection(passwd)
        set3 = set(string.digits).intersection(passwd)
        if set1 and set2 and set3:
            str_passwd=''.join(passwd)+'\n'#要把产生的密码变成字符串，因为前面已经给变成集合了
            pwds.add(str_passwd)
    fw =open('pwds.txt','w')
    fw.writelines(pwds)
else:
    print('你输入的不是数字')

