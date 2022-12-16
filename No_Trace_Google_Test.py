from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
# 無痕模式
opts.add_argument("--incognito")
# 開啟chrome瀏覽無痕模式
driver = webdriver.Chrome(chrome_options=opts)
# 打開google
driver.get("http://www.google.com")

time.sleep(2)  # 等待兩秒
driver.quit()  # 關閉視窗
