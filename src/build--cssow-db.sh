docker exec -i mariadb-cssow_api mysql -uroot -pAdmin1. < ~/dev/cssow/db/setup/db-setup.sql
docker exec -i mariadb-cssow_api mysql -uroot -pAdmin1. < ~/dev/cssow/db/backups/db-backup__20200525.sql
docker exec -i mariadb-cssow_api mysql -uroot -pAdmin1. -e 'SHOW DATABASES;'
