username = "javel.23_"
password= "ılovemylife"
security_code = 28375046

from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Çevre değişkenini al
secret_data = os.getenv("SECRET_KEY")

# Kontrol amaçlı yazdır (Güvenlik için prodüksiyonda bunu yapmayın)
print(secret_data)
