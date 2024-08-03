import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from time import sleep

# Configure Chrome options
options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver
try:
    driver = uc.Chrome(options=options)
    driver.get("https://europedataentry.com/login")
    wait = WebDriverWait(driver, 20)
except WebDriverException as e:
    print(f"Error initializing the Chrome driver: {e}")
    exit(1)

# Login to the website
try:
    mobile_number = wait.until(EC.element_to_be_clickable((By.ID, "phone")))
    mobile_number.send_keys(f"{input()}")

    password = driver.find_element(By.ID, "password")
    password.send_keys(f"{input()}")

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_button.click()
except (TimeoutException, NoSuchElementException) as e:
    print(f"Error during login: {e}")
    driver.quit()
    exit(1)

# Function to read and parse data from the text file
def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        records = re.findall(r'First Name: (.*?)\nLast Name: (.*?)\nEmail: (.*?)\nPhone: (.*?)\nGender: (.*?)\nDate Of Birth: (.*?)(?:\n|$)', data)
        return records
    except FileNotFoundError as e:
        print(f"Error reading file: {e}")
        exit(1)
    except re.error as e:
        print(f"Error parsing file: {e}")
        exit(1)

# Function to convert gender to camel case
def convert_gender(gender):
    gender_map = {
        'male': 'Male',
        'female': 'Female',
        'others': 'Others'
    }
    return gender_map.get(gender.lower(), gender)

# Function to fill the form with the parsed data
def fill_form(record):
    firstname, lastname, email, phone, gender, birth = record
    gender = convert_gender(gender)  # Convert gender to camel case

    try:
        # Fill in the form fields
        firstname_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/input[1]")))
        firstname_field.send_keys(firstname)

        lastname_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/input[2]")))
        lastname_field.send_keys(lastname)

        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/input[3]")))
        email_field.send_keys(email)

        phone_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/input[4]")))
        phone_field.send_keys(phone)

        gender_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/select")))
        gender_field.click()
        gender_option = wait.until(EC.presence_of_element_located((By.XPATH, f"//option[text()='{gender}']")))
        gender_option.click()

        birth_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/input[5]")))
        birth_field.send_keys(birth)

        submit = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/form/button")))
        submit.click()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error filling the form: {e}")

# Read the data from the text file
parsed_data = read_data("data.txt")

# Fill the form for each record
for record in parsed_data:
    fill_form(record)
    sleep(2)  # Add sleep to simulate realistic form submission delay

try:
    while True:
        pass
except KeyboardInterrupt:
    driver.quit()
