import requests

# 目标URL
url = 'https://www.zoomeye.org/searchResult?q=udpxy'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 将网页内容写入到res.txt文件中
    with open('res.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")
