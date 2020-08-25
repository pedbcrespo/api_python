import pymysql
import datetime
# criando conexao com banco de dados, mysql no caso
connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='orla_dados'
)

cursor = connection.cursor()

# funcoes para buscar, alterar, inserir ou deletar dados do banco
def dic(list_column, datas):
    dc = {}
    for column in list_column:
        if type(datas[list_column.index(column)]) == datetime.date:
            dc[column] = datas[list_column.index(column)].strftime('%d/%m/%Y')
        else:
            dc[column] = datas[list_column.index(column)]
    return dc


def get_data(table):
    cursor.execute(
        f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'orla_dados' AND TABLE_NAME = '{table}'")
    columns = [elem[0] for elem in cursor]
    cursor.execute(f"SELECT * FROM {table}")
    datas = [elem for elem in cursor]

    return [dic(columns, elem) for elem in datas]


def put_data(table, id_elem, new_elem):
    tcmd = ''
    for camp in new_elem:
        if camp == 'nascimento':
            date_s = datetime.datetime.strptime(new_elem[camp], '%d/%m/%Y').date()
            tcmd += f' {camp} = "{date_s}",'
        else:
            tcmd += f' {camp} = "{new_elem[camp]}",'

    cursor.execute(f"UPDATE {table} SET {tcmd[:-1]} WHERE id = {id_elem}")
    connection.commit()

def post_data(table, new_elem):
    list_values = []
    for camp in new_elem:
        if camp == "nascimento":
            date_s = datetime.datetime.strptime(new_elem[camp], '%d/%m/%Y').date()
            date_s = date_s.strftime('%Y-%m-%d')
            list_values.append(f'"{date_s}"')
        else:
            list_values.append(f'"{new_elem[camp]}"')
    values = ', '.join(list_values)
    camps = ', '.join(camp for camp in new_elem)
    cursor.execute(f"INSERT INTO {table} ({camps}) VALUES ({values})")
    connection.commit()

def delete_data(table, id_elem):
    cursor.execute(f"DELETE FROM {table} WHERE id = {id_elem}")
    connection.commit()

if __name__ == '__main__':
    print(get_data('usuario'))
