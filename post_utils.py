from github import Github
from supabase import create_client, Client
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_yesterday_posts():
    """
    db에서 어제 발행된 posts 가져오는 함수
    """
    SUPABASE_URL = os.environ['SUPABASE_URL']
        
    SUPABASE_API_KEY = os.environ['SUPABASE_API_KEY']

    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d 00:00:00+00')
    today = datetime.now().strftime('%Y-%m-%d 00:00:00+00')
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)
    
    data,count= supabase.table('posts').select('*').gt("post_created_at",yesterday).lt("post_created_at",today).execute()
    
    issue_body =  f"\n \n"
    
    
    for item in data[1]:
        title,link,author = item["title"], item["link"], item["author"]
        content = f"[{title}]({link})" +  "\n -"+ author + " <br/>\n "
        issue_body+=content
        
    return issue_body
    

    