import random
import string

# Sample data
cabin_classes = ["Economy", "Premium Economy", "Business", "First Class"]
fare_types = ["Regular", "Discount", "Flexible"]
restrictions = ["None", "Non-refundable", "Fully refundable", "Advance purchase required"]
fare_basis_codes = ["ABCD", "EFGH", "IJKL", "MNOP", "QRST", "UVWX", "YZ01", "2345", "6789", "WXYZ"]

def generate_fare_basis_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def generate_fare_basis_code():
    return random.choice(fare_basis_codes)

def generate_cabin_class():
    return random.choice(cabin_classes)

def generate_fare_type():
    return random.choice(fare_types)

def generate_restrictions():
    return random.choice(restrictions)

def generate_fare_amount():
    return round(random.uniform(100, 5000), 2)

def generate_insert_statement():
    with open('Populate_Fare_Basis.SQL', 'w') as data:
        for i in range(20):  
            fare_basis_key = generate_fare_basis_key()
            fare_basis_code = generate_fare_basis_code()
            cabin_class = generate_cabin_class()
            fare_type = generate_fare_type()
            restriction = generate_restrictions()
            fare_amount = generate_fare_amount()

            insert_statement = (
                f"INSERT INTO Fare_Basis_Dim (Fare_Basis_Key, Fare_Basis_Code, Cabin_Class, Fare_Type, Restrictions, Fare_Amount) "
                f"VALUES ('{fare_basis_key}', '{fare_basis_code}', '{cabin_class}', '{fare_type}', '{restriction}', {fare_amount});\n"
            )
            data.write(insert_statement)

generate_insert_statement()
