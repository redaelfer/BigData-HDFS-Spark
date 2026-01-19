import socket
import time
import requests
import json
import random

API_URL = "https://api.coincap.io/v2/assets/bitcoin"

last_price = 42000.00

def get_crypto_data():
    global last_price
    try:
        response = requests.get(API_URL, timeout=2)
        if response.status_code == 200:
            data = response.json()
            price = float(data['data']['priceUsd'])
            timestamp = data['timestamp'] 
            last_price = price 
            return f"{timestamp},{price}\n"
    except Exception as e:
        print(f"⚠️ Mode Hors-Ligne (Erreur API): {e}")
    
    timestamp = int(time.time() * 1000)
    variation = random.uniform(-50, 50)
    last_price += variation
    return f"{timestamp},{last_price:.2f}\n"

def start_server():
    host = '0.0.0.0'
    port = 9999
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    
    print(f"--- LE PRODUCTEUR EST PRÊT SUR LE PORT {port} ---")
    
    conn, addr = s.accept()
    print(f"✅ Spark connecté : {addr}")
    
    try:
        while True:
            data = get_crypto_data()
            if data:
                print(f"Envoi -> {data.strip()}")
                conn.send(data.encode('utf-8'))
            time.sleep(1)
    except BrokenPipeError:
        print("❌ Spark s'est déconnecté.")
    except Exception as e:
        print(f"❌ Erreur critique : {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    while True:
        start_server()
        time.sleep(5)