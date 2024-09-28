from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Create a Polkadot wallet
def create_polkadot_wallet():
    try:
        keypair = Keypair.create_from_mnemonic(Keypair.generate_mnemonic())
        return {
            'address': keypair.ss58_address,
            'mnemonic': keypair.mnemonic,
            'public_key': keypair.public_key
        }
    except Exception as e:
        print(f"Error creating Polkadot wallet: {e}")
        return None

# View the balance of a Polkadot address
def get_polkadot_balance(address):
    try:
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",
            type_registry_preset='polkadot'
        )
        result = substrate.query(
            module='System',
            storage_function='Account',
            params=[address]
        )
        return result['data']['free']
    except SubstrateRequestException as e:
        print(f"Error retrieving balance for {address}: {e}")
        return None

# Send DOT from one address to another
def send_dot(sender_mnemonic, recipient_address, amount):
    try:
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",
            type_registry_preset='polkadot'
        )
        keypair = Keypair.create_from_mnemonic(sender_mnemonic)

        # Compose a balance transfer call
        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={
                'dest': recipient_address,
                'value': amount
            }
        )

        # Create and sign extrinsic
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        return receipt
    except SubstrateRequestException as e:
        print(f"Error sending DOT: {e}")
        return None
