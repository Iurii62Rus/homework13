import re


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    def is_valid_email(email):
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.(com|ru|net)$'
        return re.match(pattern, email) is not None

    sender = sender.strip().lower()
    recipient = recipient.strip().lower()

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Cannot send email from {sender} to {recipient}")
        return

    if sender == recipient:
        print("Cannot send an email to yourself!")
        return

    if sender == "university.help@gmail.com":
        print(f"Email successfully sent from {sender} to {recipient}.")
    else:
        print(f"NON-STANDARD SENDER! Email sent from {sender} to {recipient}.")


send_email('This is a test message', 'vasyok1337@gmail.com')
send_email('You see this message as the top student of the course!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Please correct the assignment', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Reminding myself about the webinar', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

