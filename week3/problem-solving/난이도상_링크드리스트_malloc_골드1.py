# 링크드리스트 - malloc (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/3217
import sys

try:
    sys.stdin = open('난이도상_링크드리스트_malloc_골드1.txt', 'r')
except FileNotFoundError:
    pass

ob = sys.stdin.readline
N = int(input().rstrip())

memory_size = 100001
dicts = {}

class Node:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.next = None
        self.prev = None

root_node = Node(1, 100000)

def insert_memory(memory_name, insert_size):
    curr_start = root_node.start
    curr_size = root_node.size

    if curr_size >= insert_size:
        left_amount = curr_size - insert_size 

        if left_amount >= 0:
            new_start = curr_start + insert_size
            root_node.start = new_start
            root_node.size = left_amount 
            dicts[memory_name] = f'{new_start - insert_size}:{insert_size}'


def free_memory(memory_name):
    global root_node

    text = dicts.pop(memory_name)
    infos = text.split(':')
    new_node = Node(int(infos[0]), int(infos[1]))
    
    temp_node = root_node
    root_node = new_node 
    
    if root_node.size + root_node.start == temp_node.start:
        root_node.size += temp_node.size
    else: 
        root_node.next = temp_node




def print_node():
    node = root_node
    print(f'{node.start}:{node.size}')
    
    while node.next is not None:
        node = node.next
        print(f'{node.start}:{node.size}')


insert_memory('가가', 100)
insert_memory('나나', 100)

free_memory('가가')
free_memory('나나')

print_node()
print(dicts)

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




