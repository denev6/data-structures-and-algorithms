연결리스트 문제는 머리로 풀기보다 직접 그림을 그리면서 풀여야 풀린다.

만약 첫 노드(head)를 결과로 반환해야 한다면, 빈 노드를 만들고 주어진 리스트를 연결한다.

```python
empty_node = Node()
empty_node.next = head

 ...

return empty_node.next
```

그럼 head를 조작하며 이동해도 시작점을 고정할 수 있다.
