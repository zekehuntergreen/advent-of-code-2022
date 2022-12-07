from typing import Any
from anytree import Node, RenderTree


terminal_output = open("test_input.txt", "r").readlines()


class FileTreeNode(Node):
    node_type: str
    size: int

    def __init__(self, *args: Any, node_type: str, size=0, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.node_type = node_type
        self.size = size


root = FileTreeNode("/", node_type="dir")
current = root

for line in terminal_output:
    split_line = line.split()
    if split_line[0] == "$":
        if split_line[1] == "cd":
            destination = split_line[2]
            if destination == "/":
                current = root
            elif destination == "..":
                current = current.parent
            else:
                current = list(
                    filter(lambda c: c.name == destination, current.children)
                )[0]
    else:
        if split_line[0] == "dir":
            child = FileTreeNode(split_line[1], node_type="dir", parent=current)
        else:
            child = FileTreeNode(
                split_line[1], size=int(split_line[0]), node_type="file", parent=current
            )


def find_dir_sizes(node, acc):
    if node.children:
        dir_size = 0
        for child in node.children:
            child_size, acc = find_dir_sizes(child, acc)
            dir_size += child_size
        node.size = dir_size
        if dir_size <= 100000:
            acc += dir_size
    return node.size, acc


_, acc = find_dir_sizes(root, 0)

for pre, fill, node in RenderTree(root):
    print("%s%s %s %s" % (pre, node.name, node.node_type, node.size))

print("sum of sizes of directories under 100000", acc)

space_used = root.size
space_unused = 70000000 - space_used
space_needed = 30000000
to_delete = space_needed - space_unused


def find_candidates_to_delete(node, acc):
    if node.children:
        for child in node.children:
            acc = find_candidates_to_delete(child, acc)
        if node.size > to_delete:
            acc.append(node)
    return acc


acc = find_candidates_to_delete(root, [])
acc.sort(key=lambda n: n.size)

print(f"smallest dir over {to_delete} is", acc[0].size, acc[0].name)
