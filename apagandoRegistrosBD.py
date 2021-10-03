import mybd
import lendoBD
bd_cursor = mybd.bd.cursor()
sql = "delete from alunos where nome = 'Joaquim'"
bd_cursor.execute(sql)
mybd.bd.commit()
print(bd_cursor.rowcount,"registro deletado.")
