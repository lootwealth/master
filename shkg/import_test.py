import aes_license
import logging
import sys

def get_host_cfg():
    pass

if __name__ == '__main__':
    get_value = aes_license.crypt_operation(filename='config.txt', decrypt_model=True)
    # print(get_value)
    local_host_config_obj = aes_license.LocalHostConfig(data=get_value)
    local_host_config = local_host_config_obj.get_local_oc()
    print((local_host_config))
    # if local_host_config:
    #     print(f'<{local_host_config["localhost_address"]}> use cfg {local_host_config["host_cfg"]}')
    #     # logging.info(f'"{local_host_config[1]}" use cfg {local_host_config[0]}')
    # if local_host_config is False:
    #     logging.error(f'local host mac "{local_host_config[1]}" not in license list, program exit !')
    #     sys.exit()
