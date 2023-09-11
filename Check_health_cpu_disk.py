#!/usr/bin/env python3
import shutil
import psutil

def disk_usage_check (disk):
    du = shutil.disk_usage(disk)
    free_per = du.free / du.total *100
    return free_per > 15

def cpu_usage_check ():
    usage_per =psutil.cpu_percent(1)
    return usage_per < 60

if not disk_usage_check("/") or not cpu_usage_check():
    print("Bad Health!")
else:
    print("Health looks good")