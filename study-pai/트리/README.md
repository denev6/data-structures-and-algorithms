# 복습하기 좋은 문제

- (기본) 104, 297
- (BST) 108, 938
- (응용) 310, 938

# BST

`Binary Search Tree`. 이진 탐색 트리.

- 왼쪽 하위 노드는 현재 노드보다 작음
- 오른쪽 하위 노드는 현재 노드보다 큼

# NOTE

- DFS: 스택, 재귀
- BFS: 큐, 반복

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 중첩함수 주의사항

```python
class Solution:
    """UnboundLocalError: 
    cannot access local variable 'var' where it is not associated with a value
    """
    def func(self):
        var = 0 # local variable
        
        def inner():
            var += 1
        
        inner()
        return var
    
class Solution:
    """return (var:) 1"""
    var = 0 # class variable

    def func(self):
        def inner():
            self.var += 1
        
        inner()
        return self.var 
```

## 다중 대소비교

```python
>>> 1 < 3 > 2
True
>>> n = 3
>>> 1 < n < 4
True
```

다중 비교는 `and`로 변환 후 처리됨