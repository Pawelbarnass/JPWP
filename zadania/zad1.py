# Zadanie 1: Wzorzec Projektowy Builder

class EmailMessage:
    def __init__(self):
        self.recipient = None
        self.sender = None
        self.subject = None
        self.body = None
        self.attachments = []

    def __str__(self):
        attachments_str = ', '.join(self.attachments) if self.attachments else 'None'
        return (f"To: {self.recipient}\nFrom: {self.sender}\n"
                f"Subject: {self.subject}\nBody: {self.body}\n"
                f"Attachments: {attachments_str}")

class EmailBuilder:
    def __init__(self):
        self.email = EmailMessage()
        self.email.sender = "default.sender@example.com" # Domyślny nadawca

    def set_recipient(self, recipient: str) -> 'EmailBuilder':
        # TODO: Ustaw odbiorcę wiadomości (self.email.recipient)
        # Zwróć self, aby umożliwić łańcuchowe wywołania (fluent interface)
        self.email.recipient = recipient
        return self

    def set_subject(self, subject: str) -> 'EmailBuilder':
        # TODO: Ustaw temat wiadomości (self.email.subject)
        # Zwróć self
        self.email.subject = subject
        return self

    def set_body(self, body: str) -> 'EmailBuilder':
        # TODO: Ustaw treść wiadomości (self.email.body)
        # Zwróć self
        self.email.body = body
        return self

    def add_attachment(self, attachment: str) -> 'EmailBuilder':
        # TODO: Dodaj załącznik do listy załączników (self.email.attachments)
        # Zwróć self
        self.email.attachments.append(attachment)
        return self

    def build(self) -> EmailMessage:
        # TODO: Zwróć zbudowany obiekt EmailMessage.
        # Dodatkowo: sprawdź, czy odbiorca i temat są ustawione. Jeśli nie, rzuć ValueError.
        if not self.email.recipient or not self.email.subject:
            raise ValueError("Odbiorca i temat muszą być ustawione przed zbudowaniem wiadomości.")
        return self.email

# Przykład użycia (po uzupełnieniu TODO):
# builder = EmailBuilder()
# email = (builder.set_recipient("test@example.com")
#          .set_subject("Ważna wiadomość")
#          .set_body("To jest treść wiadomości.")
#          .add_attachment("raport.pdf")
#          .add_attachment("zdjecie.jpg")
#          .build())
# print(email)

# try:
#     email_error = EmailBuilder().set_recipient("error@example.com").build()
# except ValueError as e:
#     print(f"Błąd: {e}")