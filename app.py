import inspect
import filetype
import json
from os import listdir
from pathlib import Path
from rich import print
from rich.prompt import Confirm
from time import sleep
import typer

import logging
log = logging.getLogger(__name__)

import configure
from helpers import TaskTimer
from helpers import msgs


class MyApp:
  '''Doc string.
  '''
  def __init__(self):

    log.debug('Start')

    self.timer = TaskTimer.TaskTimer()
    self.run()

    log.debug('End')


  #
  # Class methods
  def run(self):
    '''The primary controller function for this class.
    '''
    log.debug('Start')

    try: 
      self.timer_start()

      print('Hello, World!')
      self.test_logging()

      self.generate_summaries()
      self.timer_stop()
      self.goodbye()

    except KeyboardInterrupt:
      log.debug('Keyboard interrupt')
      self.stopped()
      return

    except Exception as e:
      log.critical(e)
      self.error(e)
      return

    log.debug('End')

  def generate_summaries(self):
    '''Populates multiple task summary dicts.
    '''
    log.debug('End')
    print(msgs.write_gather)
    
    # Time
    self.timer_summary = self.timer.timer_results

    log.debug('End')

  #
  # Timer
  def timer_start(self):
    '''Starts the image processing timer
    and captures the start time.
    '''
    self.timer.start()

  def timer_stop(self):
    '''Stops the image processing timer
    and captures the stop + elapsed times.
    '''
    self.timer.stop()
    self.timer.elapsed()

  #
  # Endings
  def stopped(self):
    '''Famous last words.
    '''
    self.timer_stop()
    print('\n')
    print(msgs.hr)
    print(f'[red]{msgs.task_stopped}')
    print(msgs.div)
    log.debug('Goodbye stopped') 

  def error(self, error):
    '''Famous last words.
    '''
    self.timer_stop()
    print(msgs.hr)
    print(error)
    print(msgs.hr)
    print(f'[red]{msgs.task_error}')
    print(msgs.div)
    log.debug('Goodbye error')

  def goodbye(self):
    '''Famous last words.
    '''
    print(msgs.hr)
    print(f'[green]{msgs.task_end}')
    print(msgs.div)
    log.debug('Goodbye normal')

  #
  # Test
  def test_logging(self):
    '''Test logging configuration by logging a message at every level.
    '''
    log.info('Test info')
    log.debug('Test debug')
    log.warning('Test warning')
    log.error('Test error')
    log.critical('Test critical')


#
# Run this puppy
def hello():
  '''Prints the app banner to console.
  '''
  print(f'[blue]{msgs.div}')
  print(f'{configure.APP_NAME}: {configure.APP_REPO}')
  print(configure.APP_DESC)
  print(f'[blue]{msgs.div}')

def main():         
  '''App description here.
  '''
  # Logging config
  import logging
  from helpers import logger
  logger.setup_logging()
  log = logging.getLogger(__name__)
  log.debug('Logging set')

  # Start app
  hello()
  task = MyApp()


if __name__ == '__main__':
    typer.run(main)

                