from typing import List

def print_array(arr: List[int]) -> None:
    print("Array:", arr)

def reverse_array(arr: List[int]) -> List[int]:
    return arr[::-1]

def rotate_array(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]