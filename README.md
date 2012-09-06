floodmapsv2
===========

Replacement floodmaps website

# Installation
## On Debian or Ubuntu (e.g. turnkeylinux core VM)
apt-get install postgresql python-setuptools python-virtualenv libapache2-mod-wsgi libpg-dev python-dev gcc postgis postgresql-8.4-postgis libproj0 libproj-dev gdal-bin libgdal1-dev libgeos-dev

## Create a folder to hold the application
mkdir -p /opt/

## Download source or download and copy zip file
git clone https://github.com/VincentHussey/floodmapsv2.git

## Create a virtual environment
cd /opt/floodmapsv2

virtualenv env

## Database configuration
It may be necessary to reinitialise the database using UTF8 encoding.
It may be necessary to modify pg_hba.conf

# Run in a virtual environment
source env/bin/activate

# Install required files
pip install -r requirements.txt

# Create the database
(modify as necessary)
su postgres
cd /opt/floodmapsv2/utils
./create_database_debian.sh
Enter password for user flood twice

# Check settings and locations for gdal, geos & proj
find / -name "proj"

# Create tables and synchronise the database
It may be necessary to set the locale e.g dpkg-reconfigure locales & choose en_US.UTF-8, en_GB.UTF-8, en_IE.UTF-8 
ref. https://code.djangoproject.com/ticket/16017

cd /opt/floodmapsv2/floodmapsv2/floodmapsv2/
../manage.py syncdb
../manage.py migrate floodmaps
