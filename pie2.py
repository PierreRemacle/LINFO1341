import pyshark
import matplotlib.pyplot as plt

# Read in the Wireshark file
cap = pyshark.FileCapture('./Archive (1)/testpierre@.pcapng')

# Initialize empty dictionaries to store the counts of domain and IP addresses
domain_counts = {}
ip_counts = {}

# Iterate through each packet in the capture
for pkt in cap :
    # Check if the packet contains a DNS layer and a DNS query
    if 'DNS' in pkt and pkt.dns.qry_name not in ["lb._dns-sd._udp.0.1.168.192.in-addr.arpa" , "lb._dns-sd._udp.home" , "db._dns-sd._udp.home" , "b._dns-sd._udp.home" , "db._dns-sd._udp.0.1.168.192.in-addr.arpa" , "b._dns-sd._udp.0.1.168.192.in-addr.arpa" , "bag.itunes.apple.com" , "e673.dsce9.akamaiedge.net" , "caldav.fe.apple-dns.net" , "p66-caldav.icloud.com","pki-goog.l.google.com","ocsp.pki.goog","ocsp2.globalsign.com","cdn.globalsigncdn.com.cdn.cloudflare.net","guzzoni-apple-com.v.aaplimg.com","guzzoni.apple.com","outlook.ha.office365.com","contacts.fe.apple-dns.net","p66-contacts.icloud.com","contacts.fe.apple-dns.net","CDG-efz.ms-acdc.office.com","outlook.ha.office365.com","outlook.office365.com","i.scdn.co","dealer.spotify.com","api.spotify.com","gs.apple.com.v.aaplimg.com","us-sandbox-courier-4.push-apple.com.akadns.net","eu-nw-courier-4.push-apple.com.akadns.net","api.apple-cloudkit.fe.apple-dns.net","gateway.icloud.com","www.apple.com","gateway.icloud.com","gs.apple.com","notify.bugsnag.com","1-courier.sandbox.push.apple.com","1-courier.push.apple.com","api.apple-cloudkit.com","gateway.icloud.com","www.apple.com","gs.apple.com","7.1.168.192.in-addr.arpa","_dns.resolver.arpa"]  :
        # Extract the domain name and IP address from the DNS query
        domain = pkt.dns.qry_name
        ip ="fart"
        
        print(domain)
        # Increment the count for the domain name and IP address
        domain_counts[domain] = domain_counts.get(domain, 0) + 1
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

# Create the nested pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(list(domain_counts.values()), labels=list(domain_counts.keys()), radius=0.5,
       wedgeprops=dict(width=0.3, edgecolor='w'))
# Add a title

# Show the chart
plt.show()
