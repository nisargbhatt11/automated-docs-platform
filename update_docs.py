from datetime import datetime

# Get the current date and time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

try:
    with open('docs/index.html', 'a') as file:
        file.write(f'<p>Updated automatically by Python script on {current_time}!</p>\n')
    print("Update successful.")
except Exception as e:
    print("An error occurred:", e)
