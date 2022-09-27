# Datetime Basics 2

## Manipulate Time

In this exercise, we will focus on the use and manipulation of time in Python

- Subtract time
- Add time
- Write a program to remind a tenant to pay rent on time

##

## Usage

`datetime` module offers a special function called `timedelta`.

```
from datetime import datetime
current_datetime = datetime.now()
```

##

## Tasks

### Task 1

Using the variable called `current_datetime`, subtract 15 days from the current time.

- If today is 8/07/2021, your result should look like this:

Hint: use `.strtime()` method to reformat the time

```
2021-06-23
```

### Task 2

Using the variable called `current_datetime`, add 7 days to your current day.

- Your result should look like this, if today is 8/07/2021:

```
2021-07-15
```

### Task 3

Your task is to determine when rent is due for a customer, we shall make assumption that tenant always pays 25 days from the first day of a month. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.

Start by creating a datetime instance with 25 January, 2021.

`start_date = datetime(year=2020, month=1, day=1)`

- Your result should look like this:

```
Hello Friedrich, your rent of 300 € is due on 25 January, 2021.
```
