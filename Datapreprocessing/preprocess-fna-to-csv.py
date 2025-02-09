from Bio import SeqIO
import csv

def convert_fna_to_csv(fna_file, csv_file):
    """
    Reads an FNA file and writes each sequence to a CSV file.
    
    Args:
        fna_file (str): Path to the input FNA file.
        csv_file (str): Path to the output CSV file.
    """
    with open(csv_file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header row
        csv_writer.writerow(["ID", "Sequence"])
        
        # Parse the FNA file
        for record in SeqIO.parse(fna_file, "fasta"):
            csv_writer.writerow([record.id, str(record.seq)])
    
    print(f"Sequences have been written to {csv_file}")

# Example usage
fna_file_path = ".//IBS dataset//ncbi_dataset//data//GCA_000001405.29//GCA_000001405.29_GRCh38.p14_genomic.fna"  # Replace with the path to your .fna file
csv_file_path = ".//processed_data//output_sequences.csv"  # Desired output CSV file path
convert_fna_to_csv(fna_file_path, csv_file_path)

