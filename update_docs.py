from datetime import datetime

# Get the current date and time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Open the file in append mode and write the update
with open('docs/index.html', 'a') as file:
    file.write(f'<p>Updated automatically by Python script on {current_time}!</p>\n')

print("Documentation updated with date and time: " + current_time)
#test commit 21:01 EU
