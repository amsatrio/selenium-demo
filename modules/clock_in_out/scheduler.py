import time
import schedule

from modules.clock_in_out.service import clock_in, clock_out
from modules.logger.service import loge, logi

def main():
    logi("start clock_in_out scheduler")

    schedule.every().monday.at("07:57").do(clock_in)
    schedule.every().tuesday.at("07:58").do(clock_in)
    schedule.every().wednesday.at("07:57").do(clock_in)
    schedule.every().thursday.at("07:55").do(clock_in)
    schedule.every().friday.at("07:56").do(clock_in)

    schedule.every().monday.at("17:01").do(clock_out)
    schedule.every().tuesday.at("17:00").do(clock_out)
    schedule.every().wednesday.at("17:03").do(clock_out)
    schedule.every().thursday.at("17:02").do(clock_out)
    schedule.every().friday.at("17:02").do(clock_out)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(10)
    except KeyboardInterrupt:
        loge("Scheduler stopped by user.")
    except Exception as e:
        loge(f"An error occurred: {e}")    