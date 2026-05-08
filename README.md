# 🎓 Canvas Shadow Radar

![Status](https://img.shields.io/badge/Status-Active-success.svg)
![React](https://img.shields.io/badge/Frontend-React%20%7C%20Tailwind-8A2BE2.svg)
![AWS](https://img.shields.io/badge/Cloud-AWS%20Macie-FF9900.svg)

## 📌 Overview
The EdTech supply chain is notoriously leaky. Students and developers frequently build custom scripts to interact with Learning Management Systems (LMS) like Instructure Canvas. Unfortunately, they regularly hardcode their **Canvas API Bearer Tokens** and commit them to public GitHub repositories. 

The **Canvas Shadow Radar** is an automated threat intelligence dashboard that tracks the exposure of these tokens, highlighting severe violations of data privacy and FERPA compliance.

## 🚨 The Threat Vector
A leaked Canvas API token doesn't just expose a student's grades. Depending on the user's role (Student, TA, or Administrator), a valid token allows an attacker to query:
* `/api/v1/users/self/profile` (Full names, primary emails, institutional IDs)
* `/api/v1/conversations` (Direct messages between students and faculty)
* `/api/v1/courses/:id/users` (Complete class rosters for a given institution)

## 🏗️ Target AWS Architecture
In an enterprise deployment, this radar leverages native AWS Security and Data Protection services:
* **Detection:** Custom AWS Lambda functions running scheduled cron jobs (via EventBridge) to scrape public git commits for the `71~` or `1~` token pattern.
* **Data Classification:** Amazon Macie is used to automatically discover and classify the sensitive PII (Personally Identifiable Information) retrieved during token validation.
* **Storage:** Telemetry and historical leak data are stored in Amazon DynamoDB.
* **Hosting:** The frontend is a static React application distributed globally via Amazon CloudFront and Amazon S3.

## 🚀 Usage (Local Scanner)

```bash
# 1. Clone the repository
git clone [https://github.com/PurpleHaze2320/canvas-shadow-radar.git](https://github.com/PurpleHaze2320/canvas-shadow-radar.git)
cd canvas-shadow-radar

# 2. Run the token analysis simulator
python canvas_scanner.py --scan