import logging
logging.basicConfig(filename='shkg.log', level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S %p",)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")