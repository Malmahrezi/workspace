-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Crime report table
SELECT description
  FROM crime_scene_reports
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND street = 'Humphrey Street';

-- Two incidents happened the day we mentione and Only one is related to theft. Other is related to littering.

-- The witnesses could be the accomplice. So, finding the names of the witnesses from the interviews table. Also, checking their interviews' transcripts.
SELECT name, transcript
  FROM interviews
 WHERE year = 2021
   AND month = 7
   AND day = 28;

   -- name- Eugene repeated twice, so we will check him in peple table.
    SELECT name
    FROM people
    WHERE name = 'Eugene';
-- it appears that their is only on 'Eugene'

-- Now we will check the other three people who gave interview on that specific day
SELECT name, transcript
  FROM interviews
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND transcript LIKE '%bakery%'
 ORDER BY name;
 -- Witnesses are- Eugene, Raymond, and Ruth.


 -- We will check the person who withdraw money from the ATM, "Eugene clue"
 SELECT account_number, amount
  FROM atm_transactions
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw';
-- Finding the name connected with account number. Putting these names in the 'Suspect List'
SELECT name, atm_transactions.amount
  FROM people
  JOIN bank_accounts
    ON people.id = bank_accounts.person_id
  JOIN atm_transactions
    ON bank_accounts.account_number = atm_transactions.account_number
 WHERE atm_transactions.year = 2021
   AND atm_transactions.month = 7
   AND atm_transactions.day = 28
   AND atm_transactions.atm_location = 'Leggett Street'
   AND atm_transactions.transaction_type = 'withdraw';

-- As Ryaymon said, they called a person and they speaked for less than a minut, and they asked for the other half of the call to buy. a flight ticket of the earliest flight on july 29, 2021.
--First we will find the Airport , the origin of the flight of the thief
SELECT abbreviation, full_name, city
  FROM airports
 WHERE city = 'Fiftyville';
 -- Finding the flights on July 29 from Fiftyville airport, and ordering them by time.
 SELECT flights.id, full_name, city, flights.hour, flights.minute
  FROM airports
  JOIN flights
    ON airports.id = flights.destination_airport_id
 WHERE flights.origin_airport_id =
       (SELECT id
          FROM airports
         WHERE city = 'Fiftyville')
   AND flights.year = 2021
   AND flights.month = 7
   AND flights.day = 29
 ORDER BY flights.hour, flights.minute;
 --First flight at 8:20 to LaGuardia Airport in New York City (Flight id- 36). This could be the one we are looking for.
-- Checking the list of passengers in that flight, have them all in the suspecting list, and the order of their name by their passport numbers.
SELECT passengers.flight_id, name, passengers.passport_number, passengers.seat
  FROM people
  JOIN passengers
    ON people.passport_number = passengers.passport_number
  JOIN flights
    ON passengers.flight_id = flights.id
 WHERE flights.year = 2021
   AND flights.month = 7
   AND flights.day = 29
   AND flights.hour = 8
   AND flights.minute = 20
 ORDER BY passengers.passport_number;
 -- Checking the phone call records to find the person who bought the tickets.
 -- first checking the possible name of the celluer, and adding them to the suspect list. and order them according to the duration of the call.
SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.caller
 WHERE phone_calls.year = 2021
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
 ORDER BY phone_calls.duration;
 -- then we check the call receiver . and order them according to the duratiojn of the call.
 SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.receiver
 WHERE phone_calls.year = 2021
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
   ORDER BY phone_calls.duration;

-- Ruth gave clues- The thief drove away in a car from the bakery, within 10 minutes from the theft. SO, checking the license plates of cars within that time frame. Then, checking out the names of those cars' owners. They could be suspects.
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
  FROM people
  JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
 WHERE bakery_security_logs.year = 2021
   AND bakery_security_logs.month = 7
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.activity = 'exit'
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute >= 15
   AND bakery_security_logs.minute <= 25
 ORDER BY bakery_security_logs.minute;

 -- Bruce must the thief as he is present in all the 4 lists- List of passengers, list of people who did the specific atm transactions, list of people who called, and list of people who drove away in cars from the bakery.
 -- he took newyork city flight to escape
 -- and he might get help from Robin who purchased the flight ticket


