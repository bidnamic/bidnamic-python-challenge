import io
import csv
import logging

logger = logging.getLogger('django')


def get_file(file):
    """
    This function convert uploaded .csv file to csv.reader object and return started from 2nd line
    Args:
        file: csv file

    Returns:
        File data
    """
    try:
        csv_file = io.StringIO(file.read().decode())
        csv_datas = csv.reader(csv_file)
        next(csv_datas)
    except StopIteration:
        logger.warning('File doesn\'t have second line')
        return None
    except AttributeError:
        logger.warning('File doesn\'t uploaded')
        return None

    logger.info('Upload file read success')
    return csv_datas
