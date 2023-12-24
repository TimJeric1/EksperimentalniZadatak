from faker import Faker
import mysql.connector

fake = Faker()

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test_db"
)

mycursor = mydb.cursor()

print("Inserting data...")
# Generate and insert fake data into the database
for _ in range(50000):
    name = fake.name()
    email = fake.email()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)
    



mydb.commit()
mycursor.close()
mydb.close()
print("50000 records inserted.")

