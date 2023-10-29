"""
버블 정렬(Bubble Sort)
> 모든 요소를 바로 뒤에 있는 값과 비교해서 swap해서 정렬

- 가장 간단한 윈리. 하지만 가장 효율적이라고 말할 수는 없다.

1. 뒤에 있는 요소와 값을 비교
2. 뒤에 있는 값이 더 작으면 노드 교환(swap)
3. 이 과정을 반복

- 시간 복잡도는 최악과 평균은 $O(N^2)$, 최선은 $O(N)$
  - 최선: 모두 정렬이 되어있는경우 한번씩밖에 비교하지 않으므로 O(N)

# 버블정렬 의사코드
def bubble_sort(li):
    # 외부 반복문(리스트 전체를 돈다):
      # 내부 반복문(값을 비교해서 swap):
        # if 현재 노드 값이 뒤에 있는 노드의 값보다 큰 경우:
          # swap
        # if 그렇지 않으면
          # pass
    return 정렬된 리스트
"""
def bubble_sort(li):
    length = len(li) - 1
    for i in range(length):
        for j in range(length - i):
            if li[j] > li[j+1]:
                li[j+1], li[j] = li[j], li[j+1]
    return li