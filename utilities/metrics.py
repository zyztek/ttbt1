from prometheus_client import start_http_server, Counter

class MetricsCollector:
    def __init__(self):
        self.views = Counter('tiktok_views', 'Total de videos vistos')
        self.likes = Counter('tiktok_likes', 'Total de likes dados')
    
    def start(self, port=8000):
        start_http_server(port)
    
    def record_view(self):
        self.views.inc()
    
    def record_like(self):
        self.likes.inc()