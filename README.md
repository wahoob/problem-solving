<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8871e5,50:b678c4,100:f77187&height=200&section=header&text=Problem%20Solving&fontSize=64&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Data%20Structures%20%26%20Algorithms&descSize=20&descAlignY=58" width="100%" />

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=24&pause=1000&center=true&vCenter=true&width=600&lines=Grinding+LeetCode%2C+one+problem+at+a+time;Clean+solutions+%2B+complexity+analysis;Multiple+approaches+per+problem;O(n)+or+bust+%F0%9F%9A%80" alt="Typing animation" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/wahoob/problem-solving?style=for-the-badge&color=8871e5)

<br/>

**A curated collection of algorithm & data-structure solutions — every problem solved multiple ways, with time/space complexity analysis.**

</div>

---

## 📊 Progress

| Category | Solved | Problems |
|:---------|:------:|:---------|
| 🧮 Arrays & Hashing | **1** | Contains Duplicate |
| 👉 Two Pointers | 0 | — |
| 🪟 Sliding Window | 0 | — |
| 📚 Stack | 0 | — |
| 🔍 Binary Search | 0 | — |
| 🔗 Linked List | 0 | — |
| 🌳 Trees | 0 | — |
| 🧗 Dynamic Programming | 0 | — |

<div align="center">

**Total solved: 1** &nbsp;•&nbsp; ![Progress](https://img.shields.io/badge/dynamic/json?style=flat-square&label=&color=8871e5&query=%24&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwahoob%2Fproblem-solving&suffix=%20and%20counting...&cacheSeconds=3600&logo=fire&logoColor=white&message=grinding)

</div>

## 🗂️ Solutions

| # | Problem | Difficulty | Solution | Topics |
|:--|:--------|:----------:|:--------:|:-------|
| 0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟢 Easy | [Python](arrays_hashing/0217_contains_duplicate.py) | Array, Hash Table |

## 🧠 Approach Philosophy

Every solution file follows the same structure:

1. **Problem statement** — linked and summarized in the module docstring
2. **Multiple approaches** — from brute force to optimal, each as its own class
3. **Complexity analysis** — time & space documented on every approach

```python
class Solution:
    """Hash set — early exit on first duplicate.

    Time:  O(n)
    Space: O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

## 🛠️ Running a Solution

```bash
git clone git@github.com:wahoob/problem-solving.git
cd problem-solving
python -i arrays_hashing/0217_contains_duplicate.py
>>> Solution().containsDuplicate([1, 2, 3, 1])
True
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8871e5,50:b678c4,100:f77187&height=120&section=footer" width="100%" />

</div>
