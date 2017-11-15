# :soccer: Football Stats Database :soccer:
## A CPSC304 project
### by Issac Ahouma, Edward Cai, Gary Gao, Jean-Claude Tissier

### Requirements
- Python 3.5 and later
- Windows: Microsoft Visual C++ Build Tools
- pip install -r requirements.txt

### Steps to run
- Go to config.py and uncomment the database and environment you are working with
- Run drop_data.py to drop any tables that may be in the database
- Run create_tables.py to create empty tables
- Run generate_data.py to generate the .csv data files. This script seeds data from .csv files in /dataSeed
- Run app.py to host the app locally on port 5000
- PLAY :stars: