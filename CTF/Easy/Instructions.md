# WLHS CTF Challenge: Leaked Credentials & Log Analysis Attack Path

## Overview
Welcome to the **WLHS CTF Challenge**! This environment is designed to test your skills in penetration testing, forensic investigation, and defense strategy.

Participants will engage in:
- **Discovery**: Uncover hidden credentials and misconfigured files.
- **Exploitation**: Gain unauthorized access using real-world attack vectors.
- **Investigation**: Analyze logs to trace attacker activity.
- **Defense**: Implement security measures to harden the system.

Your objective is to navigate the challenge environment, retrieve the flag, and submit it.

---

## Connection Details

### **CTF Challenge Server**
- **HTTP Server:** `http://<server-ip>:8080`
- **MySQL Database:** `mysql -h <server-ip> -u <user> -p<password> -P 3307`
- **SSH Access (if enabled):** `ssh user@<server-ip>`

### **Flag Submission Server**
- Submit flags to: `http://<flag-validator-ip>:5000/submit_flag`
- Use the API to validate the flag.

---

## Tools Available

### **Attack Tools**
- **Gobuster / FFUF** – Directory fuzzing to locate hidden paths.
- **Curl / Wget** – Retrieve remote files and inspect responses.
- **MySQL Client** – Connect to the vulnerable database.

### **Forensic Investigation**
- **grep / awk / tail** – Analyze logs for unauthorized access.
- **Fail2Ban** – Monitor brute-force attempts.

### **Defense & Hardening**
- **chmod / chown** – Modify file permissions.
- **Firewall Rules** – Restrict access to sensitive services.
- **Logging & Monitoring** – Detect and respond to attacks.

---

## Flag Validation
Once you obtain the flag, submit it via:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"flag":"FLAG{EXAMPLE}"}' http://<flag-validator-ip>:5000/submit_flag
