# Linked Business Python Test

The goal of the task is to read and extract information from given input files, store the data into a DB and then expose them via a RESTful API.
The code should be written in Python using any modern web framework such as Django or Fast API and any suitable algorithm to mine the necessary information from the files.

Your code should be well documented and delivered in a private GitHub or GitLab repo.

## Task description 

You should develop an algorithm in Python to parse the given txt files and extract the following information regarding the company:

* The official name
* The GEMH number (ΓΕΜΗ)
* The company's website - if it is mentioned in the file (irrelevant webpages such as businessregistry and acci should be skipped)
* The date of the website's registration

The above data should be stored in a MySQL database. 
The data should be available via a RESTful API endpoint which will take as input the company's GEMH number and return all the
available information for the company.

