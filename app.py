from flask import Flask, render_template

app = Flask(__name__,
static_folder='static',
template_folder='templates'
)

# Comprehensive User Data for Rohit Jain
user_data = {
    "header": {
        "name": "Rohit Jain",
        "title": "Senior Full-Stack Developer | AI Automation Architect",
        "location": "Jaipur, Rajasthan",
        "contact": [
            "+91 89469 19241",
            "engrohitjain5@gmail.com",
            "https://github.com/rislrohitjain/",
            "https://linkedin.com/in/rohit-jain-061571a3",
            "https://huggingface.co/spaces/rislrohitjain/"
        ],
        "resume_url": "static/Resume_Original_Rohit_Jain.pdf"  # Replace with actual file download link
    },
    "summary": "Results-driven Full-Stack Developer and AI Automation Architect with 9+ years of experience delivering high-impact government portals and enterprise systems serving 100,000+ users. Proven track record of cutting result generation time by 50% via optimized stored procedures[cite: 1].",
    "stats": [
        {"value": "9+", "label": "Years Exp"},
        {"value": "100K+", "label": "Users Served"},
        {"value": "50K+", "label": "Daily API Calls"},
        {"value": "8", "label": "AI Applications"}
    ],
    "skills": {
        "AI & LLM": ["Python Agentic AI", "Ollama", "LangChain", "Gemini API", "Claude", "RAG Systems", "ChromaDB Vector DB", "n8n"],
        "Backend": ["Python (Intermediate)", "FastAPI", "Flask", "PHP (Laravel/CakePHP)", ".NET Core Web API", "REST/SOAP APIs"],
        "Database": ["MySQL", "MSSQL", "ChromaDB Vector DB", "Stored Procedures"],
        "BI & DevOps": ["Pentaho", "Tableau", "Git", "Docker", "IIS"]
    },
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
            "title": "BrowserStack Testathon Jaipur 2026",
            "type": "Onsite / In-Person Event",
            "date": "Saturday, September 5, 2026 | 10:00 AM IST onwards",
            "location": "Metacube Software Pvt. Ltd., Sitapura Industrial Area, Jaipur",
            "organizer": "BrowserStack Community Team – Jaipur",
            "learnings": [
                "3-Hour Live Hackathon: Designed, documented, and built an end-to-end automated test suite for a live buggy web application under strict 3-hour time constraints.",
                "BrowserStack Suite Mastery: Gained hands-on experience using BrowserStack Automate (cross-browser/device execution), BrowserStack Test Management, Test Companion, and Test Observability for failure analysis.",
                "Framework & SDK Integration: Integrated Selenium/Playwright test scripts using BrowserStack SDK and published complete test repositories to GitHub."
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

@app.route('/')
def index():
    # Renders the separate resume.html file
    return render_template('index.html', user=user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)