def compare(apeach, lion):
    apeach_score = 0
    lion_score = 0
    for idx, (a, l) in enumerate(zip(apeach, lion)):
        if a >= l and a > 0:
            apeach_score += (10 - idx)
        elif l > 0:
            lion_score += (10 - idx)
    
    if lion_score > apeach_score:
        return True, lion_score - apeach_score
    else:
        return False, 0

def solution(n, info):
    maxi = 0
    result = []
    optimal_shoot = []

    def dfs(arrow, shoot, idx):
        nonlocal maxi, result, optimal_shoot

        # 모든 화살을 쏜 경우
        if arrow == n:
            is_win, diff = compare(info, shoot)
            if is_win:
                if diff > maxi:
                    maxi = diff
                    optimal_shoot = shoot[:]  # 최대 차이 갱신 시 리스트 복사
                elif diff == maxi:
                    # 같은 점수 차이면 더 낮은 점수에 많이 맞춘 것을 선택
                    if not optimal_shoot or shoot[::-1] > optimal_shoot[::-1]:
                        optimal_shoot = shoot[:]
            return

        # 더 이상 쏠 수 없으면 남은 화살 몰아주기
        if idx == 11:
            shoot[10] += (n - arrow)  # 남은 화살 몰아줌
            dfs(n, shoot, idx)
            shoot[10] -= (n - arrow)
            return

        # 화살을 쏘지 않는 경우
        dfs(arrow, shoot, idx + 1)

        # 현재 점수에 화살을 쏘는 경우 (단, 화살이 남아있어야 함)
        if arrow + info[idx] + 1 <= n:
            shoot[idx] = info[idx] + 1
            dfs(arrow + shoot[idx], shoot, idx + 1)
            shoot[idx] = 0

    dfs(0, [0] * 11, 0)
    
    if not optimal_shoot:
        return [-1]
    
    return optimal_shoot