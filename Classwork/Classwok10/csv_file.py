import csv

# чтение из файла
data = []
with open("test.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    # data = csvreader[1:]
    # print(data)
    for row in csvreader:   # считываем по строкам
        print(row)          # каждая строка - СПИСОК, заголовок тоже
        data.append(row)
header = data.pop(0)
print(header)
print(data)
#
data.append(['qwe', 'wer', 'ert'])

# запись файла
with open('test_write.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
    csvwriter.writerow(['WTF', 'HUAS'])
#
# чтение из файла
data = []
with open("test.csv", 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    print(csvreader)
    for row in csvreader:   # считываем по строкам
        print(row)          # каждая строка - СЛОВАРЬ, ключи из заголовока
        data.append(row)    # список словарей

print(data)

for row in data:

    print(row["First"], row["Second"],  row["Third"])
