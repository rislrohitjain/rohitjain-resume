from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__,
static_folder='static',
template_folder='templates'
)

# Comprehensive User Data for Rohit Jain
user_data = {
    "header": {
        "name": "Rohit Jain",
        "title": "Senior Full-Stack Developer | AI Automation Architect",
        "location": "Flat No. 103, Astha Empire 2, Chordiya City, Keshupura, Jaipur, Rajasthan 302026",
        "map_url": "https://www.google.com/maps/place/Rohit+Jain+software+engineer/@26.8876809,75.7066443,17z/data=!3m1!4b1!4m6!3m5!1s0x396db52cbbd5a387:0xb8755b323c8a6581!8m2!3d26.8876761!4d75.7092192!16s%2Fg%2F11szc_c7td",
        "contact": [ 
            "+91 89469 19241",
            "engrohitjain5@gmail.com",
            "https://github.com/rislrohitjain/",
            "https://linkedin.com/in/rohit-jain-061571a3",
            "https://huggingface.co/spaces/rislrohitjain/"
        ],
        "resume_url": "static/Resume_Original_Rohit_Jain.pdf"  # Replace with actual file download link
    },
    "summary": "Results-driven Full-Stack Developer and AI Automation Architect with 9+ years of experience delivering high-impact government portals and enterprise systems serving 100,000+ users. 1st Rank Winner & Champion at BrowserStack Testathon Jaipur ($105 USD Prize). Proven track record of cutting result generation time by 50% via optimized stored procedures[cite: 1].",
    "stats": [
        {"value": "9+", "label": "Years Exp"},
        {"value": "1st Rank", "label": "BrowserStack Winner ($105)"},
        {"value": "100K+", "label": "Users Served"},
        {"value": "50K+", "label": "Daily API Calls"},
        {"value": "8", "label": "AI Applications"}
    ],
    "skills": {
        "AI & LLM": ["Python Agentic AI", "LangGraph", "Ollama & Llama", "LangChain", "Gemini API", "Claude", "RAG Systems", "ChromaDB Vector DB", "n8n"],
        "Backend": ["Python (Intermediate)", "FastAPI", "Flask", "PHP (Laravel/CakePHP)", ".NET Core Web API", "REST/SOAP APIs"],
        "Database": ["PostgreSQL", "MySQL", "MSSQL", "ChromaDB Vector DB", "Stored Procedures"],
        "BI & DevOps": ["Pentaho", "Tableau", "Git", "Docker", "IIS"]
    },
    "projects": [
        {
            "id": "support-task-dashboard",
            "tab_title": "Support Task Dashboard — Automated Email Intelligence & Work Tracking",
            "title": "Support Task Dashboard — Automated Email Intelligence & Work Tracking",
            "badge": "Project #1 • 100% Local Machine & Docker",
            "tagline": "Automated email ingestion, local LLM parsing, PostgreSQL tracking, interactive dashboard portal, and pivoted Excel daily work sheets — running entirely via Docker on local machine only for 100% privacy.",
            "video_url": "Mail_Read_Every_Set_cron_using_ollama_llama_postgressql.mp4",
            "video_title": "Support Task Dashboard Project Demo (Python + Ollama + Llama + PostgreSQL + LangGraph on Local Docker)",
            "presentation_url": "RSOS_AI_Task_Automation_Executive_Presentation.pptx",
            "presentation_view_url": "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Frohitjain-resume.vercel.app%2Fstatic%2FRSOS_AI_Task_Automation_Executive_Presentation.pptx",
            "presentation_title": "RSOS AI Task Automation Executive Presentation",
            "summary": "An end-to-end automated system engineered to ingest support emails from designated mailboxes via scheduled cron jobs, parse unstructured email threads into structured task reports using local Llama models with Ollama and LangGraph, persist data into PostgreSQL, and present insights on a unified portal with graphical charts, CSV, and pivoted Excel exports for daily work sheets. Deployed and orchestrated via Docker strictly on the local machine to guarantee 100% data confidentiality and zero external API dependencies.",
            "highlights": [
                "100% Local Machine & Docker Orchestration: The entire multi-service stack (Python App, Ollama Local LLM, and PostgreSQL Database) runs locally in isolated Docker containers on the local machine only—guaranteeing complete data privacy, zero cloud data leakage, and zero recurring API costs.",
                "Scheduled Cron Email Ingestion: Background automation continuously polls and fetches emails from specific support inboxes via IMAP/APIs.",
                "Local LLM Inference with Ollama & Llama: Privacy-preserving, zero-data-leakage extraction of user tasks, ticket resolutions, and activity logs without external API costs.",
                "LangGraph Agentic Orchestration: Structured state graphs managing extraction pipelines, schema validation, error correction, and fallback rules.",
                "PostgreSQL Relational Persistence: Normalizes and stores task records, ticket statuses, timestamps, developer IDs, and email metadata into an ACID-compliant schema.",
                "Interactive Web Dashboard Portal: Modern web UI providing live task monitoring, team workload tracking, search, filtering, and real-time support status.",
                "Multi-Format Reporting & Work Sheets: Instant exports to graphical charts, CSV data, and formatted/pivoted Excel files detailing per-user work per email for daily worksheet submissions.",
                "Executive Slide Deck Available: Downloadable comprehensive presentation (.pptx) detailing architecture, ROI analysis, and enterprise automation impact."
            ],
            "skills_explained": [
                {
                    "name": "Docker (Local Machine Only)",
                    "badge": "100% Private Deployment",
                    "icon": "bi-box-seam-fill",
                    "desc": "Orchestrated the entire multi-service stack (Python App, Ollama LLM, and PostgreSQL) via Docker on the local machine only, ensuring zero cloud dependence and absolute data privacy."
                },
                {
                    "name": "Python",
                    "badge": "Core Engine & Automation",
                    "icon": "bi-code-slash",
                    "desc": "Built automated pipelines, IMAP mail fetchers, cron daemons, data manipulation with Pandas, and dynamic Excel generation."
                },
                {
                    "name": "Ollama & Llama Model",
                    "badge": "Local AI Inference",
                    "icon": "bi-cpu-fill",
                    "desc": "Zero-cloud-cost, privacy-first local LLM inference to extract structured JSON data from messy enterprise emails."
                },
                {
                    "name": "LangGraph",
                    "badge": "Agentic Orchestration",
                    "icon": "bi-diagram-3-fill",
                    "desc": "State graph design patterns with self-correction, schema validation, and fallback mechanisms for reliable pipeline execution."
                },
                {
                    "name": "PostgreSQL",
                    "badge": "Enterprise Relational DB",
                    "icon": "bi-database-fill",
                    "desc": "Structured table schemas, foreign key relationships, indexed search queries, and historical work logging."
                },
                {
                    "name": "Excel Automation & Charting",
                    "badge": "Reporting & Analytics",
                    "icon": "bi-file-earmark-spreadsheet-fill",
                    "desc": "Automated generation of graphical charts and formatted, pivoted Excel sheets for daily team worksheet reporting."
                },
                {
                    "name": "Crontab / Scheduler",
                    "badge": "Automated Scheduling",
                    "icon": "bi-clock-history",
                    "desc": "Configured automated execution intervals for 24/7 autonomous monitoring of support mail queues."
                }
            ]
        },
        {
            "id": "aimukeshajmera",
            "tab_title": "Mukesh Ajmera AI Financial Portal",
            "title": "Mukesh Ajmera — AI-Powered Financial Advisory & Insurance Intelligence Platform",
            "badge": "Project #2 • Python Full-Stack & Database • Live Vercel Production",
            "tagline": "Full-stack Python web application with database persistence, intelligent conversational AI assistant (LIC MITRA) with voice input, 20+ schemes catalog, comparison engine, SheetJS Excel export, and live Vercel cloud deployment.",
            "live_url": "https://aimukeshajmera.vercel.app/",
            "video_url": None,
            "presentation_url": None,
            "summary": "Engineered and deployed an end-to-end full-stack Python web platform with relational database persistence for authorized financial advisory services in Sarwar, Rajasthan. Designed and integrated 'LIC MITRA' — a domain-specialized conversational AI assistant featuring voice speech recognition, interactive quick chips, and automated WhatsApp handoff. Features a dynamic catalog of 20+ pre-loaded insurance and post office savings schemes, financial comparison matrices, visitor tracking analytics (118+), Google Maps integration, SheetJS client-side Excel exports, and responsive Tailwind UI deployed live on Vercel.",
            "highlights": [
                "Full-Stack Python & Database Architecture: Scalable Python backend with relational database schema storing user consultation bookings, client inquiries, and visitor analytics.",
                "Intelligent Conversational Assistant (LIC MITRA): Integrated smart multilingual AI assistant supporting interactive quick chips, voice input (Hindi/English), and direct WhatsApp handoff.",
                "20+ Pre-Loaded Financial Schemes Catalog: Real-time filtering, categorization (LIC Life Cover, Post Office Sovereign PPF/SSY), and structured comparison matrices.",
                "Interactive Live Embed Preview: Embedded directly inside this portfolio tab so visitors and recruiters can interact with the live application on-screen.",
                "Client-Side SheetJS Excel & Analytics: Automated Excel spreadsheet generation for scheme data, live visitor counter (118+), and full Google Reviews (⭐ 5.0) integration.",
                "High-Availability Vercel Cloud Deployment: Serverless cloud deployment with HTTPS SSL, zero-downtime CI/CD from Git, and 100% mobile-responsive design."
            ],
            "skills_explained": [
                {
                    "name": "Python & Web Framework",
                    "badge": "Full-Stack Backend",
                    "icon": "bi-code-slash",
                    "desc": "Engineered backend API routes, query handling, session management, dynamic templating, and request routing."
                },
                {
                    "name": "Relational Database",
                    "badge": "Data Persistence",
                    "icon": "bi-database-fill",
                    "desc": "Designed relational schemas to persist client advisory leads, visitor logs, and structured financial scheme metadata."
                },
                {
                    "name": "Conversational AI (LIC MITRA)",
                    "badge": "AI & Speech Recognition",
                    "icon": "bi-robot",
                    "desc": "Built domain-specific conversational chatbot with Web Speech API voice input and contextual financial recommendation chips."
                },
                {
                    "name": "Tailwind CSS & Modern UI",
                    "badge": "Responsive Frontend",
                    "icon": "bi-palette-fill",
                    "desc": "Crafted mobile-first interface with dual dark/light themes, card shimmer skeleton states, and hero banner slider."
                },
                {
                    "name": "SheetJS Excel Engine",
                    "badge": "Client Exporting",
                    "icon": "bi-file-earmark-spreadsheet-fill",
                    "desc": "Integrated dynamic spreadsheet generation allowing users to download formatted comparative financial plans."
                },
                {
                    "name": "Vercel Cloud CI/CD",
                    "badge": "Serverless Production",
                    "icon": "bi-cloud-check-fill",
                    "desc": "Configured automated Git-based serverless deployment pipeline with SSL certificates and edge caching."
                }
            ]
        },
        {
            "id": "rsos-admission-portal",
            "tab_title": "RSOS Dual-Stream Portal",
            "title": "RSOS Dual-Stream & On-Demand Online Admission Platform",
            "badge": "Project #3 • 100,000+ Candidates • Enterprise Scale",
            "tagline": "Full-lifecycle enterprise admission platform serving 100,000+ candidates across Rajasthan with automated seat allotment cutting processing time by 40%.",
            "video_url": None,
            "presentation_url": None,
            "summary": "Architected and engineered Rajasthan State Open School (RSOS) mission-critical admission and examination platform handling 100,000+ active candidates. Engineered high-concurrency MySQL stored procedures cutting result generation time by 50%, implemented robust RBAC across 15+ administrative roles with zero security breaches, and automated seat-matrix allocation.",
            "highlights": [
                "100,000+ Candidate Concurrency: Architected complete SDLC web platform managing statewide admissions, verification, and hall-ticket generation.",
                "40% Time Saved via Automated Seat Allocation: Replaced legacy manual allocation with algorithmic seat-matrix allotment.",
                "50% Speedup via MySQL Stored Procedures: Optimized high-volume relational queries and complex stored procedures for sub-second result computation.",
                "15+ Role-Based Access Control (RBAC): Hardened security protecting confidential candidate databases and examination marks.",
                "Real-Time Executive Dashboards: Integrated Pentaho and Tableau BI reporting delivering live district-wise enrollment metrics."
            ],
            "skills_explained": [
                {
                    "name": "PHP & Laravel",
                    "badge": "MVC Backend Architecture",
                    "icon": "bi-code-slash",
                    "desc": "Scalable REST APIs, background queue workers, session security, and state-wide admission workflows."
                },
                {
                    "name": "MySQL Stored Procedures",
                    "badge": "Query Optimization",
                    "icon": "bi-database-fill",
                    "desc": "Designed complex stored procedures and database triggers that slashed result generation times by 50%."
                },
                {
                    "name": "Role-Based Security",
                    "badge": "Enterprise RBAC",
                    "icon": "bi-shield-lock-fill",
                    "desc": "Multi-tier privilege control protecting examination marks across 15 administrative roles with 0% unauthorized access."
                },
                {
                    "name": "Pentaho & Tableau BI",
                    "badge": "Data Visualization",
                    "icon": "bi-bar-chart-fill",
                    "desc": "Configured executive reporting dashboards tracking statewide enrollment targets and fee reconciliation."
                }
            ]
        },
        {
            "id": "ecourt-highcourt-gateway",
            "tab_title": "E-Court & High Court Gateway",
            "title": "E-Court & High Court Secure Inter-Agency API Integration",
            "badge": "Project #4 • AES Encryption • Government Security",
            "tagline": "Mission-critical API integration gateway linking State Department portals with High Court and E-Court judicial systems using AES payload encryption and automated token lifecycle management.",
            "video_url": None,
            "presentation_url": None,
            "summary": "Designed and deployed high-security inter-agency API gateways connecting executive government databases with High Court and E-Court case management systems. Implemented end-to-end symmetric AES encryption for sensitive judicial transit payloads, automated token validation, and fault-tolerant retry queues.",
            "highlights": [
                "Judicial Case Synchronization: Two-way real-time API communication linking administrative state portals with High Court legal databases.",
                "AES Transit Payload Encryption: Engineered military-grade AES encryption and dynamic token exchange protocols.",
                "SOAP & REST Hybrid Integration: Unified consumption of legacy SOAP XML endpoints and modern RESTful JSON services.",
                "99.9% Uptime & Comprehensive Audit Logging: Cryptographically verifiable transaction logs and failover retry queues."
            ],
            "skills_explained": [
                {
                    "name": "API Security & Encryption",
                    "badge": "AES & Token Auth",
                    "icon": "bi-shield-check",
                    "desc": "Implemented end-to-end payload encryption and secure bearer token exchanges for judicial compliance."
                },
                {
                    "name": "REST & SOAP Protocols",
                    "badge": "Interoperability",
                    "icon": "bi-arrow-left-right",
                    "desc": "Engineered hybrid protocol adapters to connect legacy SOAP services with modern web frontends."
                },
                {
                    "name": "Python & PHP Middleware",
                    "badge": "High Throughput",
                    "icon": "bi-cpu-fill",
                    "desc": "Optimized microservices processing high-volume daily legal notifications with zero dropped packets."
                }
            ]
        }
    ],
    "agentic_team": [
        {"name": "Business Analyst Agent", "role": "Requirements & Domain Modeling"},
        {"name": "Product Manager Agent", "role": "Roadmap & User Stories"},
        {"name": "UI/UX Design Agent", "role": "Wireframing & Interface Spec"},
        {"name": "Frontend Developer Agent", "role": "Responsive UI & Components"},
        {"name": "Python Backend Developer Agent", "role": "REST/FastAPI & Business Logic"},
        {"name": "API Design Agent", "role": "OpenAPI Spec & Contract Validation"},
        {"name": "Database Architect Agent", "role": "Schema & Index Optimization"},
        {"name": "Database Migration Agent", "role": "DDL & DML Migration Scripts"},
        {"name": "Code Reviewer Agent", "role": "Static Analysis & Best Practices"},
        {"name": "Unit Test Generator Agent", "role": "Automated Test Suite Generation"},
        {"name": "QA & Automation Testing Agent", "role": "End-to-End Test Automation"},
        {"name": "Performance & Load Testing Agent", "role": "Benchmarking & Profiling"},
        {"name": "Security & Vulnerability Scanner Agent", "role": "SAST/DAST & OWASP Audit"},
        {"name": "DevOps CI/CD Agent", "role": "Pipeline Automation & Workflows"},
        {"name": "Cloud Infrastructure Agent", "role": "Terraform & Cloud Architecture"},
        {"name": "Deployment & Release Manager Agent", "role": "Zero-Downtime Releases"},
        {"name": "Site Reliability & Monitoring Agent", "role": "Metrics, Logs & Alerting"},
        {"name": "Technical Documentation Agent", "role": "API Docs & Knowledge Base"},
        {"name": "Project Orchestrator Agent", "role": "Multi-Agent Coordination"}
    ],
    "events": [
        {
            "title": "Claude Community Jaipur Meetup",
            "type": "Upcoming In-Person Event",
            "status": "🎟️ Event Registered • Waiting for Event Date (October 24, 2026)",
            "registration_date": "Confirmed RSVP • Ticket Issued",
            "date": "Saturday, October 24, 2026 | 10:30 AM – 1:00 PM GMT+5:30",
            "location": "Malaviya National Institute of Technology (MNIT), JLN Marg, Malviya Nagar, Jaipur, Rajasthan 302017",
            "organizer": "Claude Community Jaipur in collaboration with Jaipur Data & AI Community (Speakers: Jason Sears - Engineering Lead, Origin Digital Chicago ✈️ | Ajay Sharma - Senior Solution Architect, Origin Digital Jaipur)",
            "event_url": "https://luma.link/XxRFO63oFj",
            "ticket_url": "https://luma.link/rXSoj2F9sT",
            "map_url": "https://luma.link/7cBc9mWN8q",
            "learnings": [
                "Claude Code & MCP (Model Context Protocol): Practical deep-dive into Anthropic's Model Context Protocol (MCP) server standards, tool calling, and autonomous developer workflows.",
                "Production Agentic AI Architectures: Engineering multi-agent coordination, prompt caching economics, and real-world generative AI production deployment.",
                "Global Speaker Keynote & Lightning Demos: Insights from Jason Sears (Engineering Lead, Origin Digital Chicago) and Ajay Sharma on enterprise-scale LLMs.",
                "Jaipur AI Community Collaboration: Live in-person networking and peer architecture discussions with Jaipur's leading AI engineers, founders, and developers at MNIT Jaipur."
            ]
        },
        {
            "title": "BrowserStack Testathon Jaipur 2026",
            "type": "Onsite Hackathon & Championship Competition",
            "is_champion": True,
            "rank": "1st Rank Champion",
            "prize": "$105 USD Prize Awarded by BrowserStack",
            "badge": "🥇 1st Rank Champion • $105 USD Prize",
            "achievement": "🏆 1st Rank Winner & Champion — Awarded 1st Prize of $105 USD from BrowserStack in Live 3-Hour Automation Hackathon",
            "date": "Saturday, September 5, 2026 | 10:00 AM IST onwards",
            "location": "Metacube Software Pvt. Ltd., Sitapura Industrial Area, Jaipur",
            "organizer": "BrowserStack Community Team – Jaipur",
            "learnings": [
                "🥇 1st Rank Champion (1st Prize of $105 USD): Secured the 1st Rank across all participating software engineers and QA professionals in Jaipur, winning the top cash prize of $105 USD awarded directly by BrowserStack.",
                "⚡ 3-Hour Live Hackathon & Bug Hunting: Built, documented, and executed a complete end-to-end automated test suite for an intentionally buggy live web application under strict 3-hour time constraints, maximizing defect discovery and assertion coverage.",
                "☁️ BrowserStack Cloud Test Suite: Mastered and deployed BrowserStack Automate (parallel cross-browser and real mobile device testing), BrowserStack Test Management, Test Companion, and Test Observability for automated failure and log analysis.",
                "🛠️ Framework & SDK Integration: Integrated automated Selenium/Playwright test scripts using BrowserStack SDK, configuring continuous test execution and publishing complete test suites to GitHub."
            ]
        },
        {
            "title": "UiPath Jaipur: Agentic Automation in Practice (Maestro Flow & Live Build)",
            "type": "Onsite / In-Person Event",
            "date": "Saturday, October 3, 2026 | 11:00 AM – 3:00 PM IST",
            "location": "Vanshiv Technologies, New Sanganer Road, Jaipur 302020",
            "organizer": "UiPath Community Jaipur Chapter (Host: Gaurav Kheterpal | Speakers: Umesh Dutt Sharma - AI Solutions Architect, Shashwat Raghuwanshi - Nagarro Senior Engineer, Aayushi Saxena)",
            "event_url": "https://community.uipath.com/events/details/uipath-jaipur-presents-agentic-automation-in-practice-maestro-flow-live-build-and-hands-on-lab-in-person-meetup/",
            "achievement": "🏆 Achieved 6th Rank in Live Technical Quiz & Received Official UiPath Swag Gift (Orange Multi-Cable Charger Set)",
            "images": [
                "images/uipath_speakers.jpg",
                "images/uipath_quiz_1.jpg",
                "images/uipath_quiz_2.jpg",
                "images/uipath_swag.jpg"
            ],
            "learnings": [
                "Agentic AI & Maestro Flow Orchestration: Built live and orchestrated Agentic AI workflows using UiPath Maestro Flow, Autopilot, and AI Agent Builder from an empty canvas to running execution.",
                "Hands-On Complaint Classifier Lab: Built a working AI-driven complaint intake & classification process with human-in-the-loop approval workflows.",
                "Real Enterprise Problem Solving: Mastered agentic vs rule-based architecture trade-offs, token economics, cost optimization at scale, and production observability logging."
            ]
        },

        {
            "title": "Cloud Coffee Connect — AI on AWS & Open Source",
            "type": "Onsite / In-Person Event",
            "date": "Saturday, September 19, 2026 | 10:00 AM – 1:00 PM IST",
            "location": "Pratham Software, Sitapura Industrial Area, Jaipur",
            "organizer": "AWS User Group Jaipur – Rajasthan",
            "learnings": [
                "AI Deployment on AWS: Learned practical strategies for deploying, optimizing, and scaling open-source LLMs and AI models on AWS infrastructure.",
                "AI/ML Architecture & Pipelines: Explored end-to-end open-source AI pipelines combined with AWS cloud services.",
                "Onsite Networking & Peer Learning: Engaged in live architectural discussions with cloud engineers, AI developers, and AWS community leaders in Jaipur."
            ]
        },
        {
            "title": "Atlassian × Tableau: Integrating Jira & Confluence with Tableau",
            "type": "Onsite / In-Person Event",
            "date": "Sunday, September 20, 2026 | 11:00 AM – 2:00 PM IST",
            "location": "Kundan Hall, The Fern Jaipur, Tonk Road, Jaipur",
            "organizer": "Atlassian Community Events – Jaipur",
            "learnings": [
                "Live Technical Integration (by Hemant Saini): Learned to architect and configure live connections between Jira Cloud, Confluence, and Tableau Server/Cloud using OAuth, SSO, and Personal Access Tokens (PATs).",
                "Embedding Metrics in Confluence: Mastered embedding live interactive Tableau dashboards directly into Confluence pages for real-time team visibility.",
                "Certification Pathways: Learned exam structures and preparation roadmaps for Atlassian Certification (Anamika Soni) and Tableau Certification (Tarun Gupta)."
            ]
        },
        {
            "title": "Agile Testing Alliance (ATA)",
            "type": "Onsite / In-Person Event",
            "date": "Saturday, September 26, 2026 | 10:00 AM – 2:00 PM IST",
            "registration_date": "Registered: August 28, 2026",
            "location": "Asymbl Technology - 1st floor, E-81 & 82, SL Marg, Lal Bahadur Nagar, Milap Nagar, Jaipur 302018",
            "map_url": "https://maps.app.goo.gl/U3gswhRJYYxN4H2f6?g_st=aw",
            "video_url": "rohit_ai_ata.mp4",
            "images": [
                "images/ata_1.jpg",
                "images/ata_2.jpg",
                "images/ata_3.jpg"
            ],
            "organizer": "Agile Testing Alliance (ATA)",
            "learnings": [
                "Agile QA & Quality Engineering: Learned modern agile testing methodologies, test automation standards, and continuous testing pipelines.",
                "Community Collaboration: Interacted and networked in-person with quality engineering leaders across the ATA Jaipur community."
            ]
        }
    ],
   "experience": [
        {
            "role": "Senior Software Developer",
            "company": "Data Ingenious Global Limited",
            "period": "April 2024 – Present",
            "details": [
                "Lead Laravel Developer for RSOS Dual-Stream & On-Demand Admission Portal.",
                "Architected full SDLC for a platform serving 100,000+ candidates.",
                "Engineered automated seat-allotment modules, cutting processing time by 40%.",
                "Implemented RBAC for 15+ user roles, achieving zero unauthorized access incidents.",
                "Deployed Ollama for AI code-assistance, reducing manual code-reviews by 30%[cite: 1].",
                "Integrated Gemini and Claude APIs into VS Code, reducing debugging time by 25%[cite: 1].",
                "Piloting Agentic AI workflows (n8n, LangChain) and .NET Core microservices[cite: 1]."
            ]
        },
        {
            "role": "Software Developer",
            "company": "DevIT Solutions Pvt. Ltd.",
            "period": "February 2020 – April 2024",
            "details": [
                "Delivered large-scale government portals serving 50,000+ daily users in Rajasthan[cite: 1].",
                "Secured High Court/E-Court API integrations using AES encryption and tokens[cite: 1].",
                "Reduced RSOS result-generation time by 50% via optimized MySQL stored procedures[cite: 1].",
                "Built Paramedical Council seat-matrix algorithms with 99.9% accuracy[cite: 1].",
                "Designed Pentaho and Tableau BI dashboards for real-time reporting on 10+ KPIs[cite: 1].",
                "Managed full SDLC across Laravel, CakePHP, CodeIgniter, MySQL, and MSSQL[cite: 1]."
            ]
        },
        {
            "role": "Software Developer",
            "company": "Akal Information Systems Ltd.",
            "period": "October 2017 – January 2020",
            "details": [
                "Developed enterprise web applications for government and corporate clients[cite: 1].",
                "Contributed to complex API integrations and database optimization projects[cite: 1].",
                "Collaborated with cross-functional teams to meet aggressive delivery timelines[cite: 1]."
            ]
        },
        {
            "role": "Junior Software Developer",
            "company": "Vertex Plus Software Pvt. Ltd.",
            "period": "August 2016 – October 2017",
            "details": [
                "Built responsive web applications and client portals using PHP and Bootstrap[cite: 1].",
                "Gained foundational expertise in SOAP and REST API consumption[cite: 1]."
            ]
        },
        {
            "role": "Junior Developer",
            "company": "On-Graph Technologies Pvt. Ltd.",
            "period": "December 2015 – August 2016",
            "details": [
                "Developed CMS-driven websites and community portals[cite: 1].",
                "Integrated SMS gateways and real-time notification systems[cite: 1]."
            ]
        }
    ]
}

user_data["learning_project"] = user_data["projects"][0]

@app.route('/')
def index():
    # Renders the separate resume.html file
    return render_template('index.html', user=user_data)

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/llms.txt')
@app.route('/.well-known/llms.txt')
def llms():
    return send_from_directory('static', 'llms.txt')

@app.route('/presentation')
def presentation():
    return redirect("https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Frohitjain-resume.vercel.app%2Fstatic%2FRSOS_AI_Task_Automation_Executive_Presentation.pptx")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)