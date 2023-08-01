from typing import Dict, Any
# from second.utils import NestedDict


class Package:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, package):
        self.dependencies.append(package)

    def check_cycle(self):
        all_deps = []
        for dep in self.dependencies:
            all_deps.append(dep)
            all_sub_deps = dep.check_cycle()
            if self.name == dep.name or self.name in [sub_dep.name for sub_dep in all_sub_deps]:
                raise ValueError(f"Circular dependency detected: {self.name} -> {self.name}")
            all_deps += dep.check_cycle()
        return all_deps

    def __repr__(self) -> Dict[str, Any]:
        self.check_cycle()
        result = dict()
        result[self.name] = dict()
        for dep in self.dependencies:
            result[self.name][dep.name] = dep.__repr__()
        print(self.name, result)
        return result

        # result = f"- {self.name}\n"
        # deps_str = ""
        # for dep in self.dependencies:
        #     deps_str += f"{dep}"
        # for line in deps_str.splitlines():
        #     result += f"\t{line}\n"
        # return result
