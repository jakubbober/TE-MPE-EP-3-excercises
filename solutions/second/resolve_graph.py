from second.file_system import FileSystem
from second.utils import read_json
from second.package import Package


def resolve_graph(filename: str) -> FileSystem:
    file = read_json(filename)
    packages = [Package(name) for name in list(file.keys())]

    for package in packages:
        for dependency in file[package.name]:
            package.add_dependency(Package(dependency))

    file_system = FileSystem(packages)

    return file_system
