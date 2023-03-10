import sys

input = sys.stdin.readline
n = int(input())
human = {}
for i in range(n):
  info = input().rstrip()
  m = info.split(' ')[2]
  d = info.split(' ')[1]
  if len(m) == 1:
    m = '0' + m
  if len(d) == 1:
    d = '0' + d
  human[info.split(' ')[0]] = (int)(info.split(' ')[3] + m + d)
human = sorted(human.items(), key= lambda item:item[1])
print(human.pop(len(human)-1)[0])
print(human.pop(0)[0])

