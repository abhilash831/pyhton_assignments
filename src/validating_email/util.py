import re

def is_valid(email):
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    return bool(re.match(pattern, email))

def get_valid_emails(emails):
    valid_emails = list(filter(is_valid, emails))
    valid_emails.sort()
    return valid_emails