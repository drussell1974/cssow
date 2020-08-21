## Run project tasks 

sudo cp db/setup/db-cssow_api-init.1.sql build/db/backups/current

BUILDNO=$(date +%F)-${1:-development}

echo Creating release-$BUILDNO...

yarn --cwd src/student_web build
yarn --cwd src/teacher_web build

# Create docker-compose with new build number
sed "s/BUILDNO/$BUILDNO/"  build/docker-compose.TEMPLATE.yml > build/docker-compose.yml

    
if [ $1 ] ;then
    ## create tar releases
    echo -e "\nbuild.sh: \e[1;33m building images... ($BUILDNO) \e[0m"
    
    # build and push

    sudo docker-compose -f build/docker-compose.yml build

    echo -e "\nbuild.sh: \e[1;33m pushing images... ($BUILDNO) \e[0m"

    sudo docker-compose -f build/docker-compose.yml push

    # Remove build from docker-compose.yml (build before this line)

    sed "/build:/d" -i build/docker-compose.yml

    echo -e "\nbuild.sh: \e[1;33m creating release tar file ...($BUILDNO) \e[0m"

    cp dotenv/.env build/.env
    tar -czvf releases/release-$BUILDNO.tar.gz ./build 

    cp build/teacher-web/teacher-web.build.tar.gz releases/teacher-web.$BUILDNO.tar.gz
    cp build/student-web/student-web.build.tar.gz releases/student-web.$BUILDNO.tar.gz

    echo -e "\nbuild.sh: \e[1;33m committing release tar file ...($BUILDNO) \e[0m"

    git add releases/release-$BUILDNO.tar.gz
    git add releases/teacher-web.$BUILDNO.tar.gz
    git add releases/student-web.$BUILDNO.tar.gz

    git commit --no-verify -m "build: release-$BUILDNO"

    git tag $BUILDNO
    git push --no-verify origin $BUILDNO
else
    echo -e "\nbuild.sh: \e[1;32m local build only $BUILDNO. Run 'cd build && sudo docker-compose up --build' \e[0m"
    echo -e "\nbuild.sh: \e[1;32m To create live build run build with suffix e.g. 'yarn build v1' \e[0m"
    cp dotenv/.env.development build/.env
fi