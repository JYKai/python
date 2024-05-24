def solution(phone_book):
    book_dict = {}
    for phone_number in phone_book:
        book_dict[phone_number] = 1
        
    for phone_number in phone_book:
        check = ''
        for number in phone_number:
            check += number
            if check in book_dict and check != phone_number:
                return False
    return True
