# Downtime Updator

#### Install MySql in Server
**_NOTE:_**  Install only if not installed
```
sudo apt update
sudo apt install mysql-server
```

#### Create Database
Login to mysql with below command
Enter password and click enter when it prompts for password.
```
mysql -u DB_USERNAME -p
```
To create database use below command
```
CREATE DATABASE DB_NAME;
```
Where,

-   DB_NAME: Name of database you want to create.

#### Configure Project

Edit file config.py as below
``` python
    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        'mysql',                            # DB_ENGINE
        'root',                             # DB_USERNAME
        'password',                         # DB_PASS
        'localhost',                        # DB_HOST
        3306,                               # DB_PORT
        'downtime-updater'                  # DB_NAME
    )
```
Where,

-   DB_HOST:    IP address of Server where mysql is installed.
-   DB_USERNAME: UserName of mysql database.
-   DB_PASS: Password for DB_USERNAME.
-   DB_PORT: Port for mysql server. (By default it will be 3306)
-   DB_NAME: Name of database created in above step.

#### Generating Setup File

```
pip install -r requirements.txt
python setup.py bdist_msi
```
**_NOTE:_**  Setup file will be generated and placed in dist folder.

#### Installing Application

1. Copy file generated (i.e, Downtime Updater-1.0-*.msi) in previous step to system in which application needs to be installed.
2. Double click copied file and keep on clicking next.
3. Click on finish to complete installation.

#### Running Application
-   Double click shortcut created on desktop with name **Downtime Updater**