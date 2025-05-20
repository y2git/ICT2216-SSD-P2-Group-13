docker-compose up --build

-d if u want run in background

restart cmd:
docker-compose down && docker-compose up --build -d

Import the test.sql to ur db (cus i can't save the /mysql_data to github for some reason, if u wanna try uncomment the line in .gitignore)