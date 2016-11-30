Provisioning for site

## Packages

* nginx
* Python 3
* Git
* pip
* virtualenv

Usage on Ubuntu

sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv


## Setup for Nginx virtual host

* Check nginx.template.conf
* Modify 'superlists-staging.co.kr' to your site

## Upstart Job

* Check gunicorn-upstart.template.conf
* Modify 'superlists-staging.co.kr' to your site

## Structure
Assumption: User's home is /home/username

/home/username
|-sites
  |-SITENAME
    |-database
    |-source
    |-static
    |-virtualenv