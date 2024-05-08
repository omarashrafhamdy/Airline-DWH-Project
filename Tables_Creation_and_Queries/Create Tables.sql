CREATE TABLE Passenger_Dim (
    Passenger_Key INT PRIMARY KEY,
    Passenger_ID VARCHAR(10),
    Passenger_FirstName VARCHAR(50),
    Passenger_LastName VARCHAR(50),
    Passenger_Contact VARCHAR(100),
    Passenger_Type VARCHAR(10),
    Passenger_Gender VARCHAR(10),
    Passenger_Age INT,
    Passenger_Date_of_Birth DATE,
    Passenger_Nationality VARCHAR(50),
    Passenger_Country VARCHAR(50),
    Passenger_City VARCHAR(50)
);

CREATE TABLE Date_Dim (
    Date_Key INT PRIMARY KEY,
    Date_ DATE,
    Day_of_Week VARCHAR(20),
    Day_Number_in_Epoch INT,
    Week_Number_in_Epoch INT,
    Month_Number_in_Epoch INT,
    Day_Number_in_Calendar_Month INT,
    Day_Number_in_Calendar_Year INT,
    Fiscal_Last_Day_Ind CHAR(1),
    Calendar_Month VARCHAR(20),
    Calendar_Month_Number_in_Year INT,
    Calendar_Year_Month VARCHAR(7),
    Calendar_Quarter VARCHAR(2),
    Calendar_Year_Quarter VARCHAR(7),
    Calendar_Year INT,
    Fiscal_Month VARCHAR(20),
    Fiscal_Month_Number_in_Year INT,
    Fiscal_Year_Month VARCHAR(7),
    Fiscal_Quarter VARCHAR(2),
    Fiscal_Year_Quarter VARCHAR(7),
    Fiscal_Year INT
);

CREATE TABLE Time_Dim (
    Time_Key VARCHAR2(8) PRIMARY KEY,
    Timestamp TIMESTAMP,
    Hour NUMBER(2),
    Minutes NUMBER(2),
    Seconds NUMBER(2)
);

CREATE TABLE Airport_Dim (
    Airport_Key INT  PRIMARY KEY,
    Airport_ID VARCHAR2(3),
    Airport_Name VARCHAR2(100),
    City VARCHAR2(100),
    Country VARCHAR2(100),
    Timezone VARCHAR2(100)
);

CREATE TABLE Aircraft_Dim (
    Aircraft_Key INT PRIMARY KEY,
   Aircraft_Code  VARCHAR2(10),
    Aircraft_Type VARCHAR2(100),
    Manufacturer VARCHAR2(100),
    Model VARCHAR2(100),
    Year_Manufactured NUMBER(4),
    Seating_Capacity NUMBER,
    Cargo_Capacity_lbs NUMBER,
    Max_Range_miles NUMBER
);

CREATE TABLE Fare_Basis_Dim (
    Fare_Basis_Key INT PRIMARY KEY,
    Fare_Basis_Code VARCHAR2(10),
    Cabin_Class VARCHAR2(50),
    Fare_Type VARCHAR2(50),
    Restrictions VARCHAR2(100),
    Fare_Amount NUMBER(10, 2)
);

CREATE TABLE Passenger_Profile_Dim (
    Passenger_Profile_Key VARCHAR2(10) PRIMARY KEY,
    Frequent_Flyer_Tier VARCHAR2(20),
    Club_Membership_Status VARCHAR2(20),
    Lifetime_Mileage_Tier VARCHAR2(30)
);

CREATE TABLE Booking_Channel_Dim (
    Channel_Key INT PRIMARY KEY,
    Channel_ID VARCHAR(50),
    Channel_Type VARCHAR(50),
    Channel_Description VARCHAR(255),
    Channel_Contact_Information VARCHAR(255),
    Channel_Partnerships VARCHAR(255)
);


CREATE TABLE Class_of_Service_Flown (
    Class_of_Service_Key Number PRIMARY KEY,
    Class_ID VARCHAR2(50),
    Class_Purchased VARCHAR2(50),
    Class_Flown VARCHAR2(50),
    Purchased_Flown_Group VARCHAR2(50),
    Class_Change_Indicator VARCHAR2(50)
);


CREATE TABLE Interaction_Dim (
    Interaction_Key INT PRIMARY KEY,
    Type VARCHAR(50),
    Description VARCHAR(255)
);


CREATE TABLE Hotel_Dim (
    Hotel_Key INT PRIMARY KEY,
    Hotel_ID VARCHAR2(50),
    Stars INT,
    Avg_Night_Price NUMBER,
    City VARCHAR2(100),
    Country VARCHAR2(100)
);


CREATE TABLE Payment_Method_Dim (
    Payment_Method_Key INT PRIMARY KEY,
    Payment_Type VARCHAR2(50)
);


CREATE TABLE Redeem_Dim (
    Redeem_Key INT PRIMARY KEY,
    Type VARCHAR2(50),
    Description VARCHAR2(255)
);



CREATE TABLE Staff_Dim (
    Staff_Key INT PRIMARY KEY,
    Staff_ID VARCHAR2(50),
    Name VARCHAR2(100),
    Gender VARCHAR2(10),
    Address VARCHAR2(255),
    Job_Title VARCHAR2(100),
    Department VARCHAR2(100),
    Phone VARCHAR2(20),
    Supervisor_ID VARCHAR2(50)
);


CREATE TABLE Flight_Class_Dim (
    Flight_Class_Key INT PRIMARY KEY,
    Type VARCHAR(50)
);