# CLAUDE.md — Rohit Jain Portfolio & Resume Web Application

This file provides architecture instructions and context for **Claude Code** and **Claude Desktop** when working with this repository.

---

## 📌 Project Overview
- **Project Name:** Rohit Jain — Interactive Resume & AI Automation Portfolio
- **Live URL:** [https://rohitjain-resume.vercel.app/](https://rohitjain-resume.vercel.app/)
- **Repository Path:** `D:\projects\python\rohitjain-resume`
- **Owner:** Rohit Jain (Senior Full-Stack Developer & AI Automation Architect)

---

## 🛠️ Tech Stack & Architecture
- **Backend Framework:** Python (Flask), Gunicorn (Production WSGI)
- **Frontend:** HTML5, Jinja2 Templates, Bootstrap 5.3, Bootstrap Icons 1.11, Custom Responsive Bento Grid
- **Design System:** High-contrast dark theme (default) & clean light theme toggle with persistent CSS variables
- **Containerization:** Docker (`python:3.11-slim`), Docker Compose (multi-stage, port 7860)
- **Deployment & Hosting:** Vercel Serverless (`vercel.json`), GitHub (`main` branch)
- **SEO & AI Reference:** JSON-LD Schema.org, `static/llms.txt`, `robots.txt`, `sitemap.xml`

---

## 📂 Key Files & Directory Structure
```text
rohitjain-resume/
├── app.py                     # Main Flask entrypoint and complete user_data dictionary
├── templates/
│   └── index.html             # Single-page responsive bento-grid UI & modals
├── static/
│   ├── images/                # Profile photo, meetup photos, award proofs (BrowserStack, Claude Meetup, ATA)
│   ├── llms.txt               # AI engine & crawler documentation
│   ├── robots.txt             # Web crawler configuration
│   └── sitemap.xml            # Search engine sitemap
├── Dockerfile                 # Gunicorn container configuration (Exposes port 7860)
├── docker-compose.yml         # Local container orchestration (`rohitjain_resume_app`)
├── requirements.txt          # Python dependencies (flask, gunicorn)
├── vercel.json                # Vercel serverless routing configuration
└── CLAUDE.md                  # Claude Code & Claude Desktop context guide
```

---

## ⚡ Core Development & Deployment Commands

### 1. Local Python Development
```bash
# Run locally with Flask development server (http://127.0.0.1:5000)
python app.py
```

### 2. Local Docker Container (Port 7860)
```bash
# Build and start container in detached mode
docker compose up -d --build

# Verify container status
docker ps --filter "name=rohitjain_resume_app"

# Test local endpoint
curl http://localhost:7860/
```

### 3. Git Version Control
```bash
# Check status & commit changes
git status
git add .
git commit -m "Your descriptive commit message"
git push origin main
```

### 4. Deploy to Vercel Production
```bash
# Deploy latest commit directly to live production
npx vercel --prod --yes
```

---

## 🎨 UI & Layout Guidelines
1. **Section Order in Bento Grid:**
   - Sidebar Profile Card & Master Skills (Col 1)
   - Hero Card & Key Metrics Bar (Col 2–4)
   - Development Studio & Verified Google Location Map
   - Featured Engineering Projects (Tabbed Architecture)
   - **Tech Events & Community Participation (`#events`)**
   - **Autonomous Agentic AI Ecosystem (19 Specialized AI Agents)**
   - Professional Milestones & Career Timeline
2. **Spacing & Compactness:**
   - Avoid excessive whitespace or artificial `mt-auto` stretching.
   - Event info panels group Date, Venue, Organizer, and Action Badges into a single sleek card.
   - Thumbnails use `76x52px` with smooth hover zoom animations and open in full-screen modal zoom upon clicking.
3. **Data Integrity:**
   - Whenever updating honors, hackathon achievements, or events, ensure synchronization across:
     - `app.py` (`user_data["events"]` and `user_data["stats"]`)
     - `templates/index.html` (JSON-LD schema `award` list)
     - `static/llms.txt` (AI entity reference)
