# 💊 Drug Interaction Analyzer
> **Check drug interaction risks instantly using real FDA data.**

![Python](https://img.shields.io/badge/python-3.10.11-blue)
![Requests](https://img.shields.io/badge/Library-Requests-orange)
![FDA API](https://img.shields.io/badge/API-OpenFDA-red)
![OOP](https://img.shields.io/badge/Architecture-OOP-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Table of Contents

- [What Is This](#what-is-this)
- [Tools & Technologies](#tools--technologies)
- [Project Architecture](#project-architecture)
- [Application Workflow](#application-workflow)
- [Risk Logic](#risk-logic)
- [Exception Handling Strategy](#exception-handling-strategy)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)
- [Sample Output](#sample-output)
- [How to Run](#how-to-run)
- [Future Roadmap](#future-roadmap)
- [Author & Contact](#author--contact)

---

## What Is This?

**Drug Interaction Analyzer** is a Python command-line application that checks real-world drug interaction risks between any two drugs using live data from the **U.S. FDA OpenFDA API**.

Given two drug names, the app fetches their official FDA labels, extracts warnings, side effects, and drug interaction sections, cross-references them against each other, calculates a risk level, and generates a clean HTML report all automatically.

Built entirely in Python using Object-Oriented Programming, real API integration, and file handling. This project simulates a real-world clinical data pipeline in code.

> *"Are these two drugs safe to take together? Ask the analyzer."*

---

## Tools & Technologies

| Tool | Role |
|------|------|
| **Python 3.10.11** | Core programming language |
| **Requests** | HTTP calls to OpenFDA API |
| **OpenFDA API** | Real FDA drug label database |
| **JSON** | Data storage and retrieval |
| **OOP** | Class-based modular architecture |
| **HTML Generation** | Automated report writing |
| **Exception Handling** | Robust multi-level error management |

---

# Project Architecture

```
drug-interaction-analyzer/
│
├── drug_interaction.py       # Core application class (OOP)
│   ├── __init__()            # Takes user input for both drug names
│   ├── fetch_drug()          # Calls OpenFDA API and returns raw JSON
│   ├── save_data()           # Cleans & saves drug data to .json file
│   ├── comparison()          # Cross-references interaction sections
│   ├── generate_report()     # Creates result.html with full report
│   └── save_history()        # Appends search history to history.json
│
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

# Application Workflow

```
User enters Drug A name
User enters Drug B name
        │
        ▼
[ OpenFDA API Called ]
        │
        ▼
[ Raw JSON Response Received ]
        │
        ▼
[ Data Cleaned & Extracted ]
Warnings
Side Effects
Drug Interactions
Dosage Information
        │
        ▼
[ Data Saved ]
drug_a.json
drug_b.json
        │
        ▼
[ Cross-Reference Interaction Sections ]
- Does Drug A mention Drug B?
- Does Drug B mention Drug A?
        │
        ▼
[ Risk Level Calculated ]
High / Moderate / Low
        │
        ▼
[ HTML Report Generated ]
result.html
        │
        ▼
[ History Saved ]
history.json
```

## Risk Logic

The risk level is determined by **cross-referencing official FDA drug interaction labels** — not hardcoded rules.

| Condition | Risk Level |
|-----------|------------|
| Drug A's label mentions Drug B **AND** Drug B's label mentions Drug A | 🔴 High Risk |
| Only one label mentions the other drug | 🟡 Moderate Risk |
| Neither label mentions the other drug | 🟢 Low Risk |

> This works dynamically for **any drug** — no hardcoded drug names or aliases needed.

---

## Exception Handling Strategy

| Scenario | Handling |
|----------|----------|
| No internet connection | `ConnectionError` → clear message printed |
| Server timeout | `Timeout` → user informed to retry |
| API returns non-200 status | Status code printed, `None` returned |
| Drug not found in FDA database | Checked before processing |
| Data is not a list | Type validation before extraction |
| Empty results from API | Caught and reported |
| Unexpected request error | General `RequestException` handler ✅ |

---

## Sample Output

> **Example Input:** Panadol and Ibuprofen
<p align="center">
  <img src="https://github.com/genome-miner/drug_interaction_analyzer/blob/main/Image.png?raw=true" alt="Alt text" width="850">
</p>

## Key Concepts Demonstrated

1. **REST API Integration** — Live calls to OpenFDA with dynamic query building
2. **Object-Oriented Programming** — Clean single-class architecture with separation of concerns
3. **JSON File Handling** — Reading, writing, and appending structured data
4. **Data Cleaning** — Normalizing inconsistent API responses (lists vs strings)
5. **Cross-Reference Logic** — Dynamic drug interaction detection without hardcoding
6. **HTML Report Generation** — Automated professional report writing with f-strings
7. **Exception Handling** — Multi-level error management for network and data issues
8. **History Tracking** — Persistent search log with date stamping

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/drug-interaction-analyzer.git
cd drug-interaction-analyzer
```

**2. Install required library:**
```bash
pip install -r requirements.txt
```

**3. Run:**
```bash
python main.py
```

**4. How to use:**
- Enter **Drug A** name when prompted (e.g. `panadol`)
- Enter **Drug B** name when prompted (e.g. `ibuprofen`)
- Program fetches FDA data automatically
- Open **`result.html`** in your browser to view the full report
- Search history saved automatically to **`history.json`**

---

## Future Roadmap

| Feature | Description |
|---------|-------------|
| 🖥️ GUI Interface | Tkinter or Flask web interface instead of command line |
| 💊 Multi-drug Check | Compare more than 2 drugs simultaneously |
| 📄 PDF Export | Save the report as a downloadable PDF |
| 🔍 Generic Name Search | Search by generic name + brand name both |
| 📊 History Dashboard | Visual history of all past searches |

---

## Author & Contact

**Sana Aziz Sial**  
Biotechnologist and Bioinformatician
- 🎓 [University of Veterinary and Animal Sciences](https://www.uvas.edu.pk/)
- 📧 [Email](sanaazizsial@gmail.com)
- 🐙 [GitHub](https://github.com/genome-miner)
- 🔗 [LinkedIn](in/sana-aziz-sial-73b189265)

---

## License

This project is licensed under the [MIT License](https://github.com/genome-miner/drug_interaction_analyzer/blob/main/LICENSE).

---
<div align="center">

⭐ If you found this useful, consider giving it a star!
