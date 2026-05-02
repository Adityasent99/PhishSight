PhishSight 

A simple browser extension that inspects the URL for any common phishing signals and explains the risk. 

# Architecture: 

Chrome Extension (popup.html + popup.js)
↓
FastAPI Backend (main.py)
↓
Analyzer Pipeline (analyzer.py)
├── Entropy Calculator
├── Suspicious TLD Checker
└── Brand Impersonation Checker
↓
Risk Score + Explanation

## Tech Stack: 

- Backend:  Python, FastAPI
- Extension:  HTML, CSS, JavaScript
- Analysis: Custom rule-based pipeline 


 Running the project locally

**1. Clone the repo:**

```bash
git clone https://github.com/Adityasent99/PhishSight.git
cd PhishSight
```

**2. Set up the backend:**

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install fastapi uvicorn requests
cd backend
uvicorn main:app --reload
```

**3. Load the extension:**

- Open Chrome and go to `chrome://extensions`
- Enable Developer Mode
- Click Load unpacked and select the `extension` folder

**4. Test it:**

- Click the PhishSight icon in Chrome
- Paste any URL and hit Analyze
