import sqlite3


def create_database():
    try:
        print("Tentando criar o banco de dados...")
        conn = sqlite3.connect('contatos.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS contatos
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contact_name TEXT,
                    contact_number TEXT,
                    message_sent BOOL,
                    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()
        print("Banco de dados criado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")


def insert_contacts(contact_name, contact_number, message_sent=False):
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO contatos 
                        (contact_name, contact_number, message_sent) 
                        VALUES (?, ?, ?)''', (contact_name, contact_number, message_sent))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def get_contacts():
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()
    c.execute("SELECT id, contact_name, contact_number, message_sent FROM contatos")
    contacts = c.fetchall()
    conn.close()
    return contacts


def get_contact(contact_number):
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contatos WHERE contact_number = ?", (contact_number,))
    contact = c.fetchone()
    conn.close()
    return contact


def update_contact(contact_id, contact_name, contact_number, message_sent):
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()
    c.execute('''UPDATE contatos 
                        SET contact_name = ?, contact_number = ?, message_sent = ?
                        WHERE id = ?''', (contact_name, contact_number, message_sent, contact_id))
    conn.commit()
    conn.close()


def count_contacts():
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()

    try:
        c.execute("SELECT COUNT(*) FROM contatos")
        count = c.fetchone()[0]
        return count

    finally:
        c.close()
        conn.close()


def count_contacts_with_message_sent_true():
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()

    try:
        c.execute("SELECT COUNT(*) FROM contatos WHERE message_sent = 1")

        count = c.fetchone()[0]
        return count

    finally:
        c.close()
        conn.close()


def update_all_contacts_message_sent_false():
    conn = sqlite3.connect('contatos.db')
    c = conn.cursor()

    try:
        c.execute("UPDATE contatos SET message_sent = 0 WHERE message_sent = 1")
        conn.commit()

    finally:
        c.close()
        conn.close()
