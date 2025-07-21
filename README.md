# Multi-Hash File Integrity Checker

This project is a Python tool for verifying the integrity of files using cryptographic hash functions (MD5, SHA-1, SHA-256, and SHA3-256).  
It allows users to compare two files and check whether they are identical or have been modified, based on their computed hash values.  
Hash results can be saved for future integrity checks.

The tool was developed as part of a university assignment in informatics and telecommunications, with a focus on cybersecurity and digital forensics principles.







## Acknowledgements

This tool was created as part of my coursework in informatics and telecommunications, focusing on file integrity and cryptographic hash functions.  
It reflects practical skills developed during academic training.


## Features

- Computes file hashes using four different algorithms
- Compares hash values between two files
- Detects file tampering or corruption
- Saves hashes to text files for audit trails or verification
- Modular and ready for extension

## How to use

**1. Run the script:**

    python main.py

**2. Enter the names of two files when prompted:**

Example: original.txt and copy.txt

**3. The program will:**

Calculate the MD5, SHA-1, SHA-256, and SHA3-256 hashes for each file.

Compare the hash values to determine if the files are identical.

Print the results.

Ask if you want to save the hashes to a file.


## Examples

Enter file 1: original.txt
Enter file 2: copy.txt

    Files have identical hash values.

    MD5:     5d41402abc4b2a76b9719d911017c592
    SHA-1:   aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
    SHA-256: 2c26b46b68ffc68ff99b453c1d30413413422
    Keccak:  4e07408562bedb8b60ce05c1decfe3ad16b72230959eea17bcd3dd316abe03e3

    Hashes saved to: output_hashes.txt
## Authors

Filippos Psarros

informatics and telecommunications Student

GitHub: psarrosfilippos

[README.md](https://github.com/user-attachments/files/21339610/README.md)
