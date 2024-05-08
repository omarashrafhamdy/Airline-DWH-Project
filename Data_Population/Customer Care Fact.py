import random
import datetime

# Define ranges for each item
date_range_start = datetime.date(2010, 1, 1)
date_range_end = datetime.date(2024, 4, 30)
passenger_range = (1, 2000)
passenger_profile_range = (1, 24)
interaction_range = (1, 4)
interaction_time_range = (0, 86399)
staff_range = (1, 34)
airport_range = (1, 34)
problem_severity_range = (1, 5)
feedback_rate_range = (1, 5)

# Function to generate random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)

# Function to generate random time key within a range
def random_time_key():
    return f"{random.randint(interaction_time_range[0], interaction_time_range[1]):08}"

# Function to generate random insert statement
def generate_insert(customer_care_key):
    insert_statement = f"INSERT INTO customer_care_fact VALUES ({customer_care_key}, "
    insert_statement += f"{random.randint(passenger_range[0], passenger_range[1])}, "  # Passenger_Key
    insert_statement += f"{random.randint(passenger_profile_range[0], passenger_profile_range[1])}, "  # Passenger_Profile_Key
    insert_statement += f"{int(random_date(date_range_start, date_range_end).strftime('%Y%m%d'))}, "  # Reservation_Date_Key
    insert_statement += f"{random.randint(interaction_range[0], interaction_range[1])}, "  # Interaction_Key
    insert_statement += f"'{random_time_key()}', "  # Interaction_Time_Key
    insert_statement += f"{random.randint(staff_range[0], staff_range[1])}, "  # Staff_Key
    insert_statement += f"{random.randint(airport_range[0], airport_range[1])}, "  # Departure_Airport_Key
    insert_statement += f"{random.randint(airport_range[0], airport_range[1])}, "  # Arrival_Airport_Key
    insert_statement += f"{random.randint(100000, 999999)}, "  # Ticket_Number
    insert_statement += f"{random.randint(1, 4)}, "  # Segment_Number
    insert_statement += f"'{random.randint(100, 999):03}', "  # Flight_Number
    insert_statement += f"{random.randint(problem_severity_range[0], problem_severity_range[1])}, "  # Problem_Severity
    insert_statement += f"{random.randint(feedback_rate_range[0], feedback_rate_range[1])}"  # Feedback_Rate
    insert_statement += ");\n"
    return insert_statement

# Generate and save 100 INSERT statements
with open('populate_customer_care_fact.sql', 'w') as f:
    for customer_care_key in range(1, 1001):
        insert_statement = generate_insert(customer_care_key)
        f.write(insert_statement)
