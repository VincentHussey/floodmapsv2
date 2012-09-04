floodmapsv2
===========

Replacement floodmaps website

# Installation
# On Debian or Ubuntu (e.g. turnkeylinux core VM)
apt-get install postgresql python-setuptools python-virtualenv libapache2-mod-wsgi libpg-dev python-dev gcc postgis postgresql-8.4-postgis

# Create a folder to hold the application
mkdir -p /opt/

# Download source or download and copy zip file
git clone https://github.com/VincentHussey/floodmapsv2.git

# Create a virtual environment
cd /opt/floodmapsv2

virtualenv env

# Run in a virtual environment
source env/bin/activate

# Install required files
pip install -r requirements.txt

