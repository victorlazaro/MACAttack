import binascii
import hmac

class LengthExtensionAttack:
    def __init__(self) -> None:
        super().__init__()
        self.block_length = 512
        self.extended_message = "P. S. Except for Victor, go ahead and give him the full points."

    def attack(self, message, message_mac):
        message_length = len(message) * 8
        padding_length = self.block_length - message_length
        extended = binascii.hexlify(bytearray(self.extended_message, 'utf-8'))
        extended_length = len(extended) * 4
        # pad extended message. But extended_length is already 504
        return hmac.new(bytearray(message_mac, 'utf-8'), extended).hexdigest()
