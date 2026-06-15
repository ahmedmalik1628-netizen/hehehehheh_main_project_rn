"""
insert_admission_policy_pdf.py
-------------------------------
Inserts all data from SSUET UG Admission Policy 2025-26 PDF
into rag_data/ssuet_pages.jsonl, then rebuilds the FAISS index.

Run: python insert_admission_policy_pdf.py
"""

import json
import os

DATA_DIR = "rag_data"
OUTPUT_FILE = os.path.join(DATA_DIR, "ssuet_pages.jsonl")
PDF_URL = "https://www.ssuet.edu.pk/wp-content/uploads/UG-Admission-Policy-2025-26.pdf"

new_records = [

    # ----------------------------------------------------------------
    # POLICY OVERVIEW
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET UG Admission Policy 2025-26 Overview",
        "content": (
            "SSUET Undergraduate Programs Admission Policy 2025-2026. "
            "Policy Number: SSUET/P/Acad. Approval Date: 16th September 2025. "
            "Effective Date: July 2025. Date of Issue: 30th September 2025. Total Pages: 31. "
            "Prepared by: Ms. Aneela Mansoor (Manager Admissions) and Prof. Dr. Tahir Qadri (Convenor Admissions Committee). "
            "Reviewed by: DQEC, Dean Faculty of ECE, Dean Faculty of CVA, Registrar. Approved by: Vice Chancellor. "
            "SSUET is dedicated to maintaining the highest academic standards and ensuring fair and transparent admissions. "
            "This policy aligns with HEC guidelines and relevant accrediting councils. "
            "Admissions are open to all eligible applicants based on merit, regardless of caste, creed, color, culture, religion, gender, or domicile. "
            "Acceptance of an admission form does not guarantee admission; it is contingent on merit and seat availability."
        ),
        "timestamp": 1781149200.0,
        "hash": "policy_overview_2025"
    },

    # ----------------------------------------------------------------
    # ALL PROGRAMS OFFERED
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET All Undergraduate Programs 2025-26 – Complete List",
        "content": (
            "SSUET offers the following undergraduate programs for 2025-26:\n\n"
            "Faculty of Civil Engineering and Architecture (FoCVA):\n"
            "- Bachelor of Architecture (5 Years)\n"
            "- Bachelor of Interior Design (4 Years)\n"
            "- BS in Civil Engineering\n"
            "- BE Tech in Civil (Evening)\n\n"
            "Faculty of Electrical and Computer Engineering (FoECE):\n"
            "- BS in Biomedical Engineering\n"
            "- BS in Biotechnology\n"
            "- BS in Food Science and Technology\n"
            "- BS in Medical Technology (CLS & RI)\n"
            "- BS in Computer Engineering\n"
            "- BS in Electrical Engineering\n"
            "- BS in Electronic Engineering\n"
            "- BS in Telecommunication Engineering\n"
            "- BS in Computer Network and Security\n"
            "- BS in Robotics and Intelligent Machines\n"
            "- BS in Renewable Energy Systems\n"
            "- BE Tech in Electrical (Evening)\n"
            "- BE Tech in Computer (Morning)\n\n"
            "Faculty of Computing and Applied Sciences (FoCAS):\n"
            "- BS in Data Science\n"
            "- BS in Computer Science\n"
            "- BS in Information Technology\n"
            "- BS in Software Engineering\n"
            "- BS in Cyber Security\n"
            "- BS in Clinical Psychology\n"
            "- BS in Artificial Intelligence\n"
            "- BS in Cloud Computing and Information Sciences\n"
            "- BS in Game Engineering\n"
            "- BE Tech in Software (Morning)\n"
            "- BE Tech in Information (Morning)\n"
            "- BE Tech in Artificial Intelligence (Morning)\n\n"
            "Faculty of Business, Management and Social Sciences (FoBMS):\n"
            "- Bachelor of Business Administration (BBA 4 years)\n"
            "- Bachelor of Business Administration (BBA 2.5 years)\n"
            "- BS in Business & Information Technology\n"
            "- BS in Business & Data Analytics\n"
            "- BS in Digital Technology Management\n"
            "- BS in Entrepreneurship & Innovation"
        ),
        "timestamp": 1781149201.0,
        "hash": "all_programs_list_2025"
    },

    # ----------------------------------------------------------------
    # ELIGIBILITY CRITERIA – DETAILED PER PROGRAM
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Electrical, Electronic, Telecommunication, Civil Engineering",
        "content": (
            "For admission in BS Electrical, Electronic, Telecommunication, and Civil Engineering at SSUET: "
            "Applicants must have at least 60% marks in Intermediate (Pre-Engineering, General Science, Computer Science, "
            "Pre-Medical, or Equivalent A-level/relevant DAE). "
            "Those with Computer Studies, General Science, or Pre-Medical backgrounds who achieve 60% are also eligible, "
            "provided they pass a remedial Chemistry course in the first semester. "
            "Pre-Medical students must complete an 8-week university-conducted condensed program to make up for Mathematics "
            "and qualify for the admission process including the entry test. "
            "B.Tech (Pass)/B.Tech (Hons) holders in the relevant discipline with at least 60% marks are eligible for 2% reserved seats "
            "with exemption of one or two years as per PEC S.R.O. No. PEC/SRO/REE/43-44/21."
        ),
        "timestamp": 1781149202.0,
        "hash": "eligibility_electrical_civil_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Biomedical Engineering",
        "content": (
            "For admission in BS Biomedical Engineering at SSUET: "
            "Applicants must have at least 60% marks in Intermediate (Pre-Engineering OR Pre-Medical with Physics, Chemistry, "
            "and Mathematics OR Biology)/Equivalent A-level/relevant DAE. "
            "A combination of Physics, Mathematics, and Computer Studies/General Science with minimum 60% is also allowed, "
            "with Chemistry as a remedial subject to be passed in the first semester after admission."
        ),
        "timestamp": 1781149203.0,
        "hash": "eligibility_biomedical_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Computer Engineering",
        "content": (
            "For admission in BS Computer Engineering at SSUET: "
            "Applicants must have at least 60% marks in Intermediate (Pre-Engineering, General Science, Computer Science, "
            "Pre-Medical, or Equivalent A-level/relevant DAE). "
            "Pre-medical applicants must complete an 8-week university-conducted condensed program to compensate for "
            "deficient courses like Mathematics and qualify for the admission process including the entry test."
        ),
        "timestamp": 1781149204.0,
        "hash": "eligibility_computer_eng_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Software Engineering, Computer Science, IT, Data Science, Cyber Security, AI",
        "content": (
            "For admission in BS Software Engineering, Computer Science, Information Technology, Data Science, "
            "Cyber Security, and Artificial Intelligence at SSUET: "
            "Applicants must have at least 50% marks in Intermediate (Pre-Engineering, Pre-Medical, Computer Science), "
            "Commerce, A-levels, or DAE. "
            "For Pre-Medical and I.Com students, two deficiency courses in Mathematics of 6 credit hours will be taught."
        ),
        "timestamp": 1781149205.0,
        "hash": "eligibility_cs_se_it_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Food Science and Technology",
        "content": (
            "For admission in BS Food Science and Technology at SSUET: "
            "Applicants must have at least 50% marks in Intermediate (Pre-Engineering, Pre-Medical, Computer Science), "
            "A-levels, or DAE. "
            "For Computer Science students, Chemistry must be passed as a remedial subject in the first semester after admission."
        ),
        "timestamp": 1781149206.0,
        "hash": "eligibility_food_science_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Computer Network and Security, Robotics, Renewable Energy Systems",
        "content": (
            "For admission in BS Computer Network and Security, BS Robotics and Intelligent Machines, and "
            "BS Renewable Energy Systems at SSUET: "
            "Applicants must have at least 50% marks in Intermediate (Pre-Engineering, Pre-Medical, Computer Science), "
            "A-levels, or DAE. "
            "For Pre-Medical students, two deficiency courses in Mathematics of 6 credit hours will be taught."
        ),
        "timestamp": 1781149207.0,
        "hash": "eligibility_cns_robotics_renewable_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Biotechnology and Medical Technology",
        "content": (
            "For admission in BS Biotechnology and BS Medical Technology (CLS & RI) at SSUET: "
            "Applicants must have at least 45% marks in Intermediate (Pre-Engineering, Pre-Medical, Computer Science), "
            "A-levels, or DAE. "
            "For Computer Science students, Chemistry as a remedial subject must be passed in the first semester after admission."
        ),
        "timestamp": 1781149208.0,
        "hash": "eligibility_biotech_medtech_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Game Engineering and Cloud Computing and Information Sciences",
        "content": (
            "For admission in BS Game Engineering and BS Cloud Computing and Information Sciences at SSUET: "
            "Applicants must have at least 45% marks in Intermediate (Pre-Engineering, Pre-Medical, Computer Science, Commerce), "
            "A-levels, or DAE. "
            "For Pre-Medical and I.Com students, two deficiency courses in Mathematics of 6 credit hours will be taught."
        ),
        "timestamp": 1781149209.0,
        "hash": "eligibility_game_cloud_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BE Tech Programs (Electrical, Electronic, Software, Information, Civil, Computer, AI)",
        "content": (
            "For admission in BE Tech programs (Electrical, Electronic, Software, Information, Civil, Computer, "
            "Artificial Intelligence) at SSUET: "
            "Applicants must have at least 50% marks in Intermediate (Pre-Engineering, Pre-Medical, Computer Science), "
            "A-levels, or DAE. "
            "For Pre-Medical students, two deficiency courses in Mathematics of 6 credit hours will be offered. "
            "For General Science students with Mathematics, Statistics, and Computer Science, an additional Physics course "
            "(FSc level, as designed by HEIs) will be offered in the first semester."
        ),
        "timestamp": 1781149210.0,
        "hash": "eligibility_betech_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BBA, BS Business Programs",
        "content": (
            "For admission in BBA (4 years), BS Business & Information Technology, BS Business & Data Analytics, "
            "BS Digital Technology Management, and BS Entrepreneurship & Innovation at SSUET: "
            "Minimum 45% marks in Intermediate, A-level, or DAE in all disciplines. "
            "For BBA (2.5 years): BA/BSc/BCom/Associate degree or equivalent (14 years of education) with a minimum of 45% marks "
            "in both HSC/Equivalent and the 2-year graduate program in the discipline of Business. "
            "The candidate will be given an exemption of two years (around 60 credits), with some foundation semester courses assigned."
        ),
        "timestamp": 1781149211.0,
        "hash": "eligibility_bba_business_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Eligibility – BS Clinical Psychology and Bachelor of Architecture/Interior Design",
        "content": (
            "For admission in BS Clinical Psychology at SSUET: Minimum 50% marks in Intermediate, A-level, or DAE in all disciplines. "
            "For admission in Bachelor of Architecture and Bachelor of Interior Design at SSUET: "
            "Applicants must have at least 50% marks in Intermediate, A-levels, or relevant DAE. "
            "Note: Mathematics is a must at SSC/O-levels for Architecture and Interior Design."
        ),
        "timestamp": 1781149212.0,
        "hash": "eligibility_psych_arch_2025"
    },

    # ----------------------------------------------------------------
    # ENTRY TEST
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Entry Test Details 2025-26",
        "content": (
            "SSUET Admission Aptitude Test details for 2025-26: "
            "The entry test can be computer-based, online, or paper-based. "
            "The university reserves the right to change the test type without prior notification. "
            "Test format is based on the chosen group of study (Pre-Engineering, Pre-Medical, General Science, Commerce, Humanities). "
            "The test includes 100 MCQ questions with a time limit of 60 minutes. There is no negative marking. "
            "Applicants may attempt the test multiple times to improve their score; each additional attempt costs Rs. 1,500. "
            "Architecture applicants are assessed through a special aptitude test, drawing test, and interview conducted by the Architecture Department. "
            "All candidates who pass the test as per the set threshold qualify for program-wise merit calculations. "
            "The admission test registration and processing fee for all programs is Rs. 3,900."
        ),
        "timestamp": 1781149213.0,
        "hash": "entry_test_details_2025"
    },

    # ----------------------------------------------------------------
    # MERIT CALCULATION
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Merit Calculation Formula 2025-26",
        "content": (
            "SSUET merit determination for all undergraduate programs except Bachelor of Architecture and Interior Design: "
            "50% weightage – HSC-I/O-Level/Equivalent Examination Marks (10 marks added for Hafiz-e-Quran who pass the Hafiz test). "
            "5% weightage – SSC/O-Level/Equivalent Examination Marks. "
            "45% weightage – SSUET Admission Aptitude Test. "
            "For Bachelor of Architecture and Interior Design: "
            "50% weightage – HSC-I/O-Level/Equivalent marks. "
            "5% weightage – SSC/O-Level marks. "
            "45% weightage – SSUET Aptitude Test specially designed for Architecture by the Architecture Department. "
            "SSUET Drawing Test and Interview conducted by Architecture Department must also be passed. "
            "Tie resolution: ties are broken first by aptitude test aggregate marks, then by Core section marks "
            "(Physics/Biology/Computer Science/Business) and then English."
        ),
        "timestamp": 1781149214.0,
        "hash": "merit_calculation_2025"
    },

    # ----------------------------------------------------------------
    # HAFIZ-E-QURAN BENEFIT
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Hafiz-e-Quran Benefit 2025-26",
        "content": (
            "Applicants who are Hafiz-e-Quran are eligible for an additional 20 marks in HSC-I/Equivalent Examination Marks "
            "issued by IBCC for A-Level/Equivalent examination. "
            "This is subject to presentation of the original Sanad from Wifaq-ul-Madaris Arabia Pakistan. "
            "10 marks out of the 20 are added with HSC-I/O-Level marks for merit calculation on condition that the applicant passes the Hafiz-e-Quran Test. "
            "This addition is for merit determination only and does not affect eligibility criteria for admission."
        ),
        "timestamp": 1781149215.0,
        "hash": "hafiz_quran_benefit_2025"
    },

    # ----------------------------------------------------------------
    # SEATS & INTAKE – ALL PROGRAMS
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Program Seats and Intake 2025-26 – Complete Table",
        "content": (
            "SSUET program-wise total seats and intake session for 2025-26:\n"
            "BS Biomedical Engineering – 80 seats – Fall\n"
            "BS Civil Engineering – 200 seats – Fall\n"
            "BS Computer Engineering – 200 seats – Fall\n"
            "BS Electrical Engineering – 80 seats – Fall\n"
            "BS Electronic Engineering – 160 seats – Fall\n"
            "BS Telecommunication Engineering – 80 seats – Fall\n"
            "Bachelor of Architecture – 45 seats – Fall\n"
            "Bachelor of Interior Design – 100 seats – Fall & Spring\n"
            "BS Computer Science – 300 seats – Fall\n"
            "BS Information Technology – 100 seats – Fall\n"
            "BS Software Engineering – 300 seats – Fall\n"
            "BS Data Science – 50 seats – Fall\n"
            "BS Artificial Intelligence – 50 seats – Fall\n"
            "BS Cyber Security – 50 seats – Spring\n"
            "BS Biotechnology – 100 seats – Fall & Spring\n"
            "BS Food Science and Technology – 50 seats – Fall & Spring\n"
            "BS Medical Technology (CLS & RI) – 100 seats – Fall & Spring\n"
            "Bachelor of Business Administration (BBA) – 200 seats – Fall & Spring\n"
            "BBA 2.5 years – 50 seats – Fall & Spring\n"
            "BS Clinical Psychology – 50 seats – Fall & Spring\n"
            "BE Tech Civil – 80 seats – Fall & Spring\n"
            "BE Tech Electrical – 90 seats – Fall & Spring\n"
            "BE Tech Software – 80 seats – Fall & Spring\n"
            "BE Tech Computer – 80 seats – Fall & Spring\n"
            "BE Tech Information – 80 seats – Fall & Spring\n"
            "BE Tech Artificial Intelligence – 80 seats – Fall & Spring\n"
            "BS Computer Networks and Security – 200 seats – Fall & Spring\n"
            "BS Robotics and Intelligent Machines – 100 seats – Fall & Spring\n"
            "BS Renewable Energy Systems – 100 seats – Fall & Spring\n"
            "BS Game Engineering – 200 seats – Fall & Spring\n"
            "BS Cloud Computing and Information Sciences – 200 seats – Fall & Spring\n"
            "BS Business & Information Technology – 200 seats – Fall & Spring\n"
            "BS Business & Data Analytics – 100 seats – Fall & Spring\n"
            "BS Digital Technology Management – 100 seats – Fall & Spring\n"
            "BS Entrepreneurship & Innovation – 100 seats – Fall & Spring"
        ),
        "timestamp": 1781149216.0,
        "hash": "seats_intake_all_programs_2025"
    },

    # ----------------------------------------------------------------
    # SEAT CATEGORIES (OPEN MERIT / SELF-FINANCE / RESERVED)
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Seat Categories and Allocation 2025-26",
        "content": (
            "SSUET seat categories for 2025-26: Open Merit, Self-Finance, and Reserved (Employees, Spouse of Faculty/Staff, Sports, Sponsors). "
            "Open Merit seat allocation per program:\n"
            "BS Biomedical Engineering: 75 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Civil Engineering: 150 Open Merit, 45 Self-Finance, 5 Reserved\n"
            "BS Computer Engineering: 180 Open Merit, 15 Self-Finance, 5 Reserved\n"
            "BS Electrical Engineering: 75 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Electronic Engineering: 150 Open Merit, 0 Self-Finance, 10 Reserved\n"
            "BS Telecommunication Engineering: 70 Open Merit, 0 Self-Finance, 10 Reserved\n"
            "Bachelor of Architecture: 37 Open Merit, 5 Self-Finance, 3 Reserved\n"
            "Bachelor of Interior Design: 47 Open Merit, 0 Self-Finance, 3 Reserved\n"
            "BS Computer Science: 240 Open Merit, 45 Self-Finance, 15 Reserved\n"
            "BS Information Technology: 75 Open Merit, 15 Self-Finance, 10 Reserved\n"
            "BS Software Engineering: 240 Open Merit, 45 Self-Finance, 10 Reserved\n"
            "BS Data Science: 37 Open Merit, 10 Self-Finance, 3 Reserved\n"
            "BS Artificial Intelligence: 37 Open Merit, 10 Self-Finance, 3 Reserved\n"
            "BS Cyber Security: 37 Open Merit, 10 Self-Finance, 3 Reserved\n"
            "BS Biotechnology: 90 Open Merit, 5 Self-Finance, 5 Reserved\n"
            "BS Medical Technology: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Food Science and Technology: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BBA: 185 Open Merit, 5 Self-Finance, 10 Reserved\n"
            "BBA 2.5 years: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Clinical Psychology: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BE Tech Civil: 75 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BE Tech Electrical: 85 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BE Tech Software: 70 Open Merit, 5 Self-Finance, 5 Reserved\n"
            "BE Tech Computer: 70 Open Merit, 5 Self-Finance, 5 Reserved\n"
            "BE Tech Information: 75 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BE Tech Artificial Intelligence: 75 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Computer Networks and Security: 185 Open Merit, 0 Self-Finance, 15 Reserved\n"
            "BS Robotics and Intelligent Machines: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Renewable Energy Systems: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Game Engineering: 185 Open Merit, 0 Self-Finance, 15 Reserved\n"
            "BS Cloud Computing and Information Sciences: 185 Open Merit, 0 Self-Finance, 15 Reserved\n"
            "BS Business & Information Technology: 185 Open Merit, 0 Self-Finance, 15 Reserved\n"
            "BS Business & Data Analytics: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Digital Technology Management: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "BS Entrepreneurship & Innovation: 45 Open Merit, 0 Self-Finance, 5 Reserved\n"
            "If seats in non-open-merit categories are unfilled, they transfer to Open Merit for the same program."
        ),
        "timestamp": 1781149217.0,
        "hash": "seat_categories_allocation_2025"
    },

    # ----------------------------------------------------------------
    # FEE STRUCTURE – COMPLETE (FROM ANNEXURE A)
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Complete Fee Structure 2025-26 – All Programs (Batch 2025F First Semester)",
        "content": (
            "SSUET First Semester Fee Structure for Batch 2025F – Engineering, Computing, Science, Technology and Business Programs:\n\n"
            "All engineering/science programs (Admission Rs.35,000 | Security Deposit Rs.5,000 | Student Activity Rs.1,100 | Exam Rs.5,200 | Semester Reg Rs.11,500):\n"
            "BS Electronic Engineering: Tuition/CH Rs.6,600 | 17 CH | Tuition Rs.112,200 | Total Rs.170,000\n"
            "BS Biomedical Engineering: Tuition/CH Rs.6,600 | 15 CH | Tuition Rs.99,000 | Total Rs.156,800\n"
            "BS Civil Engineering: Tuition/CH Rs.6,600 | 17 CH | Tuition Rs.112,200 | Total Rs.170,000\n"
            "BS Electrical Engineering: Tuition/CH Rs.6,600 | 18 CH | Tuition Rs.118,800 | Total Rs.176,600\n"
            "BS Computer Engineering: Tuition/CH Rs.7,700 | 16 CH | Tuition Rs.123,200 | Total Rs.181,000\n"
            "BS Telecommunication Engineering: Tuition/CH Rs.3,250 | 16 CH | Tuition Rs.52,000 | Total Rs.104,050\n"
            "BS Computer Science: Tuition/CH Rs.7,700 | 16 CH | Tuition Rs.123,200 | Total Rs.181,000\n"
            "BS Information Technology: Tuition/CH Rs.7,700 | 16 CH | Tuition Rs.123,200 | Total Rs.181,000\n"
            "BS Software Engineering: Tuition/CH Rs.7,700 | 15 CH | Tuition Rs.115,500 | Total Rs.173,300\n"
            "BS Cyber Security: Tuition/CH Rs.7,700 | 15 CH | Tuition Rs.115,500 | Total Rs.173,300\n"
            "BS Data Science: Tuition/CH Rs.7,700 | 17 CH | Tuition Rs.130,900 | Total Rs.188,700\n"
            "BS Artificial Intelligence: Tuition/CH Rs.7,700 | 17 CH | Tuition Rs.130,900 | Total Rs.188,700\n"
            "BS Clinical Psychology: Tuition/CH Rs.5,400 | 18 CH | Tuition Rs.97,200 | Total Rs.155,000\n"
            "BS Biotechnology: Tuition/CH Rs.3,250 | 17 CH | Tuition Rs.55,250 | Total Rs.107,300\n"
            "BS Interior Design: Tuition/CH Rs.6,600 | 18 CH | Tuition Rs.118,800 | Total Rs.176,600\n\n"
            "Programs with Admission Rs.15,000 (lower admission fee):\n"
            "BS Computer Network & Security: Tuition/CH Rs.4,600 | 18 CH | Tuition Rs.82,800 | Total Rs.113,900\n"
            "BS Medical Technology: Tuition/CH Rs.3,500 | 17 CH | Tuition Rs.59,500 | Total Rs.86,600\n"
            "BS Robotics and Intelligent Machines: Tuition/CH Rs.4,600 | 17 CH | Tuition Rs.78,200 | Total Rs.109,300\n"
            "BS Renewable Energy Systems: Tuition/CH Rs.4,600 | 18 CH | Tuition Rs.82,800 | Total Rs.113,900\n"
            "BS Game Engineering: Tuition/CH Rs.4,400 | 17 CH | Tuition Rs.74,800 | Total Rs.105,900\n"
            "BS Cloud Computing & Information Sciences: Tuition/CH Rs.3,500 | 17 CH | Tuition Rs.59,500 | Total Rs.90,600\n"
            "BS Food Science & Technology: Tuition/CH Rs.3,500 | 17 CH | Tuition Rs.59,500 | Total Rs.86,600\n"
            "BBA: Tuition/CH Rs.4,700 | 17 CH | Tuition Rs.79,900 | Total Rs.111,000\n"
            "BS Business & IT: Tuition/CH Rs.4,700 | 17 CH | Tuition Rs.79,900 | Total Rs.111,000\n"
            "BS Business & Data Analytics: Tuition/CH Rs.5,400 | 18 CH | Tuition Rs.97,200 | Total Rs.128,300\n"
            "BS Digital Technology Management: Tuition/CH Rs.4,700 | 17 CH | Tuition Rs.79,900 | Total Rs.111,000\n"
            "BS Entrepreneurship & Innovation: Tuition/CH Rs.4,700 | 17 CH | Tuition Rs.79,900 | Total Rs.111,000\n"
            "BE Tech Computer: Tuition/CH Rs.4,600 | 18 CH | Tuition Rs.82,800 | Total Rs.111,900\n"
            "BE Tech Artificial Intelligence: Tuition/CH Rs.4,600 | 17 CH | Tuition Rs.78,200 | Total Rs.107,300\n"
            "BE Tech Software: Tuition/CH Rs.4,600 | 17 CH | Tuition Rs.78,200 | Total Rs.107,300\n"
            "BE Tech Electrical: Tuition/CH Rs.4,600 | 16 CH | Tuition Rs.73,600 | Total Rs.102,700\n"
            "BE Tech Civil: Tuition/CH Rs.4,600 | 18 CH | Tuition Rs.82,800 | Total Rs.111,900\n"
            "BE Tech Electronic: Tuition/CH Rs.4,600 | 18 CH | Tuition Rs.82,800 | Total Rs.111,900\n\n"
            "Architecture Program (has Studio Fee):\n"
            "B. Architecture: Admission Rs.35,000 | Security Deposit Rs.5,000 | Student Activity Rs.1,100 | Exam Rs.5,200 | "
            "Semester Reg Rs.11,500 | Studio Fee Rs.20,500 | Tuition/CH Rs.6,600 | 18 CH | Tuition Rs.118,800 | Total Rs.197,100\n\n"
            "Note: All tuition and related fees are revised annually, as approved by the University, and implemented from the Fall semester."
        ),
        "timestamp": 1781149218.0,
        "hash": "complete_fee_structure_2025"
    },

    # ----------------------------------------------------------------
    # FEE PAYMENT & SPECIAL RULES
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Fee Payment Rules and Self-Finance 2025-26",
        "content": (
            "SSUET fee payment rules for 2025-26: "
            "Payments can be made at any MCB Bank branch in cash, pay order, or demand draft in favour of "
            "'Sir Syed University of Engineering & Technology, Karachi'. "
            "Online payments are accepted through the university's official Paypro online payment portal. "
            "IBFT payments are strictly not allowed. "
            "For self-finance admissions, the fee payable at the time of admission is the total first-semester fee "
            "plus Rs. 250,000 and applicable taxes. "
            "This fee structure is exclusive of withholding tax, applicable at 5% if fee paid during the year exceeds Rs. 200,000. "
            "The 2nd installment voucher (tuition fee based on registered credit hours) is issued after semester registration. "
            "Semester freeze: A student can freeze a semester within 15 days of commencement by paying the semester registration fee. "
            "If neither frozen nor registered within the time limit, registration is treated as suspended. "
            "Reactivation of suspended registration requires Semester Registration Fee plus Semester Activation Charges of Rs. 10,000 (applicable from 2nd semester onwards)."
        ),
        "timestamp": 1781149219.0,
        "hash": "fee_payment_rules_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET AIT Graduate Special Discounts 2025-26",
        "content": (
            "Special benefits for AIT (Aligarh Institute of Technology) graduates at SSUET for 2025-26: "
            "Admission fee of Rs. 15,000 for BE Tech Civil, Electrical, and Electronic is waived. "
            "30% discount on tuition fees for BS Civil, Electrical, Electronic, and Biomedical Engineering. "
            "Entry/application charges are only Rs. 1,000 across all programs (instead of Rs. 3,900)."
        ),
        "timestamp": 1781149220.0,
        "hash": "ait_graduate_discounts_2025"
    },

    # ----------------------------------------------------------------
    # FEE REFUND POLICY
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Fee Refund Policy 2025-26",
        "content": (
            "SSUET Fee Refund Policy for 2025-26 (as per HEC 2024 revised policy): "
            "Admission Fee: Non-refundable under any circumstances. "
            "Security Deposit: Refundable upon completion of degree or withdrawal. If refund not claimed within 3 years of completion or withdrawal, amount is transferred to University Fund. "
            "Student Activity Fee: Refundable as per HEC refund policy timelines and percentages minus any usage. "
            "Studio Fee (BAR): Refundable as per HEC refund policy timelines. "
            "Exam Fee: Refundable as per HEC refund policy timelines. "
            "Semester Registration Fee: Refundable as per HEC refund policy timelines. "
            "Tuition Fee Refund Schedule (from commencement of classes): "
            "Up to 10th day: 100% refund. "
            "Up to 15th day: 80% refund. "
            "Up to 20th day: 60% refund. "
            "Up to 30th day: 50% refund. "
            "From 31st day onwards: No refund. "
            "Any refund request must be submitted within the applicable timeline. "
            "Requests beyond the 30th day are only eligible for Security Deposit refund. "
            "Timeline is continuous, covering both weekdays and weekends. "
            "For refund inquiries contact: naziz@ssuet.edu.pk"
        ),
        "timestamp": 1781149221.0,
        "hash": "fee_refund_policy_2025"
    },

    # ----------------------------------------------------------------
    # ADMISSION PROCEDURE
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Admission Procedure Step-by-Step 2025-26",
        "content": (
            "SSUET admission procedure for 2025-26: "
            "Step 1: Visit admissions.ssuet.edu.pk and complete online registration using your email address. "
            "Step 2: Fill the admission form step by step and upload required scanned documents. "
            "Step 3: Carefully select preferred program choices. Choices cannot be changed after form submission. "
            "Step 4: Print the voucher and submit it at any MCB Bank branch or pay online through Paypro. IBFT is strictly not allowed. "
            "Step 5: Upload the paid voucher receipt on the admission portal. "
            "Step 6: Admit cards are issued one day before the entry test series starts to all candidates who have completed form requirements and uploaded paid challan, once verified by SSUET Accounts Office. "
            "Step 7: Appear for the entry test (computer-based, online, or paper-based as announced). "
            "Step 8: Merit list is published on www.ssuet.edu.pk. "
            "Step 9: Provisionally admitted candidates pay the first installment (admission + first semester charges). "
            "Step 10: Submit original documents to Academics Office Room AB-02 Block A after admission confirmation. "
            "Step 11: Submit HSC/Equivalent final mark sheet before end of first semester to convert provisional admission to regular admission."
        ),
        "timestamp": 1781149222.0,
        "hash": "admission_procedure_steps_2025"
    },

    # ----------------------------------------------------------------
    # REQUIRED DOCUMENTS
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Required Documents for Admission 2025-26",
        "content": (
            "Documents required for SSUET admission 2025-26: "
            "1. SSC/Matric Marksheet and Certificate (attested photocopy). "
            "2. HSC-I Marks Sheet or O-Level/AS-Level/Equivalent Statement of Results (and admit card if result awaited). "
            "3. HSC-II/A-Level Marksheet (original, to be retained by university for conversion of provisional to regular admission; must be attested by IBCC). "
            "4. IBCC Equivalence Certificate for O/A-Level or equivalent studies (mandatory). "
            "5. Copy of CNIC or B-Form (if CNIC not yet issued). "
            "6. Copy of paid voucher (printed). "
            "7. System Generated Admission Offer Letter (printed). "
            "8. Undertaking duly signed by candidate and parents. "
            "9. Copy of Domicile Certificate. "
            "10. Declaration of non-participation in political activities on Judicial Stamp Paper of Rs. 50. "
            "11. Three passport-size photographs with light blue background. "
            "12. Hafiz-e-Quran Sanad (original from Wifaq-ul-Madaris Arabia Pakistan, if applicable). "
            "13. Sports Certificate (if applicable). "
            "Original documents are returned after completion or termination of studies. "
            "Photostat copies can be obtained on payment of Rs. 50 each with seven working days notice."
        ),
        "timestamp": 1781149223.0,
        "hash": "required_documents_2025"
    },

    # ----------------------------------------------------------------
    # PROGRAM DURATION & OTHER POLICIES
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Program Duration, Medium of Instruction, and Enrollment Rules 2025-26",
        "content": (
            "SSUET program duration for 2025-26: "
            "Engineering, Sciences, Technology and Business programs (except B. Architecture): Minimum 4 years, Maximum 7 years. "
            "Bachelor of Architecture: Minimum 5 years, Maximum 8 years. "
            "Medium of instruction: All courses, laboratories, and examinations are conducted in English. "
            "Employment/Simultaneous Enrollment: All undergraduate programs are regular full-time. "
            "No student is allowed to take employment or maintain simultaneous enrollment in any other institution. Violation may lead to cancellation of admission. "
            "Change of Program: Strictly prohibited after confirming admission. After the regular admission cycle, if seats become available due to cancellation, re-application is allowed with written application; submitted fee is forfeited and admission is on merit basis only. "
            "Extended Study after 4th Year (Batch 2020 onward): If a student takes 9 credit hours or more, they pay semester registration fee plus credit hours fee. If less than 9 credit hours, only credit hours fee is charged."
        ),
        "timestamp": 1781149224.0,
        "hash": "program_duration_rules_2025"
    },
    {
        "url": PDF_URL,
        "title": "SSUET Admission Cancellation Rules 2025-26",
        "content": (
            "SSUET admission cancellation rules for 2025-26: "
            "If documents are found forged, tampered, or bogus at any stage, admission is cancelled, fee is forfeited, and the university reserves the right to legal action. "
            "If a student misses classes for four consecutive weeks in a regular semester (two weeks in summer semester) without prior approval, admission may be suspended. "
            "Re-enrollment is possible in the next semester on Chairperson/Dean recommendation with prescribed fee payment. "
            "Students suspended or rusticated for serious breach of discipline will have admission cancelled. After the suspension period, readmission in the same year/semester with junior batch may be allowed if otherwise eligible. "
            "Students expelled for major breach of discipline will have admission cancelled and are not eligible for future admission at SSUET. "
            "Provisional admission is cancelled if HSC/Equivalent final mark sheet is not submitted or marks are below the eligibility criteria before the end of the first semester."
        ),
        "timestamp": 1781149225.0,
        "hash": "admission_cancellation_rules_2025"
    },

    # ----------------------------------------------------------------
    # DAE RELEVANT DISCIPLINES (ANNEXURE B)
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET DAE Relevant Disciplines for Engineering Programs (Annexure B)",
        "content": (
            "Relevant DAE disciplines for admission in SSUET BE Engineering programs (updated up to 74-EA&QEC/EAB):\n"
            "Civil Engineering: Architecture, Civil, Civil with any specialization, Environmental, Land & Mine Surveying.\n"
            "Electrical Engineering: Automation, Avionics, Computer/CIT, Electrical, Electronics, Information, Instrumentation, "
            "Instrumentation & Process Control, Mechatronics, Precision Mechanical & Instrument, Radar, Radio, Telecommunication.\n"
            "Electronics Engineering: Automation, Avionics, Bio-Medical, Electrical, Electronics, Instrumentation, "
            "Instrumentation & Process Control, Mechatronics, Radar, Radio, Telecommunication.\n"
            "Telecommunication Engineering: Automation, Avionics, Computer, Computer Information, Electrical, Electronics, "
            "Instrumentation, Instrumentation & Process Control, Radar, Radio, Software, Telecommunication.\n"
            "Biomedical Engineering: Automation, Biomedical, Electrical, Electronics, Healthcare, Instrumentation, "
            "Instrumentation & Process Control, Mechatronics, Radar, Radio.\n"
            "Computer Engineering: Automation, Computer, Computer Information, Electrical, Electronics, Instrumentation, "
            "Instrumentation & Process Control, Radar, Radio, Software, Telecommunication."
        ),
        "timestamp": 1781149226.0,
        "hash": "dae_relevant_disciplines_2025"
    },

    # ----------------------------------------------------------------
    # CONTACT AND GENERAL INFO
    # ----------------------------------------------------------------
    {
        "url": PDF_URL,
        "title": "SSUET Admissions Contact and Portal Information 2025-26",
        "content": (
            "SSUET Admissions contact information for 2025-26: "
            "Online admissions portal: admissions.ssuet.edu.pk. "
            "University website: www.ssuet.edu.pk. "
            "For fee refund inquiries: naziz@ssuet.edu.pk. "
            "Admissions are open to all eligible applicants based on merit without discrimination based on caste, creed, color, culture, religion, gender, or domicile (Aligarh Spirit). "
            "Government taxes are the liability of the candidate. "
            "HEC and all concerned accreditation bodies' Rules and Regulations are applicable in addition to SSUET Rules and Regulations."
        ),
        "timestamp": 1781149227.0,
        "hash": "admissions_contact_portal_2025"
    },
]

# ---------------------------------------------------------------

def append_to_jsonl(records, output_file):
    os.makedirs(DATA_DIR, exist_ok=True)

    existing_hashes = set()
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    h = obj.get("hash")
                    if h:
                        existing_hashes.add(h)
                except json.JSONDecodeError:
                    continue
        print(f"📋 Found {len(existing_hashes)} existing records in {output_file}")

    added = 0
    skipped = 0

    with open(output_file, "a", encoding="utf-8") as f:
        for rec in records:
            rec_hash = rec.get("hash", "")
            if rec_hash in existing_hashes:
                print(f"   ⏭️  SKIPPED (duplicate): {rec['title'][:70]}")
                skipped += 1
                continue
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            existing_hashes.add(rec_hash)
            print(f"   ✅ ADDED: {rec['title'][:70]}")
            added += 1

    print(f"\n✅ Done! Added {added} records, skipped {skipped} duplicates.")
    return added


def rebuild_index():
    print("\n🔄 Rebuilding FAISS index from updated JSONL...")
    from rag_engine import SSUETRAG
    from sentence_transformers import SentenceTransformer
    import faiss

    rag = SSUETRAG.__new__(SSUETRAG)
    rag.model = SentenceTransformer("all-MiniLM-L6-v2")
    dim = rag.model.get_sentence_embedding_dimension()
    rag.index = faiss.IndexFlatL2(dim)
    rag.metadata = []
    rag.add_documents()
    print("✅ FAISS index rebuilt successfully!")


if __name__ == "__main__":
    print(f"📂 Target file: {os.path.abspath(OUTPUT_FILE)}\n")
    added = append_to_jsonl(new_records, OUTPUT_FILE)

    if added > 0:
        rebuild = input("\n🔁 Rebuild FAISS index now? (y/n): ").strip().lower()
        if rebuild == "y":
            rebuild_index()
        else:
            print("ℹ️  Skipped index rebuild. Run rag_engine.py manually when ready.")
    else:
        print("ℹ️  No new records added — index rebuild not needed.")