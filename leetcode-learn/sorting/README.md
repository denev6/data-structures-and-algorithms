- `sortColors`: Selection Sort
- `heightChecker`: Bubble Sort
- `insertionSortList`: Insertion Sort
- `sortArray`: Heap Sort
- `smallestTrimmedNumbers`: Radix Sort
- `maximumGap`: Counting Sort

# 요약

|Algorithm|Time|Space|Is Stable|
|:---:|:---:|:---:|:---:|
|Bubble Sort|$O(N^2)$|$O(1)$|O|
|Insertion Sort|$O(N^2)$|$O(1)$|O|
|Selection Sort|$O(N^2)$|$O(1)$|X|
|Heap Sort|$O(N\log N)$|$O(1)$|X|
|Counting Sort|$O(N)$|$O(N)$|O|
|Radix Sort|$O(N)$|$O(N)$|O|
|Bucket Sort|$O(N)$ ~ $O(N^2)$|$O(N)$|O|

# 언어별 정렬 특징

## Python

```python
lst = [3, 4, 1]
sorted_lst = sorted(lst)
lst.sort()
```

- `sorted`는 원본 유지
- `sort`는 in-place 정렬
- sort와 sorted 모두 Tim-Sort 알고리즘 사용
- Tim-Sort는 $O(N\log N)$ 시간
- Tim-Sort는 stable 정렬

```python
sorted(lst, key=lambda x: (len(x), x), reverse=True)
# 정렬 조건: 1) 길이, 2) 사전 순
```

- key를 이용해 정렬 조건 설정
- reverse를 이용해 내림차순 정렬


## Go

go는 built-in 정렬 메서드가 다양하기 때문에 [공식문서](https://pkg.go.dev/sort)를 살펴 보는 것을 추천한다.

```go
sort.Slice(unstable, func(i, j int) bool {...})
sort.SliceStable(stable, func(i, j int) bool {...})
```

- `Slice`는 unstable 정렬
- `SliceStable`는 stable 정렬
- $O(N\log N)$ 시간
- "sort" 라이브러리에서 자료형에 따라 다른 메서드 제공
- (권장) v1.22 표준 라이브러리인 "slices"에서 개선된 메서드로 SortFunc 제공

## C++

```cpp
std::sort(vectors.begin(), vectors.end());
std::stable_sort(vectors.begin(), vectors.end());
```

- `sort`는 unstable
- `stable_sort`는 stable
- $O(N\log N)$ 시간