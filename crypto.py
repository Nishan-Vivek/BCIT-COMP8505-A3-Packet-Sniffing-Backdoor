from Crypto.Cipher import AES

KEY = 'PUT SHARED KEY HERE 1234'
IV = 'PUT IV HERE 1234'


def encrypt(payload):
    crypt = AES.new(KEY, AES.MODE_CFB, IV)
    cipher_payload = crypt.encrypt(payload)
    return cipher_payload


def decrypt(cipher_payload):
    crypt = AES.new(KEY, AES.MODE_CFB, IV)
    payload = crypt.decrypt(cipher_payload)
    return payload
