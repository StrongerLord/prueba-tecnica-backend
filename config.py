from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_DB_USERNAME"]
password = os.environ["MYSQL_DB_PASSWORD"]
host = os.environ["MYSQL_DB_HOSTNAME"]
database = os.environ["MYSQL_DB_DATABASE"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)