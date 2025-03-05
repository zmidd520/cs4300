
# Homework 2 Setup

To run the project, `cd` into the 'hw2' directory
Use the command `source hw2/bin/activate` to activate the python environment (the venv folder is also named hw2)

### Project Layout

The homepage of the app lists the available movies, each with a "Book a Seat" button.

Accessing the booking page requires that the user is logged in, at which point they may select
a seat and a booking date. If the selected combination of seat, date, and movie is already taken,
the user will be asked to redo their selection. If the selection is unique, the user is brought to
their booking history, which shows the movie, date, and seat number for every booking they have made.

The API allows users to view information about currently available movies, see the current status of seats
(Available or Booked), and see old bookings or create new ones. To update the seat statuses for the current
day, go to "https://app-zmiddlet-5.devedu.io/seats", which updates the status of each seat based on whether
or not it is booked for the current day.
