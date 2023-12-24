import subprocess
import re
import matplotlib.pyplot as plt

# Run ab command and capture the output
ab_output = subprocess.run(["ab", "-n", "50", "-c", "10", "http://127.0.0.1:5000/read-users"], capture_output=True, text=True).stdout

# Extract relevant data using regular expressions
requests_match = re.search(r'Requests per second:\s+([0-9.]+)', ab_output)
request_per_sec = float(requests_match.group(1)) if requests_match else None

time_match = re.search(r'Time taken for tests:\s+([0-9.]+) seconds', ab_output)
time_taken = float(time_match.group(1)) if time_match else None

time_per_request_match = re.search(r'Time per request:\s+([0-9.]+) \[ms\] \(mean\)', ab_output)
time_per_request = float(time_per_request_match.group(1)) if time_per_request_match else None

percentage_data = re.search(r'Percentage of the requests served within a certain time \(ms\)\n([\s\d%\n]+)\n', ab_output)
if percentage_data:
    percentages = []
    times = []
    
    for line in percentage_data.group(1).split('\n'):
        match = re.match(r'\s*(\d+)%\s+(\d+)', line.strip())
        if match:
            percentages.append(int(match.group(1)))
            times.append(int(match.group(2)))

    # Plotting the data
    print(f"Time per request (ms): {time_per_request}")

    print(f"Time taken for all tests to finish: {time_taken}")


    # Plotting Percentage of requests served within a certain time (ms)
    plt.figure(figsize=(10, 6))
    plt.plot(percentages, times, marker='o', linestyle='-')
    plt.xlabel('Percentage')
    plt.ylabel('Time (ms)')
    plt.title('Percentage of requests served within a certain time (ms)')
    plt.grid(True)
    plt.xticks(percentages)  # Set X-axis ticks to match percentage values
    plt.show()


    

else:
    print("No data found for 'Percentage of requests served within a certain time (ms)'")
