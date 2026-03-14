# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys


try:
    sys.stdin = open('난이도하_링크드리스트_에디터_실버2.txt', 'r')
except FileNotFoundError:
    pass

str = input()
M = int(input())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.pre = self.tail
        self.tail = new_node
    

    def print_list(self):
        values = []
        node = self.head
        values.append(node.data)
        
        while node.next is not None:
            node = node.next
            if node.data == 'dummy':
                break
            values.append(node.data)
        
        return values
    
    
    def position_cursor(self):
        node = self.head
        while node.next is not None:
            node = node.next
        
        self.current = node


    def get_current_node(self):
        return self.current.data
    

    def move_left(self):
        node = self.current
        if node.pre is None:
            return

        node = node.pre
        self.current = node


    def move_right(self):
        node = self.current
        if node.data == 'dummy':
            return
        elif node.next is None:
            new_node = Node('dummy')
            node.next = new_node
            self.current = node.next
            return
        
        node = node.next
        self.current = node

    def insert_left(self, data):
        # 새롭게 생성한 노드
        new_node = Node(data)
        # 현재 커서 노드
        cur_node = self.current
        # 앞에 아무 노드가 없을 시
        if cur_node.pre is None :
            self.head = new_node
            new_node.next = cur_node
            cur_node.pre = new_node
            return
        # 현재 보다 하나 앞 선 노드
        pre_node = cur_node.pre

        # 전선 재배치
        cur_node.pre = new_node
        new_node.pre = pre_node
        pre_node.next = new_node
        new_node.next = cur_node


    def delete_left(self):
        cur_node = self.current
        # 앞 노드가 없을 시 => 무시
        if cur_node.pre is None:
            return
        # 앞 노드
        pre_node = cur_node.pre

        # 앞앞 노드가 없을 시 => head 갱신
        if pre_node.pre is None:
            self.head = cur_node
            cur_node.pre = None
            return
        # 앞앞 노드
        prepre_node = pre_node.pre

        # 배선 작업
        prepre_node.next = cur_node
        cur_node.pre = prepre_node
            


words = LinkedList()
for i in range(len(str)):
    words.append(str[i])

words.append('dummy')
words.position_cursor()

for i in range(M):
    input = sys.stdin.readline
    command = list(input().rstrip().split(" "))

    if command[0] == 'L':
        words.move_left()
    elif command[0] == 'D':
        words.move_right()
    elif command[0] == 'B':
        words.delete_left()
    elif command[0] == 'P':
        words.insert_left(command[1])
    


answer = ''.join(words.print_list())
print(answer)