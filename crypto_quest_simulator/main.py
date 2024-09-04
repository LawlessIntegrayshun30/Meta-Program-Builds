# main.py

from crypto_quest_simulator import CryptoQuestSimulator

class Main:
    """
    A class to run the main function
    """

    def __init__(self, wallets: dict, emails: dict):
        """
        The constructor for Main class.

        Parameters:
           wallets (dict): A dictionary containing the wallet addresses and their respective keys
           emails (dict): A dictionary containing the email addresses and their respective passwords
        """
        self.crypto_quest_simulator = CryptoQuestSimulator(wallets, emails)

    def main(self, wallet_address: str, email_address: str) -> str:
        """
        The main function to run the simulation

        Parameters:
            wallet_address (str): The address of the wallet to be accessed
            email_address (str): The address of the email account to be accessed

        Returns:
            str: The result of the simulation
        """
        return self.crypto_quest_simulator.simulate_quest(wallet_address, email_address)


if __name__ == "__main__":
    # Define the wallets and emails here
    # This is a placeholder for the actual wallets and emails
    wallets = {"wallet1": "key1", "wallet2": "key2"}
    emails = {"email1": "password1", "email2": "password2"}

    # Instantiate the Main class
    main = Main(wallets, emails)

    # Run the main function
    print(main.main("wallet1", "email1"))
