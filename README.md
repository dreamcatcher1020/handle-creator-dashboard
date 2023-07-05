# 1. Setup & Running Locally
## 1.1 Prerequisites
### 1.1.1 Python

Install Python3 and dependencies!

```bash
# Install Python3
$ sudo apt update
$ sudo apt install python3-pip

# Install python3-venv to set up virtual environment 
$ sudo apt install python3-venv
```

### 1.1.2 PostgreSQL
Install PostgreSQL DB
```bash
# Install PostgreSQL DB
$ sudo apt update
$ sudo apt install postgresql

# Check if it is installed and running successfully
$ sudo systemctl status postgresql
```

## 1.2 Setup & Running Project Locally

### 1.2.1 Project Configuration

```bash
# Clone project from Github
$ git clone https://github.com/Forte-AI/handle-creator-dashboard.git

# Create .env file and configure it
$ cd handle-creator-dashboard
$ touch .env
```

### 1.2.2 DB migration & Running

```bash
# Setting virtual environment and activate
$ python3 -m venv venv
$ source venv/bin/activate

# Install packages
$ python3 -m pip install -r requirements.txt

# Migrate DB models
$ python3 manage.py migrate

# Creat a new superuser
$ python3 manage.py createsuperuser

# Run server
$ python3 manage.py runserver
```

# 2. Setup & Running on AWS EC2

## 2.1 Create a new AWS EC2 instance
You can create two kinds of EC2 instances based on Ubuntu AMI or Amazon Linux AMI

A new pem file will be created according to EC2 server. (askhandle-linux.pem)

```bash
    Public IPv4 DNS : ec2-54-196-68-195.compute-1.amazonaws.com
    Public IPv4 Address : 54.196.68.195
```

## 2.2 Allowing access using user name and password by Putty (or WinSCP)

```bash
# SSH login using the pem file
$ ssh -i askhandle-linux.pem ec2-user@ec2-54-196-68-195.compute-1.amazonaws.com
```

## 2.3 Install & Setup Docker and Docker Compose

```bash
# Install & Enable Docker
$ sudo yum install docker -y
$ sudo systemctl enable docker.service
$ sudo systemctl start docker.service

# Add uesr to docker group
$ sudo usermod -aG docker ec2-user

# Add Docker-compose
$ sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# Add permission to execute
$ sudo chmod +x /usr/local/bin/docker-compose

# Check Docker & Docker-compose is running
$ docker --version
$ docker-compose --version
```
## 2.4 Project Deployment from Github

```bash
# Install Git
$ sudo yum install git -y
$ git --version

# Git clone
$ git clone https://github.com/Forte-AI/handle-creator-dashboard.git

# Build & Run
$ cd handle-creator-dashboard
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml up

# Check running on https://creator.askhandle.com/
```

