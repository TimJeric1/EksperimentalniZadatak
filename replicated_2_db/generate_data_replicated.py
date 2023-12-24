from faker import Faker
import mysql.connector

fake = Faker()

# Connect to MySQL Master
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="111",
    database="mydb"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),email VARCHAR(100));")

print("Inserting data into Master...")
# Generate and insert fake data into the master database
for _ in range(50000):
    name = fake.name()
    email = fake.email()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)

mydb.commit()
mycursor.close()
mydb.close()
print("50000 records inserted into Master.")
