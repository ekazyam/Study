#!/usr/bin/env python
import pickle
from datetime import datetime, time


def save_task(task, file):
    pickle.dump(task, file)


def save_task(file):
    return pickle.load(file)


def create_task(name, due_date, required_time):
    return dict(name=name, due_date=due_date, required_time=required_time, finished=False)


def format_task(task):
    state = "完了" if task['finished'] else "未完了"
    format = "{state} {task[name]}:{task[due_date:%Y-%m-%dまで 予定所要時間 {task[required_time]}分"
    return format.format(task=task, state=state)


def finish_task(task):
    task['finished'] = True

if __name__ == '__main__':
    # create task.
    t = create_task("たすく", datetime(2012, 4, 1), time(0, 25))
    finish_task(t)
    t['finished']
    print(t['finished'])
