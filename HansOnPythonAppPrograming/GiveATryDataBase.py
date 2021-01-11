from  mysql import connector

cnx = connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='python')
cursor = cnx.cursor()


##+---------------+-------------+------+-----+---------+----------------+
##| Field         | Type        | Null | Key | Default | Extra          |
##+---------------+-------------+------+-----+---------+----------------+
##| CD_WAIFU      | int(9)      | NO   | PRI | NULL    | auto_increment |
##| NM_WAIFU      | varchar(45) | NO   |     | NULL    |                |
##| NR_IDADE      | int(3)      | YES  |     | NULL    |                |
##| NM_ANIME      | varchar(40) | NO   |     | NULL    |                |
##| TP_COR_CABELO | varchar(15) | YES  |     | NULL    |                |
##| CM_ALTURA     | int(4)      | YES  |     | NULL    |                |
##+---------------+-------------+------+-----+---------+----------------+

##waifu ={
##    ('Maki Nishikino', 15, 'Love Live! School Idol Project', 'Vermelho', 161),
##    ('Sagiri izumi', 13, 'Eromanga Sensei', 'Branco', 148),
##    ('Isla', 0, 'Plastic Memories', 'Rosa', 150)}
##
##sql = '''
##       INSERT INTO WAIFUS(NM_WAIFU, NR_IDADE, NM_ANIME, TP_COR_CABELO, CM_ALTURA)
##       VALUES (%s, %s, %s, %s, %s)
##      '''

sql = '''
    SELECT * FROM WAIFUS
      '''

try:
    cursor.execute(sql)    
except Exception as e:
    print('Unable to fetch data.')


records = cursor.fetchall();
for record in records:
    print(record)
    print("\n")
    
cnx.close()
