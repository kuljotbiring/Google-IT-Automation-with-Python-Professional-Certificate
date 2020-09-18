#!/usr/bin/env python3

import re
import operator
import csv

error = {}
users = {}

with open('logs.txt', "r") as logfile:
    for line in logfile:
        line = line.strip()
        err = (re.search(r"ERROR ([\w ].*) ", line))
        message = (re.search(r"(ERROR|INFO)", line))
        name = (re.search(r"\(([^)]+)\)", line))

        if name:
            name = name.group(1)

        if message:
            message = message.group(1)

        if name not in users:
            info_count = {'INFO': 0, 'ERROR': 0}
            users[name] = info_count

        if name in users and message == 'ERROR':
            users[name]['ERROR'] += 1

        elif name in users and message == 'INFO':
            users[name]['INFO'] += 1

        if err:
            err = err.group(1)

        else:
            continue

        if err in error:
            error[err] += 1

        else:
            error[err] = 1

sorted_errors = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
error_cols = ["Error", "Count"]
csvfile = open('error_message.csv', 'w+')

writer = csv.writer(csvfile)
writer.writerow(error_cols)

for row in sorted_errors:
    writer.writerow(row)

per_user = sorted(users.keys())

names = []

for key in per_user:
    names.append([key,users[key]["INFO"],users[key]["ERROR"]])


stats_cols = ["Username", "INFO", "ERROR"]

with open('user_statistics.csv', 'w+') as csv2file:
    writer = csv.writer(csv2file)
    writer.writerow(stats_cols)
    writer.writerows(names)
