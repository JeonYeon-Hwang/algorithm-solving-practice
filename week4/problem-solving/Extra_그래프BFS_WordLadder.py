# 그래프, BFS - Word Ladder
# 문제 링크: https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        edges_infos = {}
        stand_len = len(beginWord)

        for n in range(len(wordList) + 1):
            word = None

            if n >= len(wordList):
                word = beginWord
            else:
                word = wordList[n]

            graph[word] = []

            for i in range(stand_len):
                sliced = word[:i] + '_' + word[i + 1:]
                edges_infos.setdefault(sliced, []).append(word)

                edge_info = edges_infos[sliced]
                edge_len = len(edge_info)
                adding = edge_info[edge_len - 1]

                if edge_len > 1:
                    # edge 기존 점들에게 추가하기
                    for i in range(edge_len - 1):
                        graph.setdefault(edge_info[i], []).append(adding)
                    # 새로운 정점에 기존 edge를 추가
                    for i in range(edge_len - 1):
                        graph.setdefault(adding, []).append(edge_info[i])


        depth = 1
        s = set()
        q = deque()
        q.append(beginWord)
       

        while q:
            q_size = len(q)
            depth += 1

            for _ in range(q_size):
                cur_word = q.popleft()

                for next in graph[cur_word]:
                    if next not in s:
                        s.add(next)
                        q.append(next)

                        if next == endWord:
                            return depth

        return 0
    


if __name__ == "__main__":

    beginWord = "talk"
    endWord = "tail"
    wordList = ["talk","tons","fall","tail","gale","hall","negs"]

    sol = Solution()
    result = sol.ladderLength(beginWord, endWord, wordList)
    
    print(f"결과: {result}")