from crontab import CronTab
import path_utils
import logging
from task import Task
from task_provider import TaskProvider


class CommandProvider:
    def __init__(self):
        log_path = f'{path_utils.datadir()}/command-provider.log'
        logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)

    def do_info(self) -> None:
        """
        Invoke Info command
        """
        print(f"Command Info")
        logging.info('Command Info')
        cron = self.__get_crontab()
        print(cron)

    def do_start(self):
        """
           Invoke Start command
           """
        print(f"Command Start")
        logging.info('Command Start')
        cron = self.__get_crontab()
        tasks: list[Task] = TaskProvider().all_tasks()
        for task in tasks:
            job = cron.new(
                command=f'python3 {path_utils.curdir()}/git_backup_action.py {task.path}')
            self.__set_interval(job, task)
            cron.write()

    def __set_interval(self, job, task):
        if task.interval == Task.Interval.MINUTES:
            job.minute.every(task.every_unit)
        elif task.interval == Task.Interval.HOURS:
            job.hour.every(task.every_unit)
        else:
            job.day.every(task.every_unit)

    def do_stop(self) -> None:
        """
        Invoke Stop command
        """
        print(f"Command Stop")
        logging.info('Command Stop')
        cron = self.__get_crontab()
        cron.remove_all()

    @staticmethod
    def __get_crontab() -> CronTab:
        return CronTab(user=True)
