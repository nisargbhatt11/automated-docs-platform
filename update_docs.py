from datetime import datetime

# Get the current date and time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Specify the text file name
file_path = 'docs/update_log.txt'  # You can replace this with any path you like

try:
    # Open the text file in append mode and write the update message
    with open(file_path, 'a') as file:
        file.write(f'Updated automatically by Python script on {current_time}!\n')
    print("Update successful.")
except Exception as e:
    print("An error occurred:", e)
