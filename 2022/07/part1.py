from abc import abstractmethod
from typing import Optional


class Node:

    def __init__(self, parent: Optional['Node'], name: str, size: int = 0) -> None:
        self.name = name
        self.children = set()
        self.parent = parent
        self._size = size

    def get_path(self) -> str:
        if self.parent is None:
            return self.name

        return self.parent.get_path() + "/" + self.name

    def __repr__(self) -> str:
        return f"{self.name} ({self.get_size()})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return False

        return self.get_path() == o.get_path()

    def __hash__(self) -> int:
        return hash(self.get_path())

    @abstractmethod
    def get_size(self) -> int:
        pass


class FileNode(Node):

    def __init__(self, parent: Optional['Node'], name: str, size: int) -> None:
        super().__init__(parent, name, size)

    def get_size(self) -> int:
        return self._size


class DirectoryNode(Node):

    def __init__(self, parent: Optional['Node'], name: str) -> None:
        super().__init__(parent, name)

    def get_size(self) -> int:
        size = 0
        for child in self.children:
            size += child.get_size()
        return size


class Tree:
    TOTAL_DISK_SPACE = 70_000_000
    DESIRED_FREE_SPACE = 30_000_000

    def __init__(self, lines: list[str]) -> None:
        self.root = DirectoryNode(None, "/")
        self.parse_input(lines)

    def parse_input(self, lines: list[str]) -> None:
        current_node = self.root

        while len(lines):
            line = lines.pop(0)

            # Change directory
            if line.startswith("$ cd"):
                path = line[5:]
                # Root
                if path == "/":
                    current_node = self.root
                # Parent
                elif path == "..":
                    current_node = current_node.parent
                # Child
                else:
                    current_node.children.add(DirectoryNode(current_node, path))
                    current_node = self.search(current_node, path)
            # List directory contents
            elif line == "$ ls":
                # Read until next command
                while len(lines) and not lines[0].startswith("$"):
                    x, name = lines.pop(0).split(" ")
                    # X describes directory
                    if x == "dir":
                        current_node.children.add(DirectoryNode(current_node, name))
                    # X describes file size
                    else:
                        current_node.children.add(FileNode(current_node, name, int(x)))

    @staticmethod
    def search(root: Node, name: str) -> Optional[Node]:
        for node in root.children:
            if node.name == name:
                return node

        return None

    def get_directories(self, root: Node) -> list[DirectoryNode]:
        result = []
        for node in [n for n in root.children if isinstance(n, DirectoryNode)]:
            result.append(node)
            result.extend(self.get_directories(node))

        return result

    def used_space(self) -> int:
        return self.root.get_size()

    def space_to_free(self) -> int:
        return (self.TOTAL_DISK_SPACE - self.used_space() - self.DESIRED_FREE_SPACE) * -1


with open("07/input.txt") as f:
    data = f.read()

tree = Tree([l.strip() for l in data.splitlines()])
dirs = [d.get_size() for d in tree.get_directories(tree.root) if d.get_size() <= 100_000]

print("Part 1:", sum(dirs))
