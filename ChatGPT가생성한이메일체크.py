import re

def is_valid_email(email):
    # 이메일 검증을 위한 정규 표현식 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # re.match를 사용하여 패턴과 일치하는지 확인
    return re.match(pattern, email) is not None

# 샘플 이메일 주소
emails = [
    "test@example.com",  # 정상적인 이메일
    "user.name@domain.co",  # 정상적인 이메일
    "user-name@sub.domain.net",  # 정상적인 이메일
    "user@domain",  # 최상위 도메인 누락 (잘못된 형식)
    "@nouser.com",  # 사용자명 없음 (잘못된 형식)
    "username@.com",  # 도메인명 없음 (잘못된 형식)
    "username@domain..com",  # 연속된 점 (잘못된 형식)
    "user name@domain.com",  # 공백 포함 (잘못된 형식)
    "user#name@domain.com",  # 특수문자 포함 (잘못된 형식)
    "valid-email123@sub.example.org"  # 정상적인 이메일
]

# 이메일 검증 실행
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")

"""
정규 표현식 자세한 설명:
- `^` : 문자열의 시작을 의미합니다.
- `[a-zA-Z0-9._%+-]+` : 이메일의 사용자명을 검사하는 부분으로, 다음을 포함할 수 있습니다.
  - `a-zA-Z0-9` : 영문 대소문자와 숫자 허용
  - `._%+-` : 점(`.`), 밑줄(`_`), 퍼센트(`%`), 더하기(`+`), 빼기(`-`) 허용
  - `+` : 위의 문자들이 하나 이상 포함될 수 있음을 의미
- `@` : 반드시 포함되어야 하는 `@` 기호
- `[a-zA-Z0-9.-]+` : 도메인명 검사
  - `a-zA-Z0-9` : 영문 대소문자와 숫자 허용
  - `.-` : 점(`.`)과 하이픈(`-`) 허용
  - `+` : 하나 이상 포함될 수 있음을 의미
- `\.` : 도메인과 최상위 도메인(TLD)을 구분하는 점(`.`)
  - 백슬래시(`\`)는 점(`.`)이 특수문자로 해석되지 않도록 이스케이프 처리
- `[a-zA-Z]{2,}` : 최상위 도메인(TLD) 검사
  - `a-zA-Z` : 영문 대소문자만 허용
  - `{2,}` : 최소 2자 이상 필요 (예: `.com`, `.net`, `.org` 등)
- `$` : 문자열의 끝을 의미합니다.

이 정규 표현식은 일반적인 이메일 형식을 검증하지만, 실제 이메일 유효성 검사는 더 정교한 방식이 필요할 수 있습니다.
"""
