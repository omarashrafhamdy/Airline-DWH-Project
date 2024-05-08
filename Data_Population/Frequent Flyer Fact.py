import random
import datetime

# Define ranges for each item
date_range_start = datetime.date(2010, 1, 1)
date_range_end = datetime.date(2024, 4, 30)
passenger_profile_range = (1, 24)
airport_range = (1, 34)
redeem_key_range = (1, 11)
ticket_number_range = (100000, 999999)
miles_earned_range = (100, 1000)
miles_flown_range = (100, 10000)
miles_redeemed_range = (50, 500)

# Function to generate random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)

# Function to generate random insert statement
def generate_insert(frequent_flyer_key):
    insert_statement = f"INSERT INTO frequent_flyer_fact VALUES ({frequent_flyer_key}, "
    insert_statement += f"{random.randint(passenger_profile_range[0], passenger_profile_range[1])}, "  # Passenger_Profile_Key
    insert_statement += f"{int(random_date(date_range_start, date_range_end).strftime('%Y%m%d'))}, "  # Flight_Date_Key
    insert_statement += f"{random.randint(airport_range[0], airport_range[1])}, "  # Departure_Airport_Key
    insert_statement += f"{random.randint(airport_range[0], airport_range[1])}, "  # Arrival_Airport_Key
    insert_statement += f"{random.randint(redeem_key_range[0], redeem_key_range[1])}, "  # Redeem_Key
    insert_statement += f"{random.randint(ticket_number_range[0], ticket_number_range[1])}, "  # Ticket_Number
    insert_statement += f"{random.randint(miles_earned_range[0], miles_earned_range[1])}, "  # Miles_Earned
    insert_statement += f"{random.randint(miles_flown_range[0], miles_flown_range[1])}, "  # Miles_Flown
    insert_statement += f"{random.randint(miles_redeemed_range[0], miles_redeemed_range[1])}"  # Miles_Redeemed
    insert_statement += ");\n"
    return insert_statement

# Generate and save 100 INSERT statements
with open('populate_frequent_flyer_fact.sql', 'w') as f:
    for frequent_flyer_key in range(1, 1001):
        insert_statement = generate_insert(frequent_flyer_key)
        f.write(insert_statement)
