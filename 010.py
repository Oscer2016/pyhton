#data sort:Ques2_2.py
#encoding=utf-8

data_list = [ ]         #初始化一个空列表

#循环10次，输入10个数字放到列表中
for integer in range(10):
      x = input('请输入第' + str(integer+1) + '个元素：')
      data_list = data_list+[x]

print '排序前数据： ',data_list

#用sort方法对列表中的数据进行排序
data_list.sort()

print '排序后数据： ',data_list
