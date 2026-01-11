from selenium.webdriver.common.by import By

driver = None
loc = (By.CSS_SELECTOR, ".telA")
# driver.find_element(By.CSS_SELECTOR, ".telA")
print(type(loc))
print(loc)
print("未解包之前", loc)
print("解包之后", *loc)
