# Cybersecurity Incident Report: Network Traffic Analysis

| Part 1: Provide a summary of the problem found in the DNS and ICMP traffic log. |
| :--- |
| The network protocol analyzer logs indicate; first the UDP packets is sent from local computer to DNS server requesting to resolve IP address for the domain name of www.yummyrecipesforme.com, which is responded with ICMP packets showing error message “upd port 53 unreachable”. Since port 53 is used for DNS protocol, this is an issue with the DNS server. Issues with DNS service is further supported by presence of ‘A?’ flag symbol related to DNS protocol which is used while finding A records. It is possible that this is an indication that DNS server is down or there is a malicious attack on the DNS server. |


| Part 2: Explain your analysis of the data and provide at least one cause of the incident. |
| :--- |
| The incident occured today at 1:24 p.m. Several customers of clients reported that they were not able to access the client company website www.yummyrecipesforme.com along with “destination port unreachable” error being displayed in the web browser while loading the page. The network security team responded and began tests with the network protocol analyzer tool tcpdump. The resulting logs revealed that the UDP packets sent for DNS resolution were being responded with ICMP packets showing “udp port 53 unreachable” error. The port 53, which is used for DNS service, is not reachable on DNS server. We are continuing to investigate the root cause of the issue to determine how we can restore access to the wepage. Our next steps include checking whether the DNS server is down or if traffic to port 53 is blocked by firewall. The DNS server might be down because of misconfiguration or a DoS attack, for which we have to check the system for signs of an attack. |
