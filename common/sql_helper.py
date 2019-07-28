import pymssql
from common import config_manage

config = config_manage.get_yaml_config()


class Sql_Helper:
    def __init__(self, database='YCHMALL'):
        self.host = config['sqlServer']['host']
        self.port = config['sqlServer']['port']
        self.user = config['sqlServer']['user']
        self.password = config['sqlServer']['pwd']
        self.database = database

    def _GetConnect(self):

        '''得到连接信息，返回conn.cursor()'''
        self.conn = pymssql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    database=self.database,
                                    charset="utf8")
        # cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 定义游标
        cur = self.conn.cursor(as_dict=True)  # sqlserver连接,as_dict=True 设置返回字典类型，默认是元组
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
        try:
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库
            self.conn.commit()  # update/delete/insert必须要这一步
        except:
            # 发生错误时回滚
            self.conn.rollback()
            # 关闭数据库连接
            self.conn.close()


if __name__ == '__main__':
    # host = '192.168.7.250'
    # port = 1433
    # user = 'sa'
    # pwd = 'ych123456.'
    # db = 'YCHMALL'
    sql = "select *from Mall_LeaguerLevel where IsDelete=0 and LevelName='atuo级别';"
    a = Sql_Helper()
    result = a.ExecQuery(sql)
    print(result[0]['LevelName'])
    print(result[0])
