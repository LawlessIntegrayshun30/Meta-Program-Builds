# wallet_manager.py

from typing import Dict

class WalletManager:
    """
    A class to manage the access to the wallets
    """

    def __init__(self, wallets: Dict[str, str]):
        """
        The constructor for WalletManager class.

        Parameters:
           wallets (Dict[str, str]): A dictionary containing the wallet addresses and their respective keys
        """
        self.wallets = wallets

    def access_wallet(self, wallet_address: str) -> str:
        """
        The function to access a specific wallet

        Parameters:
            wallet_address (str): The address of the wallet to be accessed

        Returns:
            str: The key of the wallet
        """
        if wallet_address in self.wallets:
            return self.wallets[wallet_address]
        else:
            return "Wallet not found"
