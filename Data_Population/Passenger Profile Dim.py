import itertools

frequent_flyer_tiers = ["Basic", "MidTier", "WarriorTier"]
club_membership_statuses = ["Non-Member", "Club Member"]
lifetime_mileage_tiers = ["Under 100,000 miles", "100,000-499,999 miles", "1,000,000-1,999,999 miles", "2,000,000-2,999,999 miles"]

def generate_insert_statements():
    with open('Populate_Passenger_Profile.SQL', 'w') as data_file:
        passenger_profile_key = 1
        for combination in itertools.product(frequent_flyer_tiers, club_membership_statuses, lifetime_mileage_tiers):
            frequent_flyer_tier, club_membership_status, lifetime_mileage_tier = combination
            insert_statement = (
                f"INSERT INTO Passenger_Profile_Dim (Passenger_Profile_Key, Frequent_Flyer_Tier, "
                f"Club_Membership_Status, Lifetime_Mileage_Tier) "
                f"VALUES ('{passenger_profile_key}', '{frequent_flyer_tier}', "
                f"'{club_membership_status}', '{lifetime_mileage_tier}');\n"
            )
            data_file.write(insert_statement)
            passenger_profile_key += 1

generate_insert_statements()
