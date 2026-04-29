'''
[해설] 주차 요금 계산
========================================
핵심 아이디어:
  1. "HH:MM" → 분 변환 후 dict로 입차 시각 저장
  2. 출차 시 누적 주차 시간 합산
  3. 마지막에 parked에 남은 차량 → 23:59 기준 정산
  4. 차량 번호 오름차순 정렬 후 요금 계산

자료구조:
  parked    = {차번호: 입차 시각(분)}  ← 현재 주차 중
  total_time = {차번호: 누적 시간(분)} ← 오늘 총 주차 시간
'''

import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parked = {}
    total_time = {}

    for record in records:
        time_str, car, action = record.split()
        h, m = map(int, time_str.split(':'))
        minutes = h * 60 + m

        if action == 'IN':
            parked[car] = minutes
        else:
            elapsed = minutes - parked.pop(car)
            total_time[car] = total_time.get(car, 0) + elapsed

    # 아직 주차 중인 차량 → 23:59 정산
    for car, in_time in parked.items():
        elapsed = 23 * 60 + 59 - in_time
        total_time[car] = total_time.get(car, 0) + elapsed

    result = []
    for car in sorted(total_time):
        t = total_time[car]
        if t <= base_time:
            result.append(base_fee)
        else:
            result.append(base_fee + math.ceil((t - base_time) / unit_time) * unit_fee)
    return result

'''
========================================
포인트 정리
========================================
1. 시간 → 분: h * 60 + m  (문자열 비교 불가, 반드시 숫자로)
2. dict.pop(key): 값 꺼내면서 동시에 삭제
3. dict.get(key, 0): 없으면 0 반환 (KeyError 방지)
4. math.ceil((t - base_time) / unit_time): 올림 나눗셈

자주 틀리는 케이스:
  - 같은 차량이 하루에 여러 번 입출차 → get으로 누적 합산
  - 마지막에 parked 남은 차량 처리 누락
  - sorted(total_time): 키(차량번호) 기준 정렬
'''

# 테스트
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN","06:00 0000 IN","06:34 0000 OUT",
           "07:59 5961 OUT","07:59 0148 IN","18:59 0000 IN",
           "19:09 0148 OUT","22:59 5961 IN","23:00 0000 OUT"]
print(solution(fees, records))  # [14600, 34400, 5000]

fees2 = [120, 0, 60, 591]
records2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT"]
print(solution(fees2, records2))  # [0, 591]
