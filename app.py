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
            "github.com/rislrohitjain/",
            "linkedin.com/in/rohit-jain-061571a3"
        ],
        "resume_url": "static/Resume Original Rohit Jain.pdf"  # Replace with actual file download link
    },
    "summary": "Results-driven Full-Stack Developer and AI Automation Architect with 9+ years of experience delivering high-impact government portals and enterprise systems serving 100,000+ users. Proven track record of cutting result generation time by 50% via optimized stored procedures[cite: 1].",
    "stats": [
        {"value": "9+", "label": "Years Exp"},
        {"value": "100K+", "label": "Users Served"},
        {"value": "50K+", "label": "Daily API Calls"}
    ],
    "skills": {
        "AI & LLM": ["Ollama", "Gemini API", "Claude", "n8n", "Agentic Workflows"],
        "Backend": ["PHP (Laravel/CakePHP)", "Learn Python", "Learn .NET Core Web API", "REST/SOAP APIs"],
        "Database": ["MySQL", "MSSQL", "Stored Procedures"],
        "BI & DevOps": ["Pentaho", "Tableau", "Git", "Docker", "IIS"]
    },
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
    app.run(debug=True)