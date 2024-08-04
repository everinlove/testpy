"""
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
"""



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 定义要访问的网页URL
url = 'https://www.zoomeye.org/searchResult?q=udpxy+%2Bsubdivisions%3A%E5%8C%97%E4%BA%AC&page=1'

# 创建WebDriver实例，Selenium会自动查找默认的ChromeDriver路径
driver = webdriver.Chrome()

# 访问网页
driver.get(url)

# 等待页面加载完成
driver.implicitly_wait(10)

# 输出页面标题
print("页面标题:", driver.title)

# 获取页面outerHTML内容
outer_html_content = driver.page_source

# 打印outerHTML内容
print("页面outerHTML内容:")
print(outer_html_content)

# 关闭浏览器
driver.quit()

