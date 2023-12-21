import feedparser
from supabase import create_client, Client
import pytz
from bs4 import BeautifulSoup
import ssl
import yaml
from utils.og_image import og_image
from utils.parse_date import parse_date
from utils.date_utils import is_one_month_ago, is_yesterday
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

now = datetime.now()

def crawl_posts():
    
    with open('db_tech_blog.yml') as f:
        community_list = yaml.full_load(f)
        
        print("수집중인 블로그 : " + str(len(community_list)) + "개")

        SUPABASE_URL = os.environ['SUPABASE_URL']
        SUPABASE_API_KEY = os.environ['SUPABASE_API_KEY']

        supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

        for item in community_list:
            name = item["name"]
            
            # 일단 rss 존재하는 블로그부터 수집
            if "rss" in item:
                    
                rss = item["rss"]
                print(name + "탐색중")
                
                if hasattr(ssl, '_create_unverified_context'):
                    ssl._create_default_https_context = ssl._create_unverified_context
                    
                feeds = feedparser.parse(rss)
                
                for feed in feeds.entries:
                    
                    updated = feed.updated
                    updated = updated.replace('GMT', '+0000')
                    updated = parse_date(updated)
                    updated = updated.replace(tzinfo=pytz.utc)
                    
                    isOneMonthAgo = is_one_month_ago(updated)
                    
                    isYesterday = is_yesterday(updated)
                                        
                    title = feed.title
                    description = BeautifulSoup(feed.description, 'html.parser').get_text(separator=' ', strip=True)[0:80]
                    link = feed.link
                    thumbnail = og_image(feed.link)
                    post_created_at = feed.updated
                    textValue = BeautifulSoup(feed.description, 'html.parser').get_text(separator=' ', strip=True)
                    

                    
                    if isOneMonthAgo:
                        data, count = supabase.table('posts').select('*').eq('title', feed.title).execute()
                        isExist = len(data[1]) != 0
                                
                        if not isExist:
                            
                                
                            print("새로 추가 : " + title)
                            
                            data = supabase.table("posts").insert({
                            "title":title,
                            "description":description,
                            "link":link,
                            "thumbnail":thumbnail,
                            "post_created_at":post_created_at,
                            "author":name,
                            "textValue":textValue,
                            }).execute()


if __name__ == "__main__":
    crawl_posts()
