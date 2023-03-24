import config as CONF
import pymysql

def connectDB(_host, _port, _user, _passwd, _dbname):
    return pymysql.connect(
                    host=_host,
                    port=_port,
                    user=_user,
                    password=_passwd,
                    database=_dbname)

def insertDB(nev, kor, magassag):
    conn =connectDB(
        CONF.defaults["DB_HOST"],
        CONF.defaults["DB_PORT"],
        CONF.defaults["DB_UNAME"],
        CONF.defaults["DB_PASSWD"],
        CONF.defaults["DB_NAME"]
        )
    cursor = conn.cursor()
    sql = f"INSERT INTO `elso`(`Név`, `Kor`, `Magasság`) VALUES ('{nev}', '{kor}', '{magassag}');"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    