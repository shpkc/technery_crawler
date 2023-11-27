from datetime import datetime, timedelta, timezone



def is_one_month_ago(date_str):
    print(date_str)
    current_date = datetime.now(timezone.utc)
    
    # 입력된 날짜 문자열을 datetime 객체로 변환 (시간대 정보 포함)
    input_date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z').replace(tzinfo=timezone.utc)
    
    # 현재 날짜에서 한 달 전의 날짜 계산
    one_month_ago = current_date - timedelta(days=30)

    
    return input_date >= one_month_ago
