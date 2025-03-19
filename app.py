from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import chromedriver_autoinstaller
from userinfo import username, password, security_code

class InstagramBot:
    def __init__(self, username, password, security_code):
        self.username = username
        self.password = password
        self.security_code = security_code
        driver_path = chromedriver_autoinstaller.install()
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        self.browser = webdriver.Chrome(service=service, options=options)

    def sign_in(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        
        try:
            cookie_button = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tümünü kabul et')]"))
            )
            cookie_button.click()
        except:
            pass
        
        username_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = self.browser.find_element(By.NAME, "password")
        
        username_input.send_keys(self.username)
        time.sleep(random.uniform(2, 4))
        password_input.send_keys(self.password)
        time.sleep(random.uniform(2, 4))
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        
        try:
            security_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='verificationCode']"))
            )
            security_input.send_keys(self.security_code)
            time.sleep(2)
            confirm_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Onayla')]")
            confirm_button.click()
        except:
            pass
        
        time.sleep(7)
        self.check_suspicious_login()
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(5)

    def check_suspicious_login(self):
        try:
            approval_button = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Bu bendim')]"))
            )
            approval_button.click()
            time.sleep(5)
        except:
            pass

    def get_followers(self, max_followers=1000):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(5)
        
        try:
            followers_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]")
            ))
            followers_button.click()
            time.sleep(5)
            
            modal = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role=dialog] ul"))
            )
            
            action = webdriver.ActionChains(self.browser)
            followers = set()
            last_count = 0
            
            while True:
                user_elements = modal.find_elements(By.TAG_NAME, "li")
                
                for user in user_elements:
                    try:
                        link_element = user.find_element(By.TAG_NAME, "a")
                        username = link_element.text.strip()
                        link = link_element.get_attribute("href")
                        if username and username not in followers:
                            followers.add(username)
                            print(f"{len(followers)} {link}")
                    except:
                        pass
                
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
                
                new_count = len(followers)
                if new_count >= max_followers or new_count == last_count:
                    break
                last_count = new_count
                
            print(f"Toplam takipçi sayısı: {len(followers)}")
            
        except Exception as e:
            print(f"Takipçi listesi açılamadı: {e}")
    
    def close(self):
        try:
            if self.browser:
                time.sleep(44444444445)
                self.browser.quit()
                print("Tarayıcı kapatıldı.")
        except Exception as e:
            print(f"Tarayıcı kapatma hatası: {e}")
            
    def followUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(1)

        followButton  = self.browser.find_element(By.TAG_NAME("button"))
        if followButton =="Takip Et":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username} sayfasını zaten takip ediyorsunuz")


    def followUsers(self,users):
        for user in users:
            self.followUser(user)


if __name__ == "__main__":
    app = InstagramBot(username, password, security_code)
    app.sign_in()
    app.get_followers()
    app.followUsers(["justinbieber","adele"])
    app.close()