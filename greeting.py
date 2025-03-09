import sys
import time

def send_greeting(recipient):
    """
    Send a greeting message using the MCP greeting protocol
    Format: greeting://{recipient}
    """
    greeting = f"Hello {recipient}! Greeting sent at {time.strftime('%Y-%m-%d %H:%M:%S')}"
    print(f"Sending greeting to {recipient}...")
    print(greeting)
    return greeting

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python greeting.py <recipient>")
        sys.exit(1)
    
    # Extract recipient from greeting://recipient format
    recipient = sys.argv[1].replace("greeting://", "")
    send_greeting(recipient)