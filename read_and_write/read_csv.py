from csv import DictReader

with open('../files/books.csv', newline='') as f:
    reader = DictReader(f)
    books = []
    for i in reader:
        del i['Publisher']
        books.append(i)
