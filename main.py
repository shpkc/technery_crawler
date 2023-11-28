from crawl import crawl
import schedule
import time



def main():
    schedule.every(1).hour.do(crawl)
    
    crawl()
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
