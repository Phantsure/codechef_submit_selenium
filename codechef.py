import time 
import sys
import os

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

IS_FIREFOX = True

if IS_FIREFOX:
    os.environ['MOZ_HEADLESS'] = '1'
    # path to profile
    profile = webdriver.FirefoxProfile('/home/USERNAME/.mozilla/firefox/rohzahnf.default')
    driver = webdriver.Firefox(executable_path='./geckodriver',
                               firefox_profile=profile)
else:
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=/home/USERNAME/.config/\
google-chrome/')
    options.headless = True
    driver = webdriver.Chrome(executable_path = '../chrome/chromedriver',
                              options = options)

driver.implicitly_wait(60)
target = sys.argv[1]
message = sys.argv[2]

try:
    driver.get("https://www.codechef.com/submit/{}".format(target))
    x_arg = '//input[@id="edit-sourcefile"]'
    title = driver.find_element_by_xpath(x_arg)
    title.send_keys(message)
    submit = driver.find_element_by_xpath('//input[@id="edit-submit-1"]')
    submit.click()
    time.sleep(5)
except Exception as e:
    f = open("error.log", "a")
    print("Error Occured.\n Check the error.log file")
    f.write(str(e))
    f.close()
finally:
    driver.close()
