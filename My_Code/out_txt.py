poem='''\Программировать весело.Если работа скучна,Чтобы придать ей весёлый тон -используй Python!'''

f= open('poem.txt','w')# открываем для записи (writing)f.write(poem)# записываем текст в файлf.close()# закрываем файл

f= open('poem.txt')# если не указан режим, по умолчанию подразумевается# режим чтения ('r'eading)

while True:
    line = f.readline()
    if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
        breakprint(line, end='')f.close()# закрываем ф
    break
    print(line, end='')
f.close()