from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import chromedriver_autoinstaller
from userinfo import username, password, security_code  # Kullanıcı bilgilerini içe aktar

class Instagram:
    def __init__(self, username, password, security_code):
        self.username = username
        self.password = password
        self.security_code = security_code

        # ChromeDriver'ı otomatik indir ve yolunu al
        driver_path = chromedriver_autoinstaller.install()

        # WebDriver için Service oluştur
        service = Service(driver_path)
        options = webdriver.ChromeOptions()

        # WebDriver başlat
        self.browser = webdriver.Chrome(service=service, options=options)

    def signIn(self):
        """Instagram'a giriş yapar ve doğrulama kodunu girer."""
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)  # Sayfanın yüklenmesini bekle

        usernameInput = self.browser.find_element(By.NAME, "username")
        passwordInput = self.browser.find_element(By.NAME, "password")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        
        time.sleep(5)  # Giriş işleminin tamamlanmasını bekle

        try:
            # Doğrulama kodu girme ekranını kontrol et
            security_input = self.browser.find_element(By.NAME, "verificationCode")
            security_input.send_keys(self.security_code)
            
            time.sleep(2)  # Kısa bir bekleme süresi
            
            # "Onayla" butonunu bul ve tıkla
            confirm_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Onayla')]")
            confirm_button.click()
            print("Güvenlik kodu başarıyla girildi ve onaylandı.")
            
            time.sleep(7)
            self.browser.get("https://www.instagram.com/javel.23_/explore/"
)  # Ana sayfaya yönlendir
            print("Instagram ana sayfasına geçildi.")

            # Çıkan pop-up'ı kapatma işlemi
            time.sleep(5)  # Sayfanın yüklenmesini bekle
            try:
                close_button = self.browser.find_element(By.XPATH, "//button[contains(@class, 'HoLwm')]")
                close_button.click()
                print("Açılan pop-up başarıyla kapatıldı.")
            except Exception as e:
                print("Pop-up kapatma butonu bulunamadı veya hata oluştu: ", e)

        except Exception as e:
            print(f"Doğrulama kodu girme işlemi başarısız oldu: {e}")

    def getFollowers(self):
        """Takipçileri alır (Geliştirme aşamasında)."""
        pass

    def followUser(self, username):
        """Belirtilen kullanıcıyı takip eder (Geliştirme aşamasında)."""
        pass

    def unFollowUser(self, username):
        """Belirtilen kullanıcıyı takipten çıkarır (Geliştirme aşamasında)."""
        pass

    def close(self):
        """Tarayıcıyı kapatır."""
        try:
            if self.browser:
                time.sleep(5)  # Kapatmadan önce bekleme süresi
                self.browser.quit()
        except Exception as e:
            print(f"Tarayıcı kapatma hatası: {e}")

# Programı başlat
app = Instagram(username, password, security_code)
app.signIn()

# Tarayıcıyı düzgün şekilde kapat
app.close()

# selenium kullanırken chromedriver yüklememiz gerekli!
# bunun için şu linki kullanın! Bilgisayarınızdaki Chrome sürümünü otomatik tespit ederek uygun ChromeDriver'ı indirir:
# https://pypi.org/project/chromedriver-autoinstaller/
# Nasıl yapılacağını README sayfasında detaylı olarak anlatacağım.
