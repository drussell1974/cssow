## Run project tasks 

sudo cp db/setup/db-cssow_api-init.1.sql build/db/backups/current


yarn --cwd src/teacher_web build:dev
yarn --cwd src/student_web build:dev
