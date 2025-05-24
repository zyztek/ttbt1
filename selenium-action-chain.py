from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_by_offset(random.randint(0, 10), random.randint(0, 10)).perform()