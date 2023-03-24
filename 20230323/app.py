
# INSERT INTO `elso`(`Név`, `Kor`, `Magasság`) VALUES ('Béla', '12', '150');
# SELECT Kor FROM `elso`;

# Telepítettük a XAMPP alkalmazást (cross-platform)
# elinditottuk az apache-ot és mysql-t
#     ha valakinek hibát ir, hogy foglalt a port:
#         config gomb, ini fájl szerkesztése
#         a port számot mindenhol kicserüljük valami újra
# megnyitottuk böngészőben a localhost/phpmyadmin felületet
# bal oldalon készítettünk adatbázist (pl: 10b néven)
# létrehoztunk egy táblát 4 oszloppal (pl: adatok néven)
# megj.: az adatbázis név, táblanév ne tartalmazzon ékezetet, szóközt
# az oszlopok:
#     oszlopnév - tipus - egyéb
#     id - int - A_I oszlop pipa
#     név - varchar - maxhossz
#     kor - int
#     magasság - int
# a táblára kattintva a felső menüsorban kiválasztottuk a "jogok" fület
# új felhasználó létrehozása (szóközt ékezetet ne tartalmazzanak a mezők)
#     név: 10b_user
#     password: 10b_user (2 helyen kell megadni)
#     Hely: legördülő menü -> helyi
#     a többi dolgot békénhagytuk



import pymysql
# pip install pymysql

defaults= {
    "DB_HOST": "127.0.0.1",
    "DB_NAME": "10b",
    "DB_TABLE": "elso",
    "DB_UNAME": "10b_user",
    "DB_PASSWD": "10b_user"
}

conn=pymysql.connect(host=defaults["DB_HOST"],
                     user=defaults["DB_UNAME"],
                     password=defaults["DB_PASSWD"],
                     database=defaults["DB_NAME"])

cursor = conn.cursor()
sql = "INSERT INTO `elso`(`Név`, `Kor`, `Magasság`) VALUES ('Józsi', '15', '142');"
cursor.execute(sql)
conn.commit()
conn.close()

