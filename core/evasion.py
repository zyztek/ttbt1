from selenium.webdriver import ActionChains
import random
import time

class HumanBehaviorSimulator:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
    
    def random_delay(self, min_sec=2, max_sec=5):
        time.sleep(random.uniform(min_sec, max_sec))
    
    def human_click(self, element):
        self._simulate_mouse_movement(element)
        element.click()
        self.random_delay(0.3, 0.8)
    
    def human_type(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.07, 0.12))
            if random.random() < 0.1:  # 10% de error tipográfico simulado
                element.send_keys(Keys.BACKSPACE)
                time.sleep(0.15)
                element.send_keys(char)
    
    def _simulate_mouse_movement(self, element):
        self.actions.move_to_element(element)
        for _ in range(random.randint(2, 4)):
            x = random.randint(-8, 8)
            y = random.randint(-8, 8)
            self.actions.move_by_offset(x, y)
        self.actions.perform()
    
    def watch_video(self):
        base_time = random.gauss(18, 4)
        time.sleep(abs(base_time))
    
    def random_scroll(self):
        scroll_pattern = random.choice([
            [300, 150, -200, 80],
            [450, -100, 50, 200],
            [150, 300, -150]
        ])
        for delta in scroll_pattern:
            self.driver.execute_script(f"window.scrollBy(0, {delta})")
            self.random_delay(0.5, 1.2)