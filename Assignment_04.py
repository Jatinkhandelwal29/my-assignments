# 1. Create a CSV file for address book



import csv
data=(["Name", "Address", "Mobile", "Email"],
                    ["Jatin", "Delhi", "9876543210", "jatin@gmail.com"],
                    ["Kannu", "Mumbai", "9123456780", "kannu@gmail.com"],
                    ["Jhanvi","Bengluru","9988776655","jhanvi@gmail.com"])
with open("assignment.csv","w", newline="") as file:
    writer=csv.writer(file)
    for x in data:
        writer.writerow(x)

with open("assignment.csv","r") as file:
    reader=csv.reader(file)
    for x in reader:
        print(x)
print("\n")






# 2. Weather data using OpenWeatherMap API





import requests

def weather(city, api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        desc = data["weather"][0]["description"]
        country = data["sys"]["country"]
        city_name = data["name"]

        print(f"\nWeather Report for {city_name}, {country}")
        print(f"Condition     : {desc.capitalize()}")
        print(f"Temperature   : {temp}°C")
        print(f"Feels Like    : {feels_like}°C")
        print(f"Humidity      : {humidity}%")
        print(f"Pressure      : {pressure} hPa")
        print(f"Wind Speed    : {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError:
        print("===Invalid city name or missing data===")

api_key = "4eb473ea10169bbc7f7be43bf9ccaa1c"
cities = input("Enter city names separated by comma :- ").split(',')

for city in cities:
    city = city.strip()
    weather(city, api_key)







# 3. Database practice with SQLite




import sqlite3
# Step 1: Create or connect to a database
conn = sqlite3.connect("practice.db")

# Step 2: Create 2 tables 
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT
)
""")

# Step 3: Insert records 
conn.execute("INSERT INTO students (name, marks) VALUES ('Jatin', 85)")
conn.execute("INSERT INTO students (name, marks) VALUES ('Kannu', 90)")
conn.execute("INSERT INTO students (name, marks) VALUES ('Annu', 78)")

conn.execute("INSERT INTO teachers (name, subject) VALUES ('Aadi', 'Math')")
conn.execute("INSERT INTO teachers (name, subject) VALUES ('Aayu', 'Science')")

conn.commit()  # Save the changes

# Step 4: SELECT operations
print("\nAll Students:")
for row in conn.execute("SELECT * FROM students"):
    print(row)

print("\nStudents with marks above 80:")
for row in conn.execute("SELECT * FROM students WHERE marks > 80"):
    print(row)

print("\nAll Teachers:")
for row in conn.execute("SELECT * FROM teachers"):
    print(row)

# Step 5: Update a record
conn.execute("UPDATE students SET marks = 95 WHERE name = 'Jatin'")
conn.commit()

# Step 6: Delete a record
conn.execute("DELETE FROM students WHERE name = 'Anjali'")
conn.commit()

# Final Display after update & delete
print("\nFinal Students After Update and Delete:")
for row in conn.execute("SELECT * FROM students"):
    print(row)

# Close the connection
conn.close()