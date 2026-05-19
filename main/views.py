from django.shortcuts import render


def home(request):
    """Render the portfolio landing page."""
    context = {
        "skills": [
            {"name": "Python", "level": 95},
            {"name": "Django", "level": 90},
            {"name": "JavaScript", "level": 86},
            {"name": "HTML/CSS", "level": 94},
            {"name": "React", "level": 82},
            {"name": "SQL", "level": 88},
        ],
        "projects": [
            {
                "title": "AI Insight Dashboard",
                "description": "A machine-learning analytics workspace with smart summaries, visual reports, and role-based access.",
                "tech": ["Python", "Django", "React", "PostgreSQL"],
                "accent": "ai",
            },
            {
                "title": "Cloud Commerce API",
                "description": "A scalable e-commerce backend with payment flows, inventory automation, and clean REST endpoints.",
                "tech": ["Django REST", "Celery", "Redis", "Stripe"],
                "accent": "commerce",
            },
            {
                "title": "Realtime DevOps Monitor",
                "description": "A live status platform for deployments, incidents, logs, and service health across engineering teams.",
                "tech": ["JavaScript", "WebSockets", "SQLite", "Docker"],
                "accent": "ops",
            },
        ],
        "services": [
            "Full-stack web applications",
            "AI product prototypes",
            "API design and integration",
            "Performance optimization",
        ],
        "timeline": [
            {
                "year": "2026",
                "title": "Senior Software Engineer",
                "text": "Building production-grade Django, AI, and cloud systems for modern teams.",
            },
            {
                "year": "2024",
                "title": "Full-Stack Developer",
                "text": "Delivered polished web platforms, dashboards, and automation tools.",
            },
            {
                "year": "2022",
                "title": "Computer Science Graduate",
                "text": "Focused on data structures, databases, software design, and applied AI.",
            },
        ],
    }
    return render(request, "main/home.html", context)
