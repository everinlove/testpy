import requests

# 目标URL
#url = 'https://www.zoomeye.org/searchResult?q=udpxy+subdivisions:%E5%8C%97%E4%BA%AC&page=1'
url = 'https://www.zoomeye.org/searchResult?q=udpxy'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 打印网页内容
    print(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")
