from scapy.all import *
import pandas as pd
import os

def pcapng_to_csv(filename):
    # Open the pcapng capture file
    pkts = rdpcap(filename)

    # Extract the desired packet fields and store them in a list
    rows = []
    for pkt in pkts:
        row = {}
        if 'IP' in pkt:
            row['Source'] = pkt['IP'].src
            row['Destination'] = pkt['IP'].dst
        if 'TCP' in pkt:
            row['Source Port'] = pkt['TCP'].sport
            row['Destination Port'] = pkt['TCP'].dport
        rows.append(row)

    # Write the extracted data to a CSV file
    df = pd.DataFrame(rows)
    csv_filename = os.path.splitext(filename)[0] + '.csv'
    df.to_csv(csv_filename, index=False)

folder_path = './Archive (1)'
for filename in os.listdir(folder_path):
    if filename.endswith('.pcapng'):
        full_path = os.path.join(folder_path, filename)
        pcapng_to_csv(full_path)
