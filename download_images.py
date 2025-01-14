import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Update with the correct path to your ChromeDriver
service = Service("C:\\Users\\asus\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL and login credentials
login_url = "https://portal.svkm.ac.in/usermgmt/login"
student_image_url = "https://portal.svkm.ac.in/MPSTME-NM-M/savedImages/"
username = "70552300015"
password = "Lavesh@2004"

# List of student IDs (example, expand as needed)
student_ids = [
    "70552300001",
    "70552300002",
    "70552300003",
    "70552300004",
    "70552300005",
    "70552300008",
    "70552300010",
    "70552300011",
    "70552300012",
    "70552300013",
    "70552300014",
    "70552300015",
    "70552300017",
    "70552300019",
    "70552300020",
    "70552300022",
    "70552300023",
    "70552300024",
    "70552300025",
    "70552300026",
    "70552300027",
    "70552300028",
    "70552300029",
    "70552300030",
    "70552300031",
    "70552300032",
    "70552300033",
    "70552300034",
    "70552300036",
    "70552300038",
    "70552300039",
    "70552300040",
    "70552300044",
    "70552300045",
    "70552300046",
    "70552300047",
    "70552300048",
    "70552300049",
    "70552300050",
    "70552300051",
    "70552300053",
    "70552300054",
    "70552300055",
    "70552300056",
    "70552300057",
    "70552300059",
    "70552300060",
    "70552300061",
    "70552300062",
    "70552300064",
    "70552300065",
    "70552300066",
    "70552300067",
    "70552300068",
    "70552300069",
    "70552300070",
    "70552300071",
    "70552300073",
    "70552300074",
    "70552300076",
    "70552300077",
    "70552300078",
    "70552300079",
    "70552300081",
    "70552300086",
    "70552300087",
    "70552200086"
]

# Create directory to save images
save_dir = "C:\\Users\\asus\\Downloads\\AI\\attendance_system\\student_images"
os.makedirs(save_dir, exist_ok=True)

# Login to the portal
driver.get(login_url)
time.sleep(2)  # Allow the page to load

# Fill the login form
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for the login to complete

# Check login success
if "homepage" in driver.current_url:
    print("Login successful!")
else:
    print("Login verification failed. Exiting...")
    driver.quit()
    exit()

# Function to download the images using Selenium
def download_image_selenium(student_id):
    image_url = f"{student_image_url}{student_id}.JPG"
    save_path = os.path.join(save_dir, f"{student_id}.JPG")
    
    # Open the image URL in a new tab
    driver.execute_script("window.open('');")  # Open a new blank tab
    driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
    driver.get(image_url)  # Navigate to the image URL
    time.sleep(2)  # Allow the image to load
    
    try:
        # Save the image from the browser
        with open(save_path, "wb") as f:
            f.write(driver.find_element(By.TAG_NAME, "img").screenshot_as_png)
        print(f"Downloaded: {image_url}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")
    
    # Close the current tab and return to the main tab
    driver.close()  # Close the current tab
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the main tab

# Download images for each student
for student_id in student_ids:
    download_image_selenium(student_id)

# Close the browser after completing all downloads
driver.quit()
