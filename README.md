🔐 Django Authentication System (Login • Logout • Password Reset)

A fully functional Django authentication system built using Django’s built-in auth views, custom templates, secure email handling with Gmail SMTP, and environment variable protection using .env.

This project implements real-world auth flows, not just basic login pages.

⸻

🚀 Features
	•	✅ User Registration
	•	✅ User Login & Logout
	•	✅ Profile Page
	•	✅ Password Reset via Email
	•	✅ Secure Gmail SMTP integration
	•	✅ Environment variable based secrets (.env)
	•	✅ Media & profile image handling
	•	✅ Clean URL routing with Django Auth Views

⸻

🧠 What I Learned (Key Takeaways)
	•	How Django’s built-in auth system actually works
	•	Why URL names matter more than template names
	•	How Django generates secure password reset tokens
	•	Why email delivery ≠ email verification
	•	How SMTP works behind the scenes
	•	How to safely store secrets using .env
	•	Why URL order matters ('' catch-all must come last)
	•	Production-grade project structure

⸻

🛠 Tech Stack
	•	Backend: Django
	•	Auth: django.contrib.auth
	•	Database: SQLite (development)
	•	Email: Gmail SMTP
	•	Templates: Django Templates + Bootstrap
	•	Environment Variables: python-dotenv
