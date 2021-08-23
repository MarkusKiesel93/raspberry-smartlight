from crontab import CronTab

from config import settings


class Sheduler:
    def __init__(self):
        self.my_cron = CronTab(user=settings.sheduler_user)

    def reset(self):
        for job in self.my_cron:
            if job.comment == settings.sheduler_comment:
                self.my_cron.remove(job)
                self.my_cron.write()

    def set_time_on(self, hour: int, minute: int):
        self.reset()

        job = self.my_cron.new(command=settings.sheduler_command)
        job.hour.on(str(hour))
        job.minute.on(str(minute))
        job.set_comment(settings.sheduler_comment)
        self.my_cron.write()
