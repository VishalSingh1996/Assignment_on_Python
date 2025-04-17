import psutil
import time

def monitor_cpu(threshold=80):# We can take 10 also or any lower number for testing
    print("Monitoring CPU usage...")
    try:
        while True:
            usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU usage: {usage}%")
            if usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {usage}%")
            time.sleep(1)  # Sleep for a second before checking again
    except KeyboardInterrupt:
        print("\nMonitoring stopped by you.")
    except Exception as e:
        print(f"An error occurred: {e}")

monitor_cpu(80)