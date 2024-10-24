from flask import Flask, render_template
import threading
import time
from coin_fetcher import fetch_prices, load_existing_prices
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def load_prices():
    with open('moeda_precos.json') as f:
        prices = json.load(f) 
    return prices

print('get_prices')

@app.route('/prices', methods=['GET'])
def prices():
    return render_template('prices.html')

def start_fetching():
    while True:
        fetch_prices() 
        time.sleep(60) 

if __name__ == "__main__":
    # Inicia uma thread para a coleta de preços
    fetch_thread = threading.Thread(target=start_fetching)
    fetch_thread.daemon = True  # A thread vai encerrar quando a aplicação Flask for interrompida
    fetch_thread.start()

    # Inicia a aplicação Flask
    app.run(debug=True, port=3000)
