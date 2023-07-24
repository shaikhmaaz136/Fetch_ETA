
# Data Engineering Take Home: 
# ETL off a SQS Queue

The objective of this Take Home test is to read the data from "container 1" and mask the personal information before uploading it into "container 2" whilst creating the table.


# Appendix

While writing the script we have to make sure that the installation of libraries in your virtual environment or local machine is donne properly to setup the environment.

- The first step includes establishing the connection with the docker container and make sure that they are up and running. 
- The second step is to import boto3 so that there is no hurdle in interaction of local machine with the AWS's Simple Queue Service. In this step we wrote a function 'queue_url' to fetch the data which is located in localhost:4566
- The third step consist of connection with the PostgreSQL database using pythonscript so that we can create the table and write the data into it. Additionally it also needs to include the functions to mask the sensitive information before uploading it. 
The important libraries in this step includes hashlib, json psycopg2 for establishing connection and masking the data and loading it into the database. 
- In the forth step we simply ran the query to fetch all the mssages and take a look at the no, and messages


## Tech Stack

**Interface:** Visual Studio, Terminal, AWSCLI

**Server:** Docker


## Installation

You need to install AWSCLI for executing this python script and make sure that the proper path is given of the tool. Other than the AWSCLI there are another important libraries that are needed to be imported before running the script and is given below.

```bash
pip install awscli
pip install boto3
pip install psycopg2
pip install hashlib
```
    

## Question and Answer Section
**Question:** How would you deploy this application in production?

**Answer:**
- I would make sure to package the script and it's dependencies into a docker container
- Then to build the docker image using the docker file with the necessary python dependencies installed.
- We can then run the Docker container, exposing the required ports and connecting it to other services like PostgreSQL
- Monitoring the containerand ensuring that the ETL task runs as expected, and clean up resources after completion
- By followung these steps I am sure we can deploy this application in production allowing its portable execution across different environments

**Question:**  What other components would you want to add to make this production ready?

**Answer:** To make sure the ETL script is production ready we need to setup the Continuous Integration and Continuous Deployment pipelines for automated testings and deployment and have backup and disaster recovery plan for data protection


**Question:**  How can this application scale with a growing dataset?

**Answer:** 
- We can surely modify the size of the batch and handle larger message volumes in each iteration.
- Optimized SQL queries is also used for data insertion into the database and use bulk insert methods
- The storage requirements must be modified as per the needs and it is best to migrate towards cloud based solutions as it will automatically scale as per the need.
- If we are dealing with the huge amount of data then parallel processing is the key to handle it and introduction to spark or say handling the data AWS's Glue will help to scale efficiently.

**Question:**  How can PII be recovered later on?

**Answer:** In this case it is impossiblle to be recovered in it's original form after the pii is masked using hashing techniques. Inorder to satidfy the nneed of recovering the pii later we need to go with an alternate approach sucha s encryption. It is kind of a reversible technique that allows to get back the original pii using a decription key.
However, while handling sensitive data we need to make sure that the data is safeguarded.


**Question:**  What are the assumptions you made?

**Answer:** In this case it is impossiblle to be recovered in it's original form after the pii is masked using hashing techniques. Inorder to satidfy the nneed of recovering the pii later we need to go with an alternate approach sucha s encryption. It is kind of a reversible technique that allows to get back the original pii using a decription key.
However, while handling sensitive data we need to make sure that the data is safeguarded.


## Next Steps
- Make the ETL production ready by making sure the data is safe and production ready.
- Make sure to make the structure such that it has a scope to grow in near future and the schema is robust
- Make sure to create and deploy the application whilst providing the support and its use in dynamic environment/ interface


## Challenges
There was a clash in my environment and i waas not able to use the AWSCLI tool whcih was very important to read the data from container 1. I had to make sure to uninstall everything and then re-install again and give a designated path using echo in bash so that it can read the necessary tools and packages in my python script.
Though the task was supposed to require 2 to 3 hours i had to spend atleast an entire day in troubleshooting the issues and setup the environment.

