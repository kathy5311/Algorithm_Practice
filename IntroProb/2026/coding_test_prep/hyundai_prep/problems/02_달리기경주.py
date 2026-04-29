'''
[유형] 구현/시뮬레이션
[난이도] 프로그래머스 Lv.1
[문제] 달리기 경주
========================================

선수들이 1등부터 꼴찌 순서로 players 배열에 있습니다.
callings 배열에는 추월한 선수의 이름이 순서대로 주어집니다.
추월 = 자신의 바로 앞 선수와 자리 교체

모든 추월 후 최종 순위를 반환하세요.

[조건]
  - 1 <= players 길이 <= 50,000
  - 1 <= callings 길이 <= 1,000,000
  - 1등 선수는 절대 추월하지 않음

[입출력 예]
players  = ["mumu","soe","poe","kai","mine"]
callings = ["kai","kai","mine","kai"]
→ ["mumu","kai","mine","soe","poe"]

설명:
  "kai" 추월 → ["mumu","soe","kai","poe","mine"]  (poe와 자리 교체)
  "kai" 추월 → ["mumu","kai","soe","poe","mine"]  (soe와 자리 교체)
  "mine" 추월→ ["mumu","kai","soe","mine","poe"]  (poe와 자리 교체)
  "kai" 추월 → ["kai","mumu","soe","mine","poe"]  (mumu와 자리 교체)
'''

def solution(players, callings):
    pass


# 테스트
print(solution(["mumu","soe","poe","kai","mine"], ["kai","kai","mine","kai"]))
# ["mumu","kai","mine","soe","poe"]
