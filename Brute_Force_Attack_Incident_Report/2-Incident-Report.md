# Security Incident Report


### Section 1: Identify the network protocol involved in the incident

The network protocol involved in the incident are the DNS (Domain Name System) protocol, used to translate domain names into IP addresses and facilitate network request resolution, 
and  the HTTP (Hypertext Transfer Protocol), used for access and data transfer on the web.  The issue was with accessing the webpage for www.yummyrecipesforme.com using the http protocol. 
Also, as we looked into the tcpdump log file, the usage of http protocol was observed at the application layer while downloading the malicious file to users’ computers.


### Section 2: Document the incident

Multiple customers reported the website’s helpdesk stating that when they accessed the website www.yummyrecipesforme.com, they were prompted to download 
and run a file that contained free recipes. They complained about their computers have been performing slowly ever since. The website owner tried logging 
into the admin panel but were locked out of their account.

The cybersecurity team responded and created a sandbox environment to test the website behabiour. The analyst then ran tcpdump to capture network traffic 
packets being transferred while accessing the website. As claimed by customers, the analyst was prompted to download a file inorder to access free recipes, 
accepted the download and ran it. The browser then redirected to a fake website (www.greatrecipesforme.com).

The cybersecurity analyst discovered unusual activity in a tcpdump log, indicating that a browser initially accessed yummyrecipesforme.com. After the connection 
was established using the HTTP protocol, the analyst recalled downloading and running a file from the site. Shortly after, the logs revealed a sudden change in 
network behavior as the browser redirected to greatrecipesforme.com, requesting a new IP address and rerouting all traffic to this secondary site.

Upon reviewing the websites’ source code and the downloaded file, the senior cybersecurity professional found evidence of an attacker injecting malicious code 
into yummyrecipesforme.com. This code tricked users into downloading a harmful file masked as a browser update. The website owner reported being locked out of 
their admin account, leading the team to conclude that the attacker likely used a brute force attack to take control and reset the password. Once executed, 
the malicious file compromised the users' devices, exposing their systems to the attacker.

### Section 3: Recommend one remediation for brute force attacks

To enhance security and defend against brute force attacks, the team plans to enforce several protective measures. One key strategy is to prohibit the reuse of 
old passwords, including default ones, to ensure attackers cannot exploit previous credentials during password resets. Additionally, limiting the number of login 
attempts and more frequent password updates will reduce the window of opportunity for unauthorized access by ensuring compromised passwords are rendered useless sooner.

Another layer of protection will be added with the implementation of multi-factor authentication (MFA) or two-factor authentication (2FA). This method combines a 
traditional password with a one-time passcode (OTP) sent to the user’s phone or email. By requiring verification through both credentials and the OTP, unauthorized 
access becomes significantly more challenging, even for attackers attempting brute force methods. These measures collectively strengthen the system’s resilience to such vulnerabilities.
