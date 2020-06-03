# Scraped_Database

This is a program to scrape historical price data of Bitcoin into a MySQL database. This will be done using the mysql.connection library for Python.

To run this program, a virtual enviroment needs to be created with the proper dependencies. 

To do this navigate to the project directory and run:
./create_venv.sh

Once your virtual enviroment is set up you can create the database by opening MySQL and creating a database named 
"Bitcoin-Prices". Navigate back to the project directory and run the ./create_database.sh script. This will create your MySQL database. 

You may run into login problems with MySQL, if so run the following commands:

sudo mysql -u root
use mysql;
[mysql] update user set plugin='mysql_native_password' where User='root';
[mysql] flush privileges;

To update the database navigate to the project directory and run the ./updater_database.sh script. This can easily be turned into a cronjob to update automatically. To create a cronjob to automatically update database type the following:

crontab -e

Select your preferred text editor then navigate to the bottom of the file and add a cronjob to the first line that isn't commented out. Your cronjob should look like:
2 0 * * * /path/to/projectfolder/updater_database.sh

This particular job will update your database at 12:02 every morning, however you can set it for anytime you like. Learn more about setting up cronjobs here https://www.youtube.com/watch?v=QZJ1drMQz1A


