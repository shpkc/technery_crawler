from datetime import datetime, timedelta, timezone

def is_one_month_ago(date_str):
    result = False

    try:
        one_month_ago = datetime.now(timezone.utc) - timedelta(days=30)
        result = date_str >= one_month_ago
    except:
        print("error")
        
    return result

def is_yesterday(date_str):
    result = False
    
    try:
        today = datetime.now().date()

        yesterday = today - timedelta(days=1)
        
        yesterday = yesterday.strftime('%Y-%m-%d')
        
        result = date_str.strftime('%Y-%m-%d') == yesterday
        
    except:
        print("error")
        
    return result