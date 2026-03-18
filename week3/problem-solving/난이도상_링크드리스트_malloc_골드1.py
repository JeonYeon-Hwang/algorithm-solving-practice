# 링크드리스트 - malloc (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/3217
import sys

try:
    sys.stdin = open('난이도상_링크드리스트_malloc_골드1.txt', 'r')
except FileNotFoundError:
    pass

ob = sys.stdin.readline
N = int(input().rstrip())
dictionary = {}

class Node:
    def __init__(self, max_free, start_address):
        self.max_free = max_free
        self.start_address = start_address

        self.left = None
        self.right = None
        self.parent = None
        

root_node = Node(100000, 1)
    

    


def insert_data(data_name, data_size, node): 
    if node.max_free >= data_size:
        # 딕셔너리에 기록을 한다
        dictionary[data_name] = f"{node.start_address}:{data_size}"

        node.max_free -= data_size
        node.start_address += data_size
        return
    
    if node.left is None:
        node.left = Node(data_size, node.start_address)
        node.left.parent = node
    if node.right is None:
        node.right = Node(data_size, node.start_address)
        node.right.parent = node
    
    result = -1

    if node.left.max_free >= data_size:
        result = insert_data(data_name, data_size, node.left)
    elif node.right.max_free >= data_size:
        result = insert_data(data_name, data_size, node.right)
        
    node.max_free = max(node.left.max_free, node.right.max_free)
    return result


def free_data(data_name, node):
    lst = list(dictionary[data_name].split(':'))
    start_address = int(lst[0])
    node = search_data(start_address, node)



def search_data(pivot_address, node):
    print(f"{node.start_address} {pivot_address}")
    # if node.start_address > pivot_address:
    #     search_data(pivot_address, node.left)
    # elif node.start_address < pivot_address:
    #     search_data(pivot_address, node.right)
    # elif node.start_address == pivot_address:
    #     return node


insert_data('닝닝', 100, root_node)
insert_data('갱갱', 100, root_node)
free_data('갱갱', root_node)

print(f"{root_node.max_free} {root_node.start_address}")
print(dictionary)

for _ in range(N):
    input = sys.stdin.readline
    cmd = input().rstrip()

    if cmd[0:5] == 'print':
        raw_command = cmd[5:]
        command = raw_command[1:-2]
        # print(command)
    elif cmd[0:4] == 'free':
        raw_command = cmd[4:]
        command = raw_command[1:-2]
        # print(command)
    else:
        lst = list(cmd.split('='))
        name = lst[0]
        raw_command = lst[1]
        command = raw_command[7:-2]
        # print(command)




