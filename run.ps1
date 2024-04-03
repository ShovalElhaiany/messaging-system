# Create and set up virtual environment (optional)
py -m venv .venv
.venv/scripts/activate

# Upgrade pip within the virtual environment
python.exe -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Load initial data (optional)
python load_data.py

# Run the development server
python manage.py runserver
