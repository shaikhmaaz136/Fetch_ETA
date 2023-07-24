import boto3
import hashlib
import json
import psycopg2

## Params

# Replace these values with your PostgreSQL container's connection details
host = "localhost"     # Example: localhost or IP address
port = "5432"     # Example: 5432
database = "postgres" # Example: mydatabase
user = "postgres"          # Example: postgres
password = "postgres"      # Example: mysecretpassword

# Connect to the PostgreSQL container
connection = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

queue_url = 'http://localhost:4566/000000000000/login-queue'

def receive_all_messages(queue_url):
    messages = []

    # Specify the dummy profile name
    aws_profile = 'dummy_profile'

    # Set up the SQS client with the dummy profile
    sqs = boto3.Session(profile_name=aws_profile).client('sqs', endpoint_url='http://localhost:4566')

    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10  # Adjust the number of messages to receive in each batch
        )

        if 'Messages' in response:
            messages.extend(response['Messages'])
        else:
            break

    return messages

# Use the function to receive all messages

print("Reading messages from Queue")
all_messages = receive_all_messages(queue_url)


# Create the user_logins table if it doesn't exist
def create_user_logins_table():
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS user_logins(
            user_id varchar(128),
            device_type varchar(32),
            masked_ip varchar(256),
            masked_device_id varchar(256),
            locale varchar(32),
            --app_version varchar(32),
            create_date date
        );""")
        connection.commit()
        print("Table user_logins created successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while creating table:", error)
    finally:
        cursor.close()

# Function to mask PII fields using SHA-256 hash
def mask_pii(data):
    data = json.loads(data['Body'])
    # Mask device_id and ip fields
    data['device_id'] = hashlib.sha256(data['device_id'].encode()).hexdigest()
    data['ip'] = hashlib.sha256(data['ip'].encode()).hexdigest()
    return data

# Step 3: Write each record to the Postgres database
def write_to_postgres(data):
    try:
        cursor = connection.cursor()

        # Insert the record into the user_logins table
        cursor.execute("INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, create_date) "
                    "VALUES (%s, %s, %s, %s, %s, current_date)",
                    (data['user_id'], data['device_type'], data['ip'], data['device_id'],
                        data['locale']
                        # , data['app_version']
                        ))
        connection.commit()
        print("Record inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or inserting record:", error)
    finally:
        # Close the cursor
        cursor.close()

# Create the user_logins table
create_user_logins_table()

print("Inserting messages into postgres")

# Assuming all_messages is a list of JSON objects as you provided in the previous message
for message in all_messages:
    try:
        masked_data = mask_pii(message)
        write_to_postgres(masked_data)
    except:
        continue

print("complete")