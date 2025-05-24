class BotFactory:
    @staticmethod
    def create_bot(platform: str, driver):
        if platform == "tiktok":
            return TikTokBot(driver)
        elif platform == "instagram":
            return InstagramReelsBot(driver)
        elif platform == "youtube":
            return YouTubeShortsBot(driver)
        else:
            raise ValueError("Plataforma no soportada")