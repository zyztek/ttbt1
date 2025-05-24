from urllib.parse import urlparse, parse_qs

class LinkProcessor:
    @staticmethod
    def extract_video_id(url):
        parsed = urlparse(url)
        if parsed.netloc == 'www.tiktok.com':
            return parsed.path.split('/')[-1]
        return None
    
    @staticmethod
    def parse_deeplink(url):
        params = parse_qs(urlparse(url).query)
        return {
            'video_id': params.get('video_id', [None])[0],
            'user_id': params.get('user_id', [None])[0]
        }