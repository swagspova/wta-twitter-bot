from apscheduler.schedulers.blocking import BlockingScheduler

from datetime import datetime

from api.tennis_api import get_live_matches
from api.match_parser import parse_matches


def job():

    try:

        print(
            f"\n[{datetime.now()}] "
            f"Checking live WTA matches...\n"
        )

        data = get_live_matches()

        parse_matches(data)

    except Exception as e:

        print("ERROR:", e)


scheduler = BlockingScheduler()

scheduler.add_job(job, "interval", seconds=60)

print("🎾 WTA Monitoring Bot Started")

job()

scheduler.start()