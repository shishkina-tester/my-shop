# # Registration_login: регистрация аккаунта
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "My Account Menu"
# my_account=driver.find_element(By.CSS_SELECTOR,"#menu-item-50>a")
# my_account.click()
# # 3. В разделе "Register", введите email для регистрации
# driver.find_element(By.CSS_SELECTOR,".register [type='email']").send_keys("shishkina_tester@mail.ru")
# # 4. В разделе "Register", введите пароль для регистрации
# driver.find_element(By.CSS_SELECTOR,".register [type='password']").send_keys("QQwer1234!@#$")
# # • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# # • почту и пароль сохраните, потребуюутся в дальнейшем
# # 5. Нажмите на кнопку "Register"
# driver.find_element(By.CSS_SELECTOR,".u-column2 [type='submit']").click()
#
# driver.quit()
#
#
# # Registration_login: логин в систему
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "My Account Menu"
# my_account = driver.find_element(By.CSS_SELECTOR, "#menu-item-50>a")
# my_account.click()
# # 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='username']").send_keys("shishkina_tester@mail.ru")
# # 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='password']").send_keys("QQwer1234!@#$")
# # 5. Нажмите на кнопку "Login"
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='login']").click()
# # 6. Добавьте проверку, что на странице есть элемент "Logout"
# wait=WebDriverWait(driver,15)
# word_logout=wait.until(EC.text_to_be_present_in_element((By.ID,"body"),"Logout"))
#  print("На странице есть элемент Logout")
#
# driver.quit()



