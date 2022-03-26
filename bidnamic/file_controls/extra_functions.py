import io
import csv
import logging
logger = logging.getLogger('django')


def get_file(file):
    """
    This function convert uploaded .csv file to csv.reader object and return started from 2nd line
    @param file:
    @return: _csv.reader
    """
    csv_file = io.StringIO(file.read().decode())
    csv_datas = csv.reader(csv_file)
    next(csv_datas)
    logger.info('Upload file read success')
    return csv_datas
