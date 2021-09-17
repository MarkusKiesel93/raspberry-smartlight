from crontab import CronTab

from config import Config


class Sheduler:
    def __init__(self):
        self.my_cron = CronTab(user=Config.sheduler_user)

    def set(self, hour: int, minute: int):
        self.reset()

        job = self.my_cron.new(command=Config.sheduler_command)
        job.hour.on(str(hour))
        job.minute.on(str(minute))
        job.set_comment(Config.sheduler_comment)
        self.my_cron.write()

    def reset(self):
        for job in self.my_cron:
            if job.comment == Config.sheduler_comment:
                self.my_cron.remove(job)
                self.my_cron.write()