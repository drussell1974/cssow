sudo cp -r ~/db/backups/db-backup.cssow_api.latest.sql build/cssow-db/db/current
yarn --cwd src/student_web build
yarn --cwd src/markdown-service build && yarn --cwd src/teacher_web build