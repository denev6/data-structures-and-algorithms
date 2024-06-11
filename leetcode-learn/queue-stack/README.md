# Queue & Stack in Python3

## Deque

`deque`: (덱) double-ended queue. 양방향으로 데이터를 추가/삭제

```python
from collections import deque

q = deque()
```

- double linked list로 구현
- 좌우 삽입이 모두 O(1)
- 좌우 삭제가 모두 O(1)

deque를 이용해 queue, stack 등 자료구조를 구현할 수 있다.

## Queue with deque

```python
queue = deque([1, 3]) # 초기화
queue.appendleft(0) # 삽입: [0, 1, 3]
queue.pop() # 삭제: [0, 1]
```

- `appendleft`: 좌측에 삽입.
- `pop`: 우측에서 삭제. 삭제된 값을 반환. 값이 없다면 IndexError 발생.

## Stack with deque

```python
stack = deque([1, 3]) # 초기화
stack.append(5) # 삽입: [1, 3, 5]
stack.pop() # 삭제: [1, 3]
```

- `append`: 우측에 삽입.
