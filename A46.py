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

# _INPUT = """7
# 1 1
# 4 1
# 2 5
# 3 4
# 3 2
# 4 2
# 5 5



# """
# sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(1000000)

start_time = time.time()

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
X,Y = [0]*N,[0]*N
for i in range(N):
    X[i],Y[i] = map(int,input().split())

def calc_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

# グラフを定義
G = [[10**12 for i in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if i==j:
            continue
        G[i][j] = calc_distance(X[i],Y[i],X[j],Y[j])
        G[j][i] = calc_distance(X[i],Y[i],X[j],Y[j])

# 巡回セールスマン問題を貪欲法で解く
# 1. どこからスタートしても良いので、0からスタートする
# 2. 0から行けるところで一番近いところに行く    
# 3. 2で行ったところから行けるところで一番近いところに行く
# 4. 3を繰り返す
# 5. すべての頂点を通ったら、0に戻る
# 6. 5で戻ったところが、最短距離になる
def calc_ans(G):
    path = [0]
    distance = 0
    pos = 0
    while len(path) < N:
        next_pos = -1
        min_distance = 10**10
        for i in range(N):
            if i in path:
                continue
            if G[pos][i] < min_distance:
                next_pos = i
                min_distance = G[pos][i]
        path.append(next_pos)
        distance += min_distance
        pos = next_pos
    return path

path = calc_ans(G)
path.append(0)

for i in range(len(path)):
    path[i] += 1


# スコア計算用関数
def calc_score(path):
    # 距離の合計がスコア
    score = 0
    for i in range(N):
        score += G[path[i]-1][path[i+1]-1]
    return score

def time_judge():
    end_time = time.time()
    if end_time - start_time > 0.8:
        return True
    else:
        return False


# 山登り法でループ回数を設定
roop_num = 10**6

# ランダムシード
seed_num = 1

# ランダムシードを設定
random.seed(seed_num)

current_ans = path
current_score = calc_score(current_ans)

for i in range(roop_num):
    # 反転区間を設定
    left = random.randint(1,N)
    right = random.randint(1,N)
    if left > right:
        left,right = right,left
    
    # pathの[left,right]を反転
    new_path = current_ans[:left] + current_ans[left:right][::-1] + current_ans[right:]
    new_score = calc_score(new_path)

    # 焼きなまし法の温度
    T = 30 - 29 * i / roop_num  
    # 許容確率
    probability = math.exp(min((current_score - new_score) / T,0))
    # 許容確率で反転
    if random.random() < probability:
        current_ans = new_path
        current_score = new_score
    
    if time_judge():
        break

print(*current_ans,sep="\n")

