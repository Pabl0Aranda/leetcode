import heapq
from typing import List

def heap_push(heap: List[int], val: int) -> None:
    heapq.heappush(heap, val)

def heap_pop(heap: List[int]) -> int:
    return heapq.heappop(heap)

def heapify_list(lst: List[int]) -> None:
    heapq.heapify(lst)