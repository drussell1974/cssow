# restrict access to credentials

chmod 600 .mylogin.cnf

# create task /etc/cron.daily/mysqldump

0 1 * * * /usr/bin/mysqldump -u username -p db1 --single-transaction --quick --lock-tables=false > db-backup__$(date +%F).sql

