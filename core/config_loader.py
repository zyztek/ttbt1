# core/config_loader.py
def load_config():
    with open('config/default.json') as f:
        config = json.load(f)
    print(f"Parámetro 'max_views': {config['max_views']['description']}")