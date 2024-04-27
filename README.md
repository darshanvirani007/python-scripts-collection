# Python Script Collection

Welcome to the Python Script Collection! This repository contains a collection of useful Python scripts for various tasks and purposes. Whether you're a beginner or an experienced developer, you'll find scripts here to help you automate tasks, analyze data, or just learn more about Python programming.

## Learning

I'm a student currently learning Python and automation. This repository serves as a valuable resource for practicing my skills and exploring real-world applications. Feel free to join me on this learning journey by experimenting with the scripts and modifying them to suit your own learning goals.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Scripts](#scripts)
4. [Contributing](#contributing)
5. [Learning](#learning)
6. [License](#license)

## Installation

To use the scripts in this collection, make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Clone this repository to your local machine:

```
git clone https://github.com/your_username/python-script-collection.git
```

Navigate to the directory:

```
cd python-script-collection
```

Install any dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

Each script in this collection comes with its own usage instructions. Navigate to the script's directory and refer to the README.md file within that directory for specific instructions on how to use the script.

## Scripts

Here's a brief overview of the scripts available in this collection:

1. **script1.py**: Description of what this script does.
2. **medical_reports_classifier.py**: This Python script automates the classification of medical reports into positive and negative symptom categories using natural language processing techniques. It utilizes machine learning algorithms from the scikit-learn library to analyze the text content of PDF reports. The classification is based on predefined lists of positive and negative symptoms commonly found in medical reports.

    ## Features
    
    - **PDF Text Extraction:** Extracts text content from PDF files containing medical reports.
    - **Symptom Classification:** Classifies reports based on the presence of positive or negative symptoms.
    - **Patient Name Extraction:** Attempts to extract patient names from report texts.
    - **Output Generation:** Outputs classification results to an Excel file for further analysis.
    
    ## Usage
    
    1. Place the medical reports (in PDF format) in a designated directory.
    2. Run the script, which will process each report, classify it, and generate an Excel file with the classification results.
    3. Review the Excel file to analyze the classification outcomes.
    
    ## Dependencies
    
    - Python 3.x
    - pandas
    - PyPDF2
    - scikit-learn
    
    ## Usage Example
    
    ```bash
    python medical_report_classification.py

## Contributing

Contributions are welcome! If you have a Python script that you think would be useful to others, feel free to open a pull request. Please make sure your code follows the repository's coding standards and includes documentation where necessary.

If you find any issues or have suggestions for improvement, please open an issue on the repository's issue tracker.

