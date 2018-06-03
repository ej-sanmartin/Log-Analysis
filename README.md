Log Analysis Project 6/2/2018
=======================

Description
-----------------------

A project completed for Udacity's Fullstack Nanodegree. 

In this project, I got to demonstrate my SQL database skills. I was able to practice interacting with a live database both from the terminal and from my code. I was able to explore a large database with over a million rows. And I buit and refined complex queries and used them to draw business conclusions from data.

This project allowed me to use the Python module ```psycopg2``` and, through extensive self study, I was able to learn about databases and how to communicate with them with SQL, specfically PostreSQL for this project. I, also, sharpened my knowledge of the terminal and I learned how to even to use and navigate through an Ubuntu-based Virtual Box. The skills I practiced with this project had made me a stronger backend developer and thus a stronger full stack developer as I am also gaining front end knowledge with this course.


Requirements
-----------------------
Must have [Python2.7](https://www.python.org/downloads/), [Vagrant](https://releases.hashicorp.com/vagrant/?_ga=2.146818743.1445943320.1515078265-241047305.1515078265), and [Virtual Box 5.1](https://www.virtualbox.org/wiki/Downloads)

Download the Virtual Machine Configuration [HERE](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)

Download the newsdata.sql zip file [HERE](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


Instructions to Run Program
-----------------------

1. After downloading or already having all the programs and files needed to run this repo, move the unzipped newsdata.sql file to within the Virtual Machine Configuration folder. It should be pasted INSIDE of the Vagrant folder (path is FSND-Virtual-Machine/vagrant).

2. With the terminal, cd inside the virtual machine configuration and into vagrant.

3. Enter the command ```vagrant up``` into the terminal. It should take a while, depending on internet connection.

4. Enter the command ```vagrant ssh``` into the terminal and then ```cd /vagrant```.

5. Load the data by using the command ```psql -d news -f newsdata.sql.```

6. Place the python file (log_analysis.py) from this repo into your vagrant directory, that is inside the Virtual Machine configuration file.

7. In the terminal, run the python file with the command ```python log_analysis.py```. Python could be changed to how Python2.7 programs are run in your machine.


Author/ Contributions
-----------------------

Edgar J San Martin


Copyright
-----------------------

Edgar J San Martin © 2018
