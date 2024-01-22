from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from credentials import username,password

# Configure Chrome options if needed
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')  # headless option

# Set the path to your ChromeDriver executable
chromedriver_path = '/home/dci-student/Desktop/python/personal/translate-history/chromedriver_linux64'
chrome_options.binary_location = chromedriver_path  

# Create the Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=chrome_options)

# URL of the website
url = 'https://www.bark.com/sellers/my-barks/'

# Initialise the ChromeDriver
driver = webdriver.Chrome()
def login():
        #get the url
        driver.get(url)

        # Log in
        email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
        email_input.send_keys(username)

        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys(password, Keys.ENTER)

        sleep(3)

        #Navigate to leads page
        lead_response_element = driver.find_element(By.XPATH,
        '/html/body/div[6]/div/div/div[3]/div[3]/div/div[2]/div/div[2]/div/p/a')
        lead_response_element.click()

def close_popup():
       
       popup = driver.find_element(By.ID, 'browser-push-permission-modal-close')
       popup.click()

def find_emails():
        #wait
        sleep(2)

        #get the first email when page loads
        # Extract and print the email or perform other actions as needed
        email_element = driver.find_element(By.CLASS_NAME,'buyer-email-display')
        email = email_element.text
        print(f'Email found: {email}')

        email_list = []
        email_list.append(email)
        print(f'email:{email} added to list')

        # Find and click on elements with the specified class
        elements = driver.find_elements(By.CLASS_NAME,'responses-projects-item') 

        for element in elements:
            element.click()

            # Wait for the content to load (you may need to adjust the time)
            sleep(3)

            # Extract
            email_element = driver.find_element(By.CLASS_NAME, 'buyer-email-display')
            email = email_element.text
            print(f'Email found: {email}')

            email_list = []
            email_list.append(email)
            print(f'email:{email} added to list')

def scroll():
    #find the load more button and click it 
    pass


def main():
    #Login
    login()
    
    #wait for popup
    sleep(8)
    
    #close popup
    close_popup()
    
    #collect emails
    find_emails()

    # Close the browser window 
    driver.quit()
