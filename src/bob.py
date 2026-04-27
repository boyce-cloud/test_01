"""
Bob API Module

This module provides API functionality for the Bob agent.
"""

def hello_bob():
    """Return a greeting from Bob."""
    return "Hello from Bob API!"

def process_request(data):
    """Process an incoming request."""
    return {"status": "processed", "data": data}

if __name__ == "__main__":
    print(hello_bob())
