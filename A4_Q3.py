import numpy as np
from collections import Counter

# Function to count the frequency of each base (A, T, C, G)
def count_bases(dna_sequence):
    counts = Counter(dna_sequence)
    return dict(counts)

# Function to find the most common base
def find_most_common_base(dna_sequence):
    counts = Counter(dna_sequence)
    most_common = counts.most_common(1)[0]
    return most_common

# Function to find sequences longer than a specified threshold
def find_long_sequences(dna_sequence, threshold):
    current_sequence = []
    long_sequences = []
    for base in dna_sequence:
        if base in ['A', 'T', 'C', 'G']:  # Only count valid bases
            current_sequence.append(base)
        else:
            if len(current_sequence) > threshold:
                long_sequences.append(''.join(current_sequence))
            current_sequence = []

    if len(current_sequence) > threshold:  # For the last sequence
        long_sequences.append(''.join(current_sequence))

    return long_sequences

# Function to reverse the DNA sequence
def reverse_sequence(dna_sequence):
    return dna_sequence[::-1]

# Function to get the DNA sequence input from the user
def get_dna_input():
    dna_sequence = input("Enter the DNA sequence (A, T, C, G): ").upper()
    return np.array(list(dna_sequence))

def main():
    while True:
        print("\nChoose an option:")
        print("1. Count the frequency of each base")
        print("2. Find the most common base")
        print("3. Find base pair sequences longer than a specified threshold")
        print("4. Reverse the entire DNA sequence")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            dna_sequence = get_dna_input()

            if choice == 1:
                counts = count_bases(dna_sequence)
                print("Base counts:", counts)

            elif choice == 2:
                most_common = find_most_common_base(dna_sequence)
                print(f"The most common base is '{most_common[0]}' with {most_common[1]} occurrences.")

            elif choice == 3:
                try:
                    threshold = int(input("Enter the sequence length threshold: "))
                except ValueError:
                    print("Invalid threshold! Please enter an integer.")
                    continue

                long_sequences = find_long_sequences(dna_sequence, threshold)
                if long_sequences:
                    print(f"Sequences longer than {threshold}:", long_sequences)
                else:
                    print(f"No sequences longer than {threshold} found.")

            elif choice == 4:
                reversed_sequence = reverse_sequence(dna_sequence)
                print("Reversed DNA sequence:", ''.join(reversed_sequence))

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
