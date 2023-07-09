from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

ur1 = "https://work.mma.go.kr/caisBYIS/search/cygonggogeomsaek.do"
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
service =Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(ur1)
time.sleep(2)


