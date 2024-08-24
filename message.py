import time
import os
import random
from urllib.parse import quote
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database.db import update_contact


def send_message_to_contact(driver, contact_id, contact_name, contact_number, message, image_path=None):
    # Criação da mensagem personalizada
    if message:
        custom_message = f"Olá {contact_name}. {message}"
    else:
        custom_message = ""

    try:
        # Codifica a mensagem para a URL
        encoded_message = quote(custom_message)
        url = f"https://web.whatsapp.com/send?phone={contact_number}&text={encoded_message}"

        # Navega para a URL
        driver.get(url)

        # Aguarda até que a barra lateral do WhatsApp Web esteja visível
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "side")))

        if image_path and custom_message:
            # Envia a imagem e a mensagem
            attach_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')))
            attach_button.click()

            image_input = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
            image_input.send_keys(os.path.abspath(image_path))

            send_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span')))
            send_button.click()
            print(f"Imagem enviada para {contact_name} ({contact_number})")
        elif image_path:
            # Apenas imagem
            attach_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')))
            attach_button.click()

            image_input = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
            image_input.send_keys(os.path.abspath(image_path))

            send_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span')))
            send_button.click()
            print(f"Imagem enviada para {contact_name} ({contact_number})")

        elif custom_message:
            # Apenas mensagem
            message_box = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
            message_box.send_keys(Keys.ENTER)
            print(f"Mensagem enviada para {contact_name} ({contact_number})")

        # Atualiza o banco de dados para marcar a mensagem como enviada
        update_contact(contact_id, contact_name, contact_number, message_sent=True)

        # Delay aleatório para evitar bloqueio por parte do WhatsApp
        delay = random.uniform(15, 60)
        time.sleep(delay)

    except Exception as e:
        print(f"Erro ao enviar mensagem para {contact_name} ({contact_number}): {str(e)}")
