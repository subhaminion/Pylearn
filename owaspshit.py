# -*- coding: utf-8 -*-

import json

owasp_2016 = {
    'A1': {
        'title': 'Injection',
        'desc': """Injection flaws, such as SQL, OS, and LDAP injection occur when untrusted
data is sent to an interpreter as part of a command or query.
The attacker’s hostile data can trick the interpreter into executing unintended
commands or accessing data without proper authorization."""
    },
    'A2': {
        'title': 'Broken Authentication and Session Management',
        'desc': """
Application functions related to authentication and session management are
often not implemented correctly, allowing attackers to compromise
passwords, keys, or session tokens, or to exploit other implementation
flaws to assume other users’ identities.
        """
    },
    'A3': {
        'title': 'Cross-Site Scripting',
        'desc': """
XSS flaws occur whenever an application takes untrusted data and
sends it to a web browser without proper validation or escaping.
XSS allows attackers to execute scripts in the victim’s browser
which can hijack user sessions, deface web sites,
or redirect the user to malicious sites.
        """
    },
    'A4': {
        'title': 'Insecure Direct Object References',
        'desc': """
A direct object reference occurs when a developer exposes
a reference to an internal implementation object,
such as a file, directory, or database key.
Without an access control check or other protection,
attackers can manipulate these references to access unauthorized data.
        """
    },
    'A5': {
        'title': 'Security Misconfiguration',
        'desc': """
Good security requires having a secure configuration defined and deployed
for the application, frameworks, application server, web server, database
server, and platform. Secure settings should be defined, implemented,
and maintained, as defaults are often insecure.
Additionally, software should be kept up to date.
        """
    },
    'A6': {
        'title': 'Sensitive Data Exposure',
        'desc': """
Many web applications do not properly protect sensitive data,
such as credit cards, tax IDs, and authentication credentials.
Attackers may steal or modify such weakly protected data to conduct
credit card fraud, identity theft, or other crimes.
Sensitive data deserves extra protection such as encryption
at rest or in transit, as well as special precautions when
exchanged with the browser.
        """
    },
    'A7': {
        'title': 'Missing Fucntion Level Access Control',
        'desc': """
Most web applications verify function level access rights before making that
functionality visible in the UI.
However, applications need to perform the same access control checks on
the server when each function is accessed.
If requests are not verified, attackers will be able to forge requests
in order to access functionality without proper
authorization.
        """
    },
    'A8': {
        'title': 'Cross-Site Request Forgery(CSRF)',
        'desc': """
A CSRF attack forces a logged-on victim’s browser to send a
forged HTTP request, including the victim’s session cookie and any other
automatically included authentication information, to a vulnerable
web application.
This allows the attacker to force the victim’s browser to generate
requests the vulnerable application thinks are legitimate requests
from the victim.
        """
    },
    'A9': {
        'title': 'Using Components with known Vulnerability',
        'desc': """
Components, such as libraries, frameworks, and other software modules,
almost always run with full privileges. If a vulnerable component is exploited,
such an attack can facilitate serious data loss or server takeover.
Applications using components with known vulnerabilities may undermine
application defenses and enable a range of possible attacks and impacts.
        """
    },
    'A10': {
        'title': 'Unvalidated Redirect and Forwards',
        'desc': """
Web applications frequently redirect and forward users to
other pages and websites, and use untrusted data to determine the
destination pages. Without proper validation,
attackers can redirect victims to phishing or malware sites,
or use forwards to access unauthorized pages.
        """
    },
    'M1': {
        'title': 'Improper Platform Usage',
        'desc': """
This category covers misuse of a platform feature or failure to use
platform security controls.
It might include Android intents, platform permissions, misuse of TouchID,
the Keychain,
or some other security control that is part of the mobile operating system.
There are several ways that mobile apps can experience this risk.
        """
    },
    'M2': {
        'title': 'Insecure Data Storage',
        'desc': """
This new category is a combination of M2 + M4 from Mobile Top Ten 2014.
This covers insecure data storage and unintended data leakage.
        """
    },
    'M3': {
        'title': 'Insecure Communication',
        'desc': """
This covers poor handshaking, incorrect SSL versions, weak negotiation,
cleartext communication of sensitive assets, etc.
        """
    },
    'M4': {
        'title': 'Insecure Authentication',
        'desc': """
This category captures notions of authenticating the
end user or bad session management.
This can include:
*   Failing to identify the user at all when that should be required
*   Failure to maintain the user\'s identity when it is required
*   Weaknesses in session management
        """
    },
    'M5': {
        'title': 'Insufficient Cryptography',
        'desc': """
The code applies cryptography to a sensitive information asset.
However, the cryptography is insufficient in some way.
Note that anything and everything related to TLS or SSL goes in M3.
Also, if the app fails to use cryptography at all when it should,
that probably belongs in M2.
This category is for issues where cryptography was attempted,
but it wasn\'t done correctly.
        """
    },
    'M6': {
        'title': 'Insecure Authorization',
        'desc': """
This is a category to capture any failures in authorization
(e.g., authorization decisions in the client side, forced browsing, etc.).
It is distinct from authentication
issues(e.g., device enrolment, user identification, etc.).
If the app does not authenticate users at all in a situation where it should
(e.g., granting anonymous access to some resource or service when authenticated
and authorized access is required), then that is an authentication
failure not an authorization failure.
        """
    },
    'M7': {
        'title': 'Client Code Quality',
        'desc': """
This was the "Security Decisions Via Untrusted Inputs", one of our lesser-used
categories.
This would be the catch-all for code-level implementation problems
in the mobile client.
That\'s distinct from server-side coding mistakes. This would capture things
like buffer overflows, format string vulnerabilities,
and various other code-level mistakes where the
solution is to rewrite some code that\'s
running on the mobile device.
        """
    },
    'M8': {
        'title': 'Code Tampering',
        'desc': """
This category covers binary patching, local resource modification, method
hooking, method swizzling,
and dynamic memory modification.Once the application is delivered to the
mobile device,
the code and data resources are resident there.
An attacker can either directly modify the code, change the contents of
memory dynamically,
change or replace the system APIs that the application uses, or modify
the application\'s data and resources.
This can provide the attacker a direct method of subverting the intended
use of the software for personal or monetary gain.
        """
    },
    'M9': {
        'title': 'Reverse Engineer',
        'desc': """
This category includes analysis of the final core binary to determine its
source code, libraries, algorithms, and other assets.
Software such as IDA Pro, Hopper, otool, and other binary inspection tools
give the attacker insight into the inner
workings of the application. This may be used to exploit other nascent
vulnerabilities in the application,
as well as revealing information about back end servers, cryptographic
constants and ciphers, and intellectual property.
        """
    },
    'M10': {
        'title': 'Extraneous Fucntionality',
        'desc': """
Often, developers include hidden backdoor functionality or other internal
development security controls that are not intended to be released into a
production environment. For example, a developer may accidentally include
a password as a comment in a hybrid app. Another example includes disabling
of 2-factor authentication during testing.
        """
    }
}

print(owasp_2016.get('M2'))
