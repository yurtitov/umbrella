from crontab import CronTab

from path_utils import current_dir, check_file_exists
from logger import MainLogger
from task import Task
from task_provider import TaskProvider

logger = MainLogger().get_logger()


class CommandProvider:

    def do_info(self) -> None:
        """
        Invoke Info command
        """
        print(f"Command Info")
        logger.info('Command Info')
        cron = self.__get_crontab()
        print(cron)

    def do_start(self):
        """
           Invoke Start command
           """
        print(f"Command Start")
        logger.info('Command Start')
        cron = self.__get_crontab()
        tasks: list[Task] = TaskProvider().all_tasks()
        script = f'{current_dir()}/git_backup_action.py'
        self.__check_action_script_exist(script)
        for task in tasks:
            job = cron.new(
                command=f'{script} {task.path}')
            self.__set_interval(job, task)
            cron.write()

    def __check_action_script_exist(self, script):
        try:
            check_file_exists(script)
        except FileNotFoundError as exception:
            logger.error(f'Action script file not found: {script}. Error: {str(exception)}')
        else:
            logger.info(f'Action script file found: {script}')

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
        logger.info('Command Stop')
        cron = self.__get_crontab()
        cron.remove_all()

    @staticmethod
    def __get_crontab() -> CronTab:
        return CronTab(user=True)
