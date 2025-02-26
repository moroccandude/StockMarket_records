import requests

def fetch_coingecko_data(**context):
    """Récupère les données depuis l'API CoinGecko."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': '100',
        'page': '1',
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    data = response.json()
    # On push les données dans XCom pour la prochaine tâche
    context['ti'].xcom_push(key='raw_data', value=data)
