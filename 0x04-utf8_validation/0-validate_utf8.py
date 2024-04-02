#!/usr/bin/python3
"""UTF-8 Validation
"""

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each integer in the data list
    for byte in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading ones in the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # Validate the number of bytes in the UTF-8 character
            if num_bytes == 0:
                continue  # Single-byte character
            elif num_bytes == 1 or num_bytes > 4:
                return False  # Invalid number of bytes
        else:
            # Check if the byte is of the form 10xxxxxx
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False

        # Decrement the number of expected bytes for the current character
        num_bytes -= 1

    # If there are still bytes expected but the data has ended
    return num_bytes == 0


# Test cases
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
