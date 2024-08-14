import time
from selenium import webdriver
from message import send_message_to_contact
from flask import redirect, render_template, request, url_for
from read_document import read_excel_and_save_to_database
from database.db import count_contacts, count_contacts_with_message_sent_true, \
    update_all_contacts_message_sent_false, get_contacts_with_send_message_false, get_all_contacts_paginated


def create_routes(app):
    @app.route("/")
    def index():
        num_contacts = count_contacts()
        if num_contacts > 0:
            return redirect(url_for('send_message'))
        else:
            return redirect(url_for('upload_file'))

    @app.route('/upload')
    def upload_file():
        return render_template('upload.html')

    @app.route('/process_file', methods=['POST'])
    def process_file():
        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('upload_file'))

        read_excel_and_save_to_database(file)

        return redirect(url_for('send_message'))

    @app.route('/send_message', methods=['GET', 'POST'])
    def send_message():
        num_contacts = count_contacts()
        contacts_sent_true = count_contacts_with_message_sent_true()
        contacts_sent_false = num_contacts - contacts_sent_true

        if request.method == 'POST':
            num_contacts_to_send = int(request.form['num_contacts'])
            message = request.form['message']

            # Iniciar o navegador Chrome
            driver = webdriver.Chrome()

            # Carregar o WhatsApp Web
            driver.get("https://web.whatsapp.com")
            print("Por favor, escaneie o código QR com seu telefone.")
            time.sleep(20)

            # Iterar sobre os contatos e enviar mensagens
            contacts = get_contacts_with_send_message_false()[:num_contacts_to_send]
            for contact in contacts:
                contact_id, contact_name, contact_number, message_sent = contact

                # Verificar se o número de contato está vazio
                if not contact_number:
                    print(f"Número de contato vazio para {contact_name}, pulando para o próximo contato.")
                    continue

                if message_sent:
                    print(f"Mensagem já enviada para {contact_name}.")
                    continue

                send_message_to_contact(driver, contact_id, contact_name, contact_number, message)

            # Fechar o navegador
            driver.quit()

            return redirect(url_for('send_message'))
        else:
            return render_template('send_message.html', contacts_count=num_contacts,
                                   contacts_sent_true=contacts_sent_true,
                                   contacts_sent_false=contacts_sent_false)

    @app.route('/reset_message_sent', methods=['POST'])
    def reset_message_sent():
        update_all_contacts_message_sent_false()
        return redirect(url_for('send_message'))

    @app.route("/contacts")
    def list_contacts():
        page = request.args.get('page', 1, type=int)  # Página atual
        per_page = 10  # Quantidade de contatos por página
        paginated_data = get_all_contacts_paginated(page, per_page)

        return render_template(
            'contacts.html',
            contacts=paginated_data["contacts"],
            page=page,
            total_pages=paginated_data["total_pages"],
            total_contacts=paginated_data["total_contacts"]
        )
