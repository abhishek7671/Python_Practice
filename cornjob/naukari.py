import time
import schedule
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 🚀 Configure Naukri Details
NAUKRI_EMAIL = "abhisheksuda201@gmail.com"
NAUKRI_PASSWORD = "Abhi@7671"
RESUME_PATH = r"C:\Users\abhisheksu\Downloads\Abhishek_Suda_Resume.pdf"
JOB_KEYWORDS = ["Python Developer", "Python AWS Docker SQL"]
LOCATIONS = ["Bangalore", "Hyderabad", "Chennai", "Pune"]
EXPERIENCE = "3"  # In years
APPLY_KEYWORDS = ["AWS", "Docker", "SQL", "Microservices", "MongoDB", "Python", "Django", "RestAPI'S", "Fastapi", "Flask"]

def setup_driver():
    """Set up Selenium WebDriver with proper configurations."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
    options.add_argument("--headless=new")  # Run in headless mode (remove if you need UI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  # Required for some environments
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    except Exception as e:
        print(f"❌ WebDriver setup failed: {e}")
        return None

def login_naukri(driver):
    """Login to Naukri."""
    if not driver:
        print("❌ Driver is not initialized. Exiting login.")
        return

    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    try:
        driver.find_element(By.ID, "usernameField").send_keys(NAUKRI_EMAIL)
        driver.find_element(By.ID, "passwordField").send_keys(NAUKRI_PASSWORD)
        driver.find_element(By.CLASS_NAME, "loginButton").click()
        time.sleep(5)
    except Exception as e:
        print(f"❌ Error during login: {e}")

def update_resume():
    """Update resume on Naukri every 30 minutes."""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Updating Resume on Naukri...")

    driver = setup_driver()
    if not driver:
        print("❌ Skipping resume update due to WebDriver error.")
        return

    try:
        login_naukri(driver)
        
        # Navigate to Profile Page
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)

        # Find and Upload Resume
        upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_button.send_keys(RESUME_PATH)
        time.sleep(5)

        print(f"✅ Resume updated successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"❌ Error updating resume: {e}")

    finally:
        driver.quit()

def search_and_apply_jobs():
    """Search and apply for jobs on Naukri."""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Searching & Applying for Jobs on Naukri...")

    driver = setup_driver()
    job_links = []

    if not driver:
        print("❌ Skipping job search due to WebDriver error.")
        return

    try:
        login_naukri(driver)

        for keyword in JOB_KEYWORDS:
            # 🔹 Search for Jobs
            search_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter skills / designations']")
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)

            # 🔹 Apply Filters
            for location in LOCATIONS:
                try:
                    location_filter = driver.find_element(By.XPATH, f"//label[contains(text(), '{location}')]")
                    location_filter.click()
                    time.sleep(2)
                except Exception:
                    print(f"⚠️ Location filter '{location}' not found!")

            # Experience Filter
            try:
                exp_filter = driver.find_element(By.XPATH, f"//label[contains(text(), '{EXPERIENCE} Years')]")
                exp_filter.click()
                time.sleep(3)
            except Exception:
                print("⚠️ Experience filter not found!")

            # 🔹 Extract Job Listings
            jobs = driver.find_elements(By.XPATH, "//a[@class='title fw500 ellipsis']")
            for job in jobs[:10]:  # Limit to top 10 jobs
                job_title = job.text
                job_link = job.get_attribute("href")

                # **Auto-Apply Logic**
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

        # 🔹 Save job links to CSV
        df = pd.DataFrame({"Job Links": job_links})
        df.to_csv("naukri_jobs_applied.csv", index=False)

        print("✅ Job links saved to naukri_jobs_applied.csv!")

    except Exception as e:
        print(f"❌ Error searching/applying jobs: {e}")

    finally:
        driver.quit()

# **Schedule Tasks**
schedule.every(1).minutes.do(update_resume)  # Update resume every 30 minutes
schedule.every(6).hours.do(search_and_apply_jobs)  # Search and apply every 6 hours

# Ensure it runs only on weekdays (Monday to Friday)
while True:
    if datetime.today().weekday() < 5:  # 0-4 represents Monday-Friday
        schedule.run_pending()
    time.sleep(60)  # Check every minute
