"""
2. 삽입 정렬(Insertion Sort)
> 요소를 추출한 후 앞에 있는 값들과 비교해서 알맞은 자리에 삽입

1. 기준 노드 - 두번째 노드부터 추출
2. 추출한 노드가 앞으로 이동하며 앞에 있는 노드들의 값과 비교
3. 알맞는 위치에 삽입(swap 일어남)
4. 이 과정을 반복

- 시간 복잡도는 최악과 평균은 $O(N^2)$, 최선은 $O(N)$
  - 최선: 모두 정렬이 되어있는경우 한번씩밖에 비교하지 않으므로 O(N)

의사코드
def insertion_sort(리스트):
    # 리스트의 길이만큼 도는 반복문:
        # 이전 값들을 돌며 추출한 값과 비교:
            # 추출한 값이 더 큰 경우:
                # 지나감
            # 추출한 값이 더 작은 경우:
                # swap
    return 정렬된 리스트
"""

def insertion_sort(li):
    length = len(li)
    for i in range(1, length):
        for j in range(i):
            if li[i] > li[j]:
                pass
            else:
                li[i], li[j] = li[j], li[i]
    return li