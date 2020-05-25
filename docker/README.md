# DATABASE

Docker gets mariadb image for storing cssow_api database with volume mapping to v_cssow_data

> docker volume v_cssow_data
> docker run -d --name mariadb-cssow_api -v v_cssow_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=Admin1. mariadb
> sh ~/dev/schemeofwork_web2py_app/docker/cssow-app/restore-cssow_api.sh

## restore-cssow_api.sh file

1. Runs the /db/setup/db-setup.sql file to create a non-root user and cssow_api database
2. Runs the /db/backups/db-backup__<TIMESTAMP>.sql to restore data to cssow_api database
