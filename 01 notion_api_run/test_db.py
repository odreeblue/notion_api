from dotenv import dotenv_values
from notion_client import Client
from pprint import pprint


config = dotenv_values(".env")
notion_secret = config.get('NOTION_TOKEN')
notion = Client(auth=notion_secret)

databases = notion.search(filter={"property": "object", "value": "database"})

#pprint(pages['results'][0]['title'][0]['plain_text'])
#pprint(pages['results'][0]['id'])
cal_db_id = ""
work_db_id = ""
for database in databases['results']:
    database_title = database['title'][0]['plain_text']
    #pprint(database_title)
    if database_title == '작업_test':
        work_db_id = database['id']
        print(database_title+'의 id는 '+work_db_id)
    if database_title == '일정_test':
        cal_db_id = database['id']
        print(database_title+'의 id는 '+cal_db_id)



#print(database_id)

work_db_details = notion.databases.retrieve(database_id = work_db_id)
#pprint(work_db_details['properties'])
#pprint(work_db_details['properties']['기간'])

# name = str('작업 이름')
# pprint(work_db_details['properties'][name])

# for work_db_detail in work_db_details['properties'][name]:
#     pprint(work_db_detail)
    #pprint(work_db_details['properties'][work_db_detail])

# sort_option = []
# sort_option.append({'property': '상태', 'direction': 'ascending'})
# sort_option.append({'property': '이름', 'direction': 'descending'})

pprint(notion.databases.query(database_id=work_db_id, page_size=5))


work_db = notion.databases.query(database_id=work_db_id, page_size=5)
data1_name = work_db['results'][0]['properties'][str('작업 이름')]
data1_date = work_db['results'][0]['properties'][str('기간')]

pprint(data1_name)
print('------------------------------------')
pprint(data1_date)
###  여기까지 작업 db 내용, 이제 일정 db에 집어넣기

print('-----------일정 db--------------')
cal_db_details = notion.databases.query(database_id = cal_db_id,page_size=5)
#select_prop = cal_db_details['results'][0]['properties'][str('일정')]
pprint(cal_db_details['results'])

#cal_db_details['results'][0]['properties'][str('일정')] = data1_name

#pprint(databases['results'][0]['properties']['일정'])
#block_list = notion.block.children.list(block_id=cal_db_id)

#print(block_list)
#print(block_list['results'][0])
#for bl in block_list['results']:
#    pprint(bl)
#notion.databases.update(database_id=cal_db_id, title=title_value, properties=select_property)
