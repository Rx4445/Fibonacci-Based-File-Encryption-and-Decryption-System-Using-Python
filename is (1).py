# Function to generate Fibonacci sequence up to 'n' numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Function to encrypt the file using Fibonacci series
def encrypt_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            file_data = f.read()
        print(f"File read successfully, size: {len(file_data)} bytes")

        fib_sequence = fibonacci(len(file_data))
        encrypted_data = bytearray()

        # Encrypt each byte using Fibonacci sequence
        for i in range(len(file_data)):
            encrypted_byte = (file_data[i] + fib_sequence[i]) % 256  # Ensuring byte stays in valid range
            encrypted_data.append(encrypted_byte)

        # Write encrypted data to output file
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
        print(f"File encrypted successfully: {output_file}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

# Function to decrypt the file
def decrypt_file(encrypted_file, output_file):
    try:
        with open(encrypted_file, 'rb') as f:
            encrypted_data = f.read()
        print(f"Encrypted file read successfully, size: {len(encrypted_data)} bytes")

        fib_sequence = fibonacci(len(encrypted_data))
        decrypted_data = bytearray()

        # Decrypt each byte using Fibonacci sequence
        for i in range(len(encrypted_data)):
            decrypted_byte = (encrypted_data[i] - fib_sequence[i]) % 256  # Reverse the encryption process
            decrypted_data.append(decrypted_byte)

        # Write decrypted data to output file
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
        print(f"File decrypted successfully: {output_file}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# Example usage
input_file = 'C:/Users/studb/OneDrive/Desktop/v/example.txt.txt'
encrypted_file = 'C:/Users/studb/OneDrive/Desktop/encrypted_file.txt'
decrypted_file = 'C:/Users/studb/OneDrive/Desktop/decrypted_file.txt'

encrypt_file(input_file, encrypted_file)
decrypt_file(encrypted_file, decrypted_file)

