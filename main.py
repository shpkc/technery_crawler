from crawl import crawl
import schedule
import time
import os
from github_utils import get_github_repo, upload_github_issue
from datetime import datetime,timedelta
from pytz import timezone



def main():
    GITHUB_TOKEN = os.environ['GIT_TOKEN']
    REPOSITORY_NAME = "technery_crawler"
    
    seoul_timezone = timezone('Asia/Seoul')
    yesterday = datetime.now(seoul_timezone)-timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y년 %m월 %d일")


    issue_title = f"기술 블로그 신규 포스팅 알림 ({yesterday_date})"

    upload_contents = crawl()
    repo = get_github_repo(GITHUB_TOKEN, REPOSITORY_NAME)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
