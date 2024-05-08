CREATE SEQUENCE Aircraft_Key_Seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Aircraft_Dim_BI
BEFORE INSERT ON Aircraft_Dim
FOR EACH ROW
BEGIN
    SELECT Aircraft_Key_Seq.NEXTVAL INTO :NEW.Aircraft_Key FROM dual;
END;



CREATE SEQUENCE Airport_Key_Seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Airport_Dim_BI
BEFORE INSERT ON Airport_Dim
FOR EACH ROW
BEGIN
    SELECT Airport_Key_Seq.NEXTVAL INTO :NEW.Airport_Key FROM dual;
END;



CREATE SEQUENCE Hotel_Fact_Key_Seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER Hotel_Fact_BI
BEFORE INSERT ON Hotel_Fact
FOR EACH ROW
BEGIN
    SELECT Hotel_Fact_Key_Seq.NEXTVAL INTO :NEW.Hotel_Fact_Key FROM dual;
END;



CREATE SEQUENCE reservation_id_seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE OR REPLACE TRIGGER generate_reservation_id
BEFORE INSERT ON Hotel_Fact
FOR EACH ROW
BEGIN
    SELECT 'A1C' || CHR(67 + (reservation_id_seq.NEXTVAL - 1) / (26*26*26*26) - 1) ||
           CHR(65 + MOD((reservation_id_seq.NEXTVAL - 1) / (26*26*26), 26)) ||
           CHR(66 + MOD((reservation_id_seq.NEXTVAL - 1) / (26*26), 26)) ||
           CHR(65 + MOD((reservation_id_seq.NEXTVAL - 1) / 26, 26)) ||
           CHR(65 + MOD(reservation_id_seq.NEXTVAL - 1, 26))
    INTO :NEW.Reservation_ID
    FROM dual;
END;
