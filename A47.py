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

init_ans = [0]*T

def calc_score(ans):
    """スコア計算O(100)"""
    score = 0
    array = [0]*20
    for i in range(T):
        if ans[i] == 0:
            coef = 1
        else:
            coef = -1
        array[P[i]-1] += coef
        array[Q[i]-1] += coef
        array[R[i]-1] += coef
    for i in range(20):
        if array[i] == 0:
            score += 1
    return score

def time_judge():
    end_time = time.time()
    if end_time - start_time > 0.8:
        return True
    else:
        return False

# ループ回数
num_roop = 10**5

# ランダムシード
seed_num = 0

# ランダムシードを設定
random.seed(seed_num)

# 局所探索法

# 初期解をランダムに生成
current_ans = [0]*T
for i in range(T):
    current_ans[i] = random.randint(0,1)

# 初期解のスコアを計算
current_score = calc_score(current_ans)

for i in range(num_roop):
    # 0からTまでの整数をランダムに5つ選ぶ
    nums = random.sample(range(T), 5)
    new_ans = deepcopy(current_ans)
    for num in nums:
        new_ans[num] = 1 - current_ans[num]
    # スコア計算
    new_score = calc_score(new_ans)
    # スコアが良ければ更新
    if new_score > current_score:
        current_ans = new_ans
        current_score = new_score
        
    if time_judge():
        break
    

Ans = []
for i in range(len(current_ans)):
    if current_ans[i] == 1:
        Ans.append('B')
    else:
        Ans.append('A')

print(*Ans, sep='\n')