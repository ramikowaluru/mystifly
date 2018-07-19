
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import pandas as pd

from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import matplotlib.pyplot as plt


df=pd.DataFrame(columns=["time","value"])

def s_c(driver):
    submit=driver.find_element_by_id("ucc_go_btn_svg")
    ss=driver.find_element_by_id("to")
#     time.sleep(2)
#     ss.send_keys("INR - Indian Rupee")
    driver.find_element_by_xpath("//input[@id='to']").send_keys("INR - Indian Rupee")
    submit.click()
    value= driver.find_element_by_xpath("//span[@class='uccResultAmount']").text
    return float(value),driver.find_element_by_xpath("//span[@class='resultTime']").text
def run_for_two_hours(df):
    df2=df
    i=0
    while i<7:
        start=time.time()
#         binary = FirefoxBinary('C:/Users/Rami/Music/geckodriver.exe')
        driver = webdriver.Firefox(executable_path=r'C:/Users/Rami/Music/geckodriver.exe')
        driver.delete_all_cookies()
        driver.get("https://www.xe.com/")
        v=0
        value=0
        t=0
        while v<1:
            value,t=s_c(driver)
            v=value
        print(value,t)
        df2=df2.append({"value":value,"time":t})
        driver.quit()
        t2=600-(time.time()-start)
        if t2>0:
            time.sleep(t2)
        i=i+1
    return df2

#extracting the values from xe.com
df=run_for_two_hours(df)

#ploting the values
plt.scatter(df['time'],df['value'])
plt.xticks(rotation=90)
plt.title("Indian Rupee against dollar value over 1.5 hours")
plt.ylabel("INR value vs 1 dollar")
plt.xlabel("time")
plt.show()

