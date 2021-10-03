import mysql.connector
bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "qweasdzxc",
    database = "primeirobanco"
)
bd_cursor = bd.cursor()
sql = "insert into alunos (nome,endereco) values (%s, %s)"
valores = [
    ('Ana', "Rua das Anas, 15"),
    ("Pedro","Rua dos Pedros, 16"),
    ("Joao","Rua dos tontos, 26"),
    ("Maria","Rua das Marias, 77"),
    ("Joaquim","Rua dos Joaquim, 88"),
]
bd_cursor.executemany(sql,valores)

#O comando commit() é importante par salvar as informações no banco de dados
bd.commit()
print(bd_cursor.rowcount, "registros inseridos.")