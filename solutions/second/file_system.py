from second.package import Package
from typing import List


class FileSystem:
    def __init__(self, packages: List[Package]):
        self.packages = packages

    def __repr__(self):
        result = dict()
        for package in self.packages:
            print(package.name)
            result.update(package.__repr__())
        return result
    # def __str__(self):
    #     if not self.packages:
    #         return "No packages in the file system."
    #
    #     result = ""
    #
    #     # Print the representations for each package
    #     for package in self.packages:
    #         result += str(package)
    #
    #     return result
