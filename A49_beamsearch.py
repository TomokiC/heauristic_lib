import bisect
import io
import math
import string
import sys
from collections import defaultdict, deque
from copy import deepcopy
import random   
import time

# import numpy as np

# _INPUT = """100
# 3 8 15
# 3 10 19
# 5 13 18
# 12 13 14
# 4 8 12
# 10 13 15
# 4 6 16
# 11 16 18
# 11 14 19
# 3 4 8
# 11 14 18
# 6 9 13
# 6 8 10
# 1 8 13
# 1 4 11
# 5 11 17
# 3 4 17
# 2 7 11
# 6 8 19
# 8 17 18
# 12 18 20
# 4 7 13
# 2 10 14
# 5 10 14
# 5 11 14
# 1 14 20
# 14 16 18
# 11 14 20
# 7 10 16
# 4 15 19
# 3 5 10
# 6 11 12
# 5 12 19
# 6 9 17
# 3 13 16
# 1 7 16
# 3 4 8
# 6 10 13
# 11 18 20
# 1 5 17
# 3 10 14
# 2 5 9
# 6 10 20
# 3 10 11
# 5 16 20
# 6 11 13
# 10 13 18
# 3 12 15
# 12 15 16
# 5 15 20
# 2 6 16
# 9 17 20
# 6 8 11
# 11 13 15
# 8 11 16
# 6 8 11
# 5 6 18
# 3 12 16
# 3 4 16
# 2 6 12
# 6 10 15
# 4 7 8
# 7 13 20
# 1 6 7
# 10 13 14
# 3 9 14
# 2 4 6
# 1 8 17
# 7 12 18
# 10 12 17
# 6 7 18
# 2 9 20
# 7 9 20
# 8 18 20
# 8 12 17
# 3 9 16
# 2 5 10
# 2 8 13
# 4 10 15
# 4 14 16
# 1 16 18
# 2 10 14
# 8 9 10
# 2 13 20
# 3 15 18
# 1 2 19
# 3 7 17
# 12 15 18
# 4 9 11
# 3 11 16
# 1 8 9
# 1 4 18
# 5 17 20
# 2 8 20
# 2 7 15
# 6 13 14
# 1 10 16
# 4 13 15
# 3 17 19
# 4 9 20





# """
# sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(1000000)

start_time = time.time()

def input():
    return sys.stdin.readline()[:-1]

T = int(input())
P,Q,R = [0]*T,[0]*T,[0]*T
for i in range(T):
    P[i],Q[i],R[i] = map(int,input().split())

# 各操作での状態を定義するクラス
class State:
    
    def __init__(self) -> None:
        self.score = 0
        self.X = [0]*20
        self.LastMove = '' # 最後にどの操作をしたか
        self.LasePos = '' # 最後にどこから遷移したか
    
    # インスタンス同士の比較関数
    def __lt__(self, other):
        return self.score < other.score

# 定数定義
beam_width = 300
N = 20
NumState = [0]*(T+1)

Beam = [[State() for _ in range(beam_width)] for _ in range(T+1)]

# ビームサーチを行う関数
def beam_search():
    # 0手目の状態を初期化
    NumState[0] = 1
    Beam[0][0].score = 0

    # ビームサーチ
    for i in range(1, T+1):
        Candidate = []
        for j in range(NumState[i-1]):
            # 操作Aを行う場合
            operationA = deepcopy(Beam[i-1][j])
            operationA.LastMove = 'A'
            operationA.LasePos = j
            operationA.X[P[i-1]-1] += 1
            operationA.X[Q[i-1]-1] += 1
            operationA.X[R[i-1]-1] += 1
            for k in range(N):
                if operationA.X[k] == 0:
                    operationA.score += 1

            # 操作Bを行う場合
            operationB = deepcopy(Beam[i-1][j])
            operationB.LastMove = 'B'
            operationB.LasePos = j
            operationB.X[P[i-1]-1] -= 1
            operationB.X[Q[i-1]-1] -= 1
            operationB.X[R[i-1]-1] -= 1
            for k in range(N):
                if operationB.X[k] == 0:
                    operationB.score += 1
            
            # 候補に追加
            Candidate.append(operationA)
            Candidate.append(operationB)
        Candidate.sort()
        Candidate = Candidate[::-1]
        Candidate = Candidate[:beam_width]
        NumState[i] = len(Candidate)
        for j in range(NumState[i]):
            Beam[i][j] = Candidate[j]

# ビームサーチを実行
beam_search()

# ビームサーチの復元
ans = []
current_place = 0
for i in range(T, 0, -1):
    ans.append(Beam[i][current_place].LastMove)
    current_place = Beam[i][current_place].LasePos

ans = ans[::-1]
print(*ans, sep='\n')




