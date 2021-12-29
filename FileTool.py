class FileOperations:
    def __init__(self, path, fields, *args, **kwargs):
        self.path = path
        self.fields = fields

    def search(self, keyword): # keyword = fileOps.search('keyword')
        with open(self.path, 'r') as file:
            return [(i+1, r.replace('\n', '')) for i,r in enumerate(file.readlines()[1:]) if keyword.lower() in r.lower()]

    def __deleteByKeyword(self, deleteKey): # fileOps.delete('sport')
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