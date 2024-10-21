from selenium.webdriver.common.by import By
import time
import csv
from datetime import datetime
import argparse
import os
import sys
sys.path.append('/crawler')
from scripts.utils.utils import *

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--save_format", type=str, choices=["csv", "mysql"], default="csv")
    parser.add_argument("-u", "--url", type=str, required=True)
    args = parser.parse_args()
    
    return args

def main(args):
    ''' 0. Webpage URL for crawling '''
    url = f"web_page_url_to_crawl/{args.url}" # https://railway-news.com/
    
    
    ''' 1. Load Chrome Driver to use Selenium '''
    driver = Load_Driver()
    
    
    ''' 2. Get the date 1 year ago using func in utils.py '''
    year_ago_date = Get_Date_from_a_Year_ago()
    
    ## Formatting according to the Upload date format for each site !!!
    #ex) Aug 2022
    date_format = "%b %Y"
    year_ago_date = year_ago_date.strftime(date_format)
    year_ago_datetime = datetime.strptime(year_ago_date, date_format)
    
    
    ''' 3. Collect 1 year worth of article urls '''
    article_urls = []
    
    driver.get(url)
    
    while True:
        ''' Site-Specific article url collection code ... '''
        ## 3-0. Get article url in the current main page
        article_urls += ...
        
        ## 3-1. Find the crawled_date, the upload date of the last crawled article
        crawled_date = ...
        crawled_datetime = datetime.strptime(crawled_date, date_format)
    
        ## 3-2. Compare last crawled_date with year_ago_date
        if crawled_datetime <= year_ago_datetime: break
        else:
            ## Get next page
            try:
                next_url = 'next_page_url_to_crawl'
                soup = Load_soup(next_url)
        
            except Exception as e:
                print("CANNOT GET NEXT PAGE ! \n", e)
    
    
    ''' 4. Crawl the content of each article '''
    for article in article_urls:
        soup = Load_soup(article_url)
        
        vertical = ''
        sub_vertical = ''
        format = ''
        
        title = ''
        content = ''
        upload_date = ''
        
        ''' 5. Save Data '''
        if args.save_format == "csv":
            writer.writerow([vertical, sub_vertical, format, title, content, upload_date, article, ''])
            print([vertical, sub_vertical, format, title, content, upload_date, article, ''])

        elif args.save_format == "mysql":
            Save_to_MySQL(vertical, sub_vertical, format, title, content, upload_date, article, '')
    
    
    driver.quit()


if __name__ == '__main__':
    args = parse_arg()
    
    # If you want to save the data to csv file ,
    if args.save_format == "csv":
        csv_path = ""
        os.makedirs(csv_path, exist_ok=True)
        csv_save_path = f'{csv_path}/{args.url}.csv'
        f = open(csv_save_path, "w", encoding="utf-8", newline="")
        writer = csv.writer(f)
        writer.writerow(["Vertical", "Sub_Vertical", "Format", "Title", "Content", "Upload_Date", "URL", "Video"])
        
    main(args)
    
    if args.save_format == "csv": f.close()
