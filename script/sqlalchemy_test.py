# -*- encoding: utf-8 -*-
"""
@File    : sqlalchemy_test.py
@Time    : 2020/9/9 15:28
@Author  : Morde
@Software: PyCharm
@Description: SQLAlchemy  ORM Object-Relational Mapping，把关系数据库的表结构映射到对象上
"""

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CrawlerList(Base):
    __tablename__ = 'crawler_list'

    # 表结构
    row_id = Column(Integer, primary_key=True)
    ent_name = Column(String(255))
    ent_uid = Column(String(255))
    ent_social_no = Column(String(255))
    batch = Column(String(255))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://psdsstaff:Psdsstaff#123@10.2.13.251:3306/ent_data_working')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
'''
filter{
    equals          User.name=='ed'
    not equals      User.name!='ed'
    like            User.name.like('%ed%')
    in              User.name.in_(['ed','wen','jask'])
    not in          ~User.name.in_(['ed','wen','jask'])
    in null         User.name==None
    is not null     User.name!=None
    and             and_(User.name=='ed',Username=='ed jones')
    or              or_(User.name= 'ed',User.name=='wendy'
    match           User.name.match('wendy')
}
Query{
    one()           返回且仅返回一个查询结果。当结果的数量不足一个或者多于一个时会报错
    all()           返回列表
    first()         返回至多一个结果，而且以单项形式，而不是只有一个元素的tuple形式返回这个结果
    one_or_one()    当结果数量为0时返回None， 多于1个时报错
    scalar()        成功则返回该行的第一列的列号
    text()      
                    query.filter(text("id>1")).all()
                    query.filter(Person.id>1).all() #同上
        params():传递参数
                    query.filter(text("id>:id")).params(id=1).all() #使用:，params来传参
        from_statement():直接使用完整的SQL语句，但是要注意将表名和列名写正确
                    query.from_statement(
                        text("select * from person where name=:name")).
                        params(name='jack').all()
    count()         返回符合条件的总数
    func_count()    可以直接指出要测次数的某一项
                    session.query(func.count(User.name), User.name).group_by(User.name).all()
    order_by()
    group_by()
}
'''
data = session.query(CrawlerList).filter(CrawlerList.row_id == 16).one()

print(data)
print(data.ent_name)


session.close()

'''
增
session = DBSession()
new_ent = CrawlerList(ent_name='',ent_uid='',ent_social_no='',batch='')
session.add(new_ent)
session.commit()
session.close()
'''
'''
改
session = DBSession()
update = session.query(CrawlerList).filter(CrawlerList.ent_name=='').first()
update.ent_name = ''
session.commit()
session.close()
'''
'''
删
session = DBSession()
delete_data = session.query(CrawlerList).filter(CrawlerList.ent_name=='').first()
session.delete(delete_data)
session.commit()
session.commit()
'''