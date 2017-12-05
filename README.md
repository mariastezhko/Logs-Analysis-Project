# Logs Analysis Project
- - - -

## Description

`Logsanalysis.py` is a Python program serving as a reporting tool. It prints out reports (in plain text) based on the data in the database. The **psycopg2** module is used to connect to the database.

## Requirements

 - [Python3](https://www.python.org/)
 - [Vagrant](https://www.vagrantup.com/)
 - [VirtualBox Virtual Machine](https://www.virtualbox.org/)
 - [Data to analyze](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Installation

 1. [Download VirtualBox](https://www.virtualbox.org/). Install the package.
 2. [Download Vagrant](https://www.vagrantup.com/). Install the package.
 3. [Download the Virtual Machine configuration](https://github.com/udacity/fullstack-nanodegree-vm)
 4. [Download the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Put the file **newsdata.sql** into the **vagrant** directory, which is shared with the virtual machine.

## Usage Instructions

#### Starting the virtual machine

From the terminal, inside the **vagrant** subdirectory, run the command
```
$ vagrant up
```
Log into the virtual machine by running the command
```
$ vagrant ssh
```
#### Setting up the database

From the terminal, inside the **vagrant** subdirectory, run the command
```
$ psql -d news -f newsdata.sql
```
#### Running the program

From the terminal, inside the **vagrant** subdirectory, run the command
```
$ python3 logsanalysis.py
```
