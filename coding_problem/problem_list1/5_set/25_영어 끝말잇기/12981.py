def solution(n, words):
    answer = [[] for _ in range(n)]
    current_words = set()
    last_alpha = words[0][0]
    
    for idx, word in enumerate(words):
        if word[0] != last_alpha:
            return [idx % n + 1, len(answer[idx % n]) + 1]
        
        if word in current_words:
            return [idx % n + 1, len(answer[idx % n]) + 1]
        
        current_words.add(word)
        answer[idx % n].append(word)
        last_alpha = word[-1]

    return [0, 0]
