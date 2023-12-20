import os
from github_utils import get_github_repo, upload_github_issue
from datetime import datetime,timedelta
from pytz import timezone
from post_utils import get_yesterday_posts


"""
매일 오전 8시 issue 생성
"""
def main():
    GITHUB_TOKEN = os.environ['GIT_TOKEN']
    REPOSITORY_NAME = "technery_crawler"
    
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")


    issue_title = f"기술 블로그 신규 포스팅 알림 ({today_date})"

    upload_contents = get_yesterday_posts()
    
    repo = get_github_repo(GITHUB_TOKEN, REPOSITORY_NAME)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
    

if __name__ == "__main__":
    main()
