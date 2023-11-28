import feedparser
import os
from supabase import create_client, Client
from datetime import datetime, timedelta, timezone
import pytz
from bs4 import BeautifulSoup
import requests
import ssl
import yaml
from utils.og_image import og_image
from utils.parse_date import parse_date
from utils.is_one_month_ago import is_one_month_ago


with open('db_community.yml') as f:
    community_list = yaml.full_load(f)


url: str = "https://nettbgrchfoegbakosnu.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5ldHRiZ3JjaGZvZWdiYWtvc251Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDAzNjE1OTEsImV4cCI6MjAxNTkzNzU5MX0._dhLgVkgdYb1gXuHhfTUcGcG14s9Jw3akhPFbVmRiBo"
supabase: Client = create_client(url, key)

response = supabase.table('posts').select("*").execute()

for item in community_list:
    name = item["name"]
    rss = item["rss"]
    
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
        
    feeds = feedparser.parse(rss)
    
    for feed in feeds.entries:
        updated = feed.updated
        updated = updated.replace('GMT', '+0000')
        updated = parse_date(updated)
        updated = updated.replace(tzinfo=pytz.utc)
        
        isOneMonthAgo = is_one_month_ago(updated)
    
        if isOneMonthAgo:
            data, count = supabase.table('posts').select('*').eq('title', feed.title).execute()
            isExist = len(data[1]) != 0
            
        
            if not isExist:
                title = feed.title
                description = BeautifulSoup(feed.description, 'html.parser').get_text(separator=' ', strip=True)[0:80]
                link = feed.link
                thumbnail = og_image(feed.link)
                post_created_at = feed.updated
                
                print("새로추가 : " + title)
            
                data = supabase.table('posts').insert({
                "title":title,
                "description":description,
                "link":link,
                "thumbnail":thumbnail,
                "post_created_at":post_created_at,
                "author":name,
                }).execute()
