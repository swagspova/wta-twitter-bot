from apscheduler.schedulers.blocking import BlockingScheduler

from datetime import datetime

from api.tennis_api import get_live_matches
from api.match_parser import parse_matches
from utils.logger import logger


def job():

    try:

        print(
            f"\n[{datetime.now()}] "
            f"Checking live WTA matches...\n"
        )

        data = get_live_matches()

        parse_matches(data)

    except Exception as e:

        logger.error(e)


scheduler = BlockingScheduler()

scheduler.add_job(job, "interval", seconds=60)

logger.info(
    "Checking live WTA matches"
)

job()

scheduler.start()