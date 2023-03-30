import config as CONF
import person as P
import pymysql

def connectDB(_host, _port, _user, _passwd, _dbname):
    return pymysql.connect(
                    host=_host,
                    port=_port,
                    user=_user,
                    password=_passwd,
                    database=_dbname)

def insertDB(tablename, person: P.Person):
    conn =connectDB(
        CONF.defaults["DB_HOST"],
        CONF.defaults["DB_PORT"],
        CONF.defaults["DB_UNAME"],
        CONF.defaults["DB_PASSWD"],
        CONF.defaults["DB_NAME"]
        )
    cursor = conn.cursor()
    sql = f"INSERT INTO `{tablename}`(`Név`, `Kor`, `Magasság`) VALUES ('{person.nev}', '{person.kor}', '{person.magassag}');"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def selectDB(tablename, oszlopnevekstr, feltetel=1):
    conn =connectDB(
        CONF.defaults["DB_HOST"],
        CONF.defaults["DB_PORT"],
        CONF.defaults["DB_UNAME"],
        CONF.defaults["DB_PASSWD"],
        CONF.defaults["DB_NAME"]
        )
    cursor = conn.cursor()
    sql = f"SELECT {oszlopnevekstr} FROM `{tablename}` WHERE {feltetel};"
    cursor.execute(sql)
    rows = cursor.fetchall()
    lista=[]
    for i in rows:
        lista.append(P.Person(i[0], i[1], i[2], i[3]))
        
    conn.close()
    return lista