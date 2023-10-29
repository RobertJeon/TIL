"""
1. 선택 정렬(Selection Sort)
> 최소값을 선택해 맨 앞부터 순서대로 나열

1. 기준 노드 - 가장 앞에 있는 값부터 시작
2. 기준 노드 뒤로 가장 값이 작은 노드를 선택
3. 기준점과 최소값 노드 교환(swap)
4. 이 과정을 반복
- 시간 복잡도: 최선, 최악, 평균 모두 $O(N^2)$
  - (앞에서부터 한칸씩 가면서 갈때마다 전체 배열을 한번씩 다시 돌기 때문에 n의 제곱만큼 시간이 든다.)
  - (물론 한 번 돌때마다 왼쪽에서 하나 뺀만큼씩만 돌지만 그래도 결국에 스퀘어의 절반의 면적이 나오기 때문에 빅 오에서는 제곱으로 표시.)

의사코드
def selection_sort(리스트):
    # 리스트의 길이만큼 도는 반복문(마지막 노드는 선택되지 않음)
    # 탐색하는 노드가 저장되는 변수
    # 가장 작은 노드가 저장되는 변수

        # 탐색값의 뒤 리스트를 돈다. (반복):
            # (최소값 찾는 알고리즘)
            # 가장 작은 노드보다 현재 노드 값이 더 작으면
                # 가장 작은 값의 인덱스 바뀐다.
        # swap
    return 정렬된 리스트
"""

# 선택정렬 구현
def selection_sort(li):
    length = len(li)
    for i in range(length-1):
        cur_index = i
        smallest_index = cur_index
        # 최소값을 찾는 알고리즘
        for j in range(cur_index+1, length):
            if li[smallest_index] > li[j]:
                smallest_index = j
        li[smallest_index], li[cur_index] = li[cur_index], li[smallest_index]
    return li