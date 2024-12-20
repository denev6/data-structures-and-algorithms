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

# 중첩함수 주의사항

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