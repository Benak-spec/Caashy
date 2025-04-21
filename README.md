# Caashy - Personal Budget and Expense Tracker

## MDX-CST4160
**MDX Dubai - MSc Fintech - CST4160 Advanced Software Development for Financial Technology**

## Overview
Caashy is a lightweight and responsive web application designed to help users manage their personal finances. It supports logging expenses, viewing summaries, and provides financial insights using real-time data APIs.

## Features
- **Add Expense**: Quickly log and categorize your daily expenses
- **View History**: Display of previously logged expenses with timestamps and notes
- **Summary Dashboard**: Real-time calculation of total budget, total expenses, and balance
- **Insights Section**:
  - **Exchange Rate** (USD to INR)
  - **Live Bitcoin Price**
  - **Financial Tip of the Day**
- **Persistent Storage**: Stores data in both SQLite database and CSV
- **Unit Testing**: Built-in tests to validate logging functionality and CSV writing

## Technologies Used
- **Frontend**: HTML5, CSS3, Bootstrap, Jinja2
- **Backend**: Python (Flask)
- **Database**: SQLite, CSV
- **APIs Used**:
  - [ExchangeRate-API](https://www.exchangerate-api.com/) – Live currency rates
  - [CoinGecko API](https://www.coingecko.com/) – Bitcoin price
  - [Quotable API](https://github.com/lukePeavey/quotable) – Daily finance-related quotes

## Dependencies
- Flask
- requests
- pandas
- SQLAlchemy

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
1. Clone the repository:
```bash
git clone https://github.com/YourUsername/Caashy.git
cd Caashy
```
2. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate it:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
python create_db.py
```

### Running the Application
Start the Flask development server:
```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000`

## Usage
- Navigate to the homepage to add new expenses
- The dashboard will automatically update the budget summary
- View the latest insights in the right panel (live rate, Bitcoin price, and quote)
- All entries are stored in both `expenses.db` and `expenses.csv`

## File Structure
```
Caashy/
├── app.py
├── tracker_module.py
├── api_helpers.py
├── models.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── data/
│   ├── expenses.csv
│   └── expenses.db
├── tests/
│   └── test_expense.py
```

## Configuration
All file paths are dynamically set using Python’s `os` module to ensure platform independence. The SQLite database and CSV file are saved in the `/data` directory.

## Troubleshooting
- **Flask Errors**: Ensure dependencies are installed and Python version is compatible
- **Database Not Found**: Run `create_db.py` to initialize
- **API Failure**: Check internet connection and API endpoint availability

## Contributing
1. Fork the repository
2. Create a new branch:
```bash
git checkout -b feature/your-feature
```
3. Commit changes:
```bash
git commit -am 'Add new feature'
```
4. Push to GitHub:
```bash
git push origin feature/your-feature
```
5. Submit a Pull Request

## License
This project is licensed under the MIT License.

## Acknowledgments
- ExchangeRate-API for real-time currency data
- CoinGecko for crypto price tracking
- Quotable API for daily financial tips
- Flask and the Python developer community

