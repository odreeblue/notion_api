from dotenv import dotenv_values
from notion_client import Client
from pprint import pprint

# .env 파일에서 Notion API 키 가져오기
config = dotenv_values(".env")
notion_secret = config.get('NOTION_TOKEN')

# Notion 클라이언트 인스턴스 생성
notion = Client(auth=notion_secret)

# 일정 데이터베이스 ID 가져오기
cal_db_name = "일정_test"
cal_db_id = ""

databases = notion.search(filter={"property": "object", "value": "database"})
for database in databases['results']:
    database_title = database['title'][0]['plain_text']
    #pprint(database_title)
    if database_title == '작업_test':
        work_db_id = database['id']
        print(database_title+'의 id는 '+work_db_id)
    if database_title == '일정_test':
        cal_db_id = database['id']
        print(database_title+'의 id는 '+cal_db_id)