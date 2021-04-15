from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from bs4 import BeautifulSoup as bs

while True:
    username = input("Enter Your Username: ")
    if username =="":
        break
        print("Username Invalid")
    passw = input("Enter Your Password: ")
    if passw == "":
        break
        print("Incorrect Password")
    account = input("Enter Account name to like photos of: ")
    if account == "":
        break
        print("Account Not Found")
    path = 'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(path)
    link = "https://instagram.com"
    driver.get(link)
    sleep(3)
    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    login.send_keys(username)
    password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys(passw)

    sleep(1)

    press = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    press.click()

    def search_username():
        try:
            element = WebDriverWait(driver, 20).until(
                ec.presence_of_element_located((By.XPATH , "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"))
            )
            element.send_keys(account)
            element.send_keys(Keys.RETURN)
        except:
            driver.quit()

    def click_user():
        try:
            element = WebDriverWait(driver, 5).until(
                ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div"))
            )
            element.click()
        except:
            driver.quit()
            print("No Username Found!")

    def click_photo():
        try:
            element = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "g47SY "))
            )
            if element.text != '0':
                try:
                    element = WebDriverWait(driver, 10).until(
                        ec.presence_of_element_located((By.CLASS_NAME, "_9AhH0"))
                    )
                    element.click()

                except:
                    driver.quit()
            else:
                driver.quit()
                print("No Posts Found!")

        except:
            driver.quit()

    def like_post():
        try:
            like = WebDriverWait(driver, 20).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button'))
            )
        
        
            soup = bs(like.get_attribute('innerHTML'),'html.parser')
            if(soup.find('svg')['aria-label'] == 'Like'):
                like.click()
                try:
                    like = WebDriverWait(driver, 20).until(
                        ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a'))
                    )
                    like.click()
                except:
                    driver.quit()
            else:
                try:
                    like = WebDriverWait(driver, 20).until(
                        ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a'))
                    )
                    like.click()
                except:
                    driver.quit()
        except:
            driver.quit()

        while True:
            try:
                like = WebDriverWait(driver, 20).until(
                    ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button'))
                )
            
            
                soup = bs(like.get_attribute('innerHTML'),'html.parser')
                if(soup.find('svg')['aria-label'] == 'Like'):
                    like.click()
                    try:
                        like = WebDriverWait(driver, 2).until(
                            ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a[2]'))
                        )
                        like.click()
                    except:
                        driver.quit()
                else:
                    try:
                        like = WebDriverWait(driver, 2).until(
                            ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a[2]'))
                        )
                        like.click()
                    except:
                        driver.quit()

            except:
                driver.quit()
                print("All Posts Liked!")
                break

    search_username()
    click_user()
    click_photo()
    like_post()

        



    
