# LeetCode Solutions Collection

Welcome to the **LeetCode Solutions** repository! This repository contains my solutions to various problems on LeetCode, implemented in Python. Each solution is accompanied by clear explanations, including:

- **Problem Intuition**: The thought process and observations that led to the solution.
- **Approach**: A step-by-step breakdown of how the solution is implemented.
- **Complexity Analysis**: Detailed analysis of the time and space complexity of the solution.

## Why This Repository?
This repository is designed to:

- Document my learning journey as I solve algorithmic problems.
- Serve as a reference for commonly used problem-solving patterns.
- Help others preparing for coding interviews or improving their problem-solving skills.

## Repository Structure
The repository is organized as follows:

```
leetcode/
├── README.md
├── .gitignore
├── utils/                  # Functions and helpers
│   ├── graph_utils.py      # BFS, DFS genérics
│   ├── tree_utils.py
│   └── ...
├── problems/
│   ├── arrays/
│   │   ├── easy/
│   │   │   ├── two_sum.py
│   │   │   ├── best_time_to_buy_sell_stock.py
│   │   │   └── ...
│   │   ├── med/
│   │   │   └── ...
│   │   └── hard/
│   │       └── ...
│   ├── strings/
│   │   ├── easy/
│   │   │   ├── longest_substring.py
│   │   │   └── ...
│   │   ├── med/
│   │   │   ├── longest_palindromic_substring.py
│   │   │   └── ...
│   │   └── hard/
│   │       └── ...
│   ├── linked_lists/
│   │   ├── easy/
│   │   │   ├── reverse_linked_list.py
│   │   │   └── ...
│   │   ├── med/
│   │   │   └── ...
│   │   └── hard/
│   │       └── ...
│   ├── trees/
│   │   ├── easy/
│   │   │   ├── maximum_depth_binary_tree.py
│   │   │   └── ...
│   │   ├── med/
│   │   │   └── ...
│   │   └── hard/
│   │       └── ...
│   ├── graphs/
│   │   ├── easy/
│   │   │   ├── number_of_islands.py
│   │   │   └── ...
│   │   ├── med/
│   │   │   └── ...
│   │   └── hard/
│   │       └── ...
│   ├── dynamic_programming/
│   │   ├── easy/
│   │   │   ├── climbing_stairs.py
│   │   │   └── ...
│   │   ├── med/
│   │   │   └── ...
│   │   └── hard/
│   │       └── ...
│   └── math/
│       ├── easy/
│       │   ├── is_prime.py
│       │   └── ...
│       ├── med/
│       │   └── ...
│       └── hard/
│           └── ...
└── requirements.txt
```

Each file is named according to the problem it solves, with clear comments and structured code.

## How to Use This Repository
1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/Pabl0Aranda/leetcode.git
   ```
2. Browse through the solutions and pick the problem you’re interested in.
3. Read the code, comments, and explanations to understand the solution.

## Example Problem
Here’s an example of what you’ll find in this repository:

**Problem**: Find the median of two sorted arrays.

```python
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return float(max(maxLeftX, maxLeftY))
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted or invalid input.")


print(findMedianSortedArrays([1, 3], [2]))         # ➜ 2.0
print(findMedianSortedArrays([1, 2], [3, 4]))      # ➜ 2.5
print(findMedianSortedArrays([0, 0], [0, 0]))      # ➜ 0.0
print(findMedianSortedArrays([], [1]))             # ➜ 1.0
print(findMedianSortedArrays([2], []))             # ➜ 2.0
```

## Contributing
If you have alternative solutions or optimizations for any problem, feel free to open a pull request. Contributions are welcome!

## Contact
If you have any questions or suggestions, feel free to reach out via GitHub or email.

---

Happy coding and problem-solving! :rocket:

