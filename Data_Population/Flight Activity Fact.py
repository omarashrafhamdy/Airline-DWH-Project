import random
import datetime

# Define ranges for each item
date_range_start = datetime.date(2010, 1, 1)
date_range_end = datetime.date(2024, 4, 30)
airport_range = (1, 34)
aircraft_range = (1, 50)
flight_class_range = (1, 16)
fare_basis_range = (1, 20)
booking_channel_range = (1, 60)
payment_method_range = (1, 7)
ticket_number_range = (100000, 999999)
flight_number_range = (100, 999)
reservation_number_range = (1000, 9999)
segment_sequence_range = (1, 4)

# Function to generate random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)

# Function to generate random decimal value within a range
def random_decimal(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

# Function to generate random time key within a range
def random_time_key():
    return f"{random.randint(0, 86399):08}"

# Function to generate random insert statement
def generate_insert():
    reservation_date = random_date(date_range_start, date_range_end)
    scheduled_departure_date = reservation_date + datetime.timedelta(days=random.randint(1, 30))
    actual_departure_date = scheduled_departure_date + datetime.timedelta(days=random.randint(0, 1))
    
    insert_statement = "INSERT INTO flight_activity_fact VALUES ("
    insert_statement += f"{int(scheduled_departure_date.strftime('%Y%m%d'))}, "  # SCHEDULED_DEPARTURE_DATE_KEY
    insert_statement += f"'{random_time_key()}', "  # SCHEDULED_DEPARTURE_TIME_KEY
    insert_statement += f"{int(actual_departure_date.strftime('%Y%m%d'))}, "  # ACTUAL_DEPARTURE_DATE_KEY
    insert_statement += f"'{random_time_key()}', "  # ACTUAL_DEPARTURE_TIME_KEY
    insert_statement += f"{random.randint(1, 2000)}, "  # PASSENGER_KEY
    insert_statement += f"{random.randint(1, 24)}, "  # PASSENGER_PROFILE_KEY
    insert_statement += f"{random.randint(1, 34)}, "  # DEPARTURE_AIRPORT_KEY
    insert_statement += f"{random.randint(1, 34)}, "  # DESTINATION_AIRPORT_KEY
    insert_statement += f"{random.randint(1, 50)}, "  # AIRCRAFT_KEY
    insert_statement += f"{random.randint(1, 16)}, "  # CLASS_OF_SERVICE_KEY
    insert_statement += f"{random.randint(1, 20)}, "  # FARE_BASIS_KEY
    insert_statement += f"{random.randint(1, 60)}, "  # BOOKING_CHANNEL_KEY
    insert_statement += f"{random.randint(ticket_number_range[0], ticket_number_range[1])}, "  # TICKET_NUMBER
    insert_statement += f"'{random.randint(flight_number_range[0], flight_number_range[1]):03}', "  # FLIGHT_NUMBER
    insert_statement += f"{random.randint(reservation_number_range[0], reservation_number_range[1])}, "  # RESERVATION_NUMBER
    insert_statement += f"{random.randint(1, 4)}, "  # SEGMENT_SEQUENCE_NUMBER
    insert_statement += f"{random_decimal(50, 500)}, "  # BASE_FARE_REVENUE
    insert_statement += f"{random_decimal(10, 100)}, "  # TAXES
    insert_statement += f"{random_decimal(5, 30)}, "  # TRANSACTION_FEES
    insert_statement += f"{random_decimal(50, 500)}"  # PASSENGER_PAID_AMOUNT
    insert_statement += ");\n"
    return insert_statement



# Generate and save 100 INSERT statements
with open('populate_flight_activity.sql', 'w') as f:
    for _ in range(2000):
        insert_statement = generate_insert()
        f.write(insert_statement)
