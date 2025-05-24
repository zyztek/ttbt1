import random
import time
from selenium.webdriver.common.action_chains import ActionChains

class HumanBehavior:
    @staticmethod
    def random_watch_time():
        return random.uniform(8, 25)  # Entre 8 y 25 segundos
    
    @staticmethod
    def human_scroll(driver):
        scroll_amount = random.randint(300, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount})")
        time.sleep(random.uniform(0.5, 1.5))
    
    @staticmethod
    def human_mouse_movement(driver):
        actions = ActionChains(driver)
        for _ in range(random.randint(2, 5)):
            x_offset = random.randint(-10, 10)
            y_offset = random.randint(-10, 10)
            actions.move_by_offset(x_offset, y_offset)
        actions.pause(random.uniform(0.1, 0.3))
        actions.perform()