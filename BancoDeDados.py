#Criando Tabelas no bd primeirobanco atraves do python
import mysql.connector
bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "qweasdzxc",
    database = "primeirobanco"
)
bd_cursor = bd.cursor()
strSQL = "create table alunos"
strSQL += "(id int auto_increment primary key,"
strSQL += "nome varchar(255),"
strSQL += "endereco varchar(255))"
bd_cursor.execute(strSQL)
bd_cursor.execute("show tables")

for tabela in bd_cursor:
    print(tabela)

