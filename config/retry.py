from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def send_like(video_url):
    try:
        driver.get(video_url)
        like_button.click()
    except ElementNotInteractableException:
        raise Exception("Bot detectado")