pip install -r requirements.txt

2. (Optional) Choose model

High accuracy (default): all-mpnet-base-v2

Faster: all-MiniLM-L6-v2


# Linux/macOS
export EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Windows PowerShell
$env:EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
$env:EMBEDDING_MODEL="sentence-transformers/all-mpnet-base-v2"


python -m app.ingest


python -m app.search_cli








🔐 Queries for password_recovery_policy.md
Basic Queries

“How do I reset my forgotten corporate password?”

“What should I do if I get locked out of my account?”

“Where is the password reset portal?”

“What are the password strength requirements?”

Multi-Factor / Device Queries

“I lost my MFA phone — how do I recover access?”

“How do I get my authenticator app reconfigured?”

“What happens if I can’t receive SMS codes during password recovery?”

Security & Compromise Queries

“What should I do if I think someone hacked my account?”

“How long does a security investigation take?”

“What are the steps after detecting suspicious activity?”

Policy & Compliance Queries

“How often do passwords expire?”

“How many old passwords can I reuse?”

“Who should I contact if I need help after hours?”

Roleplay / Natural Language Queries

“I’m returning from vacation and my password expired — what now?”

“My password works but I can’t get past MFA. What do I do?”

“Can IT give me my old MFA codes?”








🏠 Queries for remote_work_policy.md
General Remote Work Queries

“What are the rules for working remotely?”

“Can I work from home full time?”

“What times do I need to be online?”

Workspace & Equipment Queries

“Am I allowed to use my personal laptop for remote work?”

“What are the requirements for my home workspace?”

“Is it okay to work from a café or public place?”

Security & Compliance Queries

“Do I have to use VPN when working remotely?”

“What things are prohibited in a remote work environment?”

“Can I print confidential documents at home?”

Travel & Cross-Border Queries

“Can I work from another country?”

“Do I need approval to work outside my province?”

“Is remote work allowed while travelling?”

Communication & Team Expectations Queries

“Do I need to keep my camera on during online meetings?”

“How quickly should I respond to messages?”

“Are daily check-ins required for remote workers?”

Technical Requirements Queries

“What happens if my internet goes down while working remotely?”

“What software updates do I need to maintain?”

“Do I need antivirus on my remote machine?”




Recommended query categories and concrete examples

Account & access (expected target: password_recovery.md, email_setup.md, onboarding_guide.md)
reset password
forgot password
password reset link not working
how do I recover my account
account recovery and password reset instructions
locked out of email — how to restore access
Remote work & WFH (expected target: remote_work_policy.md, benefits_overview.md)
work from home
WFH policy
remote work stipend
how to request to work remotely
request remote work arrangement form
VPN & connectivity (expected target: vpn_access.txt, troubleshooting_network.md)
VPN setup
how to connect to VPN from home
internal tools inaccessible from home
VPN connects but services unreachable
remote access to internal tools
Onboarding & first day tasks (expected target: onboarding_guide.md)
new hire onboarding checklist
how to set up company email
first day setup for new employee
Developer & API (expected target: api_authentication.md, code_contribution_guidelines.md)
how to authenticate to API
API token example client credentials
rotate API keys
contribute code to internal repo
cannot push to repo — permission issues
Security & best practices (expected target: security_best_practices.md)
security best practices for remote work
password policies and complexity requirements
how to report phishing
company password manager guidance
Policies & HR (expected target: data_retention_policy_long.md, holiday_policy.md)
data retention policy
how long do you keep employee records
holiday policy and requesting PTO
vacation rules
Troubleshooting & support (expected target: troubleshooting_network.md, vpn_access.txt)
wi-fi slow while working from home
how to troubleshoot network issues
email not receiving messages
Short/ambiguous queries to test semantics (should map to correct docs)
reset
password recovery process
forgot creds
WFH benefits
vacation days