from crontab import CronTab

from app.config import config


class Sheduler:
    def __init__(self):
        self.my_cron = CronTab(user=config.sheduler_user)

    def set(self, hour: int, minute: int):
        self.reset()

        job = self.my_cron.new(command=config.sheduler_command)
        job.hour.on(str(hour))
        job.minute.on(str(minute))
        job.set_comment(config.sheduler_comment)
        self.my_cron.write()

    def reset(self):
        for job in self.my_cron:
            if job.comment == config.sheduler_comment:
                self.my_cron.remove(job)
                self.my_cron.write()
