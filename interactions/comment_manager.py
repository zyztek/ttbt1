from ai_comment_generator import AIContentGenerator
from utils.logger import logger

class CommentManager:
    def __init__(self):
        self.ai_generator = AIContentGenerator()
    
    def post_ai_comment(self, driver):
        try:
            comment = self.ai_generator.generate_comment()
            text_area = driver.find_element(By.XPATH, '//textarea[@placeholder="Añade un comentario..."]')
            text_area.send_keys(comment)
            text_area.send_keys(Keys.ENTER)
            logger.info(f"Comentario publicado: {comment[:20]}...")
            return True
        except Exception as e:
            logger.error(f"Error publicando comentario: {str(e)}")
            return False