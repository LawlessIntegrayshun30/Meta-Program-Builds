# email_manager.py

from typing import Dict

class EmailManager:
    """
    A class to manage the access to the email accounts
    """

    def __init__(self, emails: Dict[str, str]):
        """
        The constructor for EmailManager class.

        Parameters:
           emails (Dict[str, str]): A dictionary containing the email addresses and their respective passwords
        """
        self.emails = emails

    def access_email(self, email_address: str) -> str:
        """
        The function to access a specific email account

        Parameters:
            email_address (str): The address of the email account to be accessed

        Returns:
            str: The password of the email account
        """
        if email_address in self.emails:
            return self.emails[email_address]
        else:
            return "Email account not found"
