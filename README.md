# Genzy Redme.md

Welcome to the **Genzy** repository! This project automates the process of logging into a website and submitting user data through a form.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Format](#data-format)
- [Main Script](#main-script)
- [License](#license)

## Introduction

This project is designed to automate data entry tasks. The script logs into a specified website and fills out forms with user data read from a text file.

## Features

- Automated login to the website.
- Data extraction from a text file.
- Form filling and submission.
- Error handling for various scenarios.

## Installation

To use this project, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/genzy.git
    cd genzy
    ```

2. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Download and install ChromeDriver**: Ensure that the ChromeDriver version matches your Chrome browser version. Place it in a directory included in your system's PATH.

## Usage

To run the script, use the following command:

```sh
python main.py



Data Format
The data.txt file contains the user data in the following format:

First Name: [first_name]
Last Name: [last_name]
Email: [email]
Phone: [phone]
Gender: [gender]
Date Of Birth: [date_of_birth]

First Name: [first_name]
Last Name: [last_name]
Email: [email]
Phone: [phone]
Gender: [gender]
Date Of Birth: [date_of_birth]

...


Example

First Name: Brennan
Last Name: Fitzpatrick
Email: brennanfitzpatrick@zentia.com
Phone: +1 (942) 576-2447
Gender: male
Date Of Birth: May 10, 1968

First Name: Curry
Last Name: Woods
Email: currywoods@zentia.com
Phone: +1 (991) 412-2301
Gender: male
Date Of Birth: Mar 30, 1991


Main Script
The main.py script performs the following tasks:

Login: Logs into the website using the provided credentials.
Data Reading: Reads and parses user data from data.txt.
Form Filling: Fills out the form on the website with the parsed data and submits it.

Key Functions
read_data(file_path): Reads and parses data from the specified text file.
convert_gender(gender): Converts the gender string to camel case.
fill_form(record): Fills out and submits the form with the given record.

Example Usage

# Read the data from the text file
parsed_data = read_data("data.txt")

# Fill the form for each record
for record in parsed_data:
    fill_form(record)
    sleep(2)  # Add sleep to simulate realistic form submission delay

try:
    while True:
        pass
except KeyboardInterrupt:
    driver.quit()

License
This project is licensed under the MIT License. See the LICENSE file for details.
