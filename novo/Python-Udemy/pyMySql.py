import  pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='681015',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

x = 'create table teste1(nome varchar(10));'

with conexao.cursor() as cursor:
    cursor.execute(x)

print('saiu')

