from src.validating_email.util import get_valid_emails

def test_get_valid_emails():
    emails = [
        "lara@hackerrank.com",
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com"
    ]
    
    expected_output = [
        "brian-23@hackerrank.com", 
        "britts_54@hackerrank.com", 
        "lara@hackerrank.com"
    ]
    
    assert get_valid_emails(emails) == expected_output