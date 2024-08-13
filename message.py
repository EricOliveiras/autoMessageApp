import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote
from database.db import update_contact

def send_message_to_contact(driver, contact_id, contact_name, contact_number, message):
  custom_message = f"Olá {contact_name}. {message}"

  try:
    encoded_message = quote(custom_message)
    url = f"https://web.whatsapp.com/send?phone={contact_number}&text={encoded_message}"

    driver.get(url)
    while len(driver.find_elements(By.ID, "side")) < 1:
      time.sleep(1)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')))
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
    print(f"Mensagem enviada para {contact_name} ({contact_number})")

    update_contact(contact_id, contact_name, contact_number, message_sent=True)

    delay = random.uniform(15, 60)

    time.sleep(delay)
  except Exception as e:
    print(f"Erro ao enviar mensagem para {contact_name} ({contact_number}): {str(e)}")