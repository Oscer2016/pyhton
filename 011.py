#Dictionary Search:Ques2_3.py

#�����ֵ�
dic={"a":"algorithm,�㷨�����һ������Ĵ��²���","b":"bug,���棬������Ĵ���","c":"compile,���룬���ø߼���������д�ĳ���ת���ɵͼ�����","d":"debugging,���棬�ҵ����Ƴ�������ƵĴ������","e":"exception,�쳣��ִ�д������һ������"}

#����Ҫ��ѯ�Ĺؼ����Ա�����ֵ��ѯ
keyword=raw_input('������Ҫ��ѯ�����ʹؼ���(a~e)�� ')

#����a~e֮��Ĺؼ�������в�ѯ�������������
while keyword >= 'a' and keyword <= 'e':
    print '��ѯ�����',dic[keyword]
    keyword = raw_input('������Ҫ��ѯ�����ʵĹؼ���(a~e): ')
      
