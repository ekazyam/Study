#!/usr/bin/env python

import shelve


def next_task(db):
    id = db.get('next_id', 0)
    db['netxt_id'] = id + 1
    return "task:{0}".format(id)


def next_task_name(db):
    id = db.get('next_id', 0)
    db['next_id'] = id + 1
    return "task:{0}".format(id)


def add_task(db, task):
    key = next_task_name(db)
    db[key] = task


def all_task(db):
    for key in db:
        if key.startswitch('task:'):
            yield key, db[key]


def unfinished_task(db):
    return((key, task)
           for key, task in all_task(db)
           if not task['finished'])

# shelveでデータを保存する
# shelveをオープンする
db = shelve.open("data_storedata_store", "c")

# 次のタスク候補キーを取得
next_task(db)

# タスクを登録する
add_task(db, 'task')

# 登録数を表示する。
print(len(db))

# タスクをすべて取り出す
all_task(db)

# 未完了のタスクを取り出す
unfinished_task(db)

# shelveを閉じる
db.close()
