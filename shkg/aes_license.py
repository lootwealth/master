from Crypto.Cipher import AES
import base64
import uuid
import logging
import sys


class AesCrypt:
    def __init__(self, data_):
        self.data_ = data_
        self.model_ = AES.MODE_ECB
        self.key_ = self.add_32('65011711lootwealth')
        self.aes = AES.new(self.key_, self.model_)

    @staticmethod
    def add_32(par):
        # print(f'par: {par}')
        par = par.encode(encoding='utf-8')
        while len(par) % 32 != 0:
            par += b'|'
        return par

    def aes_encrypt(self):
        text = self.add_32(self.data_)
        encrypt_text = self.aes.encrypt(text)
        encrypt_text = base64.encodebytes(encrypt_text)
        encrypt_text = encrypt_text.decode().strip().replace('\n', '')
        return encrypt_text

    def aes_decrypt(self):
        decrypt_text = base64.decodebytes(self.data_.encode())
        decrypt_text = self.aes.decrypt(decrypt_text)
        decrypt_text = decrypt_text.decode().strip('|')
        # print(type(decrypt_text))
        return eval(decrypt_text)


class GetData:
    def __init__(self, cfg_file, encrypt_model=None, decrypt_model=None):
        self.cfg_file = cfg_file
        self.encrypt_model = encrypt_model
        self.decrypt_model = decrypt_model

    def cfg_data(self):
        with open(self.cfg_file, 'r') as f:
            data = f.readline()
        return data


class LocalHostConfig:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def get_address():
        node = uuid.getnode()
        mac = uuid.UUID(int=node).hex[-12:]
        return mac
        # return '020c299b219d'

    def get_local_oc(self):
        localhost_address = self.get_address()
        oc_data = self.data
        if localhost_address in oc_data['host_cfg']:
            use_cfg = oc_data['host_cfg'][localhost_address]
            return dict(
                license_cfg=oc_data['license_cfg'],
                host_default_cfg=oc_data['host_default_cfg'],
                host_cfg=use_cfg,
                localhost_address=localhost_address
            )
        return False


def crypt_operation(filename, encrypt_model=None, decrypt_model=None):
    gd_obj = GetData(cfg_file=filename, encrypt_model=encrypt_model, decrypt_model=decrypt_model)
    aes_obj = AesCrypt(data_=gd_obj.cfg_data())
    # print(f"aes_obj:{aes_obj}")
    if encrypt_model:
        return aes_obj.aes_encrypt()
    if decrypt_model:
        return aes_obj.aes_decrypt()


if __name__ == '__main__':
    print(crypt_operation(filename='incofig.txt', encrypt_model=True))
    # get_value = crypt_operation(filename='configEncode.txt', decrypt_model=True)
    # print(get_value)
    # local_host_config_obj = LocalHostConfig(data=get_value)
    # local_host_config = local_host_config_obj.get_local_oc()
    # print(local_host_config)

