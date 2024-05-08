def generate_time_dim():
    with open('Populate_Time.SQL', 'w') as data:
        time_key = 0
        for hour in range(24):
            for minute in range(60):
                for second in range(60):
                    time_key_str = str(time_key).zfill(8)
                    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
                    insert_statement = (
                        f"INSERT INTO Time_Dim (Time_Key, Timestamp, Hour, Minutes, Seconds) "
                        f"VALUES ('{time_key_str}', TO_TIMESTAMP('{time_str}', 'HH24:MI:SS'), {hour}, {minute}, {second});\n"
                    )
                    data.write(insert_statement)
                    time_key += 1

generate_time_dim()
