print("Hello, World!");		#这是一个注释		#
print("Hello\nWorld!");		#这是一个换行		\n
print("Hello\\World!");	    #这是一个转义符	\
#转义字符   特殊的字符   无法”看见“的字符，与语言本身语法有冲突的字符。
#       \   续航   \n   换行   \'  单引号      \t		表示空4个字符，就是缩进，就是按一下tab键     \r  回车
print(r"01234\n56789")	        #把字符变成一个原始字符串	r
print("0123456"[-1]);			#得倒数第一个字符
print("0123456"[2:5]);	    	#代表步长   ：默认1即是2：5：1
print("01234567890123"[3:8:2]);	#开始索引结束索引，截取不包括结束索引
print("01234 6 8 0123"[3::1]);	#默认无穷大或无穷小，方向看步长方向
print(type(8));         #查看数据类型
num=8
print("输出一个浮点型%f%%"%num);	#输出一个%   %%
xcc="sddfhasi"
print("输出一个字符串%s"%xcc);
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
str = "abc_df"
print(str.capitalize())         #把字符串的首字母变成大写
print(str.title())              #当字符串中有下划线链接时，每段的开头都变为大写
print(str.upper())              #把字符串全部变为大写
print("A".lower())              #把字符串的大写字母便变成小写
print("aaAa".count("a"))        #统计字符串出现的次数
print("abcdefg".strip("g"))     #删除字符串的开头或结尾
#删除字符串的右边/左边字符串或字符
print("abcdedcba".lstrip("a"))  #左
print("abcdedcba".rstrip("a"))  #右
print(str.split("_"))           #对字符串指定切割，以列表形式返回split('分割符','分割次数')
str1 = 's'
print(str1.join(str))           #把字符串中的每个元素插入到另一个字符串中间
print(str.startswith("a"))      #判断字符串是否以什么开头
print(str.endswith("f"))        #判断字符串以什么结束
print(str.isalnum())            #判断字符串是否为数字和字母组合
print(str.isdigit())            #判断字符串是否为全数字
print(str.isalpha())            #判断字符串是否为全字母
print(str.istitle())            #判断字符串是否为大写字母开头
print(str.isupper())            #判断字符串是否为大写字母
print(str.islower())            #判断字符串是否为小写字母
#指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
#str.find(str, beg=0, end=len(string))
print(str.find("c"))            #查找字符串出现某个字符的位置
print(str.rfind("c"))           #返回字符串最后一次出现的位置，如果没有匹配项则返回 -1
print(str.replace('c','z'))     #替换字符串中的内容

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
list = [1, 3, 6, 9, 1, 8]
print(set(list))
# 方法二：
list = [1, 3, 6, 9, 1, 8]
l1 = []
for i in list:
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
list = [2, 6, 9, 10, 18, 15, 1]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            print(list)                           #验证步骤
            list[i],list[j] = list[j],list[i]     #实现位置互换
print(list)
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
str='aabbcdbaaabc'
ab = 'ab'
while ab in str:
    str = str.replace(ab, '')
print(str)
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
print(isinstance(list7,zip))

# 15、题目：传入一个json串, 返回一个字典, 字典只取出json最底层的数据, 中间如果有字典格式的字符串也需要进行处
# 理, 请以下面的数据为例, 请用递归的方法实现。
# 数据输入json = {"a": "aa", "b": [{"c": "cc", "d": "dd"}, {"f": {"e": "ee"}}]}输出：dic = {'a': 'aa', 'c': 'cc', 'e': 'ee', 'd': 'dd'}

# 16、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000
# 之间的水仙花数
# （其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。

# 17、用递归的方法求出n的阶乘？4的阶乘结果为?

# 18、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 并最终通过#get(key)的方式取出对应的value值。
# url地址如下：
#http://ip:port/extername/get_account_trade_record.json?#page_size=20&page_index=1&user_id=203317&trade_type=0"