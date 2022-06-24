class Package:
    def __init__(self, name, version, description, dependencies):
        self.name = name
        self.version = version
        self.description = description
        self.dependencies = dependencies