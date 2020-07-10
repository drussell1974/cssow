echo \"creating docker-compose.yml and .env examples...\"
sed /build/d docker-compose.yml > build/docker-compose.yml
cp .env build/.env
tar -czvf releases/release-$(date +%F).tar.gz ./build 
git add releases/release-$(date +%F).tar.gz
git commit -m 'build: release'

yarn release