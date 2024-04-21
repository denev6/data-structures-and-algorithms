# C++ vector

## 초기화

```cpp
#include <vector>
using namespace std;

vector<int> arr;
```

`vector`는 표준 라이브러리에서 제공하는 동적 배열이다. `vector<자료형>`으로 선언한다.

```cpp
vector<int> arr(3);
// arr: {0, 0, 0}

vector<int> arr(3, 1);
// arr: {1, 1, 1}

vector<int> arr = {1, 2, 3};
// arr: {1, 2, 3}
```

## 반복

```cpp
vector<int> arr = {1, 2, 3};

// index 활용
for (int i = 0; i < arr.size(); i++) {}

// 요소 반복
for (int item : arr) {}
```

## 정렬

```cpp
vector<int> arr = {7, 3, 6};

// 오름차순: {3, 6, 7}
sort(arr.begin(), arr.end());

// 내림차순: {7, 6, 3}
sort(arr.begin(), arr.end(), greater<>());
```

## 유용한 메서드

- `empty()`
- `clear()`
- `push_back`
- `pop_back`
