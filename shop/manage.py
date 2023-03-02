"CRUD"
# create - создать
# read - читать
# update - обновлять
# delete - удаление

from products import create, read, delete, update  #по названию файла ищет нужный файл

while True:
    oper = input('c/r/d/u: ')
    if oper == 'c':
        create()
    elif oper == 'r':
        read()
    elif oper == 'u':
        update()
    elif oper == 'd':
        delete()
