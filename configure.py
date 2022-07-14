import decouple
from pathlib import Path

#
# Project root
APP_DIR = Path(__file__).parent

#
# App info
APP_NAME = 'MyApp'
APP_DESC = 'A description of the app.'
APP_VS = 1.0
APP_REPO = 'https://github.com/wcDogg'
APP_AUTHOR = 'wcDogg' 

#
# Sensitive data
# !!! Do not edit here - use .env !!!

if not decouple.config('API_KEY'):
  API_KEY = decouple.config('API_KEY', default=False, cast=bool)
else: 
  API_KEY = decouple.config('API_KEY')

#
# Supported file formats.
MIME_TYPES = ['image/jpeg', 'image/tiff', 'image/png']
FILE_FORMATS = ['JPEG', 'TIFF', 'PNG']

#
# Max file size to process. Out-of-range are skipped. 
MAX_MB = 60

#
# Max width * height px to process.
# Decompression bomb threshold.
MAX_PX = 144000000

#
# Sleep allows results time to print to terminal
SLEEP = 0.10

#
# Typer defaults + help strings
DIR_HELP = 'The path to a directory with images to process.'
FILE_HELP = 'The path to an image file.'

MD_DEFAULT = False
MD_HELP = 'Write results to Markdown.'

JSON_DEFAULT = False
JSON_HELP = 'Write results to JSON.'

CSV_DEFAULT = False
CSV_HELP = 'Write results to JSON.'

TASK_CONF = 'Are the options above correct?'


#
# logger.py

# 'NOTSET' 0, 'DEBUG' 10, 'INFO' 20, 'WARNING' 30, 'ERROR' 40, 'CRITICAL' 50
LOG_CONSOLE_LEVEL = 'DEBUG'
# 'standard', 'complete'
LOG_FORMAT = 'standard'

# # https://pypi.org/project/appdirs/
# import appdirs
# LOG_DIR = Path(appdirs.user_log_dir(APP_NAME, False))

LOG_DIR = APP_DIR / 'logs'
LOG_FILE_COMBO = APP_NAME + '.log'
LOG_PATH_COMBO = Path(LOG_DIR / LOG_FILE_COMBO)

LOG_FILE_INFO = APP_NAME + '_info.log'
LOG_PATH_INFO = Path(LOG_DIR / LOG_FILE_INFO) 

LOG_FILE_DEBUG = APP_NAME + '_debug.log'
LOG_PATH_DEBUG = Path(LOG_DIR / LOG_FILE_DEBUG) 

LOG_FILE_WARN = APP_NAME + '_warning.log'
LOG_PATH_WARN = Path(LOG_DIR / LOG_FILE_WARN)

LOG_FILE_ERROR = APP_NAME + '_error.log'
LOG_PATH_ERROR = Path(LOG_DIR / LOG_FILE_ERROR)

LOG_FILE_CRIT = APP_NAME + '_critical.log'
LOG_PATH_CRIT = Path(LOG_DIR / LOG_FILE_CRIT)

#
# Processing results
# These are here vs msgs.py because they're used 
# in validations and post-process sifting. 
PROC_TRUE = 'Processed'

PROC_FALSE = 'Not processed'

PROC_ERROR = 'Error'
PROC_MSG_API = 'Problem with API'



#
# Test
def test():
  '''Prints constants to console for manual review.
  '''
  print(f'APP_DIR: {APP_DIR}')
  print(f'APP_NAME: {APP_NAME}')
  print(f'APP_DESC: {APP_DESC}')
  print(f'APP_VS: {APP_VS}')
  print(f'APP_REPO: {APP_REPO}')
  print(f'APP_AUTHOR: {APP_AUTHOR}')
  print(f'API_KEY: {API_KEY}')

  print(f'LOG_CONSOLE_LEVEL: {LOG_CONSOLE_LEVEL}')
  print(f'LOG_DIR: {LOG_DIR}')
  print(f'LOG_PATH_INFO: {LOG_PATH_INFO}')
  print(f'LOG_PATH_DEBUG: {LOG_PATH_DEBUG}')
  print(f'LOG_PATH_ERROR: {LOG_PATH_ERROR}')

# test()

