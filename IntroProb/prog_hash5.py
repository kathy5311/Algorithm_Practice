#베스트앨범
from collections import defaultdict

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

def solution(genres,plays):
    answer=[]
    #장르별 재생 횟수: total_play
    #장르별 인덱스, 재생 횟수: num_song
    total_play = defaultdict(int)
    num_song = defaultdict(list)

    for idx in range(len(genres)):
        total_play[genres[idx]]+=plays[idx]
        num_song[genres[idx]].append((idx,plays[idx])) #idx: 인덱스, plays[idx]:재생횟수
    
    #sort
    sorted_total_play=sorted(total_play.keys(), key=lambda x: total_play[x], reverse=True)

    #상위 2개 반환
    for gen in sorted_total_play:
        num_song[gen].sort(key=lambda x: (-x[1],x[0]))

        for i in num_song[gen][:2]:
            answer.append(i[0])
    return answer
print(solution(genres,plays))

