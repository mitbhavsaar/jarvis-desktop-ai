import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config

class WhatsAppCommands:
    def __init__(self):
        self.driver = None
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        if os.path.exists(config.CONTACTS_FILE):
            with open(config.CONTACTS_FILE, 'r') as f:
                return json.load(f)
        return {}

    def _init_driver(self):
        try:
            # Check if driver is already running and responsive
            if self.driver:
                self.driver.title
                return
        except Exception:
            self.driver = None

        if not self.driver:
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-data-dir={config.WHATSAPP_DATA_DIR}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.driver.get("https://web.whatsapp.com")
            print("Waiting for WhatsApp Web to load...")
            time.sleep(10) # Base wait

    def send_message(self, contact_name, message):
        # Handle "Me" or "Myself"
        if contact_name.lower() in ["me", "myself", "mera", "mane"]:
            contact_name = "Me" # Common way self is saved or searched

        phone = self.contacts.get(contact_name.lower(), contact_name)
        self._init_driver()
        
        try:
            # Wait for search box to be present
            time.sleep(2)
            search_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            search_box.clear()
            search_box.send_keys(phone)
            time.sleep(3)
            search_box.send_keys(Keys.ENTER)
            time.sleep(2)

            # Check if we are in the right chat
            msg_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.send_keys(message)
            msg_box.send_keys(Keys.ENTER)
            
            return f"Message sent to {contact_name}."
        except Exception as e:
            return f"Failed to send message. Make sure WhatsApp is logged in. Error: {str(e)}"
