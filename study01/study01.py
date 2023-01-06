#第一次编写python程序
"""

名称：py学习记录01
内容：
1，py的基础数据类型
2.变量的使用和存储过程
3.对于字符类型的基本操作

"""


print("开始测试:")

#打印函数测试
"""
print("hello world!")
"""

#整数类型测试
"""
int_value_test = 1112
print("整数类型测试：")
print(int_value_test)
print(type(int_value_test))
"""

#浮点数类型测试
"""
float_value_test = 3.1415926
print("小数类型测试：")
print(float_value_test)
print(type(float_value_test))
"""

#字符串类型测试
"""
string_value_test = "字符串变量"
print("字符类型测试：")
print(string_value_test)
print(type(string_value_test))
"""

#多个变量同时赋值测试
"""
test_data_1, test_data_2 = 11, 12.0
print("data_1 = ")
print(test_data_1)
print("data_2 = ")
print(test_data_2)
"""

#同一变量类型变化测试
"""
test = 1112
print("test = ")
print(test)
test = "类型改变了！"
print("test = ")
print(test)
"""

#变量值改变1
"""
data_source = "原数据"
data_other_1 = data_source
data_other_2 = data_source
print("data_source = ")
print(data_source)
print("data_other_1 = ")
print(data_other_1)
print("data_other_2 = ")
print(data_other_2)
data_source = "原数据已修改"
print("data_source = ")
print(data_source)
print("data_other_1 = ")
print(data_other_1)
print("data_other_2 = ")
print(data_other_2)
"""

#变量值改变2
"""
info = { 'name' : "黑渊白花", 'owner' : '呆鹅'}
print(info)
info['name'] = '普通长枪'
print(info)
"""

"""字符串格式"""
#print('单引号测试')
#print("双引号测试")
#print('''三单引号测试''')
#print("""三双引号测试""")
#temp = '''1、三单引号
#2、跨行测试'''
#print(temp)
#temp = """1、三双引号
#2、跨行测试"""
#print(temp)

"""转义字符测试"""
#print('\thello\n\tworld')

"""字符带引号测试"""
#print('"双引号测试"')
#print("'单引号测试'")
#print(''' "双引号测试"and'单引号测试' ''')
#print(""" "双引号测试"and'单引号测试' """)

#字符串拼接
"""
str_1 = "hello "
str_2 = "world "
str_3 = str_1 + str_2
print(str_1)
print(str_2)
print('str_3 = '+str_3)
"""

#字符串索引
"""
Str = "ABCDE"
print( 'Str = ' + Str)
print( 'Str[0] = ' + Str[0])
print( 'Str[4] = ' + Str[4])
print( 'Str[-1] = ' + Str[-1])
print( 'Str[-5] = ' + Str[-5])
"""

#字符串切片
"""
str = "ABCDE"
print( 'str = ' + str )
print( 'str[2:4] = ' + str[2:4] )
print( 'str[-5:-3] = ' + str[-5:-3] )
print( 'str[:2] = ' + str[:2] )
print( 'str[2:] = ' + str[2:] )
print( 'str[2:5] = ' + str[2:5] )
"""

#字符串长度
"""
test_str = 'likeszm'
print( 'lenth of'+ "'" + test_str +"'" +" = " + str( len(test_str)))
"""


