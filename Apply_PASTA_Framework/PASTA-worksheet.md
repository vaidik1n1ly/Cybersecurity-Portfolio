# PASTA worksheet


<table>
<tr>
    <th>
        <h3>Stages</h3>
    </th>
    <th>
        <h3>Sneaker company</h3>
    </th>
</tr>
<tr>
    <th>
        <p>I. Define business and security objectives</p>
    </th>
    <td>
        <p>Make 2-3 notes of specific business requirements that will be analyzed.</p>
        <ul>
            <li>Users can create member profiles internally or by connecting external accounts.</li>
            <li>The app must process financial transactions.</li>
            <li>The app should be in compliance with PCI-DSS.</li>
        </ul>
    </td>
</tr>
<tr>
    <th>
        <p>II. Define the technical scope</p>
    </th>
    <td>
        <p>List of technologies used by the application:</p>
        <ul>
            <li>Users can create member profiles internally or by connecting external accounts.</li>
            <li>The app must process financial transactions.</li>
            <li>The app should be in compliance with PCI-DSS.</li>
        </ul>
        <p>APIs facilitate the exchange of data between customers, partners, and employees, so they should be prioritized. They handle a lot of sensitive data while they connect various users and systems together. However, details such as which APIs are being used should be considered before prioritizing one technology over another. So, they can be more prone to security vulnerabilities because there’s a larger attack surface.</p>
    </td>
</tr>
<tr>
    <th>
        <p>III. Decompose application</p>
    </th>
    <td>
        <a href="">Data flow diagram</a>
    </td>
</tr>
<tr>
    <th>
        <p>IV. Threat analysis</p>
    </th>
    <td>
        <p>List 2 types of threats in the PASTA worksheet that are risks to the information being handled by the application.</p>
        <ul>
            <li>Injection</li>
            <li>Session Hijacking</li>
        </ul>
    </td>
</tr>
<tr>
    <th>
        <p>V. Vulnerability analysis</p>
    </th>
    <td>
        <p>List 2 vulnerabilities in the PASTA worksheet that could be exploited.</p>
        <ul>
            <li>Lack of prepared statements</li>
            <li>Broken API token</li>
        </ul>
    </td>
</tr>
<tr>
    <th>
        <p>VI. Attack modeling</p>
    </th>
    <td>
        <a href="">Attack tree diagram</a>
    </td>
</tr>
<tr>
    <th>
        <p>VII. Risk analysis and impact</p>
    </th>
    <td>
        <p>List 4 security controls that can reduce risk.
        SHA-256, incident response procedures, password policy, principle of least privilege
        </p>
    </td>
</tr>
</table>