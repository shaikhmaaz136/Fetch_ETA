
# Data Engineering Take Home: 
# ETL off a SQS Queue

The objective of this Take Home test is to read the data from "container 1" and mask the personal information before uploading it into "container 2" whilst creating the table.


# Appendix

While writing the script we have to make sure that the installation of libraries in your virtual environment or local machine is done properly to set up the environment.

- The first step includes establishing the connection with the docker container and making sure that they are up and running. 
- The second step is to import boto3 so that there is no hurdle in the interaction of the local machine with the AWS's Simple Queue Service. In this step, we wrote a function 'queue_url' to fetch the data which is located in localhost:4566
- The third step consists of connecting with the PostgreSQL database using Pythonscript so that we can create the table and write the data into it. Additionally, it also needs to include the functions to mask sensitive information before uploading it. 
The important libraries in this step include hashlib, json psycopg2 for establishing the connection and masking the data, and loading it into the database. 
- In the fourth step we simply ran the query to fetch all the messages and take a look at the no, and messages


## Tech Stack

**Interface:** Visual Studio, Terminal, AWSCLI

**Server:** Docker


## Installation

The important libraries that are needed to be imported before running the script are given below.

```bash
pip install awscli
pip install boto3
pip install psycopg2
pip install hashlib
```
    

## Question and Answer Section
**Question:** How would you deploy this application in production?

**Answer:**
- I would make sure to package the script and its dependencies into a docker container
- Then build the docker image using the docker file with the necessary Python dependencies installed.
- We can then run the Docker container, exposing the required ports and connecting it to other services like PostgreSQL
- Monitoring the container and ensuring that the ETL task runs as expected, and cleaning up resources after completion
- By following these steps I am sure we can deploy this application in production allowing its portable execution across different environments

**Question:**  What other components would you want to add to make this production ready?

**Answer:** To make sure the ETL script is production ready we need to set up the Continuous Integration and Continuous Deployment pipelines for automated testings and deployment and have a backup and disaster recovery plan for data protection


**Question:**  How can this application scale with a growing dataset?

**Answer:** 
- We can surely modify the size of the batch and handle larger message volumes in each iteration.
- Optimized SQL queries are also used for data insertion into the database and use bulk insert methods
- The storage requirements must be modified as per the needs and it is best to migrate towards cloud-based solutions as it will automatically scale as per the need.
- If we are dealing with a huge amount of data then parallel processing is the key to handling it like Apache Spark or AWS's Glue will help to scale efficiently.

**Question:**  How can PII be recovered later on?

**Answer:** In this case it is impossible to be recovered in its original form after the pii is masked using hashing techniques. In order to satisfy the need of recovering the PII later we need to go with an alternate approach such as encryption. It is kind of a reversible technique that allows us to get back the original PII using a decryption key.
However, while handling sensitive data we need to make sure that the data is safeguarded.


**Question:**  What are the assumptions you made?

**Answer:** In this case the ids can't be recovered in their original form after the pii is masked using hashing techniques. In order to satisfy the need of recovering the PII later we need to go with an alternate approach such as encryption with private key. It is kind of a reversible technique that allows getting back the original PII using a decryption key.
However, while handling sensitive data we need to make sure that the data is safeguarded.


## Next Steps would be
- Making the data safe and production ready.
- Optimising the code structure such that it has a scope to grow in the near future and the schema is robust
- Make sure to create and deploy the application in dynamic environment/ interface


## Challenges
There was a clash in my environment and I was not able to use the AWSCLI tool which was very important to read the data from container 1. I had to make sure to uninstall everything and then re-install again and give a designated path using echo in bash so that it can read the necessary tools and packages in my Python script.

