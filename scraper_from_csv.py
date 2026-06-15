# quick_add_to_rag.py
"""
Shortcut to add new info to RAG without re-scraping.
Step 1: Appends new records to ssuet_pages.jsonl
Step 2: Rebuilds the FAISS index from the updated JSONL
"""

import json
import time
import hashlib
import os

DATA_DIR = "rag_data"
OUTPUT_FILE = os.path.join(DATA_DIR, "ssuet_pages.jsonl")

# ---------------------------------------------------------------
# ADD YOUR NEW CONTENT HERE — just copy-paste and fill in fields
# ---------------------------------------------------------------
new_records = [
    {
        "url": "https://www.ssuet.edu.pk/admissions/undergraduate-admissions/",
        "title": "Fall 2026 UG Admissions – SSUET",
        "content": """Fall 2026 Undergraduate Admissions are NOW OPEN at SSUET.
Round 1 Application & Test Fee Submission Deadline: 17th July 2026 (Tentative).
Entry Test Schedule: 21st July 2026 Onwards (Tentative). Test Mode: On-Campus at SSUET.
Apply online at: admissions.ssuet.edu.pk
UG Programs Test Fee: Rs. 3,900/-
AIT Graduates (UG Programs): Rs. 1,000/- (collect voucher from Admissions Office)
Test Exemption: Students who passed USAT, NEDUET, MUET, NTS, ETEA, MDCAT or any public sector university test in 2026 are exempt from entry test.
Eligibility: Must have passed HSC-II or equivalent. Minimum 60% for Engineering, 50% for Science/Technology/Business programs.
Payment: MCB branch or Paypro only. IBFT and Easypaisa are NOT allowed.
Required on test day: Admit Card, CNIC/B-Form, paid voucher, stationery, and calculator. Phones and smartwatches not allowed.
PhD admissions also open for Fall 2026: PhD Biomedical Engineering, PhD Computer Engineering, PhD Electronic Engineering.""",
    },
    {
        "url": "https://www.ssuet.edu.pk/academics/",
        "title": "New Programs at SSUET 2026",
        "content": """New and updated programs at Sir Syed University of Engineering and Technology (SSUET) for 2026:

FoCAS (Faculty of Computing and Applied Sciences):
- BS Artificial Intelligence (NEW)
- BS Cloud Computing and Information Sciences (CIS) (NEW)
- BS Game Engineering (NEW)
- BS Cyber Security (CySec) (NEW)
- BS Data Science (NEW)
- BS Clinical Psychology (NEW)
- BS Economics and Mathematics (NEW)
- B.E Tech (Artificial Intelligence) (NEW)
- B.E Tech (Software) (NEW)

FoECE (Faculty of Electrical and Computer Engineering):
- BS Robotics and Intelligent Machines (NEW)
- BS Renewable Energy Systems (NEW)
- MS Climate Change and Environmental Informatics (NEW)

FoBMS (Faculty of Business Management and Social Sciences):
- BS Business Analytics (NEW)
- BS Digital Technology Management (NEW)
- BS Entrepreneurship (NEW)
- BBA 2.5 Years (NEW)

FoCVA (Faculty of Civil Engineering and Architecture):
- Bachelor of Interior Design (NEW)""",
    },
    {
        "url": "https://www.ssuet.edu.pk/scholarship-and-financial-assistance/",
        "title": "SSUET Scholarships Fall 2026",
        "content": """SSUET offers the following scholarships for Fall 2026:
- Merit-based scholarships for top 50 entry test rank holders
- Performance-based scholarships for continuing students
- Merit-cum-need based scholarships
- Siblings discount for families with multiple enrolled students
- Special discount for AIT graduates
For complete details visit: www.ssuet.edu.pk/scholarship-and-financial-assistance/
Admissions WhatsApp (messages only): 0304-2248985
Admissions email: admissions@ssuet.edu.pk""",
    },
]
# ---------------------------------------------------------------

def append_to_jsonl(records: list[dict], output_file: str):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(output_file, "a", encoding="utf-8") as f:
        for rec in records:
            # Add required fields if missing
            rec.setdefault("timestamp", time.time())
            rec.setdefault("hash", hashlib.md5(rec["content"].encode("utf-8")).hexdigest())
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"✅ Appended {len(records)} records to {output_file}")


def rebuild_index():
    """Import and re-run the RAG engine's index builder."""
    print("🔄 Rebuilding FAISS index from updated JSONL...")
    from rag_engine import SSUETRAG
    rag = SSUETRAG()
    # Force a rebuild — call whatever method loads from JSONL
    rag.build_index()   # <-- might be build_index(), load_data(), or similar
    print("✅ FAISS index rebuilt successfully!")


if __name__ == "__main__":
    append_to_jsonl(new_records, OUTPUT_FILE)
    rebuild_index()