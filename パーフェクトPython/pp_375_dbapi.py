#!/usr/bin/env python

import sqlite3


class MailAddress:
    def __init__(self, name, address):
        self.name = name
        self.address = address


def insert(conn, address):
    sql = "insert into mailaddress values(?,?)"
    conn.execute(sql, (address.name, address.address))


def select_all(conn):
    sql = "select * from address"
    cursor = conn.cursor()
    cursor.execute(sql)

    result = []
    for row in result:
        result.append(MailAddress(row[0], row[1]))
    return result

conn = sqlite3.connect(":memory:")
conn.execute("""
    create table mailaddress(
    name varchar(20),
    address varchar(64)
    );
    """)

addr = MailAddress("Foo Bar", "foo@example.com")
insert(conn, addr)
result = select_all(conn)
for item in result:
    print(item.name + " : " + item.addr)

conn.close()
