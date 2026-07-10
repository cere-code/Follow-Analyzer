# Follower Analyzer

## Description

It takes data from Instagram and uses two JSON files—following and follower—to determine who does and does not follow you.

## Features

* Compares Instagram following vs. followers lists
* Identifies users who don't follow back

## Prerequisites

* pandas
* time
* Instagram data (requested directly from Instagram using their data export tool)

## Installation

1. Request your Instagram data via Instagram’s settings (Settings → Security → Download Data).
2. Install pandas:
   `pip install pandas`
   or
   `python -m pip install pandas`

## Usage

Place the downloaded JSON files (following and follower) in the project directory. Run the script (e.g., `python analyzer.py`) to see who doesn't follow back.

## Contributing

Fork the repository, create a branch, and submit a pull request with documentation.

## FAQ / Troubleshooting

Ensure both JSON files are correctly formatted. Validate keys if data mismatches.

## Acknowledgments

This project uses pandas for data manipulation.
