from collections import defaultdict
from queue import Queue

START = 'Erdös, P.'

def GetAuthors(line):
    # Do not need anything after first parenthesis (from the date).

    line = line[:line.index('(')].strip()

    # Every name contains a comma, so split on every other comma

    i = iter(line.split(', '))

    names = map(', '.join, zip(i,i))

    if "& " in names[-1]:
        names[-1] = names[-1][2:]

    return names

def BFS(adj_list, value):
    visited = {}

    for key in adj_list.iterkeys():
        visited[key] = False

    q = Queue()
    q.put(START)
    visited[START] = True

    while not q.empty():
        cur = q.get()

        for adj in adj_list[cur]:
            if not visited[adj]:
                visited[adj] = True
                value[adj] = True
                q.put(adj)

    return value


def GetErdosNum(adj_list):
    value = {}
    for key in adj_list.iterkeys():
        value[key] = 0

    return BFS(adj_list, value)

adj_list = defaultdict(list)

N, M = map(int, input().split())

for _ in range(N):
    authors = GetAuthors(input())
    for auth1, auth2 in [(x,y) for x in authors for y in authors if x != y]:
        adj_list[auth1].append(auth2)

value = GetErdosNum(adj_list)

for _ in range(M):
    author = input()
    print("%s %d" % (author, value[author]))