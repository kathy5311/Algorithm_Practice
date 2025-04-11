from collections import deque

person = [1, 1, 1, 1]
n = 4
t = 0  # 시간 초기화
queue = deque()  # 일반 큐 (탑승 시간과 사람들의 상태를 관리)
person_queue = deque(person)  # 대기 중인 사람들

while person_queue or queue:
    # 1초 경과 후 queue에 있는 사람들의 탑승 시간 감소
    t += 1
    
    # 탑승 시간 감소
    if queue:
        # 큐에서 남은 시간 확인 (탑승 중인 사람들의 시간 감소)
        temp = deque()
        while queue:
            time_left, idx = queue.popleft()  # 큐에서 앞에서부터 꺼냄
            if time_left > -1:
                temp.append((time_left - 1, idx))  # 남은 시간 감소한 값 저장
        # 업데이트된 사람을 다시 큐에 넣음
        queue.extend(temp)

    # queue가 가득 차지 않았고, 대기중인 사람이 있으면 새로운 사람을 추가
    if len(queue) < n and person_queue:
        # 대기 중인 사람이 탑승
        time = person_queue.popleft()
        queue.append((time, len(queue)))  # 큐에 (탑승 시간, 사람 번호) 넣음
    
    # 만약 queue가 가득 차고 시간이 지나면 탑승한 사람들 중 한 명 내보내기
    if len(queue) == n:
        # queue가 가득 차면 가장 먼저 탑승한 사람은 내린다.
        time_left, idx = queue.popleft()
        # 이미 내린 사람이므로 큐에서 제거된 후 나오는 사람들은 추가되게 된다.

print(t)
