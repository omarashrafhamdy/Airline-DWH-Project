import random
from datetime import datetime, timedelta

# Define ranges for each item
passenger_key_range = (1, 2000)
reservation_channel_range = (1, 60)
hotel_key_range = (1, 55)
number_of_nights_range = (1, 10)

# Function to generate random date in YYYYMMDD format
def random_date(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%Y%m%d')
    end_datetime = datetime.strptime(end_date, '%Y%m%d')
    random_datetime = start_datetime + timedelta(days=random.randint(0, (end_datetime - start_datetime).days))
    return random_datetime.strftime('%Y%m%d')

# Function to generate random insert statement
def generate_insert():
    flight_date = random_date('20100101', '20240430')
    flight_date_key = flight_date
    # Generate reservation date before the flight date by random range between 1 to 30 days
    reservation_days_offset = random.randint(1, 30)
    reservation_date = datetime.strptime(flight_date, '%Y%m%d') - timedelta(days=reservation_days_offset)
    reservation_date_key = reservation_date.strftime('%Y%m%d')
    arrival_date_key = random_date(flight_date, flight_date)
    # Randomly adjust arrival date after the flight date by 0 to 2 days
    days_offset = random.randint(0, 2)
    arrival_date = datetime.strptime(flight_date, '%Y%m%d') + timedelta(days=days_offset)
    arrival_date_key = arrival_date.strftime('%Y%m%d')
    insert_statement = "INSERT INTO Hotel_Fact (Passenger_Key, Flight_Date_Key, Arrival_Date_Key, Reservation_Date_Key, Reservation_Channel_Key, Hotel_Key, Number_of_Nights) VALUES ("
    insert_statement += str(random.randint(passenger_key_range[0], passenger_key_range[1])) + ", "
    insert_statement += str(flight_date_key) + ", "
    insert_statement += str(arrival_date_key) + ", "
    insert_statement += str(reservation_date_key) + ", "
    insert_statement += str(random.randint(reservation_channel_range[0], reservation_channel_range[1])) + ", "
    insert_statement += str(random.randint(hotel_key_range[0], hotel_key_range[1])) + ", "
    insert_statement += str(random.randint(number_of_nights_range[0], number_of_nights_range[1])) + ");\n"
    return insert_statement

# Generate INSERT statements and write them to file
with open('populate_hotel_fact.sql', 'w') as data:
    for _ in range(50000):
        insert_statement = generate_insert()
        data.write(insert_statement)
