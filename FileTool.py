class FileOperations:
    def __init__(self, path, fields, *args, **kwargs):
        self.path = path
        self.fields = fields

    def search(self, keyword): # keyword = fileOps.search(keyword)
        with open(self.path, 'r') as file:
            return [(i+1, r.replace('\n', '')) for i,r in enumerate(file.readlines()[1:]) if keyword.lower() in r.lower()]

    def __deleteByKeyword(self, deleteKey): # fileOps.delete(keyword)
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row for row in file.readlines() if deleteKey.lower() not in row.lower()]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def __deleteByIndex(self, deleteKey): # fileOps.delete([5,7,9,10,11,22,2,3,4], by='index')
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row for i, row in enumerate(file.readlines()) if i not in deleteKey]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def delete(self, deleteKey, by='keyword'):
        if by == 'keyword':
            self.__deleteByKeyword(deleteKey)
        if by == 'index':
            self.__deleteByIndex(deleteKey)

    def appendRow(self, row = '', delimeter = ','):
        if row == '':
            with open(self.path, 'r') as file:
                header = file.readline()
                keyList = header.replace('\n', '').split(delimeter)
                row = ''
                for i,key in enumerate(keyList):
                    if i == len(keyList)-1:
                        row += input(f'Enter {key}: ') + '\n'
                    else: row += input(f'Enter {key}: ') + delimeter

        with open(self.path, 'a') as file:
            file.write(row)

    def update(self, oldKeyword, newKeyword):
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row.replace(oldKeyword, newKeyword) for row in file.readlines()]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def __getKeyword(self, word = ''):
        return input(f'Enter {word}Keyword: ')

    def __getIndexes(self):
        return list(map(int, input('Enter Indexes : ').split())) # 2, 3, 4, 5

    def menu(self):
        print(f'Selected CSV: {self.path}')
        print(f'Operations\n(1) Search\n(2) Delete\n(3) Update\n(4) Add Row\n(0) Exit ', end=':')
        selection = int(input())
        if selection == 1:
            for row in self.search(self.__getKeyword()):
                print(row)
        elif selection == 2:
            print(f'By\n(1) Keyword\n(2) Index', end=':')
            by = int(input())
            if by == 1:
                self.__deleteByKeyword(self.__getKeyword())
            elif by == 2:
                self.__deleteByIndex(self.__getIndexes())
        elif selection == 3:
            self.update(self.__getKeyword('Old '), self.__getKeyword('New '))
        elif selection == 4:
            self.appendRow()
        elif selection == 0:
            pass