from django.test import TestCase

# Create your tests here.
# wiite by keson 2022-3-23
#在python中调用sqlite3，python3中默认有sqlite这个库
#数据库的创建以及增删改查，
#注意每次运行完该代码，如果需要重新来测试数据库，则需要删除数据库中的表
#生成新的数据库时，需要将python与sqllite连接。点击数据库——>新建——>数据源——>sqlite
#然后在文件出找到创建的test.db这个数据库的文件，只有在连接成功后，才能用python对该数据库实现增删改查
import sqlite3    #导入sqlite3

conn = sqlite3.connect('F:\JetBrains\workspace\pingChenKeJi\db.sqlite3')  #连接名字为test.db的数据库，如果没有test.db这个数据库，则会创建一个名字为test.db的数据库

#先运行上面的程序，后面的程序先注释调调，等生成数据库test.db


c = conn.cursor()   #获取游标
#创建表头的sql语句
sql = '''
      DROP TABLE productsApp_product;
'''


c.execute(sql)


conn.commit()

