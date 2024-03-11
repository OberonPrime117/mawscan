import os

current_directory = os.path.dirname(__file__)
logs_directory = os.path.join(current_directory, '..', 'logs')
app_log_path = os.path.join(logs_directory, 'app.log')

print("Path to app.log:", app_log_path)
