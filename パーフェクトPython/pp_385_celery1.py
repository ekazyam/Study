#!/usr/bin/env python

from pp_383_mytask import add

delayed = add.delay(3, 2)

while delayed.ready() == False:
    time.sleep(1)

print(delayed.get())
