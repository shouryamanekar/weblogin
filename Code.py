from selenium import webdriver
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\chromedriver.exe')

def login(url,username, user, password, passw, loginbutton):
   driver.get(url)
   driver.find_element_by_id(username).send_keys(user)
   driver.find_element_by_id(password).send_keys(passw)
   driver.find_element_by_id(loginbutton).click()
   driver.minimize_window()
login("Enter your URL link here", "username", "Enter your Username here", "password", 'Enter your Password here', "loginbutton id")

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
