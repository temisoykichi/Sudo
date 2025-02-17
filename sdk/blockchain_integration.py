# blockchain_integration.py

import requests
import json
from .logging_config import logger

class BlockchainIntegration:
    def __init__(self, blockchain_url: str, token_contract_address: str):
        """
        Initializes the blockchain integration with the provided blockchain URL and token contract address.
        
        :param blockchain_url: URL of the blockchain node or API (e.g., Ethereum node URL)
        :param token_contract_address: The address of the $SUDO token contract
        """
        self.blockchain_url = blockchain_url
        self.token_contract_address = token_contract_address

    def send_transaction(self, sender_address: str, recipient_address: str, amount: float, private_key: str):
        """
        Sends a transaction from the sender to the recipient using the blockchain's API.
        
        :param sender_address: The address sending the $SUDO tokens
        :param recipient_address: The address receiving the $SUDO tokens
        :param amount: The amount of $SUDO tokens to send
        :param private_key: The private key of the sender to sign the transaction
        :return: The transaction hash or an error message
        """
        try:
            # Construct the transaction data
            transaction_data = {
                "from": sender_address,
                "to": recipient_address,
                "value": self.convert_to_wei(amount),  # Convert to smallest unit (e.g., wei for Ethereum)
                "data": "0x",  # Optional data field
                "gas": "0x5208",  # Default gas limit (example: 21000 gas units for basic transaction)
                "gasPrice": "0x09184e72a000",  # Gas price (example)
            }

            # Sign and send the transaction (simplified example)
            signed_transaction = self._sign_transaction(transaction_data, private_key)
            transaction_hash = self._send_raw_transaction(signed_transaction)

            logger.info(f"Transaction sent successfully. Hash: {transaction_hash}")
            return transaction_hash

        except Exception as e:
            logger.error(f"Error in sending transaction: {str(e)}")
            return {"error": str(e)}

    def _sign_transaction(self, transaction_data: dict, private_key: str):
        """
        Signs the transaction using the sender's private key.
        
        :param transaction_data: The transaction data to sign
        :param private_key: The sender's private key to sign the transaction
        :return: The signed transaction in raw format
        """
        # Placeholder for signing logic (e.g., using Ethereum's `eth_account` library)
        # Implement signing logic based on the blockchain you're interacting with (e.g., Ethereum, Polkadot)
        logger.info("Signing transaction...")
        signed_transaction = transaction_data  # This is a simplified placeholder
        return signed_transaction

    def _send_raw_transaction(self, signed_transaction: dict):
        """
        Sends a signed transaction to the blockchain network.
        
        :param signed_transaction: The signed transaction to send
        :return: The transaction hash of the sent transaction
        """
        try:
            # Send the transaction to the blockchain node/API
            headers = {"Content-Type": "application/json"}
            response = requests.post(self.blockchain_url, data=json.dumps(signed_transaction), headers=headers)
            
            # Handle the response and extract the transaction hash
            if response.status_code == 200:
                result = response.json()
                transaction_hash = result.get("transactionHash")
                return transaction_hash
            else:
                raise Exception("Failed to send transaction. Response: " + response.text)
        
        except Exception as e:
            logger.error(f"Failed to send raw transaction: {str(e)}")
            raise Exception(f"Blockchain transaction failed: {str(e)}")

    def convert_to_wei(self, amount: float):
        """
        Converts the amount of $SUDO tokens to the smallest unit (e.g., wei for Ethereum).
        
        :param amount: The amount in $SUDO tokens
        :return: The amount in the smallest unit (e.g., wei)
        """
        # Assume $SUDO token has 18 decimals, like Ethereum's Ether
        return int(amount * (10 ** 18))

    def get_balance(self, address: str):
        """
        Retrieves the balance of a specific address on the blockchain.
        
        :param address: The address to check the balance for
        :return: The balance of $SUDO tokens for the given address
        """
        try:
            # Placeholder API call to fetch balance
            response = requests.get(f"{self.blockchain_url}/balance/{address}")
            if response.status_code == 200:
                balance_data = response.json()
                return balance_data.get("balance", 0)
            else:
                raise Exception(f"Failed to fetch balance. Response: {response.text}")

        except Exception as e:
            logger.error(f"Error in fetching balance: {str(e)}")
            return {"error": str(e)}

    def log_event(self, event_data: dict):
        """
        Logs an event to the blockchain, for example, a governance event or task completion.
        
        :param event_data: The event data to log on-chain (e.g., task completed, governance decision)
        :return: The transaction hash for the logged event
        """
        try:
            # Event data would be a custom structure for your use case (simplified example)
            event_data["eventTimestamp"] = self._get_current_timestamp()
            
            # Placeholder for event logging (sending a transaction to log the event)
            transaction_hash = self.send_transaction(
                sender_address="your_sender_address_here",
                recipient_address="your_recipient_address_here",
                amount=0,  # No tokens involved in the logging, just an event
                private_key="your_private_key_here"
            )

            logger.info(f"Event logged successfully. Transaction Hash: {transaction_hash}")
            return transaction_hash
        except Exception as e:
            logger.error(f"Error in logging event: {str(e)}")
            return {"error": str(e)}

    def _get_current_timestamp(self):
        """
        Returns the current timestamp.
        
        :return: The current timestamp (e.g., in seconds since epoch)
        """
        from time import time
        return int(time())

