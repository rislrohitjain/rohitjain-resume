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
            "https://wa.me/918946919241",
            "https://github.com/rislrohitjain/",
            "https://linkedin.com/in/rohit-jain-061571a3",
            "https://huggingface.co/spaces/rislrohitjain/"
        ],
        "resume_url": "static/Resume_Original_Rohit_Jain.pdf"  # Replace with actual file download link
    },
    "summary": "Results-driven Senior Full-Stack Developer & AI Automation Architect with 9+ years of experience delivering mission-critical enterprise systems serving 100,000+ users. 1st Rank Champion at BrowserStack Testathon Jaipur ($105 USD Prize) and Top 5 Winner at Claude Community Jaipur Meetup. Proven track record of leading enterprise tech modernizations (PHP 8.2.10 → 8.5.9, Laravel 8 → 13.39.0, MariaDB 10.x → 12.3.3-MariaDB across 342+ tables with 0.34ms latency) and architecting agentic AI pipelines using Human & Agentic Development.",
    "stats": [
        {"value": "9+", "label": "Years Exp"},
        {"value": "1st Rank", "label": "BrowserStack Winner ($105)"},
        {"value": "100K+", "label": "Users Served"},
        {"value": "342+", "label": "Tables Upgraded (MariaDB 12.3)"},
        {"value": "8+", "label": "AI Applications"}
    ],
    "skills": {
        "AI & Agentic SDLC": ["Antigravity Agentic Workflows", "Human & Agentic Development", "Multi-Agent Systems", "LangGraph", "Ollama & Llama", "LangChain", "Gemini API", "Claude API", "RAG Architectures"],
        "Backend & Security": [".NET Core & C#", "Zero-Trust Architecture", "PHP 8.5.9 & Laravel 13.39.0", "Python (FastAPI, Flask)", "Mobile OTP & SMS Gateways", "REST/SOAP APIs"],
        "Frontend & UI/UX": ["Angular (SPA)", "Bootstrap 5", "TypeScript", "Dynamic Autocomplete Lexers ('#' tagging)", "SignalR / WebSockets", "Responsive Dark/Light UI"],
        "Databases & Procedures": ["SQL Server (Strict Stored Procedures)", "MariaDB 12.3.3 & MySQL", "PostgreSQL", "ChromaDB Vector DB", "Optimized Stored Procedures (342+ Tables)"],
        "DevOps & Governance": ["User Activity Telemetry & Audit Logs", "Microsoft-IIS/10.0 (FastCGI)", "Docker", "Git CI/CD", "Pentaho BI & Tableau"]
    },
    "projects": [
        {
            "id": "support-task-dashboard",
            "tab_title": "Support Task Dashboard — Automated Email Intelligence & Work Tracking",
            "title": "Support Task Dashboard — Automated Email Intelligence & Work Tracking",
            "badge": "Project #1 • Enterprise Office Work • Human & Agentic Development",
            "is_office_work": True,
            "development_mode": "Human & Agentic Development",
            "confidentiality_note": "Enterprise Office Work: Proprietary internal client workflows protected under NDA. Engineered with Human & Agentic Development.",
            "tagline": "Automated email ingestion, local LLM parsing, PostgreSQL tracking, interactive dashboard portal, and pivoted Excel daily work sheets — running entirely via Docker on local machine only for 100% privacy.",
            "video_url": "Mail_Read_Every_Set_cron_using_ollama_llama_postgressql.mp4",
            "video_title": "Support Task Dashboard Project Demo (Python + Ollama + Llama + PostgreSQL + LangGraph on Local Docker)",
            "presentation_url": "RSOS_AI_Task_Automation_Executive_Presentation.pptx",
            "presentation_view_url": "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Frohitjain-resume.vercel.app%2Fstatic%2FRSOS_AI_Task_Automation_Executive_Presentation.pptx",
            "presentation_title": "RSOS AI Task Automation Executive Presentation",
            "presentation_pdf_url": "RSOS_AI_Task_Automation_Executive_Presentation.pdf",
            "presentation_slides": [f"images/presentation/slide_{i}.jpg" for i in range(1, 15)],
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
            "tab_title": "RSOS Tech Upgrade (PHP 8.5 • Laravel 13 • MariaDB 12)",
            "title": "RSOS Dual-Stream & On-Demand Enterprise Portal — Major Tech Stack Upgrade & Modernization",
            "badge": "Project #3 • Enterprise Office Work • Human & Agentic Development",
            "tagline": "Full-scale modern architecture upgrade: PHP 8.2.10 → 8.5.9, Laravel 8 → 13.39.0, MariaDB 10.x → 12.3.3-MariaDB across 342 relational tables (0.34ms latency) on Windows Server IIS FastCGI, serving 100,000+ candidates.",
            "is_office_work": True,
            "development_mode": "Human & Agentic Development",
            "confidentiality_note": "Enterprise Office Work: Proprietary internal client identifiers protected under NDA. Engineered via collaborative Human & Agentic Development.",
            "image_url": "images/system_tech_stack_architecture_upgrade.png",
            "image_title": "System Tech Stack & Architecture — Live Production Telemetry (PHP 8.5.9 • Laravel 13.39.0 • MariaDB 12.3.3-MariaDB)",
            "video_url": None,
            "presentation_url": None,
            "summary": "Architected and executed an end-to-end enterprise modernization and stack migration for the Rajasthan State Open School (RSOS) mission-critical admission & examination platform serving 100,000+ candidates. Successfully upgraded legacy PHP 8.2.10 to PHP 8.5.9, transitioned from Laravel 8 to Laravel 13.39.0, and migrated the database from MariaDB 10.x to 12.3.3-MariaDB with 342 normalized tables running at 0.34ms query latency on Microsoft-IIS/10.0 FastCGI. Engineered utilizing Human & Agentic Development workflows—combining senior human software architecture with multi-agent code analysis, automated schema verification, and regression test suites.",
            "highlights": [
                "Major Tech Stack Modernization (PHP 8.5.9 & Laravel 13.39.0): Upgraded the legacy core from PHP 8.2.10 to PHP 8.5.9 and Laravel 8 to modern Laravel 13.39.0 with zero schema regression.",
                "Database Migration to MariaDB 12.3.3: Upgraded and tuned 342 relational tables from MariaDB 10.x to 12.3.3-MariaDB, achieving sub-millisecond query latency (0.34 ms) on Windows Server IIS FastCGI.",
                "Human & Agentic Development Collaboration: Employed multi-agent AI code reviewers and unit-test generators paired with human architectural oversight to safely refactor legacy modules and queries.",
                "100,000+ Active Candidates: High-concurrency state platform managing statewide admissions, verification, automated seat allotment, and hall-ticket generation.",
                "50% Speedup via Optimized Stored Procedures: Slashed result computation and tabulation generation times by 50% via optimized relational queries and indexing.",
                "Enterprise FastCGI on Windows IIS 10.0: Configured high-throughput native Windows Server IIS 10.0 FastCGI runtime with 300s execution limits and low memory footprint (10MB)."
            ],
            "skills_explained": [
                {
                    "name": "PHP 8.5.9 Engine",
                    "badge": "Modern PHP Core",
                    "icon": "bi-code-slash",
                    "desc": "Upgraded from PHP 8.2.10 to 8.5.9 on cgi-fcgi runtime with 128M memory limit and 300s execution budget, optimizing memory usage to 10MB."
                },
                {
                    "name": "Laravel 13.39.0",
                    "badge": "Next-Gen MVC Core",
                    "icon": "bi-layers-fill",
                    "desc": "Upgraded from Laravel 8 to Laravel 13.39.0, modernizing dependency management, service providers, middleware pipelines, and queue workers."
                },
                {
                    "name": "MariaDB 12.3.3 (342 Tables)",
                    "badge": "0.34ms Query Latency",
                    "icon": "bi-database-fill",
                    "desc": "Migrated 342 normalized tables from MariaDB 10.x to 12.3.3-MariaDB with optimized InnoDB buffer pooling and sub-millisecond latency."
                },
                {
                    "name": "Human & Agentic Development",
                    "badge": "Collaborative AI SDLC",
                    "icon": "bi-robot",
                    "desc": "Applied AI agent orchestration for automated syntax refactoring, unit test generation, and SQL query analysis with human architectural validation."
                },
                {
                    "name": "Windows Server IIS 10.0 (FastCGI)",
                    "badge": "Native High-Throughput",
                    "icon": "bi-hdd-network-fill",
                    "desc": "Configured enterprise FastCGI handler on Microsoft-IIS/10.0 on Windows Server 11, delivering resilient high-concurrency request processing."
                },
                {
                    "name": "MySQL Stored Procedures",
                    "badge": "50% Result Speedup",
                    "icon": "bi-lightning-charge-fill",
                    "desc": "Designed complex stored procedures and database triggers that cut state-wide result generation and marksheet generation times by 50%."
                }
            ]
        },
        {
            "id": "ecourt-highcourt-gateway",
            "tab_title": "E-Court & High Court Gateway",
            "title": "E-Court & High Court Secure Inter-Agency API Integration",
            "badge": "Project #4 • Enterprise Office Work • Human & Agentic Development",
            "is_office_work": True,
            "development_mode": "Human & Agentic Development",
            "confidentiality_note": "Enterprise Office Work: Judicial and state department endpoints anonymized under statutory government privacy rules. Delivered via Human & Agentic Development.",
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
        },
        {
            "id": "enterprise-grievance-portal",
            "tab_title": "Enterprise Grievance & Collaborative Task Platform (.NET Core • Angular)",
            "title": "Enterprise Grievance & Collaborative Task Platform (GrievancePortal)",
            "badge": "Project #5 • Enterprise Office Work • .NET Core & Angular • Zero-Trust & Antigravity Agentic SDLC",
            "is_office_work": True,
            "development_mode": "Human & Agentic Development (Antigravity Workflows)",
            "confidentiality_note": "Enterprise Office Work: Proprietary government/client department identifiers protected under NDA. Engineered via Human & Agentic Development using Google DeepMind Antigravity AI workflows.",
            "image_url": "images/enterprise_grievance_portal_architecture.png",
            "image_title": "Enterprise Grievance Portal — Topology, Workspace & Zero-Trust Navigation Architecture",
            "image_subtitle": "Enterprise .NET Core & Angular Architecture • SQL Server Stored Procedures • Zero-Trust Auth • Mobile OTP",
            "image_metrics": [
                {"label": "Backend Core", "value": ".NET Core (C#)", "sub": "Zero-Trust Web API", "color": "text-info"},
                {"label": "Frontend SPA", "value": "Angular & Bootstrap", "sub": "Dynamic '#' Cross-Linking", "color": "text-danger"},
                {"label": "Database Engine", "value": "SQL Server", "sub": "Strict Stored Procedures", "color": "text-success"},
                {"label": "SDLC & Security", "value": "Antigravity AI", "sub": "Mobile OTP & Audit Logs", "color": "text-warning"}
            ],
            "video_url": None,
            "presentation_url": None,
            "tagline": "Full-stack enterprise governance system architected with .NET Core, Angular, Bootstrap, and SQL Server. Enforces strict zero-trust stored procedure security with multi-factor mobile OTP authentication, n-level client grievance lifecycle tracking, collaborative daily task boards, real-time in-house team chat with dynamic '#' cross-linking, organization topology trees, and granular user activity audit logs—built via Antigravity Agentic AI workflows.",
            "summary": "Architected and delivered an enterprise-grade Grievance Management and Collaborative In-House Task Platform engineered for government departments and large enterprise clients. Built from the ground up on a Zero-Trust security paradigm using .NET Core Web API, Angular reactive SPA, Bootstrap, and SQL Server with 100% strict stored procedure execution. Solved critical enterprise operational challenges: disconnected grievance intake, lack of SLA visibility across multi-tier resolution hierarchies, fragmented internal team communication, and vulnerable direct database mutations. Features dynamic '#' auto-suggest mechanism unifying chats, grievances, and daily tasks; multi-role access controls (Clients, Staff, Admins, Super Admins); mobile OTP authentication; real-time team whiteboard (canvas-pad); and comprehensive immutable user activity audit logs.",
            "case_study": {
                "executive_summary": "In high-stakes public sector and enterprise environments, grievance handling and internal task execution typically suffer from siloed systems, opaque SLAs, delayed cross-department escalations, and severe security risks from direct database tampering. This platform resolves these operational bottlenecks by unifying citizen/client grievance reporting with internal operational workflows into a single high-performance, role-gated platform. Engineered using Google DeepMind Antigravity agentic workflows, the system establishes clear accountability through n-level resolution workflows, automated SMS/OTP verification, dynamic cross-entity referencing, and complete auditable activity trails.",
                "problem_solved": [
                    "Eliminated fragmented communication: Unified client-facing grievance reporting with in-house team execution, whiteboard ideation, and live chats into one integrated workspace.",
                    "Slashed escalation latency: Replaced manual email/paper handoffs with automated n-level escalation triggers, departmental priority queues, and real-time SLA tracking.",
                    "Guaranteed Zero-Trust security: Closed all SQL injection attack surfaces by enforcing 100% strict stored procedure execution—prohibiting any ad-hoc runtime SQL or insecure ORM generation.",
                    "Overcame context-switching friction: Introduced an innovative dynamic '#' cross-linking engine allowing team members to link grievances, tasks, and project nodes directly from chat messages in real time.",
                    "Secured Identity & Access: Deployed multi-factor mobile OTP authentication, departmental role mapping, and detailed user activity audit logging for compliance."
                ],
                "core_architecture": [
                    "Backend (.NET Core / C# Clean Architecture): Asynchronous Web API controllers utilizing MediatR CQRS pattern, FluentValidation, and dependency-injected security handlers delivering sub-millisecond execution.",
                    "Database (SQL Server Strict Stored Procedures): Zero-Trust database design where application database credentials lack direct table SELECT/INSERT/UPDATE/DELETE permissions; all operations execute strictly via encrypted, parameterized stored procedures with table locks and ACID transactions.",
                    "Frontend (Angular & Bootstrap): Modular Single-Page Application (SPA) structured with reactive state services, RxJS pipelines, custom directive lexers for '#' parsing, and responsive dark-mode UI.",
                    "Identity & Zero-Trust Auth: Multi-Factor Authentication (MFA) via SMS Mobile OTP gateway, JWT bearer tokens with refresh rotation, and fine-grained Role-Based Access Control (RBAC) across Super Admin, Admin, Department Managers, Staff, and Clients.",
                    "Audit Telemetry & Activity Logging: Comprehensive activity log subsystem (/settings?tab=ACTIVITIES) recording IP address, timestamp, affected entity, user ID, and delta payload for every state change."
                ],
                "innovative_ux": [
                    "Dynamic '#' Auto-Suggest & Cross-Linking: In-house Angular directive and token lexer that detects '#' keypresses in team chats, whiteboards, and notes—displaying an instant overlay menu to auto-complete and hyper-link grievances (#GRV-XXXX), daily tasks (#TSK-XXXX), and project masters.",
                    "Real-Time In-House Team Chat (/inhouse-chat): Low-latency WebSocket/SignalR bidirectional communication keeping cross-functional teams aligned on active ticket escalations.",
                    "Interactive Whiteboard Canvas-Pad (/canvas-pad): Collaborative digital whiteboard for architecture brainstorming, flowcharting, and incident triage directly within the team workspace.",
                    "Organization & Topology Graph (/topology/projects & /topology/roles): Visual structural mapping rendering hierarchical relationships between clients, departments, projects, and active personnel."
                ],
                "engineering_methodology": [
                    "Antigravity Agentic AI Workflows: Accelerated development by 4x using specialized multi-agent coding workflows in Google DeepMind Antigravity—orchestrating AI agents for domain modeling, stored procedure synthesis, TypeScript interface generation, and automated edge-case validation.",
                    "Strict Stored Procedure Code Review Agents: Employed automated AI security review agents to inspect every SQL Server stored procedure for execution plan efficiency, parameter sniffing guards, and missing indexes.",
                    "Unit & Integration Test Automation: Generated end-to-end unit test suites for .NET Core controllers and Angular component harnesses using AI agent pairing with human architectural sign-off."
                ],
                "measurable_outcomes": [
                    {"metric": "45%", "label": "Resolution Time Reduction", "desc": "Slashed end-to-end grievance resolution turnaround from 14 days to under 7.7 days via automated n-level routing."},
                    {"metric": "0", "label": "SQL Injection Surface", "desc": "100% strict stored procedure policy resulted in zero vulnerability findings during comprehensive VAPT audits."},
                    {"metric": "60%", "label": "Context-Switching Saved", "desc": "Dynamic '#' cross-linking in chat eliminated tool hopping between separate chat apps, ticket managers, and task boards."},
                    {"metric": "100%", "label": "Immutable Audit Coverage", "desc": "Every single status transition, login, and assignment cryptographically logged for statutory compliance."}
                ]
            },
            "highlights": [
                "Full-Stack .NET Core & Angular Architecture: Enterprise-grade RESTful API backend paired with reactive Angular SPA, Bootstrap styling, and strict separation of concerns.",
                "Zero-Trust SQL Server Design: 100% strict parameterized stored procedures—application credentials have zero direct table DDL/DML permissions, eliminating SQL injection.",
                "Dynamic '#' Auto-Suggest Engine: Custom lexer and autocomplete overlay cross-linking grievances (#GRV), daily tasks (#TSK), and project masters inside real-time chats and notes.",
                "Client-Facing N-Level Grievance Tracking: Multi-tier escalation workflows with priority categorization, document attachments, and real-time resolution telemetry.",
                "In-House Collaborative Workspace: Integrated daily task boards, low-latency team chat (/inhouse-chat), digital whiteboard (/canvas-pad), and scratch notes (/todos).",
                "Mobile OTP Authentication & SMS Gateways: Secure multi-factor authentication with mobile phone OTP verification and configurable gateway provider settings.",
                "Organization Topology & Hierarchy Graphs: Interactive graphical tree mapping departments, projects, client entities, and personnel role distributions.",
                "Immutable Activity Logs & Audit Trails: Comprehensive activity telemetry capturing user actions, IP addresses, timestamps, and state transitions (/settings?tab=ACTIVITIES).",
                "Built with Antigravity Agentic AI Workflows: Developed using multi-agent engineering workflows—accelerating feature delivery, stored procedure verification, and test coverage."
            ],
            "skills_explained": [
                {
                    "name": ".NET Core (C#) Web API",
                    "badge": "Enterprise Backend",
                    "icon": "bi-code-slash",
                    "desc": "Built high-performance asynchronous RESTful APIs, dependency injection containers, MediatR CQRS handlers, and secure token validation middleware."
                },
                {
                    "name": "Angular & Bootstrap SPA",
                    "badge": "Reactive Frontend",
                    "icon": "bi-layers-fill",
                    "desc": "Crafted modular component architecture with RxJS observables, dynamic '#' autocomplete directives, and responsive dark-theme Bootstrap UI."
                },
                {
                    "name": "SQL Server (Strict Stored Procedures)",
                    "badge": "Zero-Trust DB Tier",
                    "icon": "bi-database-fill",
                    "desc": "Engineered 100% parameterized stored procedures, transaction locks, and indexed tables—disallowing all direct SQL table mutation permissions."
                },
                {
                    "name": "Dynamic '#' Cross-Linking Lexer",
                    "badge": "UI/UX Innovation",
                    "icon": "bi-hash",
                    "desc": "Developed a custom in-app parser detecting hashtag triggers to seamlessly reference and deep-link grievances, tasks, and projects in chats."
                },
                {
                    "name": "Mobile OTP & Zero-Trust Auth",
                    "badge": "Identity & Security",
                    "icon": "bi-shield-lock-fill",
                    "desc": "Implemented multi-factor SMS OTP authentication, role-based access control (RBAC), and session timeouts across client and staff roles."
                },
                {
                    "name": "Antigravity Agentic SDLC",
                    "badge": "Agentic AI Engineering",
                    "icon": "bi-robot",
                    "desc": "Orchestrated AI coding agents in Google DeepMind Antigravity for automated schema design, stored procedure optimization, and test automation."
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
            "type": "Onsite / In-Person Event",
            "badge": "🏆 Top 5 Contest Winner",
            "achievement": "🏆 Top 5 Winner — Social Media Contest at Claude Community Jaipur Meetup Launch (Award presented on stage by Jason Sears, Origin Chicago)",
            "date": "Saturday, October 24, 2026 | 10:00 AM – 1:30 PM IST",
            "location": "JECRC Foundation, Jaipur, Rajasthan",
            "organizer": "Claude Community Jaipur in collaboration with Jaipur Data & AI Community (Sponsored by ORIGIN | Panellists: Jagmohan Rathore, Jobin Ephrem, Stuart Brown, Jaideep Singh, Arpit Bhargava | Award Presenter: Jason Sears - Engineering Lead, Origin Chicago)",
            "event_url": "https://luma.link/XxRFO63oFj",
            "ticket_url": "https://luma.link/rXSoj2F9sT",
            "map_url": "https://luma.link/7cBc9mWN8q",
            "linkedin_post": "https://www.linkedin.com/feed/update/urn:li:ugcPost:7519990052261625856/?openCollaboratorList=false",
            "post_content": "🏆 Honored to win the Social Media Contest (Top 5) at the Claude Community Jaipur Meetup launch! A huge thank you to Jason Sears (Origin) for presenting the award, and to everyone who engaged with my posts. Spent an electric Saturday morning at JECRC with 100+ builders discussing Enterprise Data and Agentic AI. My biggest takeaway? The future isn't humans vs. agents—it's humans WITH agents. The AI-native SDLC is already transforming how we plan, code, and deploy.",
            "images": [
                "images/claude_event_1.jpg",
                "images/claude_event_5.jpg",
                "images/claude_event_3.jpg",
                "images/claude_event_2.jpg",
                "images/claude_event_4.jpg",
                "images/claude_event_6.jpg"
            ],
            "learnings": [
                "🏆 Social Media Contest Winner (Top 5): Honored on stage with official Origin & Claude Community Jaipur award and swag kit presented directly by Jason Sears (Engineering Lead, Origin Chicago).",
                "Enterprise Data & Agentic AI: Engaged in deep technical sessions with 100+ builders on scaling enterprise workflows and navigating the transition from ad-hoc prompting to robust agentic architectures.",
                "The AI-Native SDLC (Humans WITH Agents): Explored the paradigm where autonomous agents collaborate with software engineers across planning, architecture, coding, unit testing, and deployment.",
                "Claude Code & Anthropic Model Context Protocol (MCP): Practical insights on MCP server architecture, prompt caching economics, and multi-agent systems from international engineering leaders."
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
            "organizer": "BrowserStack Community Team – Jaipur (Hosted at Metacube Software Pvt. Ltd.)",
            "post_content": "Jaipur #Testathon, that's a wrap! 🚀 Huge congratulations to our winners who put their testing skills to the test and came out on top: 🥇 First Place: Rohit Jain, 🥈 Second Place: Satvik Choudhary, 🥉 Third Place: Bhomesh Razdan — BrowserStack Official Announcement",
            "images": [
                "images/browserstack_winner_announcement.jpg",
                "images/browserstack_reward_usd105.jpg"
            ],
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
                "Lead Developer for RSOS Dual-Stream & On-Demand Admission Portal — Architected major stack modernization: PHP 8.2.10 → 8.5.9, Laravel 8 → 13.39.0, and MariaDB 10.x → 12.3.3-MariaDB across 342 tables with 0.34ms latency.",
                "Spearheaded enterprise office work projects leveraging collaborative Human & Agentic Development methodologies.",
                "Architected full SDLC for a platform serving 100,000+ candidates.",
                "Engineered automated seat-allotment modules, cutting processing time by 40%.",
                "Implemented RBAC for 15+ user roles, achieving zero unauthorized access incidents.",
                "Deployed Ollama for AI code-assistance, reducing manual code-reviews by 30%.",
                "Integrated Gemini and Claude APIs into VS Code, reducing debugging time by 25%.",
                "Piloting Agentic AI workflows (n8n, LangChain) and .NET Core microservices."
            ]
        },
        {
            "role": "Software Developer",
            "company": "DevIT Solutions Pvt. Ltd.",
            "period": "February 2020 – April 2024",
            "details": [
                "Delivered large-scale government portals serving 50,000+ daily users in Rajasthan.",
                "Secured High Court/E-Court API integrations using AES encryption and tokens.",
                "Reduced RSOS result-generation time by 50% via optimized MySQL stored procedures.",
                "Built Paramedical Council seat-matrix algorithms with 99.9% accuracy.",
                "Designed Pentaho and Tableau BI dashboards for real-time reporting on 10+ KPIs.",
                "Managed full SDLC across Laravel, CakePHP, CodeIgniter, MySQL, and MSSQL."
            ]
        },
        {
            "role": "Software Developer",
            "company": "Akal Information Systems Ltd.",
            "period": "October 2017 – January 2020",
            "details": [
                "Developed enterprise web applications for government and corporate clients.",
                "Contributed to complex API integrations and database optimization projects.",
                "Collaborated with cross-functional teams to meet aggressive delivery timelines."
            ]
        },
        {
            "role": "Junior Software Developer",
            "company": "Vertex Plus Software Pvt. Ltd.",
            "period": "August 2016 – October 2017",
            "details": [
                "Built responsive web applications and client portals using PHP and Bootstrap.",
                "Gained foundational expertise in SOAP and REST API consumption."
            ]
        },
        {
            "role": "Junior Developer",
            "company": "On-Graph Technologies Pvt. Ltd.",
            "period": "December 2015 – August 2016",
            "details": [
                "Developed CMS-driven websites and community portals.",
                "Integrated SMS gateways and real-time notification systems."
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

@app.route('/og-image.jpg')
def og_image():
    return send_from_directory('static', 'og-image.jpg')

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