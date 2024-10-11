import pytest
import datetime
import os

# Create 'reports' directory if it doesn't exist
if not os.path.exists('reports'):
    os.makedirs('reports')

# Generate timestamp in format YYYYMMDD_HHMMSS
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Construct the report file name with the timestamp
report_file = f"reports/report_{timestamp}.html"

# Run pytest with the custom report file name
pytest.main([f"--html={report_file}", "--self-contained-html"])

