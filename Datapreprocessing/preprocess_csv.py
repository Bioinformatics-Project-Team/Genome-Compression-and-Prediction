import csv
import sys

def process_csv_sequences(input_csv, output_csv):
    """
    Converts sequences from an input CSV file into a comma-separated format where each character is separated by commas.
    Outputs the results into another CSV file and prints the length of each processed line.

    Args:
        input_csv (str): Path to the input CSV file.
        output_csv (str): Path to the output CSV file.
    """
    # Increase the CSV field size limit
    csv.field_size_limit(sys.maxsize)

    with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        # Skip the header in the input file
        next(csv_reader)

        for row in csv_reader:
            sequence_id, sequence = row
            # Convert sequence to uppercase and split it into characters
            processed_sequence = list(sequence.upper())
            # Write the processed sequence to the output CSV
            csv_writer.writerow(processed_sequence)
            # Print the length of the processed sequence
            print(f"Length of {sequence_id}: {len(processed_sequence)}")

# Example usage
input_csv_path = ".//processed_data//output_sequences.csv"  # Replace with your input CSV file path
output_csv_path = ".//processed_data//final_sequences.csv"  # Replace with your desired output CSV file path
process_csv_sequences(input_csv_path, output_csv_path)