print("Hello, World!")		#这是一个注释		#
print("Hello\nWorld!")		#这是一个换行		\n
print("Hello\\World!")	    #这是一个转义符	\
#转义字符   特殊的字符   无法”看见“的字符，与语言本身语法有冲突的字符。
#       \   续航   \n   换行   \'  单引号      \t		表示空4个字符，就是缩进，就是按一下tab键     \r  回车
print(r"01234\n56789")	        #把字符变成一个原始字符串	r
print("0123456"[-1])			#得倒数第一个字符
print("0123456"[2:5])	    	#代表步长   ：默认1即是2：5：1
print("01234567890123"[3:8:2])	#开始索引结束索引，截取不包括结束索引
print("01234 6 8 0123"[3::1])	#默认无穷大或无穷小，方向看步长方向
print(type(8))         #查看数据类型
num=8
print("输出一个浮点型%f%%"%num)	#输出一个%   %%
xcc="sddfhasi"
print("输出一个字符串%s"%xcc)
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
#python中%d表示格式化一个对象为十进制整数。使用后，在需要输出的长字符串中占位置。输出字符串时，可以依据变量的值，自动更新字符串的内容
#%3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数左侧补空格，所以%3d的打印结果是 14
print("num=%3d" % num)        # output: num=  8
#其他进制转换十进制
print("num=%3d" % num)
print(0b101)                           #0b(数字0和小写字母B)代表二进制
print(0o11)                            #0o(数字0和小写字母O)代表8进制	0o11	9
print(0x101)                           #0x(数字0和小写字母X)代表16进制	0x101 	257
print(bin(0xE))                        #其他进制转换二进制（默认十进制）
print(int(0o111))                      #其他进制转换十进制
print(hex(0o111))                      #hex其他进制转换16进制
print(oct(0o111))                      #oct其他进制转换8进制
# user_name = input("请输入您的用户名：")   #input语句中结果打印输出后，都会变成字符串
# if user_name == "admin":
#     password = input("请输入密码：")
#     if password =='123456':
#         print("登陆成功")
#     else:print("密码错误")
# else:
#     print("用户名错误");
# 位运算符(&与，|或，^异或，~取反,<<做移动，>>右移动)
a=(int(0b110101))  #53
b=(int(0b101001))  #40
print(a,b)
print(bin(a))
print(bin(b))
print(bin(a&b))
print(bin(a|b))
print(bin(a^b))
print(bin(~a))
print(bin(a<<3))
print(bin(b>>2))
print(~a)           #a取相反数-1=~a
                    #110101加1为110110加上符号-
# 练习题：如存在一个正整数为123，要求分别取出每个位数上的数值？
a=123;print(a//100,a%100//10,a%10)

#索引,截取,步长加强篇
print("01234567890123"[::1])	    #步长默认为1正向输出 [开始索引:结束索引:步长]
print("01234567890123"[::-1])	    #反转输出（默认时输出方向随步长方向）
print("01234567890123"[0::-1])      #0
print("01234567890123"[1:2:-1])	    #输出方向和步长方向不一致则为空
print("01234567890123"[0:-3:-1])    #空
print("01234567890123"[-2:3])       #空
print("01234567890123"[-2:3:-1])    #输出方向与步长方向一致
print("01234567890123"[-1:-7:-2])   #319   步长为2每次跨越2步

#字符串中常见的函数
strl = "abc_df"
print(strl.capitalize())         #把字符串的首字母变成大写
print(strl.title())              #当字符串中有下划线链接时，每段的开头都变为大写
print(strl.upper())              #把字符串全部变为大写
print("A".lower())              #把字符串的大写字母便变成小写
print("aaAa".count("a"))        #统计字符串出现的次数
print("abcdefg".strip("g"))     #删除字符串的开头或结尾
#删除字符串的右边/左边字符串或字符
print("abcdedcba".lstrip("a"))  #左
print("abcdedcba".rstrip("a"))  #右
print(str.split("_"))           #对字符串指定切割，以列表形式返回split('分割符','分割次数')
str1 = 's'
print(str1.join(strl))           #把字符串中的每个元素插入到另一个字符串中间
print(strl.startswith("a"))      #判断字符串是否以什么开头
print(strl.endswith("f"))        #判断字符串以什么结束
print(strl.isalnum())            #判断字符串是否为数字和字母组合
print(strl.isdigit())            #判断字符串是否为全数字
print(strl.isalpha())            #判断字符串是否为全字母
print(strl.istitle())            #判断字符串是否为大写字母开头
print(strl.isupper())            #判断字符串是否为大写字母
print(strl.islower())            #判断字符串是否为小写字母
#指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
#str.find(str, beg=0, end=len(string))
print(strl.find("c"))            #查找字符串出现某个字符的位置
print(strl.rfind("c"))           #返回字符串最后一次出现的位置，如果没有匹配项则返回 -1
print(strl.replace('c','z'))     #替换字符串中的内容

#定义列表的方法：
list1 = [1,2,3,'test']
print(list1)
print(type(list))
#字符串转换为列表通过list
str2 = '123456'
str2 = list(str2)
print(str2)
#修改
list1[2]='二'
print(list1)
#添加,默认最后位置
list1.append('添加元素')
print(list1)
#添加/合并两个列表,被添加列表元素默认添加在元列表的末尾
list2 = '789'
list1.extend(list2)
print(list1)

#在指定索引位添加元素
list3 = '0123456'
list3 = list(list3)
list3.insert(3,'添加')       #在索引位之前添加
print(list3)
#移除列表中的元素
list3.remove('0')
print(list3)                #一次只能移除一个
del list3[1]                #删除索引位的函数
del list3[1:3]              #删除索引位的函数
list3.pop(0)                #选择索引位删除（默认最后一个）
print(list3.pop())          #删除并默认打印最后一个值
print(list3)
list4 = '135798642'
list4 = list(list4)         #数字字符串会从int类型转换成char类型
list4.sort()                #从小到大排序
print(list4)
list4 = sorted(list4,reverse=True)     #从大到小排序
print(list4)
list4.reverse()             #反转输出
print(list4)
list5=(1,2,3,4,5,6)
print(list5.index(3))       #查找一个值返回该元素索引位,若是char型则不能查找
print(type(list5))

#tuple元组中的元素不能被修改   -----元组是列表的二次加工
tuple1 = (1,2,3,4,5,6)
tuple1 = list(tuple1)       #把元组转换成列表
print(tuple1)
tuple1 = tuple(tuple1)      #把列表转换成元组
print(tuple1)
#只能通过间接的方法，把元组转换成列表，修改列表中的值后再转换成元组
#当元组中只有一个元素时，必须在该元素的后面添加一个逗号，否则该数据结构不是元组
# tuple=('字符串')
# tuple=('元组',)
#元组常见函数：
tuple2 = (1,2,2,2,4,3,56,8,'数')
print(tuple2.index('数'))      #返回元组索引位
print(tuple2.count(2))         #统计
print(tuple2[5:8])             #打印

z = '123456478914234567489'
print(z.index('4'))
#找第8索引位后第一个4的索引位
x=z.find('4',8)

#定义字典的方法
dic1 = {"id":202101,"name":"zhangsan","age":18}         #创建一个字典
print(dic1)
list1 = [("id",202101),("name","zhangsan"),("age",18)]  #转换成字典
dic1 = dict(list1)
print(dic1)
dic2 = {}                                               #定义一个空字典
print(dic2)
#字典常见函数
dic3 = {"id":202101,"name":"zhangsan","age":18}
dic3["sex"] = 1             #添加键值,使用key:value形式
print(dic3)
dic3["age"] = 20            #更改
print(dic3)
#使用setdefault()函数添加键值对
dic3.setdefault('sex',1)    #添加新的键值对
print(dic3)
print(dic3.keys())          #取出字典中的键
print(dic3.values())        #取出字典中的值
print(dic3['name'])         #取出字典的键对应的值

#遍历字典(依次取出所有的键和值)   for ... in ...
for k in dic3:
    print(k,dic3[k])
for k,v in dic3.items():
    print(k,v)
dic1.clear()                #清空字典 clear()
del dic2                    #删除字典
del (dic3['id'])            #删除字典中的键值对
#使用python中自带的del方法删除
del (dic3['name'])
dic3.pop('age')

dic4 = {"id":202101,"name":"zhangsan","age":18}
#判断字典_是否有某个键,返回布尔值
print(dic4.__contains__('name'))
# if(dic4.__contains__('name')):
#     print('有这个键')
# else:
#     print('没有这个键')
dic4.popitem()              #随机删除键值对 popitem()  默认删除最后一对键值对
dic4.update(dic3)           #更新一个字典_字典3加到字典4后面
print(dic4)
#创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
dic4 = {}.fromkeys(['name'],'zhangsan')
print(dic4)

# #集合_去重(可变集合与不可变集合)
# #可变集合set
# list5 = [1,2,5,8,1,1,1,1,2,2,56,84]
# set1 = set(list5)
# print(set1)
# set1.add('添加')
# set.remove('添加')
# set1.pop()
# 不可变集合
# ste2 = frozenset

#常见语句
#if条件判断语句
# 单分支语句
# if  条件：
#     代码块
# else：
#     代码块
# 多分支语句
# if  条件:
#     代码块
# elif    条件：
#     代码块
# elif    条件：
#     代码块
#if嵌套语句
# if  条件：
#     if 条件：
#         代码块
#     else ：
#         代码块
# else：
#     代码块
# user = input('请输入你的用户名')
# if user == 'admin':
#     passwprd = input("请输入密码：")
#     if passwprd == '123456':
#         print('登陆成功！')
#     else :
#         print('密码错误')
# else:
#     print('用户名错误');
#三目运算
# user_name = input('请输入用户名：')
# print('管理员上线'if user_name == 'admin' else '普通用户上线')

# while  循环语句
# while   条件:
#     print()
#     变化条件
# print()
# i = 1
# while   i<=10:
#     print(i);i+=1
# # 1.打印出1到10的偶数
# i = 1
# while   i<=10:
#     if  i % 2 == 0:
#         print(i,end=' ')
#     i+=1
# # 2.打印1到10的自然数之和
# i=1;j=0
# while   i<=10:
#     if  i % 1 == 0:
#         j+=i
#     i+=1
# print('\n1到10的自然数之和为%s'%j,end=' ')

# for循环语句
# for XXX in XXX:
#     代码块
# for循环语句自带一个变量
# list6 = [1,2,3,4,5,6,7,8,9]
# for i   in list6:           #语句中的i只是一个变量名，可以随意修改
#     print(i,end=' ')
# sum=0
# for i   in range(1,11):
#     sum+=1
# print('\n1到10的自然数之和为%s'%sum,end=' ')

# 1、求出1 / 1 + 1 / 3 + 1 / 5⋯⋯+1 / 99的和
sum=0
for i   in range(1,100):
    if i%2!=0:
        sum+=1/i
print(sum)
# 2、用循环语句，计算2 - 10之间整数的循环相乘的值。
sum=1
for i   in range(2,11):
    sum*=i
print(sum)
# 3、用for循环打印九九乘法表
#方法一
# for i   in range(1,10):
#     for j in range(1,10):
#         if i>=j:
#             print(j,'x',i,'=',i*j,end='  ')
#     print()
#方法二
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,(i*j)),end=' ')     #format()函数：用于格式化输出
    print()
# 4、求每个字符串中字符出现的个数如：helloworld
# 方法零：
h = 'helloworld'
for i in list(set(h)):
    print(i,h.count(i),end='    ')
    # print('{}{}'.format(i, h.count(i)), end=' ')
# 方法一：
h = 'helloworld'
for i   in range(len(set(h))):               #序列的索引来迭代，可以用range()和len()组合
    print(list(set(h))[i],h.count(list(set(h))[i]),end='    ')
# h = 'helloworld'
# seth = list(set(h))
# for i   in range(len(seth)):               #序列的索引来迭代，可以用range()和len()组合
#     print(seth[i],h.count(seth[i]),end='    ')
# 方法二：
# str1='helloworld'
# dic={}
# for i in str1:
#     if dic.__contains__(i):
#         dic[i]= dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
# 方法三：
# str1='helloworld'
# list1=list(str1)
# set1=set(list1)
# for i in set1:
#     print(i,list1.count(i))
# # 5、实现把字符串str = "duoceshi"中任意字母变为大写(用input语句实现)
# 改变一个
# str1 = "duoceshi"
# a = input('请输入要变为大写的字母')
# print(str1.replace(a,a.upper()))
# 改变任意个
# str1 = "duoceshi"
# a = input('请输入要变为大写的字母')
# for i in a:
#     b = i.upper()
#     if i in str1:
#         str1 = str1.replace(i,b)
# print(str1)
# 6、求出1900 - 2017年的闰年？‘
# 方法一，分别输出：
s = ['世纪闰年'];p = ['普通闰年']
for i in range(1900,2018):
    if i%400 == 0:
        s.append(i)
    else:
        if i%4 == 0 and i%100 != 0:
            p.append(i)
print(s,'\n',p)
# 方法二，一起输出：
l1 = []         #创建一个空列表
for i in range(1900,2018):
    if i%4 == 0 and i%100 != 0:
        l1.append(i)
    elif i%400 == 0:
            l1.append(i)
print(l1)

# 普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）
# 世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）
# 7、分别打印100以内的所有偶数和奇数并存入不同的列表当中
j = []; o = []
for i in range(1,101):
    if  i%2==0:
        j.append(i)
    else:
        o.append(i)
print(j,'\n',o)
# 8、请写一段Python代码实现删除一个list = [1, 3, 6, 9, 1, 8]# 里面的重复元素
# 方法一：
list6 = [1, 3, 6, 9, 1, 8]
print(set(list6))
# 方法二：
list6 = [1, 3, 6, 9, 1, 8]
l1 = []
for i in list6:
    if i in l1:
        pass    #表示满足此条件不进行任何操作
    else:
        l1.append(i)
print(l1)
# 9、将字符串类似："k:1|k3:2|k2:9|...|kn:m", 处理成key:value或json格式, 比如
# {"k": "1", "k3": "2"}
a = "k:1|k3:2|k2:9"
dic = {}
a = a.split('|')
for i in a:
    # print(i)
    b = i.split(':')
    # print(b)        #查看列表
    dic.setdefault(b[0],b[1])   #字典添加键值对
print(dic)
# 10、把字符串user_controller转换为驼峰命名UserController
# 方法一：
name = 'user_controller'
print(name.title().replace('_',''))
# 方法二：
name = 'user_controller'
a = name.title()
b = a.split('_')    #以列表的形式返回
# print(b)          #查看列表
print(b[0]+b[1])    #字符串相加
# 方法三：
name = 'user_controller'
a = name.split('_')
res = ''
for i in a:
    b = i.capitalize()
    res+=b
print(res)
# print("你的年龄是多少:");age = input()
# print('第二个人的年龄是',age)
# print('第一个人的年龄是',age,end='*')
# print('第一个人的年龄是%s'%age,end=' ')

# python中的函数
# 内置函数（内建函数）：安装好python后就直接可以使用的函数；print();del;pass
# 第三方函数：需要通过python安装语法或者工具执行安装第三方库后才能使用的函数；如：使用pip install 安装selenium后才能使用的find_element_by_id()函数
# 自定义函数：用户根据自己业务功能需要实现的场景，自己编写的函数

# 定义函数：def
# 函数的调用

# 1在当前模块直接调用

# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

# from pythonProject1.py1.cs import *

# def login():
#     user = input('请输入用户名：')
#     if user == 'admin':
#         password = input('请输入密码：')
#         if password == '123456':
#             return '账户余额为86153人民币'
#         else:
#             return ' 密码错误！！！'
#     else:
#         return '请重新输入用户名：'
# def login():
#     user = input('请输入用户名：')
#     if user == 'admin':
#         password = input('请输入密码：')
#         if password == '123456':
#             return '登录成功'
#         else:
#             return ' 密码错误！！！'
#     else:
#         return '请重新输入用户名：'
#
# def select_amount():
#     value = login()      # 函数的传递
#     if value == "登录成功":
#         print("您的余额为：￥8888.88")
#     else:
#         print("登录失败！")
# select_amount()

# 练习题
# 11、冒泡排序
# 给一组无规律的数据从大到小或从小到大进行排序如：list = [2, 6, 9, 10, 18, 15, 1]
listl = [2, 6, 9, 10, 18, 15, 1]
for i in range(len(listl)):
    for j in range(i+1,len(listl)):
        if listl[i]>listl[j]:
            # print(listl)                           #验证步骤
            listl[i],listl[j] = listl[j],listl[i]     #实现位置互换
print(listl)
# 12、分析以下数字的规律，0 1 1 2 3 5 8 13 21 34用Python语言编程实现输出
j=1
i=0
while i <=34:
    print(i,end=' ')
    i,j=j,i+j
# 13、先定义一个字典来存放用户名
# 和密码如dic = {'admin': '123456', 'dcs46': '654321'}
# 要求如下：
# 1、从字典中获取用户完成登入，登入时判断用户是否存在
# 存在直接登入
# 2、如果输入的登入用户判断不存在字典，则调用注册方法，完成该用户的注册，注册成功后写入字典
# dic = {'admin': '123456', 'dcs46': '654321'}
# def login():
#     user_name = input('请输入用户名：')
#     if dic.__contains__(user_name):
#         pwd = input('请输入密码：')
#         if pwd == dic[user_name]:
#             print('登陆成功！')
#         else:
#             print('密码错误,请重新输入')
#     else:
#         print('用户名不存在，请注册后再登陆')
#         register()
# def register():
#     new_user_name = input('请输入要注册的用户名：')
#     if dic.__contains__(new_user_name):
#         print('用户名已存在，请重新输入')
#     else:
#         new_pwd = input('请输入同户名密码：')
#         new_pwd1 = input('请再次输入用户密码：')
#         if new_pwd==new_pwd1:
#             print('注册成功！')
#             dic.setdefault(new_user_name,new_pwd)
#             print(dic)
#         else:
#             print('两次密码不匹配，请重新输入')
# login()
# 14、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串
print()
# 方法一
# ab=input('请输入要去除的字符串')
strl='aabbcdbaaabc'
ab = 'ab'
while ab in strl:
    strl = strl.replace(ab, '')
print(strl)
# 方法二
# def del_ab(str):
#     s = str.replace('ab','')
#     if s.count('ab')>0:
#         del_ab(s)               #递归:在函数的内部调用函数本身
#     else:
#         print(s)
# del_ab(str)

# python中常见的内置函数
# 对字符串的格式化输出
# print('{}{}{}'.format(tr1,str2,a))
# 索引位输出
# print('{0} is number one'.format())
# print("{0}{1}{0} is number one".format(str2,str1))
list6=['姓名','男','18']
print('姓名:{0[0]} 性别:{0[1]} 年龄:{0[2]}'.format(list6))
print(list4)

#zip()函数    通常用于列表合并转换为字典的键和值
# 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
list7 = zip(list6,list4)
print(list7)
dic = dict(list7)
print(dic)

# open()    作用；用于操作Window系统内的TXT文件
# 1.创建一个用于打开文件的对象
# o = open(file=r'D:\Users\Administrator\Desktop\文档.txt',mode='r',encoding='utf-8')  #utf-8或者gbk
# all = o.read()          #读取全部内容
# all = o.readline()      #默认读取文件第一行内容
# all = o.readlines()     #以列表的形式读取
# print(all)
# 写的模式 w write
# o = open(file=r'D:\Users\Administrator\Desktop\文档.txt',mode='w',encoding='utf-8')
# o.write('hello \nword')
# o.close()       #关闭文件链接对象，使写入的内容能够直接执行，写入内部文件，而不是停留在系统缓存中：同时还起到释放资源的目的
# 追加模式    a   append
# o = open(file=r'D:\Users\Administrator\Desktop\文档.txt',mode='a,encoding='utf-8')
# open()函数的扩展用法
# with open(file=)as f:
#     f.write('\n写入内容')
# isinstance()    作用：用来判断数据结构的类型
# print(type(list7))
# print(isinstance(list7,zip))

# 15、题目：传入一个json串, 返回一个字典, 字典只取出json最底层的数据, 中间如果有字典格式的字符串也需要进行处
# 理, 请以下面的数据为例, 请用递归的方法实现。
# 数据输入json = {"a": "aa", "b": [{"c": "cc", "d": "dd"}, {"f": {"e": "ee"}}]}输出：dic = {'a': 'aa', 'c': 'cc', 'e': 'ee', 'd': 'dd'}
json = {"a": "aa", "b": [{"c": "cc", "d": "dd"}, {"f": {"e": "ee"}}]}
dic={}
def read_json(json):
    for k,v in json.items():
        if isinstance(v,list):
            for i in v:
                read_json(i)
        elif isinstance(v,dict):
            read_json(v)
        else:
            dic.setdefault(k,v)
    return dic
print(read_json(json))
# 16、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000
# 之间的水仙花数
# （其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。
def sxh():
    for i in range(100, 1000):
        x = i // 100
        y = i % 100 // 10
        z = i % 10
        if i == x**3 + y**3 + z**3:
            print(i, end=' ')
sxh()
# 17、用递归的方法求出n的阶乘？4的阶乘结果为?
# n!=1×2×3×...×(n-1)×n。阶乘亦可以递归方式定义：0!=1，n!=(n-1)!×n
print()
def jc(n):
    if n==0 or n==1:
        return (1)
    else:
        return (n*jc(n-1))
print(jc(4))
# 18、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 并最终通过#get(key)的方式取出对应的value值。
# url地址如下：
#http://ip:port/extername/get_account_trade_record.json?#page_size=20&page_index=1&user_id=203317&trade_type=0"
str1='http://ip:port/extername/get_account_trade_record.json?#page_size=20&page_index=1&user_id=203317&trade_type=0'
def read_url(str):
    dic = {}
    for i in str1.split("?")[1].strip('#').split('&'):
        dic.setdefault(i.split('=')[0],i.split('=')[1])
        # c=i.split('=')
        # dic.setdefault(c[0],c[1])
    print(dic)
read_url(str1)

# python模块内可以包含：变量、常量、函数（方法）、类
# 1.直接导入整个模块
# import time                       #导入time这个模块
# print(time.time())
# 2.导入模块内的单个方法
# from  time import time            #从time模块内导入time方法
# print(time())
# 3.导入模块内的多个方法
# from time import time,strftime,asctime  #从time模块内导入time、strftime、asctime三个方法
# #导入多个方法之间，用英文逗号间隔
# 4.导入模块内的所有方法、变量等
# from time import *                #从time模块内导入的所有方法、变量等    *代表所有
# from pythonProject1.py1.xxx.py    #找不到往上层找
# 5.同时导入多个模块
# import time,string,re,random      #同时导入多个模块

# python中常见的模块
# 1.time模块
import time
# time模块中常见的方法：
print(time.time())          #1970到现在经过的秒数   time()
print(time.ctime())         #固定格式的当前时间  ctime()
# time.sleep(3)             #休眠-强制等待，使系统进程停止多少时间-单位秒    sleep()
print(time.asctime())       #转换为asc码显示当前时间  asctime()
print(time.strftime('%Y-%m-%d-%H-%M-%S'))   #时间格式化  strftime()

# 2.random模块
# import random
# 生成随机浮点数、整数、字符串，甚至帮助你随机选择列表序列中的一个元素，打乱一组数据等
# random模块中常见的方法：
# random.random() #该方法是生成0-1之间的浮点数，但是能取到0，但是取不到1
# random.randint(x,y) #该方法生成指定范围内整数，包括开始和结束值
# python中random模块
# random.randrange(x,y,step) #生成指定范围内的奇数或偶数，不包括结束值    （开始值，范围，步长）
# random.randrange(1,10,2)
# random.randrange(0,10,2)

# random.sample(seq,n) #从序列seq中选择n个随机且独立的元素
# random.sample(seq,3)    #返回的元素以列表形式存储

# random.choice(list1) #从序列中随机选一个元素生成随机字符
# print(random.choice(list1))
# random.shuffle(list1) #洗牌（随机数列）
# print(list1)

# hashlib.md5() #MD5加密
# import hashlib
# md5 = hashlib.md5()#创建一个hashlib模块内的MD5方法的对象，赋值给到一个为md5的变量
# str1 = '123456'
# md5.update(str(str1).encode('utf-8'))
# print(md5.hexdigest())

# import string,random
# print(string.digits)#输出0-9的数字
# print(string.ascii_letters)#输出26个大小写字母
# print(string.ascii_uppercase)#输出26个大写字母
# print(string.ascii_lowercase)#输出26个小写字母

# 1、使用random模块随机生成手机号码、自己定义手机号码开头的前三位
# 方法一
# def h():
#     str3 = input('请输入号码前三位数：')
#     import random
#     for i in range(8):
#         str3+=str(random.randint(0,9))
#     print(str3)
# h()
# 方法二
# def h():
#     import random
#     str3 = input('请输入号码前三位数：')
#     str3 += ''.join(random.sample('0123456789',8))
#     print(str3)
# h()
# 方法三
# str3 = '0123456789'
# def ra_phone(str3):
#     a = '123'
#     import random
#     for i in range(8):
#         b =random.choice(str3)
#         a+=b
#     print(a)
# ra_phone(str3)
# 方法四
# str3 = '0123456789'
# def ra_phone(str3):
#     a = '123'
#     import random
#     l = random.sample(str3, 8)
#     for i in l:
#         a += i
#     print(a)
# ra_phone(str3)
# 2、用random模块随机生成6位数验证码
import  string,random
str2 = string.digits+string.ascii_letters
# print(str2)
def verify(n):
    res = ''
    for i in range(6):
        res+=random.choice(n)
    print(res)
verify(str2)
# 3、通过md5加密算法把随机生成的6位数验证码进行加密返回16进制的字符串
import hashlib
str1 = string.digits+string.ascii_letters
def verify(str):
    res = ''
    for i in range(6):
        res += random.choice(str)
    return

def v_md5(str2):
    md5 = hashlib.md5()
    md5.update(str(str2).encode('utf-8'))
    print(md5.hexdigest())
v_md5(verify(strl))

# 3.os模块
# import os
# os模块提供了多数操作系统的功能接口函数。当os模块被导入后，它会自适
# 应于不同的操作系统平台，根据不同的平台进行相应的操作，在python编
# 程时，经常和文件、目录打交道，所以离不了os模块。
# os模块中常见的方法：
# os.getcwd()获取当前执行命令所在目录
# print(os.getcwd())
# os.path.isfile()判断是否文件
# path = 'D:\Program Files\python\python.txt'
# print(os.path.isfile(path1))
# python中os模块
# os.path.isdir() #判断是否是目录
# os.path.exists() #判断文件或目录是否存在
# os.listdir(dirname) #列出指定目录下的目录或文件
# path1 = 'D:\Program Files\python\python5'
# print(os.listdir(path2))
# os.path.split(name) #分割文件名与目录
# print(os.path.split(path2))
# os.path.join(path,name) #连接目录与文件名或目录
# print(os.path.join(path1,'python.txt'))

# os.mkdir(dir) #创建一个目录
# os.rename(old,new) #更改目录名称
# print(path2)
# os.rename(path1,'python2')

# 4.re模块
# 实现一个编译查找，一般在日志处理或者文件处理时用的比较多，正则表达式主要用于模式匹配和替换工作。
# 实现一个编译查找，一般在日志处理或者文件处理时用的比较多
# 正则表达式主要用于模式匹配和替换工作。
# 预定义字符集匹配：
# \d:数字0-9
# \D:非数字
# \s:空白字符
# \n:换行符
# \r:回车符
# python中re正则模块
# re模块数量词匹配：
# 符号^：表示的匹配字符以什么开头
# 符号$：表示的匹配字符以什么结尾
# 符号*：匹配*前面的字符0次或n次
# eg：ab* 能匹配a 匹配ab 匹配abb
# 符号+：匹配+前面的字符1次或n次
# 符号?：匹配?前面的字符0次或1次
# 符号{m}：匹配前一个字符m次
# 符号{m,n}：匹配前一个字符m到n次(包括n次)，m或n可以省略，mn都是
# 正整数
# re模块相关函数
# 1、match
# 从第一个字符开始匹配，如果第一个字符不是要匹配的类型、则匹配失败并报错
# 注意：如果规则带了'+',则匹配1次或者多次，无'+'只匹配一次
# 2、search
# 从第一个字符开始查找、一找到就返回第一个字符串，找到就不往下找，找不到则报错
# 3、findall
# 从第一个字符开始查找，找到全部相关匹配为止，找不到返回一个列表[]
# 4、compile
# 编译模式生成对象，找到全部相关匹配为止，找不到返回一个列表[]

# Python中常见的模块：
# time模块
# random模块
# hashlib模块
# os模块
# re模块
# string模块
# xlrd模块
# json模块
# sys模块

# 19、存在一个文件, 文件名test.txt
# 内容如下：
# 01 success
# 02 fail
# 03 fail
# 04 success
# ....请使用Python语言编写程序实现统计该文件中
# 有多少个success
# 多少个fail的功能？
# path=r'D:\Program Files\python\test.txt'
# dic={}
# def count(path):
#     o = open(file=path, mode='r', encoding='utf-8')
#     list1 = o.readlines()
#     print(list1)
#     for i in list1:
#         a=i.strip('\n').split(' ')[1]
#         print(a)
#         if dic.__contains__(a):
#             dic[a]=dic[a]+1
#         else:
#             dic[a]=1
#     print(dic)
# count(path)
def read_file1(file1):
    dic = {}
    file1 = open(file=r'D:\Program Files\python\test.txt', mode='r', encoding='utf-8')
    all = file1.readlines()
    print(all)
    for i in all:
        a = i.strip('\n')
        # print(a)
        b = a.split(' ')[1]
        # print(b)
        if b in dic:
            dic[b]=dic[b]+1
        else:
            dic[b]=1
    print(dic)
    print('出现次数"success"的次数为:%d次'%dic['success'])
    print('出现"fail"次数为:%d次'%dic['fail'])
read_file1(r'D:\Program Files\python\test.txt')

# 20、一个txt文件中已知数据为：
# C4D
# C4D/maya
# C4D
# C4D/su
# C4D/max/AE
# 统计每个字段出现的次数，比如C4D，maya, 请用最熟悉的语言或者伪代码实现该需求
def read_file1(file1):
    dic = {}
    file1 = open(file=r'D:\Program Files\python\test.txt', mode='r', encoding='utf-8')
    a = file1.readlines()
    print(a)
    for i in a:
        # print(i)
        b = i.strip('\n').split('/')
        # print(b)
        for j in b:
            if j in dic:
                dic[j]=dic[j]+1
            else:
                dic[j]=1
    print(dic)
read_file1(r'D:\Program Files\python\test.txt')
path=r'D:\Program Files\python\test.txt'
def a(path):
    dic={}
    o=open(file=path,mode='r',encoding='utf-8')
# 21、统计一个文件的行数，以e:\\write.txt文件为例(内容自己建)
path=r'D:\Program Files\python\test.txt'
def count_len(path):
    o=open(file=path,mode='r',encoding='utf-8')
    all=o.readlines()
    print(len(all))
count_len(path)

# 22、登录和注册
# 要求如下：
# 1、调用本地文件（user.txt)完成登录，如果存在则调用本地文件中用户
# 和对应的密码进行登录，用户在本地文件中的格式如：admin:123456 xiao:123123
# 2、登录用户不存在则调注册函数，将注册好的用户写入本地user.txt文件中，写入不能覆盖已有用户。
# 3、用户名的长度大于等于6位，小于等于8位，用户密码大于等于6位小于等于8位。
# path=r'D:\Program Files\python\test.txt'
# def read_txt(path):
#     dict1 = {}
#     o=open(file=path,mode='r',encoding='utf-8')
#     all=o.readlines()
#     print(all)
#     a=all[0].split(' ')
#     for i in a:
#         b=i.split(':')
#         dict1.setdefault(b[0],b[1])
#     return dict1
# def login():
#     dict2=read_txt(path)
#     user_name = input("请输入您的用户名：")
#     if dict2.__contains__(user_name):
#         user_pwd = input("请输入您的用户密码：")
#         if user_pwd == dict2[user_name]:
#             print("登录成功")
#         else:
#             print("密码错误,请重新输入")
#     else:
#         print("用户不存在，请注册后登录！")
#         b()
# def b():
#     dict2=read_txt(path)
#     new_user_name = input("请输入你要注册的用户名：")
#     if not dict2.__contains__(new_user_name):
#         if len(new_user_name)>=6 and len(new_user_name)<=8:
#             new_user_pwd = input("请输入您注册的用户密码：")
#             new_user_pwd1 = input("请再次输入您注册的用户密码:")
#             if new_user_pwd == new_user_pwd1:
#                 if len(new_user_pwd)>=6 and len(new_user_pwd)<=8:
#                     print("注册成功!")
#                     o=open(file=path,mode='a',encoding='utf-8')
#                     all=o.write('\n'+new_user_pwd1+':'+new_user_pwd)
#                     o.close()
#                     # write_user(new_user_name,new_user_pwd)
#                 else:
#                     print('密码长度非法!')
#             else:
#                 print('两次密码输入不一致!')
#         else:
#             print('注册的用户名长度非法!')
#     else:
#         print('用户名已存在，请重新输入!')
# login()
# 23、使用os模块写一个递归调用打印出e:\\home下的所有文件名的绝对路径？
import os
path = r'D:\Program Files\python\python'
def abs_path(path):
    a = os.listdir(path)
    for i in a:
        b = os.path.join(path,i)
        if os.path.isdir(b):
            abs_path(b)
        else:
            print(b)
abs_path(path)

# 24、用正则方法实现统计e:\\python文件中指定字符如"python"的行数?（文件中的python字符）
import re
path = r'D:\Program Files\python\test.txt'
def count_py(path):
    res = 0
    py_re = re.compile('python')
    o = open(file=path,mode='r',encoding='utf-8')
    all = o.readlines()
    for i in all:
        a = i.strip('\n')
        b = py_re.findall(a)
        if len(b)>0:
            res+=1
    print(res)
count_py(path)
# 25、使用正则完成市面上手机规则的编写？（手机号：11位）
import random,re,string
strl = string.digits
def ra_phone(strl):
    while True:             #当条件成立是，无限循环
        p_re = re.compile('^[1][3456789]\d{9}')
        res = ''
        for i in range(11):
            a = random.choice(strl)
            res += a
        b = p_re.findall(res)
        if len(b) > 0:
            print(b)
            break           #当打印出结果后，则停止整个循环
ra_phone(strl)
# 26、用正则实现写一段代码统计e:\\log文件中error和warning单词出现的次数分别为几次?
# 文件内容如下：
# warningabchelloerror
# warningerror
# warning
# errorwarningwarning
path = r'D:\Program Files\python\test.txt'
def count(file):
    dic = {}
    o = open(file=file,mode='r',encoding='utf-8')
    all = o.read()
    a = all.split('\n')
    w_re = re.compile('warning')
    e_re = re.compile('error')
    for i in a:
        # print(i)
        b = w_re.findall(i)
        c = e_re.findall(i)
        for j in b:
            if dic.__contains__(j):
                dic[j] = dic[j]+1
            else:
                dic[j] = 1
        for k in c:
            if dic.__contains__(k):
                dic[k] = dic[k]+1
            else:
                dic[k] = 1
    print(dic)
count(path)
# #27、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串（用正则表达式来实现）
import re
str1 = 'aabbcdbaaabc'
def del_ab(str):
    a = str.replace('ab','')
    ab_re = re.compile('ab')
    b = ab_re.findall(a)
    # print()
    if len(b)>0:
        del_ab(a)
    else:
        print(a)
del_ab(str1)

# python中的类class
# 类的分类：
# 新式类     class 类名(object)：
# 经典类     class 类名：
class people(object):       #定义一个名为peopie的新式类，且继承了object这个基类
                            #objeck是所有类的基类也即是类的起源
    head = 1                #head是类变量
    def __init__(self,name):     #构造函数，用来初始化整个类：在定义类的时候可以不写，如果不写则python
        # 调用默认的构造函数
        self.name = name    #name是实例变量

    def func(self):         #实例化话方法
        print('打篮球')

# 实例化对象
p = people('小明')            #为people这个类创建一个名为p的实例化对象
p.func()                     #用p这个实例化对象调用people类中的func1这个方法
# 类中的变量和方法
class Peole:
    head = 1
    def __init__(self,name):
        self.name = name

    def func1(self,name1):
        print(name,'打篮球')

p = Peole('xiaoming')
# p.func1('小张')
# 变量的调用
# print(Peole(p),head)        #类名的调用类变量，必须传入一个对象
# print(p.head)               #对象调用类的变量
# print(Peole(p).name)        #类名调用实际变量
# print(p.name)               #对象调用实例变量

# 类的三大特性
# 封装：把函数写在类的内部
class people:
    def __init__(self,name):
        pass

    def __init__(self,name):
        self.__name = name          #__name 叫做私有变量

    def func2(self):
        print(self.__name)
p = people('zhangsan')
p.func2()

class Func:
    def __init__(self):
        pass
    def func1(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print(j,'x',i,'=',j*i,end=' ')
            print(' ')
f = Func()
f.func1()

# 继承
class Father(object):
    def ___init__(self):
        pass
    def drink(self):
        print('喜欢喝酒')

# class Sun(Father):      #定义一个类，同时继承Father这个类
# 继承构造函数
# 方法一、
# def __init__(self):
#     Father.__init__(self):
# 方法二、
# def __init__(self):
#     super(Father,delf).__init__(self)

#     def car(self):
#         print('喜欢跑车')
#     def disco(self):
#         print('喜欢蹦迪')

# s = Sun()
# s.car()

#
# # 多态
# class Animal(object):
#     def __init__(self):
#         pass
#
#     def func(self):
#         print('这是一个动物类')
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(seif)
#
#     def func(self):
#         print('这是一只哈士奇')
#
#     def eat(self,name):
#         print(name+'骨头')
#
# class Dog_1(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#
#     def func2(self):
#         print('这是一只阿拉斯加狗')
#
#     def eat(self):
#         print('吃狗粮')

# selenium      UI自动化
# 打开浏览器
# 1.创建一个打开浏览器的驱动对象
from selenium import webdriver
driver = webdriver.Chrome()     #实际上打开一个空浏览器
# 2.打开一个网页地址
driver.get('http://www.baidu.com')  #通过使用driver对象调用get方法打开百度网页
# 在同一个浏览器内同时打开两个不同的网页地址
# w = 'window.open("http://www.baidu.com")'
# driver.execute_script(w)
# 在打开的窗口内，重新打开一个新的地址，覆盖原有打开的网页
# driver.get('http://www.qq.com')

# UI自动化之元素定位
# 1.id定位
# ele = driver.find_element_by_id('kw')   #使用driver对象调用find_element_by_id()放定位id值为kw的元素，并赋值变量给ele
# ele.send_keys('selenium')               #使用定位到的元素变量值调用send_key()方法，在输入框内输入selenium
# driver.find_element_by_id('kw').send_keys('selenim')
# 2.name定位
# 使用driver对象调用find_element_by_name()放定位name元素为wd的元素，
# 再调用send_key()方法在该元素位置输入selenium
# driver.find_element_by_name('wd').send_keys('selennium')
# 3.class定位
# driver.find_element_by_class_name('s_ipt').send_keys('selenium')
# 4.xpath定位
#//*[@id='kw']  //表示相对路径，*号表示任意标签[]内部的内容表示元素定位中可用的标识符
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenim')      #xpath中的id定位
# driver.find_element_by_xpath('//*[@name="wd"]').send_keys('selenim')    #xpath中的name定位
# driver.find_element_by_xpath('//*[@class="s_ipt"]').send_keys('selenim')   #xpath中的class定位
# driver.find_element_by_xpath('//input[@autocomplete="off"]').send_keys('selenim')
# driver.find_element_by_xpath('//*[@id="kw" and @name="wd"]').send_keys('selenim')       #组合定位
# driver.find_element_by_xpath('//*[@id="form"]/span[1]/input[1]').send_keys('selenim')   #父子定位

# 5.css定位
# driver.find_element_by_css_selector("#kw").send_keys('selenim')     #css中的id定位
# driver.find_element_by_css_selector('.s_ipt').send_keys('selenim')     #css中的class定位
# driver.find_element_by_css_selector('[id="kw"][name="wd"]').send_keys('selenim')     #css中的组合定位
# driver.find_element_by_css_selector('form>span>input').send_keys('selenim')             #父子定位

# 6.link定位
# driver.find_element_by_link_text('新闻').click()  #链接文本值定位

# 7.partial_link定位：模糊匹配定位
# driver.find_element_by_partial_link_text('hao').click()

# 8.tag_name定位：标签名定位
# eles = driver.find_elements_by_tag_name('input')    #根据标签名找出
# for i in eles:
#     if i.get_attribute('id')=='kw':
#         i.send_keys('selenim')
# 9.执行javaScript脚本语法
# js = 'document.getElementById("kw").value="selenium"'
# driver.execute_script(js)

# 页面常见控件
# 1.输入框和按钮的操作
# 如：实现论坛的登陆功能？
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://192.168.30.129/bbs')
sleep(1)    #休眠(强制等待)：作用是使用系统进程强制等待多少秒
driver.find_element_by_id('ls_username').send_keys('admin')
sleep(0)
driver.find_element_by_id('ls_password').send_keys('123456')
sleep(0)
driver.find_element_by_class_name('pn').click()

# pyinstaller -F cs.py      #生成exe文件

# 按钮、链接、隐藏框
# 按钮
# from selenium import webdriver
# from time import sleep
# sleep(1)
driver.get('http://www.baidu.com')
# sleep(1)
# driver.find_element_by_id('kw').send_keys('selenium')
# sleep(1)
# driver.find_element_by_id('su').click()

# 链接
# driver.find_element_by_link_text('hao123').click()

# 隐藏框
# from selenium.webdriver.common.action_chains import ActionChains
# ele=driver.find_element_by_name('tj_briicon')
# ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_class_name('pn').click()

# python自动化中的三种等待方式
# 1.强制等待：就是time模块内的sleep方法
# sleep(20)
# 2.隐式等待:selenium库内的webdriver模块内的implicitly_wait()方法。
# driver.implicitly_wait(20)
# 3.显式等待：针对页面的单个元素，明确等待某个元素在规定的时间内是否加载完成
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# ele=driver.find_element_by_id('kw')
# WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID,"kw")))

# python自动化中的断言方法
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# 1.获取页面元素的文本值
# value = driver.find_element_by_id('s-usersetting-top').text
# print(value)
# if value =='设置':
#     print('页面打开成功')
# else:
#     print('页面打开失败')
# 2.获取页面元素的属性值
# ele = driver.find_element_by_id('s-usersetting-top')
# value = ele.get_attribute('name')
# print(value)
# assert value == 'tj_settingicon'        #asser是python语言自带的断言关键字，当断言成功后，没有任何信息输出
#                                         #只有断言失败后，才会抛出异常信息
# 3.获取页面的title
# title = driver.title
# # print(title)
# assert title =='百度一下，你就知道'

