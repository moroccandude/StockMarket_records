import sys
import json
for data in sys.stdin:
    data = data.strip()
   
    if not data:
        continue
    try:
        records = json.loads(data)
       
    except json.JSONDecodeError as e:
        # print(f"BAD data: {data}", file=sys.stderr)
        continue
    for record in records:
      coin_id = record.get('id')
      current_price = record.get('current_price')
      volume = record.get('total_volume')
    
    # # Vérifications basiques
      if not coin_id or current_price is None or volume is None:
         continue

      try:
         price_float = float(current_price)
         volume_float = float(volume)
      except ValueError:
         continue

    # On prépare la somme des prix et la somme des carrés de prix
      price_squared = price_float * price_float

    # Format = "sumPrice=..., sumPriceSq=..., volume=..., count=1"
    # On stocke tout sur une seule ligne séparée par des virgules
      print(f"{coin_id}\t{price_float},{price_squared},{volume_float},1")
