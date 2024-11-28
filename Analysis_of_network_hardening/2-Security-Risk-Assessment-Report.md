# Security Risk Assessment Report

### Part 1: Select up to three hardening tools and methods to implement

Some of the hardening tools the organization can use to address the major vulnerabilities found include:
1. **Implement multi-factor authentication (MFA)**
: MFA is a security mechanism that requires users to verify their identity in more than one way. MFA includes multiple independent factors such as password,
PIN, security question, authenticator app, token generator, fingerprint, facial recognition, retina scan, etc.
3. **Enforcing strong password policies**
: Strong password policies can be established to include rules regarding minimum password length, complexity requirements, prohibit the reuse of passwords, and password expiration.
They can also include rules like locking accounts temporarily after a certain number of unsuccessful login attempts.
4. **Updating firewall configuration regularly**
: Updating firewall configurations regularly ensures that the network remains secure, adaptable, and compliant. As threats evolve and organizational needs change,
firewall configurations must be consistently updated to remain effective.


### Part 2: Explain your recommendations

MFA significantly enhances security by reducing reliance on a single point of failure (like a password). By requiring multiple forms of verification, 
MFA makes it highly unlikely for attackers to access accounts, even if one factor (e.g., a password) is compromised. MFA may also reduce the likelihood of 
password sharing as to access a network, one would require to possess additional authentication besides a password.

Weak or reused passwords are among the most common vulnerabilities exploited by attackers. Establishing and enforcing a password policy in an organization 
helps mitigate this risk. Complexity requirements make passwords harder to guess, while expiration rules ensure that compromised passwords are replaced before 
they can be used maliciously. Lockout policies prevent brute force attacks by temporarily disabling accounts after multiple failed login attempts, further strengthening security.

Firewalls serve as a critical barrier between internal systems and external threats, but outdated configurations can leave vulnerabilities exposed. 
Regular updates ensure that the firewall blocks known malicious IPs and adapts to organizational changes, such as new servers or applications. 
For example, removing redundant or conflicting rules improves firewall efficiency and reduces the likelihood of security gaps. 
This proactive measure supports compliance with regulatory standards and helps address evolving threats. 
