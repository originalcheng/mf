import pymysql

class MySQLConnector():
    def __init__(self,
                 host=None,
                 port=None,
                 user=None,
                 password=None,
                 db=None,):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password='admin'
        self.db='mysql'

    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.db
        )

    def cursor(self):
        if self._cursor is None:
            self._cursor = self.connection.cursor()
        return self._cursor

def testconnection():
    connection = MySQLConnector()
    connection.connect()
    cur = connection.cursor()
    cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    print()
    for row in cur:
        print(row)

    cur.close()
    conn.close()

if __name__ == '__main__':
    testconnection()