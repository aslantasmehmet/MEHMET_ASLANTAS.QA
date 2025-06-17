# Insider Web Test Automation Project

This project includes test automation for the career page and QA positions on Insider's website. It was developed using Python and Selenium WebDriver.

## 🎯 Test Scenarios

### 1. Career Page Test
- Go to the home page and access the “Careers” page from the “Company” menu
- Check that all sections on the Careers page are visible

### 2. QA Jobs Test (Istanbul)
- Go to QA Careers
- Click on “See all QA jobs”
- Choose “Istanbul, Turkey” as location and “Quality Assurance” as department
- Check that job vacancies are listed

### 3. QA Job Posting Detail Check
- Go to QA Careers and apply filters
- Listed job vacancies:
  - Position: “Quality Assurance” includes
  - Department: “Quality Assurance” includes
  - Check that it contains Location: “Istanbul, Turkey”

### 4. Job Application Page Redirect Test
- Go to QA Careers and apply filters
- Hover over a job advertisement (hover)
- Click on the “View Role” button that appears
- Verify that you were redirected to the Lever Application form
- 
## 🛠️ Technologies Used

- Python 3.13.0
- Selenium WebDriver
- Pytest
- Chrome WebDriver

## 📦 Gereksinimler

```txt
selenium==4.17.2
pytest==7.4.3
pytest-html==4.1.1
webdriver_manager==4.0.1
```

## 🚀 Installation

1. Clone the project:
```bash
git clone [repository-url]
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 🎮 Running Tests

To run all the tests:
```bash
pytest tests/test_home_page.py -v
```

To run a specific test:
```bash
pytest tests/test_home_page.py::test_careers_page_sections -v
pytest tests/test_home_page.py::test_qa_jobs_istanbul -v
pytest tests/test_home_page.py::test_qa_jobs_details -v
pytest tests/test_home_page.py::test_qa_job_application_redirect -v
```

## 📁 Project Structure

```
MEHMET_ASLANTAS.QA/
├── pages/
│   ├── base_page.py       # Basic page functions
│   ├── home_page.py       # Home page operations
│   ├── careers_page.py    # Career page operations
│   └── qa_jobs_page.py    # QA job postings page operations
├── tests/
│   ├── conftest.py        # Pytest configuration
│   └── test_home_page.py  # Test scenarios
├── requirements.txt       # Required packages
└── README.md             # Project documentation
```

## ✨ Features

- Page Object Model (POM) design pattern was used
- Reliable element waits with explicit wait
- Detailed debugging and screenshot taking
- Clean and readable code structure
- Separate test functions for each scenario

## 👤 Yazar

Mehmet ASLANTAS
QA Engineer
