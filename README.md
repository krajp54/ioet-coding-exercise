# ioet Coding Exercise

Exercise developed as part of the technical interview for the organization ioet Inc.

## Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

## Solution overview

In order to develop a solution to the proposed exercise, several steps were carried out:

1. Reading the file.
2. Processing of the schedules obtained from each of the employees.
3. Verification of the cost per hour based on the table presented for the exercise, making a distinction between weekdays and weekends.
4. Sum of the costs obtained to calculate the payment to be made for each of the employees within the .txt file.

## Run Locally

Clone the project

```bash
  git clone https://github.com/krajp54/ioet-coding-exercise
```

Go to the project directory

```bash
  cd ioet-coding-exercise
```

Run the main script

```bash
  python payment.py
```

## Usage/Examples

In order to run the script, the "employees.txt" file must be located in the root folder of the project. In case you need to use another file, you can make the change in the following section of code:

```python
  if __name__ == '__main__':
      employees = readFile('./employees.txt')
```

With the "employees.txt" file, you should see the next output:

```bash
  The amount to pay RENE is: 215 USD
  The amount to pay ASTRID is: 85 USD
  The amount to pay ALEJANDRO is: 185 USD
  The amount to pay KAREN is: 170 USD
  The amount to pay COREY is: 270 USD
```

## Running Tests

To run tests, run the following command:

```bash
  python test.py
```

## Build with

-   [Python](https://www.python.org/)

## Authors

-   **Juan Pablo Rodríguez** - [krajp54](https://github.com/krajp54)
