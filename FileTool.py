class FileOperations:
    def __init__(self, path, fields, *args, **kwargs):
        self.path = path
        self.fields = fields

    def search(self, keyword):
        with open(self.path, 'r') as file:
            return [(i+1, r.replace('\n', '')) for i,r in enumerate(file.readlines()[1:]) if keyword.lower() in r.lower()]


