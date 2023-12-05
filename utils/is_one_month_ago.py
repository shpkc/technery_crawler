from datetime import datetime, timedelta, timezone

def is_one_month_ago(date_str):
    result = False
    
    try:
        one_month_ago = datetime.now(timezone.utc) - timedelta(days=30)
        result = date_str >= one_month_ago
    except:
        print("error")
    

    
    return result
