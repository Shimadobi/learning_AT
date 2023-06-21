import os
import logging
import sys


def print_catalog():
    catalog = os.listdir(path='.')
    print(catalog)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info(f'Путь к каталогу: {os.getcwd()}')
    logging.info(f'Количество файлов в каталоге: {len(catalog)}')


print_catalog()
