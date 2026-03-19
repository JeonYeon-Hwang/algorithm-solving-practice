# 링크드리스트 - malloc (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/3217
import sys

try:
    sys.stdin = open('난이도상_링크드리스트_malloc_골드1.txt', 'r')
except FileNotFoundError:
    pass

ob = sys.stdin.readline
N = int(input().rstrip())
dicts = {}

class Node:
    def __init__(self, start, size, is_free):
        self.start = start
        self.size = size
        self.is_free = is_free
        self.next = None
        self.prev = None

dummy = Node(-1, -1, False)
root_node = Node(1, 100000, True)
dummy.next = root_node
root_node.prev = dummy

def insert_memory(memory_name, insert_size):
    global dummy

    cur_node = dummy
    # print(f"찾은 현재 노드 => {cur_node.start}:{cur_node.size}")
    while cur_node.next is not None:
        if cur_node.is_free and cur_node.size >= insert_size:
            # print(f"찾은 현재 노드 => {cur_node.start}:{cur_node.size}")
            break
        cur_node = cur_node.next

    # print(f"찾은 현재 노드 => {cur_node.start}:{cur_node.size}")
    if cur_node.size < insert_size or cur_node.is_free is False: 
        return

    new_node = Node(cur_node.start, insert_size, False)   
    # print(f"삽입할 노드 정보 => {cur_node.start}:{new_node.size}")
    dicts[memory_name] = new_node

    cur_node.start += insert_size
    cur_node.size -= insert_size
    
    if cur_node.size == 0:
        new_node.next = cur_node.next
        if cur_node.next: 
            cur_node.next.prev = new_node
    else:
        prior = cur_node.prev
        
        prior.next = new_node
        new_node.prev = prior
        new_node.next = cur_node
        cur_node.prev = new_node



def free_memory(memory_name):
    if memory_name not in dicts: 
        return
    
    val = dicts.pop(memory_name)
    val.is_free = True

    # 빈 공간을 합치는 로직 + 연결고리 없는 node는 저절로 삭제됨
    if val.next.is_free: 
        val.size += val.next.size

        # 삭제할 노드가 마지막 노드라면, 삭제처리
        if val.next.next is not None:
            # print('뒤쪽 점핑 함')
            jumped = val.next.next
            jumped.prev = val
            val.next = jumped
        else:
            # print('뒤쪽 삭제 + 고리 끊음')
            last = val.next
            last.prev = None
            val.next = None

    if val.prev.is_free:
        pre_val = val.prev
        pre_val.size += val.size
        pre_val.next = val.next
        
        if val.next: 
                val.next.prev = pre_val




def print_node():
    node = dummy
    print(f'{node.start}:{node.size}:{node.is_free}')
    
    while node.next is not None:
        node = node.next
        print(f'{node.start}:{node.size}:{node.is_free}')


# insert_memory('가가', 100)
# insert_memory('나나', 100)
# insert_memory('다다', 100)
# free_memory('나나')
# print_node()



# print('-------------------')
# insert_memory('소소', 100)
# free_memory('나나')

# print_node()
# print(dicts)

for _ in range(N):
    input = sys.stdin.readline
    cmd = input().rstrip()

    if cmd[0:5] == 'print':
        raw_command = cmd[5:]
        command = raw_command[1:-2]
        val = dicts.get(command, 0)
        if val == 0: print(f'{val}')
        else: print(f'{val.start}')
    elif cmd[0:4] == 'free':
        raw_command = cmd[4:]
        name = raw_command[1:-2]
        free_memory(name)
        # print(f'{cmd}')
    else:
        lst = list(cmd.split('='))
        name = lst[0]
        raw_command = lst[1]
        size = int(raw_command[7:-2])
        insert_memory(name, size)
        # print(f'{cmd}')



# print('-------------------')
# print_node()
# print(dicts)