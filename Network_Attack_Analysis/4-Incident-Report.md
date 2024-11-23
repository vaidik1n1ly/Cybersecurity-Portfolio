# Cybersecurity Incident Report: Network Attack Analysis

### Section 1: Identify the type of attack that may have caused this network interruption

One potential explanation for the website's connection timeout error message is a direct Denial Of Service (DoS) attack due to which, the web server is overwhelmed with SYN requests and is unable to respond the requests. 
The logs show that multiple SYN packet requests are coming from a single ip address and the web server stops responding. This event could be a Denial of Service (DoS) attack known as SYN flood attack.


### Section 2: Explain how the attack is causing the website to malfunction 

When website visitors try to establish a connection with the web server, a three-way handshake occurs using the TCP protocol. The three steps of the handshake are: 
1. Initially, a SYN packet is sent from client pc to the web server requesting to establish a connection. SYN stands for “synchronize”.
2. Then server responds back with SYN, ACK packet to the client’s request agreeing to establish the connection. The web server will reserve resources for client to connect. SYN, ACK stands for “synchronize acknowledge.”
3. Finally, client pc sends ACK packet to the web server acknowledging the permission to connect. ACK stands for “acknowledge.”
The TCP connection is now established.

In the case of SYN flood attack, a malicious attacker sends a large number of SYN packets in a rapid pace,  causing  the number of SYN requests is greater than the server resources available to handle the requests, then the server will become overwhelmed and unable to respond to the legitimate TCP connection  requests.

The logs indicate that the web server has become overwhelmed and is unable to process the visitors’ SYN requests causing visitors to receive a connection timeout error message.
