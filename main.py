import requests
import time
from datetime import datetime

# --- 💼 ARBİTRAJ AYARLARI ---
# Render US sunucusunda olduğumuz için Kalshi bizi engellemeyecek
POLY_CLOB_URL = "https://clob.polymarket.com/book" 
KALSHI_API = "https://trading-api.kalshi.com/trade-api/v2"

def get_us_identity_check():
    """Botun Amerika'da olup olmadığını test eder"""
    try:
        r = requests.get("https://ipapi.co/json/").json()
        print(f"🌍 Bot Konumu: {r.get('city')}, {r.get('country_name')}")
        print(f"🛡️ IP Adresi: {r.get('ip')}")
    except:
        print("🌍 Konum tespiti yapılamadı.")

def check_arb():
    # Bu kısım Amerika sunucusunda saniyede bir dönecek
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Piyasalar taranıyor...")
    # Buraya V62'deki profesyonel arbitraj mantığını ekleyeceğiz.

if __name__ == "__main__":
    get_us_identity_check()
    while True:
        check_arb()
        time.sleep(10) # Render Free Tier'da çok hızlı istek ban sebebi olabilir, 10sn ideal.
