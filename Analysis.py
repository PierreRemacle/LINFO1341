import pandas as pd
import glob

# Create a list of all CSV files in the current directory
csv_files = glob.glob('./ArchiveCSV/*.csv')

# Combine all CSV files into a single DataFrame
df = pd.concat([pd.read_csv(f) for f in csv_files])

# Calculate some statistics on the DataFrame
num_packets = len(df)
num_sources = len(df['Source'].unique())
num_destinations = len(df['Destination'].unique())
most_common_source = df['Source'].mode()[0]
most_common_destination = df['Destination'].mode()[0]

# Display the statistics
print("Number of packets:", num_packets)
print("Number of unique sources:", num_sources)
print("Number of unique destinations:", num_destinations)
print("Most common source:", most_common_source)
print("Most common destination:", most_common_destination)
