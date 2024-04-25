Data Validator:
A program which tries to find errors in a file and writes them into valid_file.csv and invalid_file.csv

C = invalid data element count (no other errors will also display),

I = invalid id,

N = invalid name,

E = invalid email,

 P = invalid phone,
 
 D = invalid date,
 
 T = invalid time,
 
• Invalid data elements count (if so, you will NOT check any other data)
• Invalid id that isn't an integer
• Invalid names that are not in a "last name, first name" format
• Invalid email that are not in proper email format or not .edu extension
• Invalid phone numbers that are not in a 111-222-3333 format
• Invalid date that are not in a MM/DD/YYYY format
• Invalid time that are not in a HH:MM military format
Display a summary report at the end of how many records are successfully validate, plus an error
report for each type of invalid data
