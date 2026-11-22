# A2 – Follow the Application Protocols (5 marks)

## A2.1 SMTP command sequence
Example client/server dialogue:
```text
S: 220 mail.example.edu ESMTP ready
C: EHLO student.example.edu
S: 250-mail.example.edu
S: 250-STARTTLS
S: 250 AUTH
C: MAIL FROM:<student@example.edu>
S: 250 2.1.0 Sender OK
C: RCPT TO:<teacher@example.edu>
S: 250 2.1.5 Recipient OK
C: DATA
S: 354 End data with <CRLF>.<CRLF>
C: Subject: Assignment
C:
C: Please find the assignment attached.
C: .
S: 250 2.0.0 Message accepted
C: QUIT
S: 221 2.0.0 Bye
```
POP3 with “delete after download” removes the message from the server after one device retrieves it. A phone may download and delete it, leaving the laptop and lab PC without the message; read/unread and folders are not synchronised. IMAP keeps messages on the server and synchronises folders, flags and read state across devices. Webmail also keeps the mailbox centrally and uses HTTPS.

## A2.2 FTP, SFTP and SNMP
Active FTP: client opens control TCP/21 and tells server which client port to connect to for data; the server initiates the data connection back to the client. A client-side firewall/NAT commonly blocks this inbound connection. Passive FTP: client asks for PASV/EPSV and initiates both control and data connections outbound, so it works more easily through NAT/firewalls (the server's passive port range must be allowed). SFTP uses SSH (normally TCP/22) and encrypts authentication/data; HTTPS uses TLS and is suitable for browser-based transfers. Both are preferred over plaintext FTP.

SNMP GET: manager requests an interface counter OID (for example ifInOctets / IF-MIB) from the router agent; agent returns the current value. SNMP TRAP: router asynchronously sends a notification such as linkDown to the manager when an interface fails. Use SNMPv3 with authentication and privacy; avoid public/community strings.

## A2.3 DNS and HTTP timings
In browser Developer Tools → Network → Timing, inspect DNS Lookup, Initial connection, SSL, Request sent, Waiting/TTFB and Content Download. Long DNS indicates resolver/lookup delay; long SSL/connection indicates handshake or path issues; long TTFB suggests server processing or network round-trip; long content download suggests a large object or low throughput. Waterfall ordering also reveals blocked or serial resources.

## Webmail vs IMAP estimate
Assume 50 messages with 2 KB headers/body preview each and no attachments: about 100 KB of message data plus protocol overhead. A webmail page may additionally transfer HTML/CSS/JS/images (assume 500 KB–2 MB cached/uncached), while an IMAP client can fetch headers and previews first (about 100 KB) and fetch full bodies/attachments on demand. These are illustrative estimates; actual mailbox size and client caching change the result. HTTPS webmail and IMAPS both encrypt transport; centrally managed webmail can simplify endpoint policy, while IMAP clients require secure configuration on every device.
