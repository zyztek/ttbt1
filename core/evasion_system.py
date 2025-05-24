import random
import time
from selenium.webdriver import ActionChains

class EvasionSystem:
    """Sistema avanzado para evadir detección de bots"""
    
    def __init__(self, driver):
        self.driver = driver
        self.action_chain = ActionChains(driver)
    
    def human_mouse_movement(self, element):
        """Movimientos de ratón realistas"""
        try:
            # Trayectoria curva con desviación aleatoria
            self.action_chain.move_to_element(element)
            for _ in range(random.randint(2, 5)):
                x_offset = random.randint(-15, 15)
                y_offset = random.randint(-15, 15)
                self.action_chain.move_by_offset(x_offset, y_offset)
                self.action_chain.pause(random.uniform(0.1, 0.3))
            self.action_chain.perform()
        except Exception as e:
            print(f"Error en movimiento de ratón: {str(e)}")
    
    def random_click_delay(self):
        """Retrasos variables entre acciones"""
        delay = random.choice([
            (0.8, 1.5),   # Comportamiento rápido
            (1.5, 2.8),   # Comportamiento normal
            (3.0, 4.5)    # Comportamiento lento
        ])
        time.sleep(random.uniform(*delay))
    
    def clean_browser_fingerprint(self):
        """Limpieza de huella digital del navegador"""
        self.driver.execute_script("""
            window.localStorage.clear();
            window.sessionStorage.clear();
            document.cookie.split(";").forEach(c => {
                document.cookie = c.trim().split('=')[0] + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            });
        """)