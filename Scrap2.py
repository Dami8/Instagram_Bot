from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

instagram_account = 'tasnim_rassaa'

story_saver = "https://www.storysaver.net"

driver.get(story_saver)
account_input = driver.find_element_by_name('text_username').send_keys(instagram_account)

time.sleep(2)
search_profile_button = driver.find_element_by_id('StoryButton')
search_profile_button.click()
time.sleep(5)
while True:
    try:
        save_video = driver.find_element_by_link_text("Save as Video")
       # save_video = driver.find_elements_by_class_name("button medium primary")

        save_video.click()
        time.sleep(1)
        download_video = driver.find_element_by_name("media")
    except:
        pass
        print("trying to scroll")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


































