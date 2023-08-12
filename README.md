# WordPress Brute-Force Tool

![GitHub](https://github.com/chfncghn/Wordpress-bruteforcer/blob/main/LICENSE)

A simple Python script for educational purposes to demonstrate a WordPress login brute-force tool using threading.

## Table of Contents
- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Description

This script is designed to showcase how a brute-force attack on a WordPress login page could work using a provided username and a list of passwords. It utilizes Python's threading library for concurrent attempts.

**Important:** Using this script for unauthorized and malicious purposes is against the law and unethical. It's intended for educational purposes or security testing with proper authorization.

## Usage

1. Clone the repository: ```https://github.com/chfncghn/Wordpress-bruteforcer```
2. Navigate to the repository directory: ```cd Wordpress-bruteforcer```
Replace `script_name.py` with the actual script filename, `target_username` with the WordPress username you want to brute-force, `target_login_page_url` with the URL of the WordPress login page, and `passwords_list_file` with the path to the passwords list file.

## Attack

Now let's brute-force the target for that use this command

```python wordattack.py -h```
You need to do according to the steps in the help menu
```
usage: wordattack.py [-h] -u USERNAME -p URL -w FILE
wordattack.py: error: the following arguments are required: -u/--username, -p/--url, -w/--file
```
