from collections import deque, defaultdict
from typing import List, Dict, Set

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return order

def dfs(graph: Dict[int, List[int]], start: int, visited=None) -> List[int]:
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order