CREATE TABLE Hotel_Fact (
    Hotel_Fact_Key INT PRIMARY KEY,
    Passenger_Key INT,
    Flight_Date_Key INT,
    Arrival_Date_Key INT,
    Reservation_Date_Key INT,
    Reservation_Channel_Key INT,
    Hotel_Key INT,
    Reservation_ID VARCHAR(50),
    Number_of_Nights INT,
    CONSTRAINT fk_passenger FOREIGN KEY (Passenger_Key) REFERENCES Passenger_Dim (Passenger_Key),
    CONSTRAINT fk_flight_date FOREIGN KEY (Flight_Date_Key) REFERENCES Date_Dim (Date_Key),
    CONSTRAINT fk_arrival_date FOREIGN KEY (Arrival_Date_Key) REFERENCES Date_Dim (Date_Key),
    CONSTRAINT fk_reservation_date FOREIGN KEY (Reservation_Date_Key) REFERENCES Date_Dim (Date_Key),
    CONSTRAINT fk_reservation_channel FOREIGN KEY (Reservation_Channel_Key) REFERENCES Booking_Channel_Dim (Channel_Key),
    CONSTRAINT fk_hotel FOREIGN KEY (Hotel_Key) REFERENCES Hotel_Dim (Hotel_Key)
);



CREATE TABLE Reservation_Fact (
    Scheduled_Departure_Date_Key INT,
    Scheduled_Departure_Time_Key VARCHAR(50),
    Reservation_Date_Key INT,
    Passenger_Key INT,
    Passenger_Profile_Key VARCHAR(50),
    Departure_Airport_Key INT,
    Destination_Airport_Key INT,
    Aircraft_Key INT,
    Flight_CLass_Key INT,
    Fare_Basis_Key INT,
    Booking_Channel_Key INT,
    Payment_Method_Key INT,
    Ticket_Number INT,
     Flight_Number INT,
     Reservation_Number INT,
     Segment_Sequence_Number INT,
     Taxes FLOAT,
     Transaction_Fees FLOAT,
     Passenger_Paid_Amount FLOAT,
     CONSTRAINT fk_passenger_res FOREIGN KEY (Passenger_Key) REFERENCES Passenger_Dim (Passenger_Key),
     CONSTRAINT fk_passenger_profile_res FOREIGN KEY (Passenger_Profile_Key) REFERENCES Passenger_Profile_Dim (Passenger_Profile_Key),
     CONSTRAINT fk_departure_date_res FOREIGN KEY (Scheduled_Departure_Date_Key) REFERENCES Date_Dim (Date_Key),
     CONSTRAINT fk_reservation_date_res FOREIGN KEY (Reservation_Date_Key) REFERENCES Date_Dim (Date_Key),
     CONSTRAINT fk_departure_time_res FOREIGN KEY (Scheduled_Departure_Time_Key) REFERENCES Time_Dim (Time_Key),
     CONSTRAINT fk_departure_airport_res FOREIGN KEY (Departure_Airport_Key) REFERENCES Airport_Dim (Airport_Key),
     CONSTRAINT fk_destination_airport_res FOREIGN KEY (Destination_Airport_Key) REFERENCES Airport_Dim (Airport_Key),
     CONSTRAINT fk_aircraft_res FOREIGN KEY (Aircraft_Key) REFERENCES Aircraft_Dim (Aircraft_Key),
     CONSTRAINT fk_flight_cLass_res FOREIGN KEY (Flight_CLass_Key) REFERENCES Flight_Class_Dim (Flight_CLass_Key),
     CONSTRAINT fk_fare_basis_res FOREIGN KEY (Fare_Basis_Key) REFERENCES Fare_Basis_Dim (Fare_Basis_Key),
     CONSTRAINT fk_booking_channel_res FOREIGN KEY (Booking_Channel_Key) REFERENCES Booking_Channel_Dim (Channel_Key),
     CONSTRAINT fk_payment_method_res FOREIGN KEY (Payment_Method_Key) REFERENCES Payment_Method_Dim (Payment_Method_Key)
);



CREATE TABLE Flight_Activity_Fact (
    Scheduled_Departure_Date_Key INT,
    Scheduled_Departure_Time_Key VARCHAR(50),
    Actual_Departure_Date_Key INT,
    Actual_Departure_Time_Key VARCHAR(50),
    Passenger_Key INT,
    Passenger_Profile_Key VARCHAR(50),
    Departure_Airport_Key INT,
    Destination_Airport_Key INT,
    Aircraft_Key INT,
    CLass_of_Service_Key INT,
    Fare_Basis_Key INT,
    Booking_Channel_Key INT,
    Ticket_Number INT,
     Flight_Number INT,
     Reservation_Number INT,
     Segment_Sequence_Number INT,
     Base_Fare_Revenue FLOAT,
     Taxes FLOAT,
     Transaction_Fees FLOAT,
     Passenger_Paid_Amount FLOAT,
     CONSTRAINT fk_passenger_fa FOREIGN KEY (Passenger_Key) REFERENCES Passenger_Dim (Passenger_Key),
     CONSTRAINT fk_passenger_profile_fa FOREIGN KEY (Passenger_Profile_Key) REFERENCES Passenger_Profile_Dim (Passenger_Profile_Key),
     CONSTRAINT fk_departure_date_fa FOREIGN KEY (Scheduled_Departure_Date_Key) REFERENCES Date_Dim (Date_Key),
     CONSTRAINT fk_actual_date_fa FOREIGN KEY (Actual_Departure_Date_Key) REFERENCES Date_Dim (Date_Key),
     CONSTRAINT fk_departure_time_fa FOREIGN KEY (Scheduled_Departure_Time_Key) REFERENCES Time_Dim (Time_Key),
     CONSTRAINT fk_actual_time_fa FOREIGN KEY (Actual_Departure_Time_Key) REFERENCES Time_Dim (Time_Key),
     CONSTRAINT fk_departure_airport_fa FOREIGN KEY (Departure_Airport_Key) REFERENCES Airport_Dim (Airport_Key),
     CONSTRAINT fk_destination_airport_fa FOREIGN KEY (Destination_Airport_Key) REFERENCES Airport_Dim (Airport_Key),
     CONSTRAINT fk_aircraft_fa FOREIGN KEY (Aircraft_Key) REFERENCES Aircraft_Dim (Aircraft_Key),
     CONSTRAINT fk_flight_cLass_fa FOREIGN KEY (CLass_of_Service_Key) REFERENCES Class_Of_Service_Flown (Class_Of_Service_Key),
     CONSTRAINT fk_fare_basis_fa FOREIGN KEY (Fare_Basis_Key) REFERENCES Fare_Basis_Dim (Fare_Basis_Key),
     CONSTRAINT fk_booking_channel_fa FOREIGN KEY (Booking_Channel_Key) REFERENCES Booking_Channel_Dim (Channel_Key)
);



CREATE TABLE Customer_Care_Fact (
    Customer_Care_Key INT PRIMARY KEY,
    Passenger_Key INT,
    Passenger_Profile_Key VARCHAR(50),
    Reservation_Date_Key INT,
    Interaction_Key INT,
    Interaction_Time_Key VARCHAR(50),
    Staff_Key INT,
    Departure_Airport_Key INT,
    Arrival_Airport_Key INT,
    Ticket_Number INT,
    Segment_Number INT,
    Flight_Number INT,
    Problem_Severity INT,
    Feedback_Rate INT,
    CONSTRAINT fk_passenger_profile_cc FOREIGN KEY (Passenger_Profile_Key) REFERENCES Passenger_Profile_Dim(Passenger_Profile_Key),
    CONSTRAINT fk_passenger_cc FOREIGN KEY (Passenger_Key) REFERENCES Passenger_Dim(Passenger_Key),
    CONSTRAINT fk_reservation_date_cc FOREIGN KEY (Reservation_Date_Key) REFERENCES Date_Dim(Date_Key),
    CONSTRAINT fk_interaction_cc FOREIGN KEY (Interaction_Key) REFERENCES Interaction_Dim(Interaction_Key),
    CONSTRAINT fk_interaction_time_cc FOREIGN KEY (Interaction_Time_Key) REFERENCES Time_Dim(Time_Key),
    CONSTRAINT fk_staff_cc FOREIGN KEY (Staff_Key) REFERENCES Staff_Dim(Staff_Key),
    CONSTRAINT fk_departure_airport_cc FOREIGN KEY (Departure_Airport_Key) REFERENCES Airport_Dim(Airport_Key),
    CONSTRAINT fk_arrival_airport_cc FOREIGN KEY (Arrival_Airport_Key) REFERENCES Airport_Dim(Airport_Key)
);




CREATE TABLE Frequent_Flyer_Fact (
    Frequent_Flyer_Key INT PRIMARY KEY,
    Passenger_Key INT,
    Passenger_Profile_Key VARCHAR(50),
    Flight_Date_Key INT,
    Departure_Airport_Key INT,
    Arrival_Airport_Key INT,
    Redeem_Key INT,
    Ticket_Number INT,
    Miles_Earned INT,
    Miles_Flown INT,
    Miles_Redeemed INT,
    CONSTRAINT fk_passenger_ff FOREIGN KEY (Passenger_Key) REFERENCES Passenger_Dim(Passenger_Key),
    CONSTRAINT fk_passenger_profile_ff FOREIGN KEY (Passenger_Profile_Key) REFERENCES Passenger_Profile_Dim(Passenger_Profile_Key),
    CONSTRAINT fk_flight_date_ff FOREIGN KEY (Flight_Date_Key) REFERENCES Date_Dim(Date_Key),
    CONSTRAINT fk_departure_airport_ff FOREIGN KEY (Departure_Airport_Key) REFERENCES Airport_Dim(Airport_Key),
    CONSTRAINT fk_arrival_airport_ff FOREIGN KEY (Arrival_Airport_Key) REFERENCES Airport_Dim(Airport_Key),
    CONSTRAINT fk_redeem_ff FOREIGN KEY (Redeem_Key) REFERENCES Redeem_Dim(Redeem_Key)
);