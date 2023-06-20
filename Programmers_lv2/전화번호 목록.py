

# 전화 번호 목록
# 번호 목록이 많다 100만 까지
# 시간 절약 알고리즘을 구상해야 함
# 중첩 for 문을 사용하면 100만 * 100만 이므로 안댐
def solution(phone_book):
    # 바로 앞과 비교
    for p1,p2 in zip(sorted(phone_book),(sorted(phone_book))[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = ["12","123","1235","567","88"]

print(solution(phone_book))