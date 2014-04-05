"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second intervals.
"""

from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job('interval', tick, seconds=3)
    scheduler.start()
    print('Press Ctrl+C to exit')

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()  # Not strictly necessary if daemonic mode is enabled but should be done if possible
