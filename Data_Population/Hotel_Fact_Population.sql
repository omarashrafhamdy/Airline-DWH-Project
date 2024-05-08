INSERT INTO Hotel_Fact (Passenger_Key, Flight_Date_Key, Arrival_Date_Key, Reservation_Date_Key, Reservation_Channel_Key, Hotel_Key)
SELECT 
    pd.Passenger_Key,
    dd_flight.Date_Key,
    dd_arrival.Date_Key,
    dd_reservation.Date_Key,
    bc.Channel_Key,
    hd.Hotel_Key
FROM 
    Passenger_Dim pd
    CROSS JOIN Date_Dim dd_flight
    CROSS JOIN Date_Dim dd_arrival
    CROSS JOIN Date_Dim dd_reservation
    CROSS JOIN Booking_Channel_Dim bc
    CROSS JOIN Hotel_Dim hd
WHERE
    (pd.passenger_key = 1 and dd_flight.date_key = 20100104 and  dd_arrival.date_key = 20100104 and dd_reservation.date_key = 20100103 and bc.channel_key = 1 and hd.hotel_key = 15) or
    (pd.passenger_key = 2 and dd_flight.date_key = 20100101 and  dd_arrival.date_key = 20100101 and dd_reservation.date_key = 20100101 and bc.channel_key = 5 and hd.hotel_key = 1) or
    (pd.passenger_key = 4 and dd_flight.date_key = 20100105 and  dd_arrival.date_key = 20100105 and dd_reservation.date_key = 20100101 and bc.channel_key = 3 and hd.hotel_key = 6);