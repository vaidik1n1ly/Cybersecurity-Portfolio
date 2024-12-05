# Network Hardening Tools

<table>
  <tbody>
    <tr style="height: 20px">
      <th id="0R0" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">1</div></th>
      <td class="s0" dir="ltr">Security hardening task</td><td class="s0" dir="ltr">Description</td><td class="s0" dir="ltr">Common uses</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R1" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">2</div></th>
      <td class="s1" dir="ltr">Baseline configurations</td><td class="s2" dir="ltr">A documented set of specifications within a system that is used as a basis for future builds, releases, and updates.</td>
      <td class="s2" dir="ltr">To restore a system to a previous baseline after a network outage, or unauthorized changes on a baseline.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R2" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">3</div></th>
      <td class="s1" dir="ltr">Configuration checks</td><td class="s2" dir="ltr">Updating the encryption standards for data that is stored in databases.</td>
      <td class="s2" dir="ltr">To see if there are any unauthorized changes to the system.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R3" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">4</div></th>
      <td class="s1" dir="ltr">Disabling unused ports</td><td class="s2" dir="ltr">Ports can be blocked on firewalls, routers, servers, and more to prevent potentially dangerous network traffic from passing through.</td>
      <td class="s2" dir="ltr">Before an incident occurs, to prevent malicious actors from entering the network through the open port. Can be used after an incident to prevent future attacks from happening through unused open ports.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R4" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">5</div></th>
      <td class="s1" dir="ltr">Encryption using the latest standards</td><td class="s2" dir="ltr">Rules or methods used to conceal outgoing data and uncover or decrypt the incoming data.</td>
      <td class="s2" dir="ltr">Can be implemented regularly to assess if the current encryption standards are secure and effective for your organization. The encryption standards can also be updated after a data breach.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R5" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">6</div></th>
      <td class="s1" dir="ltr">Firewall maintenance</td><td class="s2" dir="ltr">Firewall maintenance entails checking and updating security configurations regularly to stay ahead of potential threats.</td>
      <td class="s2" dir="ltr">This can happen regularly. Firewall rules can be updated in response to an event that allows abnormal network traffic into the network. This measure can be used to protect against various DDoS attacks.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R6" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">7</div></th>
      <td class="s1" dir="ltr">Hardware &amp; software disposal</td><td class="s2" dir="ltr">Ensures that all old hardware is properly wiped of all data and disposed of.</td>
      <td class="s2" dir="ltr">Prevent the network from various threats by removing outdated or unused software or hardware that do not have the latest security patches or updates. Unpatched devices can allow malicious actors to easily access the network.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R7" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">8</div></th>
      <td class="s1" dir="ltr">Multifactor authentication (MFA)</td>
      <td class="s2" dir="ltr">A security measure which requires a user to verify their identity in two or more ways to access a system or network. MFA options include a password, pin number, badge, one-time password (OTP) sent to a cell phone, fingerprint, and more.</td>
      <td class="s2" dir="ltr">Can help protect against brute force attacks and similar security events. MFA can be implemented at any time, and is mostly a technique that is set up once then maintained.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R8" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">9</div></th>
      <td class="s1" dir="ltr">Network access privileges</td><td class="s2" dir="ltr">Network access privileges involves permitting, limiting, and/or blocking access privileges to network assets for people, roles, groups, IP addresses, MAC addresses, etc. </td>
      <td class="s2" dir="ltr">Reduces the risk of unauthorized users and outside traffic from accessing the internal network. This can be implemented once, or revisited depending on the likelihood of social engineering or brute force attacks. </td>
    </tr>
    <tr style="height: 20px">
      <th id="0R9" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">10</div></th>
      <td class="s1" dir="ltr">Network log analysis</td><td class="s2" dir="ltr">The process of examining network logs to identify events of interest.</td>
      <td class="s2" dir="ltr">Can be configured to alert the security team when there is abnormal traffic on the network. This can be used either before an incident occurs, during to track network traffic, and can be configured in the response of a cybersecurity attack. A common tool used for analyzing network logs is a SIEM.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R10" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">11</div></th>
      <td class="s1" dir="ltr">Password policies</td><td class="s2" dir="ltr">The National Institute of Standards and Technology's (NIST) latest recommendations for password policies focuses on using methods to salt and hash passwords, rather than requiring overly complex passwords or enforcing frequent changes to passwords.</td>
      <td class="s2" dir="ltr">Password policies are used to prevent attackers from easily guessing user passwords, either manually or by using a script to attempt thousands of stolen passwords (commonly called a brute force attack).</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R11" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">12</div></th>
      <td class="s1" dir="ltr">Patch updates</td><td class="s2" dir="ltr">A software and operating system (OS) update that addresses security vulnerabilities within a program or product.</td>
      <td class="s2" dir="ltr">Patch updates often contain fixes to security problems. It is important to keep systems up to date with the latest security patches because attackers will be alerted to the security vulnerability when patches are released. They will be more likely to target that vulnerability before people eventually apply the patches.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R12" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">13</div></th>
      <td class="s1" dir="ltr">Penetration test (pen test)</td><td class="s2" dir="ltr">A simulated attack that helps identify vulnerabilities in systems, networks, websites, applications, and processes.</td>
      <td class="s2" dir="ltr">Pen tests are used to protect and prevent against potential attacks.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R13" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">14</div></th>
      <td class="s1" dir="ltr">Port filtering</td><td class="s2" dir="ltr">A firewall function that blocks or allows certain port numbers to limit unwanted communication.</td>
      <td class="s2" dir="ltr">Port filtering is used to control network traffic and can prevent potential attackers from entering a private network.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R14" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">15</div></th>
      <td class="s2" dir="ltr">Removing or disabling unused applications and services</td>
      <td class="s2" dir="ltr">Unused applications and services can become a point of vulnerability because they are less likely to be maintained or updated with new security features. </td>
      <td class="s2" dir="ltr">This procedure is used to reduce potential vulnerabilities within a network.</td>
    </tr>
    <tr style="height: 20px">
      <th id="0R15" style="height: 20px;" class="row-headers-background"><div class="row-header-wrapper" style="line-height: 20px">16</div></th>
      <td class="s1" dir="ltr">Server and data storage backups</td><td class="s2" dir="ltr">Server and data storage backups help protect data assets from being lost. Backups can be recorded and stored in a physical location or uploaded/synced to a cloud repository. </td>
      <td class="s2" dir="ltr">Backups are used to restore lost data from attacks, human error, equipment failures, and other unplanned losses.</td>
    </tr>
  </tbody>
</table>
