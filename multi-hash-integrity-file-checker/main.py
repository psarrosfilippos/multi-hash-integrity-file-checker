# PSARROS FILIPPOS 2628

import hashlib
import os

# MD5 calculation
def calculate_md5(file_data):
    return hashlib.md5(file_data).hexdigest()

# SHA-1 calculation
def calculate_sha1(file_data):
    return hashlib.sha1(file_data).hexdigest()

# SHA-256 calculation
def calculate_sha256(file_data):
    return hashlib.sha256(file_data).hexdigest()

# SHA3-256 (Keccak) calculation
def calculate_keccak(file_data):
    return hashlib.sha3_256(file_data).hexdigest()

# Calculates all hashes for a file and returns them as a dictionary
def calculate_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
    except Exception as e:
        print(f"Error while opening file {file_path}: {e}")
        return {}

    hash_functions = {
        "MD5": calculate_md5,
        "SHA-1": calculate_sha1,
        "SHA-256": calculate_sha256,
        "Keccak": calculate_keccak
    }

    return {name: func(file_data) for name, func in hash_functions.items()}

# Saves hash values to a text file
def save_hash_to_file(hash_values, output_path):
    try:
        with open(output_path, 'w') as f:
            for algo, h in hash_values.items():
                f.write(f"{algo}: {h}\n")
        print(f"Hash values saved to file: {output_path}")
    except Exception as e:
        print(f"Failed to save hash values: {e}")

# Verifies integrity when the hashes are the same
def verify_integrity_same(reference_hash, file_paths):
    for file_path in file_paths:
        current_hash = calculate_hash(file_path)
        if current_hash == reference_hash:
            print(f"[{file_path}]: The file is intact.")
        else:
            print(f"[{file_path}]: The file has been modified!")

# Verifies integrity when the files have different hashes
def verify_integrity_different(expected_hash, file_path):
    current_hash = calculate_hash(file_path)
    if current_hash == expected_hash:
        print(f"[{file_path}]: The file is intact.")
    else:
        print(f"[{file_path}]: The file has been modified!")

# Main function
def main():
    file_paths = []

    print("Enter two files to compare their hashes:")

    while len(file_paths) < 2:
        file_name = input(f"File {len(file_paths) + 1}: ").strip()
        if os.path.isfile(file_name):
            file_paths.append(file_name)
        else:
            print("File not found. Try again.")

    # Calculate hashes for both files
    hash_list = [calculate_hash(fp) for fp in file_paths]

    if not all(hash_list):
        print("An error occurred while calculating hashes.")
        return

    if hash_list[0] == hash_list[1]:
        print("\nThe files have identical hashes (likely identical content).")
        for algo, h in hash_list[0].items():
            print(f"{algo}: {h}")
        output_file = input("\nEnter filename to save the hash values: ").strip()
        save_hash_to_file(hash_list[0], output_file)
        verify_integrity_same(hash_list[0], file_paths)
    else:
        print("\nThe files have different hashes.")
        for i, fp in enumerate(file_paths):
            print(f"\nResults for file {fp}:")
            for algo, h in hash_list[i].items():
                print(f"{algo}: {h}")
            output_file = input(f"Enter filename to save hash values for {fp}: ").strip()
            save_hash_to_file(hash_list[i], output_file)
            verify_integrity_different(hash_list[i], fp)

if __name__ == "__main__":
    main()
