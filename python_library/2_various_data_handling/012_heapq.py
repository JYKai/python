import heapq

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

# h = [] # 힙 생성
# for score in data:
#     heapq.heappush(h, score) # 힙에 데이터 저장

heapq.heapify(data)

for i in range(3):
    print(heapq.heappop(h)) # (11.57, '차동현'), (11.67, '차정웅'), (11.92, '한시우')


print(heapq.nsmallest(3, data))