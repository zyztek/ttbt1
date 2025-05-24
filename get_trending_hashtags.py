def get_trending_hashtags(self):
    self.driver.get("https://www.tiktok.com/tag/")
    hashtags = self.driver.find_elements(By.XPATH, '//h3[@class="hashtag"]')
    return [tag.text for tag in hashtags]