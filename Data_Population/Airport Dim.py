airports = [
    {
        "Airport_Name": "John F. Kennedy International Airport",
        "City": "New York City",
        "Country": "United States",
        "Timezone": "America/New_York"
    },
    {
        "Airport_Name": "Los Angeles International Airport",
        "City": "Los Angeles",
        "Country": "United States",
        "Timezone": "America/Los_Angeles"
    },
    {
        "Airport_Name": "London Heathrow Airport",
        "City": "London",
        "Country": "United Kingdom",
        "Timezone": "Europe/London"
    },
    {
        "Airport_Name": "Dubai International Airport",
        "City": "Dubai",
        "Country": "United Arab Emirates",
        "Timezone": "Asia/Dubai"
    },
    {
        "Airport_Name": "Tokyo Haneda Airport",
        "City": "Tokyo",
        "Country": "Japan",
        "Timezone": "Asia/Tokyo"
    },
    {
        "Airport_Name": "Beijing Capital International Airport",
        "City": "Beijing",
        "Country": "China",
        "Timezone": "Asia/Shanghai"
    },
    {
        "Airport_Name": "Paris Charles de Gaulle Airport",
        "City": "Paris",
        "Country": "France",
        "Timezone": "Europe/Paris"
    },
    {
        "Airport_Name": "Frankfurt Airport",
        "City": "Frankfurt",
        "Country": "Germany",
        "Timezone": "Europe/Berlin"
    },
    {
        "Airport_Name": "Singapore Changi Airport",
        "City": "Singapore",
        "Country": "Singapore",
        "Timezone": "Asia/Singapore"
    },
    {
        "Airport_Name": "Amsterdam Airport Schiphol",
        "City": "Amsterdam",
        "Country": "Netherlands",
        "Timezone": "Europe/Amsterdam"
    },
    {
        "Airport_Name": "Hong Kong International Airport",
        "City": "Hong Kong",
        "Country": "Hong Kong",
        "Timezone": "Asia/Hong_Kong"
    },
    {
        "Airport_Name": "Sydney Airport",
        "City": "Sydney",
        "Country": "Australia",
        "Timezone": "Australia/Sydney"
    },
    {
        "Airport_Name": "San Francisco International Airport",
        "City": "San Francisco",
        "Country": "United States",
        "Timezone": "America/Los_Angeles"
    },
    {
        "Airport_Name": "Incheon International Airport",
        "City": "Incheon",
        "Country": "South Korea",
        "Timezone": "Asia/Seoul"
    },
    {
        "Airport_Name": "Toronto Pearson International Airport",
        "City": "Toronto",
        "Country": "Canada",
        "Timezone": "America/Toronto"
    },
    {
        "Airport_Name": "Munich Airport",
        "City": "Munich",
        "Country": "Germany",
        "Timezone": "Europe/Berlin"
    },
    {
        "Airport_Name": "Zurich Airport",
        "City": "Zurich",
        "Country": "Switzerland",
        "Timezone": "Europe/Zurich"
    },
    {
        "Airport_Name": "Cairo International Airport",
        "City": "Cairo",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Hurghada International Airport",
        "City": "Hurghada",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Sharm El Sheikh International Airport",
        "City": "Sharm El Sheikh",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Luxor International Airport",
        "City": "Luxor",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Marsa Alam International Airport",
        "City": "Marsa Alam",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Alexandria International Airport",
        "City": "Alexandria",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Aswan International Airport",
        "City": "Aswan",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Sohag International Airport",
        "City": "Sohag",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Mersa Matruh Airport",
        "City": "Mersa Matruh",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Asyut International Airport",
        "City": "Asyut",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Taba International Airport",
        "City": "Taba",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Borg El Arab Airport",
        "City": "Borg El Arab",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "El Arish International Airport",
        "City": "El Arish",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Assiut Airport",
        "City": "Assiut",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Marsa Matruh International Airport",
        "City": "Marsa Matruh",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "Abu Simbel Airport",
        "City": "Abu Simbel",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    },
    {
        "Airport_Name": "St. Catherine International Airport",
        "City": "St. Catherine",
        "Country": "Egypt",
        "Timezone": "Africa/Cairo"
    }
]

def generate_insert_statements(airports):
    with open('Populate_Airport.SQL', 'w') as data_file:
        for airport in airports:
            airport_key = airport["Airport_Name"][:3].upper()  # Generate airport key
            airport_name = airport["Airport_Name"]
            city = airport["City"]
            country = airport["Country"]
            timezone = airport["Timezone"] if "Timezone" in airport else "Unknown"  # Check if Timezone is available
            insert_statement = (
                f"INSERT INTO Airport_Dim (Airport_Key, Airport_Name, City, Country, Timezone) "
                f"VALUES ('{airport_key}', '{airport_name}', '{city}', '{country}', '{timezone}');\n"
            )
            data_file.write(insert_statement)
generate_insert_statements(airports)