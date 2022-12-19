from selenium import webdriver
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='https://selenium-zpdttqpoxq-nn.a.run.app',
options=options
)
#maximize the window size
driver.maximize_window()
time.sleep(10)
#navigate to browserstack.com
driver.get("https://www.browserstack.com/")
time.sleep(10)
#click on the Get started for free button
driver.find_element("id","signupModalButton").click()
time.sleep(10)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
