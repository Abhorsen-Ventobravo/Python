import mybd 
bd_cursor = mybd.bd.cursor()
bd_cursor.execute("select * from alunos")
#o comando fetchall retona uma lista de tuplas com os dados existentes nas tabelas
alunos = bd_cursor.fetchall()
for aluno in alunos:
    print(aluno)