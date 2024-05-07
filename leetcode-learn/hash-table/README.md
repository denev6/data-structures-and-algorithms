**Hash를 이용한 자료구조는 $O(1)$으로 값을 조회할 수 있다.** list는 $O(N)$ 시간이 걸리므로 단순 조회가 필요할 때는 hash된 구조가 유리하다. 

# Hash Map in Python3

```python
# 초기화
d = dict()
d = {1: "a", 2: "b", 3: "c"}

# key 조회
key in d
key in d.keys()

# value 조회
value in d.values()

# Others
d[key] = value # 삽입
value = d[key] # 조회
```

- key-value 쌍으로 자료를 저장
- key는 반드시 immutable 객체이며, 유일한 값임
- 삽입 및 조회 모두 $O(1)$
- Python 3.7부터 key의 순서가 삽입한 순서를 유지 (.keys()에서 먼저 삽입된 key가 먼저 조회)
    - 이전 버전은 삽입 순서를 보장하지 않음
    - 순서 유지 및 조작이 필요하다면 collections.OrderedDict 사용
- 없는 키를 조회하면 KeyError 발생

# Hash Set in Python3

```python
# 초기화
s = set()
s = {1, 2, 3}

# 조회
item in s

# Others
s.add(item) # 삽입
s.remove(item) # 삭제. (KeyError: item이 존재하지 않을 때)
s.discard(item) # 삭제. (item이 없어도 에러가 발생하지 않음)
s.pop() # 랜덤하게 값 하나를 삭제. (KeyError: item이 존재하지 않을 때)
s.clear() # 초기화
```

- set은 key만 있는 dict
- 탐색, 삽입, 조회 모두 $O(1)$
- 순서를 보장하지 않음
- 값이 중복되지 않음

```python
>>> lst = [1, 1, 1, 2, 2, 3]
>>> set(lst)
{1, 2, 3}
```

# Defaultdict

```python
>>> import collections
>>> d = collections.defaultdict(int)
>>> d[7]
0
```

- key가 없을 때 조회가 발생할 경우, default 값으로 value를 초기화
- default 값으로 int, list, set 사용 가능

# Counter

```python
>>> import collections
>>> collections.Counter(["a", "a", "a", "b", "b", "c"])
Counter({'a': 3, 'b': 2, 'c': 1})
```

- key의 빈도수를 value로 저장
- dictionary처럼 조회 및 조작 가능
- most_common는 빈도 순서로 정렬된 리스트 반환
    - 인자로 숫자 n을 넘겨주면 가장 빈도가 높은 n개만 반환

```python
Counter(...).most_common()
Counter(...).most_common(3)
```