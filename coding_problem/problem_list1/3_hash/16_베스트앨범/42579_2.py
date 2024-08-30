from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    total_plays = defaultdict(int)
    genre_plays = defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        total_plays[genre] += play
        genre_plays[genre].append([idx, play])
    
    # 장르를 재생 횟수의 합계로 내림차순 정렬
    sorted_genres = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        # 각 장르 내에서 노래를 재생 횟수와 인덱스 기준으로 정렬
        sorted_songs = sorted(genre_plays[genre], key=lambda x: (-x[1], x[0]))
        # 상위 두 곡만 선택
        for idx, (num, play) in enumerate(sorted_songs):
            if idx == 2:
                break
            answer.append(num)
    
    return answer

