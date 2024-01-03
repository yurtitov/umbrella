from task import Task
from properties import Property
import path_utils


class TaskProvider:
    def all_tasks(self) -> list[Task]:
        config_path = f'{path_utils.home()}/.umbrella/config.yml'
        props = Property(config_path)
        tasks = props.get_property_mandatory('tasks')
        result: list[Task] = []
        for task in tasks:
            path: str = self.__get_path(task)
            print(path)
            interval: Task.Interval = self.__get_interval(task)
            every_unit: int = self.__get_every_unit(task)
            result.append(Task(path, interval, every_unit))
        return result

    @staticmethod
    def __get_path(task) -> str:
        return task['task']['path']

    @staticmethod
    def __get_interval(task) -> Task.Interval:
        interval = task['task']['interval']
        if interval == 'minute':
            return Task.Interval.MINUTES
        if interval == 'hour':
            return Task.Interval.HOURS
        if interval == 'day':
            return Task.Interval.DAYS

    @staticmethod
    def __get_every_unit(task) -> int:
        return task['task']['every_unit']
