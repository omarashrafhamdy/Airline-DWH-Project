import random
import string

def generate_aircraft_key():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=3))
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}-{suffix}"

def generate_aircraft_code():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))

def generate_aircraft_type():
    types = ["Narrow-body", "Wide-body", "Regional jet", "Turboprop"]
    return random.choice(types)

def generate_manufacturer():
    manufacturers = ["Boeing", "Airbus"]
    return random.choice(manufacturers)

def generate_model():
    models = ["737", "A320", "E190", "CRJ900", "ATR 72", "Citation X", "G650"]
    return random.choice(models)

def generate_year_manufactured():
    return random.randint(1960, 2022)

def generate_seating_capacity():
    return random.randint(50, 500)

def generate_cargo_capacity():
    return random.randint(1000, 50000)

def generate_max_range():
    return random.randint(1000, 10000)

def generate_insert_statements():
    with open('Populate_Aircraft.SQL', 'w') as data_file:
        for i in range(100):  # Generate data for 60 aircraft
            aircraft_key = generate_aircraft_key()
            aircraft_code = generate_aircraft_code()
            aircraft_type = generate_aircraft_type()
            manufacturer = generate_manufacturer()
            model = generate_model()
            year_manufactured = generate_year_manufactured()
            seating_capacity = generate_seating_capacity()
            cargo_capacity = generate_cargo_capacity()
            max_range = generate_max_range()

            insert_statement = (
                f"INSERT INTO Aircraft_Dim (Aircraft_Key, Aircraft_Code, Aircraft_Type, Manufacturer, Model, Year_Manufactured, "
                f"Seating_Capacity, Cargo_Capacity_lbs, Max_Range_miles) "
                f"VALUES ('{aircraft_key}', '{aircraft_code}', '{aircraft_type}', '{manufacturer}', '{model}', {year_manufactured}, "
                f"{seating_capacity}, {cargo_capacity}, {max_range});\n"
            )
            data_file.write(insert_statement)

generate_insert_statements()
