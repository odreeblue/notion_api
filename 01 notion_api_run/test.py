from dotenv import dotenv_values
from notion_client import Client
from pprint import pprint


config = dotenv_values(".env")
notion_secret = config.get('NOTION_TOKEN')
notion = Client(auth=notion_secret)

pages = notion.search(filter={"property": "object", "value": "page"})
#pprint(pages)


#pprint(pages)

#pprint(pages['results'][0]['properties']['title']['title'][0]['plain_text'])
#pprint(pages['results'][0]['properties'])

pprint(pages['results'][0]['id'])
page_id = pages['results'][0]['id']
block_list = notion.blocks.children.list(block_id=page_id)
print('--------------')
pprint(block_list)
# for page in pages['results'][0]:
#    page_title = page['properties']['title']['title'][0]['plain_text']
#    if page_title_find = page_title:
#       print('찾는 페이지가 존재합니다.')
#       title_id = page['id']

target_block_id = block_list['results'][0]['id']
rich_text_temp = block_list['results'][0]['paragraph']['rich_text']
pprint(rich_text_temp)

text_value = rich_text_temp[0]['plain_text']
text_value = text_value.replace('페퍼로니', '크러스트')

rich_text_temp[0]['plain_text'] = text_value
rich_text_temp[0]['text']['content'] = text_value
pprint(rich_text_temp)

rich_text = {}
rich_text['rich_text'] = rich_text_temp

notion.blocks.update(block_id = target_block_id, paragraph = rich_text)



### 예제 코드 ###
# 옵션 모두 넣은 Search 호출
#  
# next_cursor = 'ff244636-d084-4cfb-93c3-55e6b82f53a0'
# query_word = '고객센터'
# sort_option = {"direction": "descending", "timestamp": "last_edited_time"}
# filter_option = {"property": "object","value": "page"}
# page_size_default = 10

# cs_block = notion.search(query=query_word, sort=sort_option, filter=filter_option,
#                          start_cursor=next_cursor, page_size=page_size_default)
