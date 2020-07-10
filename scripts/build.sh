## Run project tasks 

sudo cp -r ~/db/backups/db-backup.cssow_api.latest.sql build/cssow-db/db/current

BUILDNO=$(date +%F-%H%M)

echo Creating release-$BUILDNO...

yarn --cwd src/student_web build
yarn --cwd src/markdown-service build
yarn --cwd src/teacher_web build

# Create docker-compose with new build number
sed "s/BUILDNO/$BUILDNO/"  build/docker-compose.TEMPLATE.yml > build/docker-compose.yml
sudo docker-compose -f build/docker-compose.yml build
sudo docker-compose -f build/docker-compose.yml push

## create tar releases

# Remove build
sed "/build:/d" -i build/docker-compose.yml

cp .env build/.env
tar -czvf releases/release-$BUILDNO.tar.gz ./build 
git add releases/release-$BUILDNO.tar.gz
git commit -m "build: release-$BUILDNO"