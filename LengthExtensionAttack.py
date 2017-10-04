import binascii
import hmac
from sha1 import sha1

class LengthExtensionAttack:
    def __init__(self) -> None:
        super().__init__()
        self.block_length = 512
        self.key_length = 128
        self.extended_message = "Give Victor Lazaro an A"

    def attack(self, message):
        extended_message_digest = sha1(bytes(self.extended_message, 'utf-8'))

        hex_str = binascii.hexlify(bytes(message))
        hex_str += b'8'
        for i in range(126):
            hex_str += b'0'
        hex_str += b'1f8'
        hex_str += binascii.hexlify(bytes(self.extended_message, 'utf-8'))
        return extended_message_digest, hex_str
