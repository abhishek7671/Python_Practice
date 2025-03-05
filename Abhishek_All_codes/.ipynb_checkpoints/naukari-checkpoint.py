import time
import schedule
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 🔹 Configure Naukri Details
NAUKRI_EMAIL = "abhisheksuda201@gmail.com"
NAUKRI_PASSWORD = "Abhi@7671"
RESUME_PATH = "C:\Users\abhisheksu\Downloads\Abhishek_Suda_Resume.pdf"
JOB_KEYWORDS = ["Python Developer", "Python AWS Docker SQL"]
LOCATIONS = ["Bangalore", "Hyderabad", "Chennai","Pune"]
EXPERIENCE = "3"  # In years
APPLY_KEYWORDS = ["AWS", "Docker", "SQL", "Microservices","MongoDB"]

def naukri_automation():
    """Handles both resume update and job search/apply in one function."""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting Naukri Automation...")

    driver = setup_driver()
    job_links = []

    try:
        login_naukri(driver)

        # **Step 1: Update Resume**
        print("🔄 Updating Resume...")
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)
        upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_button.send_keys(RESUME_PATH)
        time.sleep(5)
        print("✅ Resume updated successfully!")

        # **Step 2: Search & Apply for Jobs**
        print("🔍 Searching & Applying for Jobs...")
        for keyword in JOB_KEYWORDS:
            search_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter skills / designations']")
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)

            for location in LOCATIONS:
                try:
                    location_filter = driver.find_element(By.XPATH, f"//label[contains(text(), '{location}')]")
                    location_filter.click()
                    time.sleep(2)
                except Exception:
                    print(f"⚠️ Location filter '{location}' not found!")

            try:
                exp_filter = driver.find_element(By.XPATH, f"//label[contains(text(), '{EXPERIENCE} Years')]")
                exp_filter.click()
                time.sleep(3)
            except Exception:
                print("⚠️ Experience filter not found!")

            jobs = driver.find_elements(By.XPATH, "//a[@class='title fw500 ellipsis']")
            for job in jobs[:10]:  
                job_title = job.text
                job_link = job.get_attribute("href")

                if any(skill.lower() in job_title.lower() for skill in APPLY_KEYWORDS):
                    driver.get(job_link)
                    time.sleep(3)
                    try:
                        apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
                        apply_button.click()
                        print(f"✅ Applied for: {job_title}")
                        time.sleep(3)
                    except Exception:
                        print(f"⚠️ Could not apply for: {job_title}")

                job_links.append(job_link)

        df = pd.DataFrame({"Job Links": job_links})
        df.to_csv("naukri_jobs_applied.csv", index=False)
        print("✅ Job links saved to naukri_jobs_applied.csv!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()

def setup_driver():
    """Set up Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def login_naukri(driver):
    """Login to Naukri."""
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)
    driver.find_element(By.ID, "usernameField").send_keys(NAUKRI_EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(NAUKRI_PASSWORD)
    driver.find_element(By.CLASS_NAME, "loginButton").click()
    time.sleep(5)

# **Schedule the Task**
schedule.every(2).hours.do(naukri_automation)  # Runs every 2 hours (Monday - Friday)

# **Keep Running on Weekdays**
while True:
    if datetime.today().weekday() < 5:  # 0-4 represents Monday-Friday
        schedule.run_pending()
    time.sleep(60)  # Check every minute
