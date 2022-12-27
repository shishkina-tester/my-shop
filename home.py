# # Home: добавление комментария
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
#
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Проскролльте страницу вниз на 600 пикселей
# driver.execute_script("window.scrollBy(0, 600);")
# # 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# book_selenium_ruby=driver.find_element(By.CSS_SELECTOR,".post-160 h3")
# book_selenium_ruby.click()
# # 4. Нажмите на вкладку "REVIEWS"
# sr_reviews=driver.find_element(By.CSS_SELECTOR,"a[href='#tab-reviews']")
# sr_reviews.click()
# # 5. Поставьте 5 звёзд
# star_5=driver.find_element(By.CLASS_NAME,"star-5")
# # 6. Заполните поле "Review" сообщением: "Nice book!"
# driver.find_element(By.ID,"comment").send_keys("Nice book!")
# # 7. Заполните поле "Name"
# driver.find_element(By.ID,"author").send_keys("Ludmila")
# # 8. Заполните "Email"
# driver.find_element(By.ID,"email").send_keys("shishkina_tester@mail.ru")
# # 9. Нажмите на кнопку "SUBMIT"
# driver.find_element(By.NAME,"submit").click()
#
# driver.quit()