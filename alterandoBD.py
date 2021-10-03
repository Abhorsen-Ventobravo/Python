import mybd
bd_cursor = mybd.bd.cursor()
sql = "update alunos "
sql += "set endereco = 'Rua das Camelias, 50' "
sql += "where nome = 'Ana'"
bd_cursor.execute(sql)
mybd.bd.commit()
print(bd_cursor.rowcount,"registro alterado.")

