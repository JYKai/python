# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    genres_total = {}
    each_genres = {}
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in genres_total:
            genres_total[g] = 0
            each_genres[g] = []
        genres_total[g] += p
        each_genres[g].append((idx, p))
    
    genres_total = sorted(genres_total.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in genres_total:
        play_list = sorted(each_genres[genre], key=lambda x: x[1], reverse=True)
        for idx, play in play_list[:2]:
            answer.append(idx)
    
    return answer