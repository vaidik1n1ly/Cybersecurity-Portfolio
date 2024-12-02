![Incident report analysis](img/ira.png)

# Incident report analysis

<table>
  <tr>
    <td>Summary</td>
    <td>The company recently experienced a security incident where company’s network services suddenly stopped responding. Upon investigating the security event, the cybersecurity team found that there was a distributed denial of service (DDoS) attack using ICMP packets flooding by exploiting an unconfigured firewall. The incident management team responded by blocking the incoming ICMP traffic and stopping non-critical services inorder to restore the critical network services.</td>
  </tr>
  <tr>
    <td>Identify</td>
    <td>A malicious actor had sent a flood of ICMP packets targeting the company’s network. The entire internal network was affected by the attack. All critical network services needed to be secured and restored to its normal state.</td>
  </tr>
  <tr>
    <td>Protect</td>
    <td>The cybersecurity team implemented a new firewall rule to limit the rate of incoming ICMP packets and an IDS/IPS system to filter out some ICMP traffic based on suspicious characteristics.</td>
  </tr>
  <tr>
    <td>Detect</td>
    <td>The cybersecurity team configured source IP address verification on the firewall to check for spoofed IP addresses on incoming ICMP packets. The team also implemented network monitoring software to detect abnormal traffic patterns.</td>
  </tr>
  <tr>
    <td>Respond</td>
    <td>For future cybersecurity incidents, the cybersecurity team will contain the cybersecurity incidents by isolating the compromised systems and disabling affected services to prevent further propagation. They will try to restore the critical systems and services. Then, they will analyze network logs to check abnormal activities. The team will also report all incidents to higher management and legal authorities.</td>
  </tr>
  <tr>
    <td>Recover</td>
    <td>To assist the company in recovering from a DDoS attack by ICMP flooding, access to all the network services need to be restored to a normal functioning state. All incoming ICMP packets will be blocked by properly configured firewall. Then, the non-critical services should be stopped to reduce internal traffic. Then, critical services should be restored first. After the ICMP flood is gone, all systems and services can be brought back online.</td>
  </tr>
</table>

<table>
  <tr>
    <td  rowspan="1">
      Reflections/Notes:
      <ul>
        <li>Regularly test incident response and recovery plans to ensure preparedness.</li>
        <li>Audit firewall rules and network configurations periodically to identify vulnerabilities.</li>
      </ul>
    </td>
  </tr>
</table>
