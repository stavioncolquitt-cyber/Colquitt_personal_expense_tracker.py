"""
Personal Expense Tracker
Author: Stavion Colquitt
Date:   2026-09-18
Tier:   Base Level
Description:
    Saves expense records (date, description, amount, category) to a plain
    text file and reads them back on each run. Demonstrates modules, file
    I/O, exception handling, and string operations.

TEST RESULTS (verified across four separate runs)
    [x] First run, no file exists
            load_records() caught FileNotFoundError and returned an empty
            list; "No expenses on record yet." displayed without crashing.
    [x] Add 2+ expenses, exit, run again
            All records reappeared on the following run, confirming the
            append write and the read-back both work.
    [x] Description longer than 30 characters
            "Annual streaming service subscription renewal" was stored as
            "Annual streaming service subsc" - exactly 30 characters in
            the saved file, confirmed by counting the field directly.
    [x] Add 0 new expenses
            The for loop ran zero times; existing records displayed
            unchanged and the file was not modified.
    [x] Column alignment with short and long descriptions
            Descriptions from 16 to 30 characters all aligned correctly;
            every saved line split into exactly 4 fields.
"""

import os
import datetime

FILENAME = "expenses.txt"


def build_record(description, amount, category):
    """Return a CSV line with today's date, truncated description, formatted amount, and category."""
    today = str(datetime.date.today())
    short_desc = description[:30]
    formatted_amount = f"{amount:.2f}"
    return ",".join([today, short_desc, formatted_amount, category])


def load_records(filename):
    """Return a list of records from the given file, or an empty list if the file doesn't exist."""
    records = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                records.append(line.split(","))
    except FileNotFoundError:
        return []
    return records


def save_record(filename, line):
    """Append one formatted record line to the expense file."""
    with open(filename, "a") as f:
        f.write(line + "\n")


def display_records(records):
    """Print the records in a formatted table."""
    if not records:
        print("No expenses on record yet.")
        return

    print(f"{'Date':<12}{'Description':<32}{'Amount':<10}{'Category':<15}")
    print("-" * 66)
    for r in records:
        if len(r) < 4:
            continue
        print(f"{r[0]:<12}{r[1]:<32}{'$' + r[2]:<10}{r[3]:<15}")


print("===== Your Expense Records =====")
records = load_records(FILENAME)
display_records(records)

count = int(input("\nHow many expenses do you want to add? "))

for i in range(count):
    print(f"\n--- Expense {i + 1} ---")
    description = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    line = build_record(description, amount, category)
    save_record(FILENAME, line)

print("\n===== Updated Expense Records =====")
records = load_records(FILENAME)
display_records(records)
print(f"\nSaved to: {os.path.abspath(FILENAME)}")