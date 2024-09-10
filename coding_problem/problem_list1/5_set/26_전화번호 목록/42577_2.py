def solution(phone_book):
    n = len(phone_book)
    phone_book.sort()
    for i in range(n - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True