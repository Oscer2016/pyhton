#Dictionary Search:Ques2_3.py

#定义字典
dic={"a":"algorithm,算法，解决一种问题的大致步骤","b":"bug,臭虫，程序里的错误","c":"compile,编译，把用高级程序语言写的程序转换成低级语言","d":"debugging,除虫，找到及移除程序设计的错误过程","e":"exception,异常，执行错误的另一个名称"}

#输入要查询的关键字以便进行字典查询
keyword=raw_input('请输入要查询的名词关键字(a~e)： ')

#输入a~e之间的关键字则进行查询，否则结束程序
while keyword >= 'a' and keyword <= 'e':
    print '查询结果：',dic[keyword]
    keyword = raw_input('请输入要查询的名词的关键字(a~e): ')
      
