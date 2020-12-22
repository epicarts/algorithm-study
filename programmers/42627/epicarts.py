import heapq

def solution(jobs):
    # jobs.sort() # jobs의 시간순서대로 정렬
    jobs_heap = []
    for start, duration in jobs:
        heapq.heappush(jobs_heap, (start, duration))

    waiting_heap = [] # 대기 하는 heap
    current_time = 0 #작업이 종료되는 시점
    total_time = 0 # 작업 요청부터 처리되기까지 모든 시간

    while jobs_heap or waiting_heap: # 두개의 힙에 아무것도 없어야함.
        # jobs_heap이 존재해야하고, 현재 시간이 잡에있는 곳보다 작을경우
        while jobs_heap and jobs_heap[0][0] <= current_time: # 모든 jobs 힙을 current 힙에 넣음.
            start, duration = heapq.heappop(jobs_heap) # 힙에서 꺼낸 후 waiting_heap에 넣음
            heapq.heappush(waiting_heap, (duration, start)) # 여기에서 반대로 바꿈. 바꾸는 이유는 최소시간으로 저장이 되어야하기 떄문

        if waiting_heap: # 기다리는 대기열 힙이 있을경우
            duration, start = heapq.heappop(waiting_heap) # 대기열 힙에서 하나 꺼냄
            total_time += (duration + (current_time - start)) # 3 =  0 + 3 + (0 - 0) / 11 =  3 + (3 + 6 - 1)  / 27 = 11 + (9 + 9) - 2
            current_time += duration # 현재시간은 걸린시간을 더해줘야함. 3 = 0 + 3 / 9 = 6 + 3 / 18 = 9 + 9
        else: # 대기 작업이 없는 경우에는 현재 시간은 전체 작업 중 가장 빠른 요청이 들어오는 시간으로 바꾼다
            current_time = jobs_heap[0][0]
    return total_time//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))