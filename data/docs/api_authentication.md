Title: API Authentication

This doc covers how developers authenticate to company APIs.

Authentication methods:
- OAuth2 with client credentials for machine-to-machine requests.
- API keys for legacy services (rotate every 90 days).
- JWT tokens issued by the Auth service.

Obtaining credentials:
- Register your application in the Developer Portal.
- Follow the API onboarding flow; you may need to use the password recovery process if your account cannot authenticate.

Examples:
- Code snippet for obtaining token using client_id/client_secret.
- How to validate tokens and check scopes.