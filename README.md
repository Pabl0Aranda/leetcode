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
leetcode-solutions-collection/
|-- ProblemName1.py
|-- ProblemName2.py
|-- ...
|-- README.md
```

Each file is named according to the problem it solves, with clear comments and structured code.

## How to Use This Repository
1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/leetcode-solutions-collection.git
   ```
2. Browse through the solutions and pick the problem you’re interested in.
3. Read the code, comments, and explanations to understand the solution.

## Example Problem
Here’s an example of what you’ll find in this repository:

**Problem**: Find the median of two sorted arrays.

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two arrays into one sorted array
        merged = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add the remaining elements from either array
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Find the median of the merged sorted array
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

# Example usage
nums1 = [1, 3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0
```

## Contributing
If you have alternative solutions or optimizations for any problem, feel free to open a pull request. Contributions are welcome!

## Contact
If you have any questions or suggestions, feel free to reach out via GitHub or email.

---

Happy coding and problem-solving! :rocket:

