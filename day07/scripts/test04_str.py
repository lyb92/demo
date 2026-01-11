# 需求： 11111+2222
from selenium.webdriver.common.by import By

num = "1129283245313421"

for n in num:
    calc_num = By.CSS_SELECTOR, "simple{}".format(n)
    print(n)
    print(calc_num)
