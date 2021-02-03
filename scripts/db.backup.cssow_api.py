import sys
import os
from datetime import datetime

dt = datetime.today()

# get command line arguments
INIT_PATH = sys.argv[1]
ARCHIVE_PATH = sys.argv[2]
CLOUD_PATH = sys.argv[3]
DATABASE = sys.argv[4]
USER = sys.argv[5]
PASSWORD = sys.argv[6]

# create file name from 
DATA_FILE_NAME = f"db-backup.DAT.{DATABASE}.{dt.year}-{dt.month:02d}-{dt.day:02d}-{dt.hour:02d}{dt.minute:02d}.sql"
SCHEMA_FILE_NAME = f"db-backup.SCH.{DATABASE}.{dt.year}-{dt.month:02d}-{dt.day:02d}-{dt.hour:02d}{dt.minute:02d}.sql"

INIT_DATA_PATH = f"{INIT_PATH}\{DATA_FILE_NAME}"
# create the mysqldump command for the data backup and execute
os.system(f"mysqldump -u{USER} -p{PASSWORD} {DATABASE} > {INIT_DATA_PATH}")
# create the mysqldump command for the schema backup and execute
INIT_SCHEMA_PATH = f"{INIT_PATH}\{SCHEMA_FILE_NAME}"
os.system(f"mysqldump --no-data --routines -u{USER} -p{PASSWORD} {DATABASE} > {INIT_SCHEMA_PATH}")

# copy latest data and schema to the cloud
try:
    CLOUD_DATA_PATH = f"{CLOUD_PATH}\db-backup.DATA.{DATABASE}.latest.sql"
    os.system( f"xcopy {INIT_DATA_PATH} {CLOUD_DATA_PATH} /Y")

    CLOUD_SCHEMA_PATH = f"{CLOUD_PATH}\db-backup.SCHEMA.{DATABASE}.latest.sql"
    os.system(f"xcopy {INIT_SCHEMA_PATH} {CLOUD_SCHEMA_PATH} /Y")
except:
    pass # TODO: give warning to write to event viewer

# copy theto backup drive
try:
    os.system(f"xcopy {INIT_DATA_PATH} {ARCHIVE_PATH}\\")
    os.system(f"xcopy {INIT_SCHEMA_PATH} {ARCHIVE_PATH}\\")
except:
    pass # TODO: give warning to write to event viewer