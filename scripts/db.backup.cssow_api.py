import sys
import os
from datetime import datetime

dt = datetime.today()

# get command line arguments
PATH = sys.argv[1]
ARCHIVE_PATH = sys.argv[2]
CLOUD_PATH = sys.argv[3]
DATABASE = sys.argv[4]
USER = sys.argv[5]
PASSWORD = sys.argv[6]

# create file name from 
FILE_NAME = f"db-backup.{DATABASE}.{dt.year}-{dt.month:02d}-{dt.day:02d}-{dt.hour:02d}{dt.minute:02d}.sql"
PATH = f"{PATH}\{FILE_NAME}"
# create the mysqldump command and execute
CMD = f"mysqldump -u{USER} -p{PASSWORD} {DATABASE} > {PATH}"
print("running data backup... %s" % CMD)  
os.system(CMD)

# copy latest to cloud
try:
    CLOUD_PATH = f"{CLOUD_PATH}\db-backup.{DATABASE}.latest.sql"
    CMD = f"xcopy {PATH} {CLOUD_PATH} /Y"
    print("copy to cloud... %s" % CMD)
    os.system(CMD)
except e:
    pass # TODO: give warning to write to event viewer

# copy to backup drive
try:
    #ARCHIVE_PATH = f"{ARCHIVE_PATH}\{FILE_NAME}"
    CMD = f"xcopy {PATH} {ARCHIVE_PATH}"
    print("copy to archive ... %s" % CMD)
    os.system(CMD)
except e:
    pass # TODO: give warning to write to event viewer