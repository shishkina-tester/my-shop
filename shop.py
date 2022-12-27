# # Shop: отображение страницы товара
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
# # 2. Залогиньтесь
# my_account = driver.find_element(By.CSS_SELECTOR, "#menu-item-50>a")
# my_account.click()
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='username']").send_keys("shishkina_tester@mail.ru")
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='password']").send_keys("QQwer1234!@#$")
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='login']").click()
# # 3. Нажмите на вкладку "Shop"
# driver.find_element(By.CSS_SELECTOR,"#menu-item-40 a").click()
# # 4. Откройте книгу "HTML 5 Forms"
# HTML5_Forms=driver.find_element(By.CSS_SELECTOR,".post-181 h3")
# name_HTML5_Forms=HTML5_Forms.text
# HTML5_Forms.click()
# # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
# if name_HTML5_Forms=="HTML5 Forms":
#     print("Заголовок книги: 'HTML5 Forms'")
# else:
#     print("Заголовок книги: ", name_HTML5_Forms)
#
# driver.quit()


#
# # Shop: сортировка товаров
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
#
#
#
# #1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # # 2. Залогиньтесь
# my_account = driver.find_element(By.CSS_SELECTOR, "#menu-item-50>a")
# my_account.click()
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='username']").send_keys("shishkina_tester@mail.ru")
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='password']").send_keys("QQwer1234!@#$")
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='login']").click()
# # 3. Нажмите на вкладку "Shop"
# driver.find_element(By.CSS_SELECTOR,"#menu-item-40 a").click()
# # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# price_sort1=driver.find_element(By.CLASS_NAME,"orderby")
# price_sort_value1=price_sort1.get_attribute("Value")
# if price_sort_value1 is not None:
#     print("Вариант сортировки не выбран по умолчанию")
# else:
#     print("Вариант сортировки выбран по умолчанию")
# # • Используйте проверку по value
# # 5. Отсортируйте товары по цене от большей к меньшей
# # • в селекторах используйте класс Select
# price_sort=driver.find_element(By.CLASS_NAME,"orderby")
# selector_price_sort=Select(price_sort)
# selector_price_sort.select_by_value("price-desc")
# # 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# price_sort=driver.find_element(By.CLASS_NAME,"orderby")
# # 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# # • Используйте проверку по value
# price_sort2=driver.find_element(By.CLASS_NAME,"orderby")
# price_sort_slt=WebDriverWait(driver,15).until(EC.text_to_be_present_in_element_value((By.CLASS_NAME,"orderby"),"price-desc"))
# print("Вариант сортировки выбран:от большей к меньшей")
#
#
#
# driver.quit()







# # Shop: отображение, скидка товара
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
#
# # 1. Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2. Залогиньтесь
# my_account = driver.find_element(By.CSS_SELECTOR, "#menu-item-50>a")
# my_account.click()
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='username']").send_keys("shishkina_tester@mail.ru")
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='password']").send_keys("QQwer1234!@#$")
# driver.find_element(By.CSS_SELECTOR,".u-column1 [name='login']").click()
# # 3. Нажмите на вкладку "Shop"
# driver.find_element(By.CSS_SELECTOR,"#menu-item-40 a").click()
# # 4. Откройте книгу "Android Quick Start Guide"
# driver.find_element(By.CSS_SELECTOR, ".post-169 h3").click()
# # 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# price_start_guide=driver.find_element(By.CSS_SELECTOR,"[itemprop='offers'] del>span").text
# assert price_start_guide=="₹600.00"
# print("Cодержимое старой цены =",price_start_guide)
# # 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# price_new_start_guide=driver.find_element(By.CSS_SELECTOR,"[itemprop='offers'] ins>span").text
# assert price_new_start_guide=="₹450.00"
# print("Cодержимое новой цены =",price_new_start_guide)
# # 7. Добавьте явное ожидание и нажмите на обложку книги
# wait=WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"images"))).click()
# # • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# wait=WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"pp_close"))).click()
# driver.quit()








# # Shop: проверка цены в корзине
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
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop"
# driver.find_element(By.CSS_SELECTOR,"#menu-item-40 a").click()
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# driver.find_element(By.CSS_SELECTOR,".post-182 a:nth-child(2)").click()
# # 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00
# # item_in_basket=driver.find_element(By.CLASS_NAME,"cartcontents")
# # item_in_basket_txt=item_in_basket.text
# # price_in_basket=driver.find_element(By.CLASS_NAME,"")
# # price_in_basket_txt=price_in_basket.text
# # assert item_in_basket_txt=="1 Item"
# # assert price_in_basket_txt=="₹180.00"
# wait=WebDriverWait(driver,15)
# item_in_basket=wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"cartcontents"),"1 Item"))
# item_in_basket1=driver.find_element(By.CLASS_NAME,"cartcontents")
# item_in_basket_txt=item_in_basket1.text
# price_in_basket=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#wpmenucartli span.amount"),"₹180.00"))
# price_in_basket1=driver.find_element(By.CSS_SELECTOR,"#wpmenucartli span.amount")
# price_in_basket_txt=price_in_basket1.text
# print("Количество товаров = ",item_in_basket_txt,", а стоимость ",price_in_basket_txt)
# # • Используйте для проверки assert
# # 5. Перейдите в корзину
# basket=driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
# basket.click()
# # 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# wait=WebDriverWait(driver,10)
# subtotal=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-title='Subtotal']>span"),"₹180.00"))
# # 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# wait=WebDriverWait(driver,20)
# total=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total [data-title='Total']>strong>span"),"₹183.60"))
# # # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# # # если все книги будут out of stock - тогда пропустите это и следующие два задания
#
# driver.quit()






#
# # Shop: работа в корзине
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# # Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop"
# shop=driver.find_element(By.CSS_SELECTOR,"#menu-item-40 a")
# shop.click()
# # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# driver.execute_script("window.scrollBy(0, 300);")
# wait=WebDriverWait(driver,5)
# html5=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".post-182 a:nth-child(2)")))
# time.sleep(10)
# html5.click()
# # Добавляю книгу Mastering JavaScript
# mastering_js=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".post-165 a:nth-child(2)")))
# # mastering_js=driver.find_element(By.CSS_SELECTOR, ".post-165 a:nth-child(2)")
# time.sleep(5)
# mastering_js.click()
# # • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# # • После добавления 1-й книги добавьте sleep
# # 4. Перейдите в корзину
# basket=driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
# basket.click()
# # 5. Удалите первую книгу
# dell_html5=driver.find_element(By.CSS_SELECTOR,".cart_item:nth-child(1) .product-remove>a")
# time.sleep(10)
# dell_html5.click()
# # • Перед удалением добавьте sleep
# # 6. Нажмите на Undo (отмена удаления)
# undo=driver.find_element(By.CSS_SELECTOR,".woocommerce-message a")
# undo.click()
# # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# quantity=driver.find_element(By.CSS_SELECTOR,".cart_item:nth-child(1) input")
# quantity.clear()
# quantity.send_keys("3")
# # • Предварительно очистите поле с помощью локатор_поля.clear()
# # 8. Нажмите на кнопку "UPDATE BASKET"
# update_basket=driver.find_element(By.CSS_SELECTOR,".actions [name='update_cart']")
# update_basket.click()
# # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# quantity_value=quantity.get_attribute("value")
# assert quantity_value=="3"
# print("value элемента quantity для 'JS Data Structures and Algorithm' равно ", quantity_value)
# time.sleep(5)
# # 10. Нажмите на кнопку "APPLY COUPON"
# apply_coupon=driver.find_element(By.CSS_SELECTOR,".actions [name='apply_coupon']")
# time.sleep(10)
# apply_coupon.click()
# # • Перед нажатимем добавьте sleep
# # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# coupon_code=driver.find_element(By.CSS_SELECTOR,".woocommerce-error>li")
# coupon_code_txt=coupon_code.text
# print(coupon_code_txt)
# # # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
#
# driver.quit()
# #В этом автотесте добавила еще 2 дополнительных тайм-слипа,так как интернет скакал,то все проходило,то нет



#
# # Shop: покупка товара
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.support.select import Select
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# import time
#
#
# # 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# # 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# driver.find_element(By.CSS_SELECTOR,"#menu-item-40 a").click()
# driver.execute_script("window.scrollBy(0, 300);")
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# wait=WebDriverWait(driver,5)
# html5=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".post-182 a:nth-child(2)")))
# time.sleep(2)
# html5.click()
# time.sleep(2)
# # 4. Перейдите в корзину
# basket=driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
# basket.click()
# time.sleep(5)
# # 5. Нажмите "PROCEED TO CHECKOUT"
# wait=WebDriverWait(driver,10)
# checkout_button=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"checkout-button")))
# checkout_button.click()
# # 6. Заполните все обязательные поля
# # • Перед заполнением first name, добавьте явное ожидание
# # • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# # • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
#
# first_name=driver.find_element(By.ID,"billing_first_name")
# first_name.send_keys("Ludmila")
#
# last_name=driver.find_element(By.ID,"billing_last_name")
# last_name.send_keys("Shishkina")
#
# email=driver.find_element(By.ID,"billing_email")
# email.send_keys("shishkina_tester@mail.ru")
#
# # time.sleep(5)
# phone=driver.find_element(By.ID,"billing_phone")
# phone.send_keys("886529826558")
#
# country=driver.find_element(By.ID,"billing_country_field")
# country.click()
#
#
# country_drop=driver.find_element(By.ID,"s2id_autogen1_search")
# country_drop.send_keys("Russia")
# # time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#select2-results-1>li:nth-child(1)").click()
#
#
# adress=driver.find_element(By.CSS_SELECTOR,"[placeholder='Street address']")
# adress.send_keys("aaaa")
# city=driver.find_element(By.CSS_SELECTOR,"[autocomplete='address-level2']")
# city.send_keys("aaaa")
# driver.execute_script("window.scrollBy(0, 200);")
# time.sleep(5)
# state=driver.find_element(By.CSS_SELECTOR,"#billing_state[name='billing_state']")
# state.send_keys("aaaa")
# postcode=driver.find_element(By.CSS_SELECTOR,"[name='billing_postcode']")
# postcode.send_keys("aaaa")
#
# # • Перед заполнением first name, добавьте явное ожидание
# # • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# # • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# # 7. Выберите способ оплаты "Check Payments"
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)
# payment_method=driver.find_element(By.ID,"payment_method_cheque")
# payment_method.click()
#
#
# # • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# # 8. Нажмите PLACE ORDER
# place_order=driver.find_element(By.ID,"place_order")
# place_order.click()
# # 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# thankyou=wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
# print("Отображается надпись 'Thank you. Your order has been received'")
# # 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
# check_payments=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"tfoot>tr:nth-child(3)>td"),"Check Payments"))
# print("В Payment Method отображается текст 'Check Payments'")
#
#
# driver.quit()

# D:/Тестирование BE TESTED ДЗ+Теория/Python/book_store_testing