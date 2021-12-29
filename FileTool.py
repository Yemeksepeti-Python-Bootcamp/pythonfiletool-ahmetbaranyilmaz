class FileOperations:
    def __init__(self, path, fields, *args, **kwargs):
        self.path = path
        self.fields = fields

    def search(self, keyword):
        with open(self.path, 'r') as file:
            return [(i+1, r.replace('\n', '')) for i,r in enumerate(file.readlines()[1:]) if keyword.lower() in r.lower()]

    def __deleteByKeyword(self, deletePointer):
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row for row in file.readlines() if deletePointer.lower() not in row.lower()]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def delete(self, deletePointer, by='keyword'):
        if by == 'keyword':
            self.__deleteByKeyword(deletePointer)
