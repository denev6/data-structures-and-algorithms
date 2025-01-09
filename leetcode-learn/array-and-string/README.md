# Two-pointer

- `start`와 `end` 포인터를 통해 배열을 앞뒤로 순회
- *twoSum.cpp* 참고.

# 부분합 문제

- 부분합은 배열이 주어졌을 때 i ~ j 사이 값을 연속으로 더하는 문제
- 일반적인 반복문 풀이 외에도 누적합을 활용할 수 있다.
- *minSubArrayLen.cpp* 참고.

```
arr = [1, 4, 5, 6, 0]
sum arr[1] to arr[3] --> 15
```

## 1. 반복문

```
sum arr[1] to arr[3]
--> for(i = 1 to 3) {sum += arr[i]}
```

```cpp
int sum = 0;
for (int i = 1; i <= 3; i++) {
    sum += arr[i];
}
```

## 2. prefixSum(누적합)

```
prefixSum[0] = 0
prefixSum[1] = arr[0]
prefixSum[2] = arr[0] + arr[1]
prefixSum[3] = arr[0] + arr[1] + arr[2]

sum arr[1] to arr[2] --> prefixSum[3] - prefixSum[2]
```

일반화하면 아래와 같다.

```
let 
    arr: nunmber array
    p: array of prefixSum
then
    p[0] = 0
    p[i + 1] = arr[0] + ... + arr[i]
    sum arr[i] to arr[j] --> p[j + 1] - p[i + 1]
```

누적합을 구하는 방법은 아래와 같다.

```cpp
vector<int> prefix(arr.size() + 1, 0);
for (int i = 0; i < arr.size(); i++) {
    prefix[i + 1] = prefix[i] + arr[i]
}
```