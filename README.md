# PDF Generator with Headers, Footers, and Line Separators
## This project is a Python script that generates a PDF document from a CSV file containing topics and the number of pages for each topic. Each page in the PDF includes a header, line separators, and a footer with the topic name and page number.

## Prerequisites
### Python 3.x

### fpdf library

### pandas library

## Installation
Install Python 3.x from the official website if you haven't already.

Install the required libraries using pip:
```bash
pip install fpdf pandas
```
## CSV File Format

The script reads data from a CSV file named topics1.csv. The CSV file should have the following structure:

| Topic | Pages |
|-------|-------|
| Topic1| 2     |
| Topic2| 3     |

- **Topic**: The name of the topic to be added as a header on each page.
  
- **Pages**: The number of pages to be generated for the corresponding topic.

## Script Description
### The script performs the following tasks:

1.Initializes the PDF document with A4 size pages.

2.Reads the data from topics1.csv.

3.Iterates over each row in the CSV to create pages with the specified number of pages for each topic.

4.Adds a header with the topic name on the first page for each topic.

5.Draws horizontal lines on each page.

6.Adds a footer with the topic name and the page number on each page.

7.Outputs the PDF document as output.pdf.


