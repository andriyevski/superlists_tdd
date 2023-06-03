from selenium import webdriver

browser = webdriver.Firefox()
browser_link=browser.get('Http://localhost:8000')


assert 'The install worked successfully! Congratulations!' in browser.title