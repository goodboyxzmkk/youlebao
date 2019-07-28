import pymysql
from common import config_manage

config = config_manage.get_yaml_config()


class MySql_Helper:
    def __init__(self, database='yunyou_goods'):
        self.host = config['mySql']['host']
        self.port = config['mySql']['port']
        self.user = config['mySql']['user']
        self.password = config['mySql']['pwd']
        self.database = database

    def _GetConnect(self):

        '''得到连接信息，返回conn.cursor()'''
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    database=self.database,
                                    charset="utf8")
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 定义游标
        # cur = self.conn.cursor()  # sqlserver连接
        if not cur:
            raise NameError('连接数据库失败')
        else:
            return cur

    def ExecQuery(self, sql):
        '''
        查询模块，传入查询语句，返回查询结果
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        '''
        cur = self._GetConnect()
        cur.execute(sql)  # 查询SQL语句
        reslist = cur.fetchall()  # 查询结果
        self.conn.close()  # 关闭连接
        return reslist

    def ExecNotQuery(self, sql):
        '''
        执行非查询语句
        '''
        cur = self._GetConnect()
        cur.execute(sql)
        self.conn.commit()  # update/delete/insert必须要这一步
        self.conn.close()


if __name__ == '__main__':
    '''mysql数据库连接,默认返回字典'''
    db = 'yunyou_goods'
    sql = "select *from GDS_Goods where id='002259CD-3096-4076-ABF5-A91300EC4FAA';"
    a = MySql_Helper(db)
    result = a.ExecQuery(sql)
    print(result)
    print(result[0]['ID'])
