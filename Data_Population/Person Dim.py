import random
import string
from datetime import datetime, timedelta

# Sample data
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James",
    "Isabella", "Oliver", "Charlotte", "Elijah", "Amelia", "Benjamin", "Mia",
    "Lucas", "Harper", "Mason", "Evelyn", "Logan", "Abigail", "Alexander", "Emily",
    "Ethan", "Elizabeth", "Jacob", "Mila", "Michael", "Ella", "Daniel", "Avery",
    "Henry", "Sofia", "Jackson", "Camila", "Sebastian", "Aria", "Aiden", "Scarlett",
    "Matthew", "Victoria", "Lily", "Liam", "Grace", "Jack", "Chloe", "Alexander", "Sophie", "Lucas",
    "Ava", "Joshua", "Zoe", "Caleb", "Madison", "Samuel", "Natalie", "Dylan",
    "Layla", "Nathan", "Hannah", "Carter", "Brooklyn", "Evan", "Audrey", "Gabriel",
    "Lillian", "Isaac", "Stella", "Ryan", "Violet", "Luke", "Savannah", "Aiden",
    "Addison", "Isaiah", "Eleanor", "Owen", "Hailey", "Andrew", "Skylar", "David",
    "Alyssa", "Leah", "John", "Ariana", "Nathan", "Brianna", "Jason", "Megan", "Christopher",
    "Samantha", "Nicholas", "Kayla", "Brandon", "Allison", "Tyler", "Makayla", "Christian",
    "Gabrielle", "Justin", "Alexis", "Austin", "Rachel", "Jonathan", "Julia", "Jose",
    "Vanessa", "Kevin", "Lauren", "Daniel", "Anna", "Jose", "Nicole", "Eric", "Jordan",
    "Ashley", "Brian", "Emma", "Thomas", "Jasmine", "Zachary", "Michelle", "Connor", "Maya", "Derek", "Sara", "Eli", "Claire", "Mason", "Ruby",
    "Cole", "Nora", "Adrian", "Alice", "Colton", "Elena", "Tristan", "Leila",
    "Dominic", "Haley", "Bryce", "Jocelyn", "Victor", "Alexa", "Preston", "Katherine",
    "Jaxon", "Caroline", "Julian", "Samantha", "Miles", "Grace", "Felix", "Elise",
    "Everett", "Amaya", "Micah", "Lydia", "Gavin", "Hannah", "Landon", "Avery"
]

last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson",
    "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis",
    "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez",
    "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
    "Perez", "Sanchez", "Ramirez", "Flores", "Rivera", "Gomez", "Diaz", "Reyes",
    "Stewart", "Morales", "Murphy", "Cook", "Rogers", "Morgan", "Peterson", "Cooper",
    "Reed", "Bailey", "Bell", "Gutierrez", "Gonzales", "Sanders", "Ross", "Howard",
    "Kim", "Collins", "Cruz", "Parker", "Evans", "Edwards", "Collins", "Roberts",
    "Turner", "Phillips", "Campbell", "Perez", "Murray", "Washington", "Coleman",
    "Hughes", "Long", "Foster", "Ward", "Torres", "Murphy", "Reed", "Bailey",
    "Watson", "Russell", "Bryant", "Alexander", "Griffin", "Dunn", "Ford", "Grant",
    "Mendoza", "Curtis", "Reyes", "Chavez", "Sullivan", "Sullivan", "Simmons", "Woods",
    "Garcia", "Pierce", "Hawkins", "Hart", "Hunt", "Chen", "Snyder", "Stone", "Hunt",
    "Arnold", "Perkins", "Black", "Bates", "Larson", "Dixon", "Holmes"
]

countries = {
    'US': [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
        'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
        'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
        'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
        'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
        'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ],
    'England': ['London', 'Birmingham', 'Manchester', 'Liverpool', 'Bristol'],
    'Scotland': ['Glasgow', 'Edinburgh', 'Aberdeen', 'Dundee', 'Inverness'],
    'Wales': ['Cardiff', 'Swansea', 'Newport', 'Bangor', 'St Davids'],
    'Northern Ireland': ['Belfast', 'Derry', 'Lisburn', 'Newry', 'Armagh'],
    'Australia': [
        'New South Wales',
        'Australian Capital Territory',
        'Northern Territory',
        'Queensland',
        'South Australia',
        'Tasmania',
        'Victoria',
        'Western Australia'
    ],
    'Spain': [
        'Andalusia', 'Aragon', 'Asturias', 'Balearic Islands', 'Basque Country',
        'Canary Islands', 'Cantabria', 'Castile and León', 'Castilla-La Mancha',
        'Catalonia', 'Extremadura', 'Galicia', 'La Rioja', 'Madrid', 'Murcia',
        'Navarre', 'Valencian Community'
    ],
    'Germany': [
        'Baden-Württemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg',
        'Hesse', 'Lower Saxony', 'Mecklenburg-Vorpommern', 'North Rhine-Westphalia',
        'Rhineland-Palatinate', 'Saarland', 'Saxony', 'Saxony-Anhalt', 'Schleswig-Holstein',
        'Thuringia'
    ],
    'France': [
        'Auvergne-Rhône-Alpes', 'Bourgogne-Franche-Comté', 'Brittany', 'Centre-Val de Loire',
        'Corsica', 'Grand Est', 'Hauts-de-France', 'Île-de-France', 'Normandy', 'Nouvelle-Aquitaine',
        'Occitanie', 'Pays de la Loire', 'Provence-Alpes-Côte^Azur'
    ]
}

marital_statuses = ["Single", "Married", "Divorced", "Widowed"]

def random_date_of_birth():
    start_date = datetime(1960, 1, 1)
    end_date = datetime.now() - timedelta(days=365*18)  # At least 18 years old
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

def generate_passenger_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}-{suffix}"

def generate_insert_statement():
    with open('Populate_Passenger.SQL', 'w') as data:
        passenger_key = 1  # Initialize the passenger key counter
        for i in range(2000):  # Adjust the number of passengers as needed
            passenger_id = generate_passenger_id()
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            contact = f"{first_name.lower()}.{last_name.lower()}@example.com"
            passenger_type = random.choice(["Adult", "Child", "Infant"])
            gender = random.choice(["Male", "Female"])
            age = random.randint(1, 80)
            date_of_birth = random_date_of_birth().strftime('%Y-%m-%d')
            nationality = random.choice(list(countries.keys()))
            country = random.choice(list(countries.keys()))
            city = random.choice(countries[country])

            insert_statement = (
                f"INSERT INTO Passenger_Dim (Passenger_Key, Passenger_ID, Passenger_FirstName, Passenger_LastName, Passenger_Contact, Passenger_Type, "
                f"Passenger_Gender, Passenger_Age, Passenger_Date_of_Birth, Passenger_Nationality, Passenger_Country, Passenger_City) "
                f"VALUES ({passenger_key}, '{passenger_id}', '{first_name}', '{last_name}', '{contact}', '{passenger_type}', '{gender}', {age}, "
                f"TO_DATE('{date_of_birth}', 'YYYY-MM-DD'), '{nationality}', '{country}', '{city}');\n"
            )
            data.write(insert_statement)
            
            passenger_key += 1

generate_insert_statement()
