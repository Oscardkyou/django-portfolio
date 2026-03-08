AUTHOR = {
    "full_name": {"en": "Dauren Askarov", "ru": "Даурен Аскаров"},
    "name": {"en": "Dauren", "ru": "Даурен"},
    "lastname": {"en": "Askarov", "ru": "Аскаров"},
    "title": {"en": "Python Backend Engineer | AI Integration", "ru": "Python Backend Engineer | AI Integration"},
    "location": {"en": "Almaty, Kazakhstan", "ru": "Алматы, Казахстан"},
    "bio": {
        "en": (
            "Python backend engineer focused on AI integration, scalable APIs, and "
            "production-grade systems for data-intensive products."
        ),
        "ru": (
            "Python backend инженер с фокусом на AI-интеграции, масштабируемых API "
            "и production-grade системах для data-intensive продуктов."
        ),
    },
    "hero_summary": {
        "en": "I build scalable APIs, AI-enabled backend systems, and real-time platforms.",
        "ru": "Я создаю масштабируемые API, backend-системы с AI и real-time платформы.",
    },
    "hero_strengths": {
        "en": "Python, FastAPI, Django, Docker, AWS, RAG, and async backend systems.",
        "ru": "Python, FastAPI, Django, Docker, AWS, RAG и асинхронные backend-системы.",
    },
    "email": "daurendevdk@gmail.com",
    "telegram": "https://t.me/DK_Oscar",
    "github": "https://github.com/Oscardkyou",
    "linkedin": "",
    "availability": {
        "en": "Available for remote backend and AI engineering opportunities.",
        "ru": "Открыт к удалённым возможностям в backend и AI engineering.",
    },
    "resume_label": {"en": "Download Resume", "ru": "Скачать резюме"},
    "cta_primary": {"en": "View Projects", "ru": "Смотреть проекты"},
    "cta_secondary": {"en": "Contact", "ru": "Контакты"},
    "focus_areas": [
        {"en": "Backend architecture for AI products", "ru": "Backend-архитектура для AI-продуктов"},
        {"en": "RAG pipelines and LLM integration", "ru": "RAG-пайплайны и интеграция LLM"},
        {"en": "High-performance API development", "ru": "Разработка высокопроизводительных API"},
        {"en": "Cloud-native delivery and observability", "ru": "Cloud-native delivery и observability"},
    ],
    "proof_points": [
        {"en": "3 backend / AI case studies", "ru": "3 backend / AI case study"},
        {"en": "API-ready portfolio", "ru": "API-ready портфолио"},
        {"en": "Remote-friendly collaboration", "ru": "Подходит для удалённого сотрудничества"},
        {"en": "FastAPI, Django, Docker, AWS", "ru": "FastAPI, Django, Docker, AWS"},
    ],
}

UI_TEXT = {
    "nav_home": {"en": "Home", "ru": "Главная"},
    "nav_about": {"en": "About", "ru": "Обо мне"},
    "nav_projects": {"en": "Projects", "ru": "Проекты"},
    "nav_case_studies": {"en": "Case Studies", "ru": "Кейсы"},
    "nav_skills": {"en": "Skills", "ru": "Навыки"},
    "nav_contact": {"en": "Contact", "ru": "Контакты"},
    "theme_light": {"en": "Light", "ru": "Светлая"},
    "theme_dark": {"en": "Dark", "ru": "Тёмная"},
    "hero_projects": {"en": "Projects", "ru": "Проекты"},
    "hero_contact": {"en": "Contact", "ru": "Контакты"},
    "featured_project": {"en": "Featured Project", "ru": "Избранный проект"},
    "see_full_case": {"en": "See full case study", "ru": "Смотреть полный кейс"},
    "projects_heading": {"en": "Projects", "ru": "Проекты"},
    "skills_heading": {"en": "Skills", "ru": "Навыки"},
    "performance_heading": {"en": "Performance", "ru": "Результаты"},
    "backend_highlights": {"en": "Backend Portfolio Highlights", "ru": "Сильные стороны backend-портфолио"},
    "task_label": {"en": "Task", "ru": "Задача"},
    "contribution_label": {"en": "My contribution", "ru": "Мой вклад"},
    "results_label": {"en": "Results", "ru": "Результаты"},
    "architecture_label": {"en": "Architecture", "ru": "Архитектура"},
    "problem_label": {"en": "Problem", "ru": "Проблема"},
    "solution_label": {"en": "Solution", "ru": "Решение"},
    "contact_details": {"en": "Contact details", "ru": "Контакты"},
    "send_message": {"en": "Send a message", "ru": "Отправить сообщение"},
    "email_label": {"en": "Email", "ru": "Email"},
    "telegram_label": {"en": "Telegram", "ru": "Telegram"},
    "github_label": {"en": "GitHub", "ru": "GitHub"},
    "availability_label": {"en": "Availability", "ru": "Доступность"},
}

PROJECTS = [
    {
        "title": "Gravora AI Knowledge Platform",
        "slug": "gravora-ai-knowledge-platform",
        "summary": "Enterprise RAG platform for fast internal knowledge retrieval.",
        "problem": "Teams spent too much time searching across scattered documents and internal chats.",
        "role": "Designed and implemented the backend architecture for retrieval, orchestration, and delivery.",
        "description": (
            "Built a backend platform for enterprise knowledge retrieval using embeddings, "
            "vector search, caching, and LLM orchestration."
        ),
        "stack": [
            "Python",
            "FastAPI",
            "OpenAI",
            "HuggingFace",
            "Redis",
            "ChromaDB",
            "Docker",
            "Prometheus",
            "Grafana",
        ],
        "features": [
            "RAG pipeline",
            "OpenAI embeddings",
            "ChromaDB vector search",
            "LLM response generation",
            "Redis caching",
            "Telegram bot integration",
        ],
        "architecture": [
            "User",
            "FastAPI API",
            "RAG Service",
            "Vector DB (ChromaDB)",
            "LLM Provider",
        ],
        "results": [
            "Search time reduced from 15 minutes to 30 seconds",
            "RAG latency kept below 180ms for key flows",
            "Improved knowledge access for internal teams",
        ],
        "github_url": "https://github.com/Oscardkyou",
        "link": "",
        "image_url": "",
        "is_featured": True,
    },
    {
        "title": "Low Latency Video Streaming Backend",
        "slug": "low-latency-video-streaming-backend",
        "summary": "Real-time backend for low-latency mobile-to-desktop streaming.",
        "problem": "Needed stable real-time video delivery with low latency and state coordination across clients.",
        "role": "Built the async backend, streaming orchestration, and infrastructure integration layers.",
        "description": "Designed an async streaming backend with WebSockets, state coordination, and durable media handling.",
        "stack": [
            "Python",
            "FastAPI",
            "WebSockets",
            "FFmpeg",
            "Redis",
            "PostgreSQL",
            "S3",
            "Docker",
            "Nginx",
        ],
        "features": [
            "Async architecture",
            "WebSocket streaming",
            "Redis state management",
            "S3 storage",
            "Docker deployment",
        ],
        "architecture": [
            "Mobile Clients",
            "WebSocket Gateway",
            "Streaming Orchestrator",
            "Redis State",
            "S3 Storage",
        ],
        "results": [
            "End-to-end latency under 150ms",
            "Supports 50+ concurrent streams",
            "Stable real-time coordination through Redis-backed state",
        ],
        "github_url": "https://github.com/Oscardkyou",
        "link": "",
        "image_url": "",
        "is_featured": False,
    },
    {
        "title": "Blockchain Monitoring System",
        "slug": "blockchain-monitoring-system",
        "summary": "Event-driven service for blockchain transaction monitoring and alerting.",
        "problem": "Required reliable monitoring of blockchain events with near real-time processing and persistence.",
        "role": "Implemented event ingestion, worker processing, and transaction persistence pipeline.",
        "description": "Built a monitoring backend for blockchain events with worker-based processing and operational alerting.",
        "stack": ["Python", "Web3", "Celery", "Redis", "PostgreSQL"],
        "features": [
            "WebSocket blockchain events",
            "RPC integration",
            "transaction monitoring",
            "event processing",
        ],
        "architecture": [
            "Blockchain Node",
            "Web3 Event Listener",
            "Celery Workers",
            "PostgreSQL",
            "Alerting",
        ],
        "results": [
            "Near real-time event monitoring",
            "Reliable background processing of transactions",
            "Operational visibility for blockchain activity",
        ],
        "github_url": "https://github.com/Oscardkyou",
        "link": "",
        "image_url": "",
        "is_featured": False,
    },
]

SKILLS = [
    {"name": "Python", "category": "Backend", "icon": "bx bxl-python"},
    {"name": "FastAPI", "category": "Backend", "icon": "bx bx-code-alt"},
    {"name": "Django", "category": "Backend", "icon": "bx bx-code-block"},
    {"name": "Flask", "category": "Backend", "icon": "bx bx-code-block"},
    {"name": "REST API", "category": "Backend", "icon": "bx bx-transfer"},
    {"name": "WebSockets", "category": "Backend", "icon": "bx bx-wifi"},
    {"name": "AsyncIO", "category": "Backend", "icon": "bx bx-time"},
    {"name": "PostgreSQL", "category": "Databases", "icon": "bx bxs-data"},
    {"name": "Redis", "category": "Databases", "icon": "bx bxs-data"},
    {"name": "SQL", "category": "Databases", "icon": "bx bxs-data"},
    {"name": "ChromaDB", "category": "Databases", "icon": "bx bx-layer"},
    {"name": "RAG", "category": "AI", "icon": "bx bx-brain"},
    {"name": "LLM integration", "category": "AI", "icon": "bx bx-bot"},
    {"name": "HuggingFace", "category": "AI", "icon": "bx bx-bot"},
    {"name": "OpenAI", "category": "AI", "icon": "bx bx-chip"},
    {"name": "Embeddings", "category": "AI", "icon": "bx bx-chip"},
    {"name": "Vector Search", "category": "AI", "icon": "bx bx-shape-circle"},
    {"name": "AWS", "category": "Cloud", "icon": "bx bxl-aws"},
    {"name": "S3", "category": "Cloud", "icon": "bx bx-cloud"},
    {"name": "Lambda", "category": "Cloud", "icon": "bx bx-cloud-lightning"},
    {"name": "Docker", "category": "DevOps", "icon": "bx bxl-docker"},
    {"name": "Nginx", "category": "DevOps", "icon": "bx bx-server"},
    {"name": "GitHub Actions", "category": "DevOps", "icon": "bx bxl-github"},
    {"name": "CI/CD", "category": "DevOps", "icon": "bx bx-git-branch"},
    {"name": "Prometheus", "category": "DevOps", "icon": "bx bx-line-chart"},
    {"name": "Grafana", "category": "DevOps", "icon": "bx bx-bar-chart-alt-2"},
    {"name": "pytest", "category": "Testing", "icon": "bx bx-check-shield"},
    {"name": "Unit tests", "category": "Testing", "icon": "bx bx-check-double"},
    {"name": "Integration tests", "category": "Testing", "icon": "bx bx-check-double"},
]

CASE_STUDIES = [
    {
        "title": "Gravora RAG Case Study",
        "slug": "gravora-rag-case-study",
        "problem": "Employees lost time searching for operational knowledge across fragmented documents and chats.",
        "solution": "Built a FastAPI-based RAG pipeline with embeddings, vector search, caching, and LLM orchestration.",
        "stack": ["Python", "FastAPI", "OpenAI", "ChromaDB", "Redis"],
        "metrics": ["Search flow reduced from 15 minutes to 30 seconds", "Latency < 180ms"],
        "architecture": ["User", "FastAPI API", "Retriever", "Vector DB", "LLM Provider"],
        "github_link": "https://github.com/Oscardkyou",
        "demo_link": "",
        "featured": True,
    },
    {
        "title": "Low Latency Streaming Case Study",
        "slug": "low-latency-streaming-case-study",
        "problem": "Needed reliable low-latency video delivery from mobile clients to desktop consumers.",
        "solution": "Implemented async streaming orchestration with WebSockets, Redis state, and durable media handling.",
        "stack": ["Python", "FastAPI", "WebSockets", "Redis", "S3"],
        "metrics": ["Latency < 150ms", "50+ concurrent streams"],
        "architecture": ["Mobile Client", "WebSocket Gateway", "Streaming Service", "Redis State", "Storage"],
        "github_link": "https://github.com/Oscardkyou",
        "demo_link": "",
        "featured": False,
    },
    {
        "title": "Blockchain Monitoring Case Study",
        "slug": "blockchain-monitoring-case-study",
        "problem": "Monitoring blockchain activity manually was slow and operationally unreliable.",
        "solution": "Built an event-driven monitoring backend using Web3 listeners, workers, and persistent event storage.",
        "stack": ["Python", "Web3", "Celery", "Redis", "PostgreSQL"],
        "metrics": ["Near real-time monitoring", "Reliable event processing pipeline"],
        "architecture": ["Blockchain Node", "Event Listener", "Celery Workers", "PostgreSQL", "Alerts"],
        "github_link": "https://github.com/Oscardkyou",
        "demo_link": "",
        "featured": False,
    }
]

PERFORMANCE = [
    {"metric": "RAG latency", "value": "< 180ms"},
    {"metric": "Streaming latency", "value": "< 150ms"},
    {"metric": "Concurrent streams", "value": "50+ clients"},
    {"metric": "Search acceleration", "value": "15 min → 30 sec"},
]

BLOG_POSTS = [
    {"title": "AI Architecture for RAG Systems", "tag": "AI Systems"},
    {"title": "Designing Async FastAPI Services", "tag": "Backend"},
    {"title": "Production LLM Integrations", "tag": "AI Integration"},
]

GITHUB_STATS = {
    "stats": "https://github-readme-stats.vercel.app/api?username=Oscardkyou&show_icons=true&theme=tokyonight",
    "activity": "https://github-readme-activity-graph.vercel.app/graph?username=Oscardkyou&theme=tokyo-night",
}

RESUME_URL = "/static/assets/dauren-askarov-resume.pdf"
