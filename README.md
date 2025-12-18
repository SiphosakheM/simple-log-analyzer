# simple-log-analyzer

# Mini-Project 2: Simple Log Analyzer (Beginner)

## Project Objective
Create a Python script that reads a mock log file (`app.log`) and generates a summary report based on the content, focusing on basic file operations and strong error handling.

## Core Requirements

1.  **File Input:** The script must read each line from a designated log file (you need to create a mock `app.log` file with sample data).
2.  **Analysis:** Count the total number of lines in the file.
3.  **Keyword Tracking:** Track how often three specific keywords appear, regardless of case (e.g., "ERROR", "WARNING", "INFO").
4.  **Output:** After processing, print a clear summary report to the console. This should include:
    * Total lines processed.
    * The count for each of the three keywords.
    * The path of the analyzed log file.
5.  **Error Handling:** Use a `try...except` block to handle the situation when the specified log file does not exist (`FileNotFoundError`).

## Concepts Covered
* File I/O (`open()`, `read()`, the `with` statement)
* Basic string methods (splitting, counting, case manipulation)
* Using a dictionary or variable for counting and tracking data
* Handling exceptions for file system operations

---

## How to Run
```bash
python log_analyzer.py
