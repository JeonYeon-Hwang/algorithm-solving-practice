# 링크드리스트 - malloc (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/3217
import sys

try:
    sys.stdin = open('난이도상_링크드리스트_malloc_골드1.txt', 'r')
except FileNotFoundError:
    pass

input = sys.stdin.readline
N_line = input().rstrip()
if not N_line:
    exit()
N = int(N_line)
dicts = {}

class Node:
    def __init__(self, start, size, is_free):
        self.start = start
        self.size = size
        self.is_free = is_free
        self.next = None
        self.prev = None

head = Node(-1, -1, False)
root = Node(1, 100000, True)

head.next = root
root.prev = head

def insert_memory(name, req_size):
    if req_size <= 0:
        dicts.pop(name, None)
        return
    
    cur = head.next

    while cur:
        if cur.is_free and cur.size >= req_size:
            break
        cur = cur.next
    
    if cur is None:
        dicts.pop(name, None)
        return

    new_node = Node(cur.start, req_size, False)
    dicts[name] = new_node

    cur.start += req_size
    cur.size -= req_size

    prior = cur.prev

    prior.next = new_node
    new_node.prev = prior
    new_node.next = cur
    cur.prev = new_node

    if cur.size == 0:
        following = cur.next
        new_node.next = following
        if following:
            following.prev = new_node

def free_memory(name):
    if name not in dicts:
        return
    
    val = dicts.pop(name)
    val.is_free = True

    if val.next and val.next.is_free:
        nxt = val.next
        val.size += nxt.size
        val.next = nxt.next
        if val.next:
            val.next.prev = val

    if val.prev != head and val.prev.is_free:
        prv = val.prev
        prv.size += val.size
        prv.next = val.next
        if val.next:
            val.next.prev = prv


for _ in range(N):
    cmd = input().rstrip()
    if not cmd:
        continue

    if '(' not in cmd:
        continue

    if cmd.startswith('print'):
        name = cmd[cmd.find('(')+1 : cmd.find(')')]
        res = dicts.get(name)
        print(res.start if res else 0)
        
    elif cmd.startswith('free'):
        name = cmd[cmd.find('(')+1 : cmd.find(')')]
        free_memory(name)
        
    else:
        name, rest = cmd.split('=')
        size = int(rest[rest.find('(')+1 : rest.find(')')])
        insert_memory(name, size)
