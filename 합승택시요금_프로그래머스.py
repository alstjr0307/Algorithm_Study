import sys, heapq
def solution(n, s, a, b, fares):
    inf = sys.maxsize
   
    graph=[[] for _ in range(n+1)]
    for i in fares:
        graph[i[0]].append((i[2],i[1]))
        graph[i[1]].append((i[2],i[0]))
    print(graph)
    answer = inf

    def dijkstra(start): 

        heap = []
        dist = [inf] *(n+1) #출발지점으로부터의 거리 리스트
        heapq.heappush(heap,(0,start)) #힙에 출발지점 삽입
        dist[start]=0
        while heap:
            value, destination= heapq.heappop(heap)
            if dist[destination] < value: #destination까지의 거리가 최소가 아닐 시에만 실행
                continue
            for v, d in graph[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist
    dp = [[]]+[dijkstra(i) for i in range(1,n+1)]

    for i in range(1, n+1):
        answer = min(answer, dp[i][a] + dp[i][b] + dp[i][s])
    
    return answer
solution(6,	4	,6	,2	,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])