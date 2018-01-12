import csv


def main():
    filename = 'CTC Income Statement.csv'
    filepath = '/Users/chengh/Downloads/'

    with open(filepath + filename, newline='') as f:
        reader = csv.reader(f)
        import ipdb; ipdb.set_trace()
        title = reader.__next__()
        headers = reader.__next__()
        contents = {}
        for row in reader:
            contents[row[0]]=row
    reader.
    print(contents)

    # f = open(filepath+filename, 'rb')
    # reader = csv.reader(f)
    # title = reader.next()
    # header = reader.next()

if __name__ == '__main__':
    main()