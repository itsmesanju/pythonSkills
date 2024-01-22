class FileSystem:

    def __init__(self):
        self.paths = collections.defaultdict(list)
        self.files = collections.defaultdict(str)

    def ls(self, path: str) -> List[str]:
        if path in self.paths:
            return [path.split("/")[-1]]
        else:
            return sorted(self.paths[path])

    def mkdir(self, path: str) -> None:
        dirs = path.split("/")
        current_path = ""
        for d in dirs:
            if d:
                current_path += f"/{d}"
                if current_path not in self.paths:
                    self.paths[current_path] = []

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
