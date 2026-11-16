# TECHNICAL REPORT ON STUDENTS' INDUSTRIAL WORK EXPERIENCE SCHEME (SIWES)

### UNDERTAKEN AT
## COMPUTER WAREHOUSE GROUP (CWG) PLC
**Block 10, Commercial Avenue, Sabo, Yaba / Plot 8, Adeola Hopewell, Victoria Island, Lagos State, Nigeria**

---

### BY
**AYANBISI ABDULRAHMAN**  
**Matriculation Number: CPE/22/9996**

---

### SUBMITTED TO:
**THE DEPARTMENT OF COMPUTER ENGINEERING**  
**SCHOOL OF ELECTRICAL SYSTEMS ENGINEERING**  
**FEDERAL UNIVERSITY OF TECHNOLOGY, AKURE (FUTA)**  
**P.M.B. 704, AKURE, ONDO STATE, NIGERIA**

---

### IN PARTIAL FULFILMENT OF THE REQUIREMENT FOR THE AWARD OF THE DEGREE OF BACHELOR OF ENGINEERING (B. ENG) IN COMPUTER ENGINEERING

**DECEMBER 2026**

---
## CERTIFICATION

This is to certify that this technical report is a detailed account of the Student Industrial Work Experience Scheme (SIWES) undertaken by **AYANBISI ABDULRAHMAN** with matriculation number **CPE/22/9996** at **COMPUTER WAREHOUSE GROUP (CWG) PLC**, Block 10, Commercial Avenue, Sabo, Yaba / Victoria Island, Lagos State. He is the sole author of this technical report, which is based on both the theoretical and practical aspects of SIWES. The SIWES lasted for a period of six (6) months (June to December 2026), and this report has been prepared in accordance with the regulations guiding its preparation in the Department of Computer Engineering, School of Electrical Systems Engineering, Federal University of Technology, Akure (FUTA).

<br><br><br>

_____________________________________________  
**AYANBISI ABDULRAHMAN**  
*(Student, CPE/22/9996)*  
Date: ________________________  

<br><br><br>

_____________________________________________  
**ENGR. A. O. ADEDOKUN**  
*(SIWES Coordinator, Department of Computer Engineering)*  
Date: ________________________  

<br><br><br>

_____________________________________________  
**PROF. J. J. POPOOLA**  
*(Head of Department, Department of Computer Engineering)*  
Date: ________________________  

---
## DEDICATION

This technical report is dedicated first and foremost to Almighty God, the Source of all wisdom, understanding, and sustenance, Whose divine grace, protection, and boundless favor saw me through the demanding six months of industrial training.

This work is also profoundly dedicated to my loving parents, whose prayers, unflagging financial sacrifices, moral encouragement, and profound belief in my engineering aspirations laid the firm foundation for my academic and professional journey. 

Finally, it is dedicated to all innovative engineers and technologists across Nigeria and the African continent who continually strive against infrastructural constraints to build resilient digital infrastructure, automated systems, and high-integrity enterprise software solutions.

---
## ACKNOWLEDGMENTS

I express my deepest gratitude to Almighty God for the gift of life, robust health, clarity of mind, and the intellectual strength granted to me throughout the six months of the Students' Industrial Work Experience Scheme (SIWES).

I wish to express my profound appreciation to the management of **Computer Warehouse Group (CWG) Plc** for granting me the privilege to undergo my industrial attachment within their prestigious establishment. I extend particular respect and gratitude to the executive leadership: **Mr. Adewale Adeyipo** (Group Managing Director / CEO), **Mr. Afolabi Sobande** (Chief Operating Officer), **Mr. Moruf Ireti Yusuf** (Chief Technology Officer), and **Mrs. Tinu Adeyemi** (Group Head of Human Resources), whose leadership maintains CWG as a bastion of technological excellence.

My sincere and heartfelt gratitude goes to my industry-based supervisor, **Mrs. Abimbola**, whose continuous guidance, patient mentorship, high technical standards, and constructive critiques fostered my engineering confidence. I am immensely indebted to **Mr. Moses Mornu**, Team Lead, for his invaluable technical masterclasses in Microsoft Active Directory, hybrid cloud architectures, and disciplined enterprise operations. Special thanks also go to **Bayo** for supervising my enterprise application workflows and Power Platform projects; to **Mr. Matthew** (Infrastructure Lead) for granting me rigorous hands-on exposure to enterprise data center operations, server racking, and power distribution; and to **Mr. Michael** (Networking Lead) for demystifying enterprise switching, structured cabling, and 802.1Q VLAN segmentation. 

I must equally acknowledge the camaraderie, technical synergy, and collaborative spirit shared with my fellow intern colleagues—**Ayo**, **Thank God**, and **David Toluwanimi**—with whom I shared diagnostic benches, solved intricate code anomalies, and tackled high-pressure enterprise deployments.

From the academic front at the **Federal University of Technology, Akure (FUTA)**, I express sincere gratitude to the Vice-Chancellor, the Dean of the School of Electrical Systems Engineering, the Head of Department of Computer Engineering, **Prof. J. J. Popoola**, and the Departmental SIWES Coordinator, **Engr. A. O. Adedokun**, alongside all distinguished lecturers and technical laboratory staff, whose solid grounding in engineering theory made my rapid adaptation to industrial technology seamless.

Finally, to my family, friends, and colleagues who offered unwavering encouragement throughout this industrial internship, I say a profound and heartfelt thank you.

---
## ABSTRACT

This technical report presents an exhaustive, academically rigorous documentation of the six-month Students' Industrial Work Experience Scheme (SIWES) undertaken by Ayanbisi AbdulRahman (CPE/22/9996) at Computer Warehouse Group (CWG) Plc, Lagos, Nigeria, spanning June to December 2026. The training was systematically structured into two intensive operational rotations: the **Metering & Energy Engineering Department** (June to August 2026) and the **IT Proximity Support, Network Infrastructure & Enterprise Software Systems Division** (September to December 2026).

During the first rotation in Metering, activities focused on the complete engineering assembly, diagnostic testing, optical parameterization, and statutory regulatory verification of solid-state single-phase and three-phase smart prepayment electricity meters. Core engineering competencies developed included Electrostatic Discharge (ESD) workbench bonding (< 1 ohm loop resistance), mechanical torque-controlled coupling of current shunt terminals (2.5–3.0 Nm), socket seating and threshold testing of lithium backup real-time clock (RTC) batteries (>= 3.05V DC) for non-volatile time-of-use (TOU) tariff tracking, GPRS/cellular IoT daughterboard mounting and SMA antenna impedance matching, power-on mains energization on calibrated multi-position test benches (230V/415V at 50Hz), optical pulse frequency calibration at 1600 imp/kWh to attain Class 1.0 accuracy (error <= ±1.0%), Standard Transfer Specification (STS IEC 62055-41) 20-digit token entry with diagnostic keypad short codes (`#001#`, `#002#`, `#003#`), infrared optical probe communication via the IEC 62056-21 protocol using the Meter Management System (MMS) to execute firmware mode switching from Factory/Staging Mode to Utility Production Mode, and anti-tamper sealing with serial-embossed lead crimps pursuant to the statutory mandates of the Nigerian Electricity Management Services Agency (NEMSA) Act 2015.

The second rotation transitioned into IT Proximity Support, Systems Administration, and Software Engineering. Network infrastructure tasks encompassed ANSI/TIA/EIA-568B Cat6/Cat6a structured cabling termination, 110-type IDC punch-down on 24-port/48-port patch panels, Cisco Layer-2/Layer-3 managed switch configurations, 802.1Q VLAN segmentation, multi-SSID enterprise Wi-Fi deployments, and 42U data center server rack management with dual-feed A/B Power Distribution Units (PDUs) and Liebert precision cooling. Systems administration involved automated OEM laptop staging (Dell Latitude and HP EliteBook) via custom Windows Configuration Designer provisioning packages (`.ppkg`), Active Directory Domain Services (AD DS) user and Organizational Unit (OU) administration, Group Policy Object (GPO) security baseline deployment, and CrowdStrike Falcon/Sophos Central Endpoint Detection and Response (EDR) telemetry monitoring.

In enterprise software engineering, two flagship solutions were developed:
1. **CWG Retail Suite:** A decoupled micro-monolith point-of-sale and inventory control platform engineered using a Laravel 12 REST API backend, Sanctum bearer authentication, and a React 19 single-page application. The system features a 3NF relational schema, an atomic POS checkout engine utilizing database transactions to prevent inventory race conditions, browser-native 80mm ESC/POS thermal receipt formatting, real-time dynamic margin computation, multi-unit stock adjustments with immutable audit logging, and a 5-tab financial analytics dashboard with eager-loaded queries.
2. **LeaveTrack (PRJ-08, Track A — Enterprise Operations Suite):** An enterprise-grade leave and attendance management system implemented on the Microsoft Power Platform. Architecture encompasses a Microsoft Dataverse relational data model (`Employees`, `LeaveTypes`, `LeaveRequests`, `Balances`, `Approvals`, `PublicHolidays`), a responsive Power Apps Canvas portal with real-time balance validation and public holiday exclusions, a Power Apps Model-Driven HR administration console, a multi-tier Power Automate approval state machine routing through Entra ID manager attributes, automated Microsoft Graph API calendar synchronization, and an executive Power BI analytics dashboard computing organizational leave liability and forward absence forecasting.

The report concludes with a technical analysis of challenges encountered alongside their engineering resolutions, and offers strategic recommendations to CWG Plc, academic institutions, and the Industrial Training Fund (ITF) for advancing technological education in Nigeria.

---
## TABLE OF CONTENTS

- **COVER PAGE** ................................................................................................................................................ i
- **CERTIFICATION** ............................................................................................................................................ ii
- **DEDICATION** ................................................................................................................................................ iii
- **ACKNOWLEDGMENTS** .................................................................................................................................. iv
- **ABSTRACT** .................................................................................................................................................. v
- **TABLE OF CONTENTS** .................................................................................................................................. vi
- **LIST OF FIGURES** ........................................................................................................................................ viii
- **LIST OF TABLES** .......................................................................................................................................... x
- **LIST OF ABBREVIATIONS** ............................................................................................................................ xi
- **CHAPTER ONE: INTRODUCTION TO SIWES PROGRAM** ................................................................................ 1
  - 1.1 Background of the SIWES Program .......................................................................................................... 1
  - 1.2 The Industrial Training Fund (ITF) ............................................................................................................. 2
  - 1.3 Aims and Objectives of the SIWES Program ................................................................................................. 3
  - 1.4 Regulatory Bodies Involved in SIWES Governance ....................................................................................... 4
  - 1.5 Attachment Schedule and Dual-Rotation Plan ............................................................................................... 5
- **CHAPTER TWO: OVERVIEW OF COMPUTER WAREHOUSE GROUP (CWG) PLC** ................................................. 7
  - 2.1 Corporate Background and History of CWG Plc .......................................................................................... 7
  - 2.2 Core Business Sectors, Divisions, and Subsidiaries ..................................................................................... 8
  - 2.3 Corporate Vision, Mission, and Core Values (W-E-C-A-R-E) .......................................................................... 10
  - 2.4 Organizational Structure and Hierarchy ...................................................................................................... 11
  - 2.5 Contributions to Nigeria's Digital Economy and Technological Sovereignty ................................................... 13
- **CHAPTER THREE: INDUSTRIAL WORK EXPERIENCE & TECHNICAL ACTIVITIES** ........................................... 15
  - **3.1 SECTION A: METERING DEPARTMENT & ENERGY AUTOMATION** ........................................................... 15
    - 3.1.1 Overview of Solid-State Energy Measurement Physics and Metering Topologies ......................................... 15
    - 3.1.2 Electrostatic Discharge (ESD) Protection Protocols and Workstation Grounding ......................................... 17
    - 3.1.3 Precision Mechanical Coupling, Terminal Lug Torque Specs, and Enclosure Assembly ................................. 19
    - 3.1.4 Real-Time Clock (RTC) Lithium Battery Installation, Voltage Thresholding, and Time-of-Use Tariffs ............. 21
    - 3.1.5 GPRS Cellular IoT Daughterboard Mounting, SMA Antenna Matching, and Network Handshake ..................... 23
    - 3.1.6 Mains Energization Bench Testing, High-Voltage Safety, and Optical Pulse Error Verification ......................... 25
    - 3.1.7 Standard Transfer Specification (STS) Token Verification and Diagnostic Keypad Short Codes ....................... 27
    - 3.1.8 Optical Port Interfacing and Mode Switching via Meter Management System (MMS) .................................... 29
    - 3.1.9 Anti-Tamper Detection Circuitry, Field Auditing, and Reverse Energy Flow Mitigation ................................ 31
    - 3.1.10 Quality Control (QC), NEMSA Act 2015 Certification, Wire Crimp Sealing, and Packaging ............................ 33
  - **3.2 SECTION B: IT PROXIMITY SUPPORT, NETWORK INFRASTRUCTURE & SYSTEMS ADMINISTRATION** ............. 35
    - 3.2.1 ITIL Help Desk Operations, Ticket Resolution Workflow, and Proximity SLA Compliance ............................... 35
    - 3.2.2 Enterprise Structured Cabling, TIA/EIA-568B Standard, and Patch Panel Termination ................................... 37
    - 3.2.3 Layer-2/Layer-3 Switching, 802.1Q VLAN Trunking, and Multi-SSID Enterprise Wi-Fi Provisioning .................. 40
    - 3.2.4 Cisco Packet Tracer Enterprise Network Simulation and Routing Topologies .............................................. 42
    - 3.2.5 Enterprise Data Center Facilities, 42U Server Racks, Dual PDU Feeds, and Environmental CRAC Cooling .......... 44
    - 3.2.6 Enterprise Server Architecture, Hardware RAID Redundancy, and IPMI/iDRAC Out-of-Band Management ....... 46
    - 3.2.7 Automated Corporate Fleet Provisioning using Windows Configuration Designer `.ppkg` Packages ................ 48
    - 3.2.8 Computer Hardware Maintenance, Component Replacement, and Hardware Upgrades ................................. 50
    - 3.2.9 Microsoft Active Directory Domain Services (AD DS) Administration and OU Hierarchy .............................. 52
    - 3.2.10 Group Policy Objects (GPOs) Deployment, Password Complexity, and Storage Device Hardening .................. 54
    - 3.2.11 Enterprise Endpoint Detection and Response (EDR) Monitoring: Sophos Central and CrowdStrike Falcon ........ 56
    - 3.2.12 IT Asset Management, Barcode Tagging, Physical Inventory Audits, and NIST 800-88 Decommissioning .......... 58
  - **3.3 SECTION C: SOFTWARE DEVELOPMENT AND ENTERPRISE SOLUTIONS** ................................................... 60
    - 3.3.1 Enterprise Software Development Methodologies: Agile Scrum Framework and CI/CD Pipelines .................... 60
    - 3.3.2 Major Project I: CWG Retail Suite (Full-Stack POS & Inventory Management Platform) ................................. 62
      - 3.3.2.1 Problem Analysis and Architectural Design: Decoupled Micro-Monolith (React 19 + Laravel 12) ................... 62
      - 3.3.2.2 3NF Relational Database Schema Design and Key Constraints .............................................................. 64
      - 3.3.2.3 Real-Time POS Checkout Engine, Barcode Scanning, and Atomic Transaction Processing .......................... 67
      - 3.3.2.4 ESC/POS 80mm Browser-Native Thermal Receipt Generation Subsystem ................................................. 70
      - 3.3.2.5 Product Catalogue Management, Dynamic Margin Calculations, and Image Upload Pipelines ....................... 72
      - 3.3.2.6 Inventory Stock Adjustment Engine, Multi-Unit Tracking, and Discrepancy Auditing .................................. 74
      - 3.3.2.7 Multi-Tab Financial Analytics and Business Intelligence Dashboard ...................................................... 76
      - 3.3.2.8 Role-Based Access Control, Cashier Interface Masking, and Security Protocols ......................................... 78
    - 3.3.3 Major Project II: LeaveTrack — Enterprise Operations Suite: Leave & Attendance Management System (PRJ-08) .. 80
      - 3.3.3.1 Problem Statement, Strategic Objectives, and Business Value Analysis ................................................. 80
      - 3.3.3.2 12-Week Delivery Lifecycle (Phases P1–P7) and Technical Milestones ................................................... 82
      - 3.3.3.3 Enterprise Architecture & Technology Stack Alignment on Microsoft Power Platform ................................. 84
      - 3.3.3.4 Dataverse Relational Data Architecture, Entity Schemas, and Relationships ........................................... 86
      - 3.3.3.5 Power Apps Canvas Application Design: Employee Self-Service and Real-Time Balance Validation ................. 88
      - 3.3.3.6 Power Apps Model-Driven Application: HR Administration Console and Policy Management ......................... 91
      - 3.3.3.7 Power Automate Multi-Tier Hierarchical Approval Workflow State Machine ............................................ 93
      - 3.3.3.8 Entra ID Hierarchical Routing and Microsoft Graph API Automated Calendar Integration .......................... 95
      - 3.3.3.9 Power BI Enterprise Analytics Dashboard: Departmental Absence Forecasting & Accrual Liability ................. 97
      - 3.3.3.10 Security Governance, UAT Test Matrix, and Application Lifecycle Management (ALM) Handover ................. 99
- **CHAPTER FOUR: CONCLUSION, CHALLENGES ENCOUNTERED, AND RECOMMENDATIONS** .................................. 102
  - 4.1 Summary of Industrial Training Experience and Professional Growth ......................................................... 102
  - 4.2 Comprehensive Matrix of Technical Challenges Encountered and Engineering Resolutions .............................. 103
  - 4.3 Actionable Recommendations ............................................................................................................... 106
    - 4.3.1 Recommendations for Host Organization: Computer Warehouse Group (CWG) Plc ...................................... 106
    - 4.3.2 Recommendations for Future SIWES Interns .......................................................................................... 107
    - 4.3.3 Recommendations for Academic Institutions: FUTA & Department of Computer Engineering .......................... 108
    - 4.3.4 Recommendations for Industrial Training Fund (ITF) & National Universities Commission (NUC) ...................... 109
- **REFERENCES** ........................................................................................................................................... 111
- **APPENDICES** ........................................................................................................................................... 114
  - Appendix A: Metering Diagnostic Keypad Short Codes & Token Decryption Structure ......................................... 114
  - Appendix B: Structured Cabling TIA/EIA-568B Pinout Specification ................................................................. 115
  - Appendix C: LeaveTrack (PRJ-08) Dataverse Entity Schema & Attribute Definitions ............................................. 116
  - Appendix D: CWG Retail Suite Relational Schema DDL & API Endpoints ............................................................. 118

---
## LIST OF FIGURES

- Figure 1.1: ITF Organizational Logo and SIWES Operational Framework
- Figure 2.1: Computer Warehouse Group (CWG) Plc Corporate Identity Logo
- Figure 2.2: CWG Plc Corporate Organogram and IT & BI Departmental Structure
- Figure 3.1: Architecture of Modern Solid-State Electronic Smart Energy Meters
- Figure 3.2: Internal PCB Layout of Single-Phase and Three-Phase Energy Meters
- Figure 3.3: ESD Grounding Station, Copper Busbar, and Static-Dissipative Workbench
- Figure 3.4: Lithium RTC Backup Battery (CR2032/CR2450) Socket Seating and Multi-Meter Voltage Verification
- Figure 3.5: GPRS / Cellular IoT Daughterboard Mounting and Internal Trace vs External Antenna Coupling
- Figure 3.6: Multi-Position Meter Test Bench Setup for Mains Energization and Pulse Accuracy Calibration
- Figure 3.7: STS Token Keypad Diagnostic Testing and Short Code Verification (#001#-#003#)
- Figure 3.8: MMS Optical Communication Probe (IEC 62056-21) and Optical Port Interface
- Figure 3.9: State Transition Diagram: Switching Meter from Factory Staging Mode to Utility Production Mode
- Figure 3.10: NEMSA Quality Compliance Verification and Wire Crimp Lead Sealing Protocol
- Figure 3.11: Final Packaging, Barcode Serialization, and QA Batch Ledger Documentation
- Figure 3.12: OSI 7-Layer and TCP/IP 4-Layer Architectural Models in Enterprise Networking
- Figure 3.13: Cat6/Cat6a Structured Cabling Pinout according to ANSI/TIA/EIA-568B Standard
- Figure 3.14: 24-Port Patch Panel, Brush Cable Management Panels, and Rack Looming
- Figure 3.15: Hardware Tools: RJ-45 Crimper, Punch-Down Tool, Patchsee Cable Tracer, and Wire Mapper
- Figure 3.16: Cisco Managed Layer-2/Layer-3 Switches and SFP+ Fiber Optic Transceiver Modules
- Figure 3.17: Multi-SSID Enterprise Wi-Fi Network Architecture and 802.1Q VLAN Trunking
- Figure 3.18: Cisco Packet Tracer Enterprise Network Simulation and Routing Topology
- Figure 3.19: 42U Data Center Server Rack, Cage Nut Fasteners, and Vertical Cable Ducts
- Figure 3.20: Dual-Feed Power Distribution Units (PDU A & B) and Liebert Precision Cooling CRAC Unit
- Figure 3.21: Enterprise Server Hardware: Dell PowerEdge Rackmount Chassis and Hardware RAID Controller
- Figure 3.22: Bare-Metal Hypervisor (Type-1) vs Hosted Hypervisor (Type-2) Virtualization Architectures
- Figure 3.23: Automated Windows 11 Enterprise Provisioning via Custom `.ppkg` Staging Packages
- Figure 3.24: Laptop Hardware Maintenance: SO-DIMM RAM Installation and PCIe NVMe M.2 SSD Upgrade
- Figure 3.25: Microsoft Active Directory Domain Services (AD DS) Management Console and OU Hierarchy
- Figure 3.26: Group Policy Management Console (GPMC) Enterprise Security Baseline Configuration
- Figure 3.27: Enterprise Endpoint Security Architecture: Sophos Central and CrowdStrike Falcon EDR
- Figure 3.28: IT Hardware Asset Inventory Management, Asset Tagging, and Physical Audit Verification
- Figure 3.29: Agile Scrum Engineering Lifecycle and Continuous Integration Pipeline
- Figure 3.30: CWG Retail Suite Decoupled Architecture (Laravel 12 API + React 19 Frontend)
- Figure 3.31: CWG Retail Suite 3NF Relational Database Entity-Relationship Diagram (ERD)
- Figure 3.32: POS Checkout Interface: Live Barcode Scanning, Product Filtering, and Cart State Machine
- Figure 3.33: ESC/POS 80mm Thermal Receipt Layout and Print Formatting Engine
- Figure 3.34: Inventory Adjustment, Low-Stock Notification, and Audit Trail Management
- Figure 3.35: Multi-Tab Financial Analytics Dashboard: Sales Performance, Margins, and Audit Logs
- Figure 3.36: LeaveTrack (PRJ-08) Enterprise System Architecture on Microsoft Power Platform
- Figure 3.37: LeaveTrack Relational Data Model (Dataverse Schema: Employees, LeaveTypes, LeaveRequests, Balances, Approvals, Holidays)
- Figure 3.38: LeaveTrack Canvas Application: Employee Leave Request and Real-Time Balance Interface
- Figure 3.39: LeaveTrack Canvas Application: My Requests, Balance Tracking, and Team Calendar View
- Figure 3.40: LeaveTrack Model-Driven Application: HR Administration Console and Policy Management
- Figure 3.41: Power Automate Multi-Tier Approval Workflow and Entra ID Hierarchical Routing Engine
- Figure 3.42: Power Automate Automated Outlook Calendar Synchronization via Microsoft Graph API
- Figure 3.43: Power BI Leave & Attendance Analytics Dashboard: Departmental Absence Trends & Accrual Liability
- Figure 3.44: LeaveTrack Managed Solution ALM Lifecycle: Dev -> Test -> Prod Deployment Pipeline

---
## LIST OF TABLES

- Table 1.1: Summary of SIWES Stakeholders, Roles, and Governance Hierarchy
- Table 1.2: Six-Month Dual-Rotation Schedule and Departmental Allocation
- Table 2.1: CWG Plc Operating Divisions, Specialized Core Competencies, and Flagship Solutions
- Table 3.1: Diagnostic Keypad Short Codes, Return Values, and Engineering Descriptions
- Table 3.2: NEMSA Statutory Inspection Thresholds and Permissible Calibration Error Margins
- Table 3.3: TIA/EIA-568B Straight-Through Wiring Pinout and Electrical Pair Assignment
- Table 3.4: Enterprise VLAN Segmentation Scheme and IP Subnet Allocations at CWG Plc
- Table 3.5: Enterprise Group Policy Objects (GPOs) and Target Enforcement Settings
- Table 3.6: CWG Retail Suite Relational Database Schema and 3NF Attributes
- Table 3.7: LeaveTrack (PRJ-08) 12-Week Phased Delivery Roadmap (P1–P7)
- Table 3.8: LeaveTrack Dataverse Entity Schema, Data Types, and Relationships
- Table 3.9: LeaveTrack Evaluation Rubric and Grading Weight Distribution
- Table 4.1: Comprehensive Matrix of Technical Challenges Encountered, Root Causes, and Engineering Resolutions

---
## LIST OF ABBREVIATIONS

- **AD DS:** Active Directory Domain Services
- **ALM:** Application Lifecycle Management
- **ANSI:** American National Standards Institute
- **API:** Application Programming Interface
- **ASIC:** Application-Specific Integrated Circuit
- **ATM:** Automated Teller Machine
- **BIOS:** Basic Input/Output System
- **BPF:** Business Process Flow
- **CI/CD:** Continuous Integration and Continuous Deployment
- **CMOS:** Complementary Metal-Oxide-Semiconductor
- **CPU:** Central Processing Unit
- **CRAC:** Computer Room Air Conditioning
- **CWG:** Computer Warehouse Group Plc
- **DAX:** Data Analysis Expressions
- **DC:** Direct Current / Domain Controller
- **DHCP:** Dynamic Host Configuration Protocol
- **DISCO:** Electricity Distribution Company
- **DLC:** Data Link Control
- **DLMS:** Device Language Message Specification
- **DNS:** Domain Name System
- **EDR:** Endpoint Detection and Response
- **EIA:** Electronic Industries Alliance
- **ERD:** Entity-Relationship Diagram
- **ESD:** Electrostatic Discharge
- **FUTA:** Federal University of Technology, Akure
- **GMD:** Group Managing Director
- **GPO:** Group Policy Object
- **GPRS:** General Packet Radio Service
- **GSM:** Global System for Mobile Communications
- **GUI:** Graphical User Interface
- **HOD:** Head of Department
- **HTTP:** HyperText Transfer Protocol
- **IC:** Integrated Circuit
- **IDC:** Insulation Displacement Contact
- **IEEE:** Institute of Electrical and Electronics Engineers
- **IEC:** International Electrotechnical Commission
- **IP:** Internet Protocol
- **IPMI:** Intelligent Platform Management Interface
- **IT:** Information Technology
- **ITF:** Industrial Training Fund
- **ITIL:** Information Technology Infrastructure Library
- **KVM:** Keyboard, Video, and Mouse Switch
- **LAN:** Local Area Network
- **LED:** Light Emitting Diode
- **MAC:** Media Access Control
- **MMS:** Meter Management System
- **NBTE:** National Board for Technical Education
- **NEMSA:** Nigerian Electricity Management Services Agency
- **NGX:** Nigerian Exchange Group
- **NIST:** National Institute of Standards and Technology
- **NUC:** National Universities Commission
- **NVMe:** Non-Volatile Memory Express
- **OOBE:** Out-of-Box Experience
- **OS:** Operating System
- **OSI:** Open Systems Interconnection
- **OU:** Organizational Unit
- **PCB:** Printed Circuit Board
- **PCIe:** Peripheral Component Interconnect Express
- **PDU:** Power Distribution Unit
- **POS:** Point of Sale
- **POST:** Power-On Self-Test
- **PPM:** Project Portfolio Management
- **PPKG:** Provisioning Package
- **RAID:** Redundant Array of Independent Disks
- **RAM:** Random Access Memory
- **RBAC:** Role-Based Access Control
- **REST:** Representational State Transfer
- **RJ-45:** Registered Jack 45
- **ROM:** Read-Only Memory
- **RTC:** Real-Time Clock
- **SDLC:** Software Development Life Cycle
- **SFP:** Small Form-Factor Pluggable
- **SIWES:** Students' Industrial Work Experience Scheme
- **SLA:** Service Level Agreement
- **SMA:** SubMiniature Version A (RF Connector)
- **SMS:** Short Message Service
- **SO-DIMM:** Small Outline Dual In-line Memory Module
- **SPA:** Single Page Application
- **SSD:** Solid-State Drive
- **SSID:** Service Set Identifier
- **STS:** Standard Transfer Specification
- **TCP/IP:** Transmission Control Protocol / Internet Protocol
- **TIA:** Telecommunications Industry Association
- **TOU:** Time-of-Use
- **TPM:** Trusted Platform Module
- **UAT:** User Acceptance Testing
- **UEFI:** Unified Extensible Firmware Interface
- **UI/UX:** User Interface / User Experience
- **UPS:** Uninterruptible Power Supply
- **UTP:** Unshielded Twisted Pair
- **VLAN:** Virtual Local Area Network
- **VoIP:** Voice over Internet Protocol
- **3NF:** Third Normal Form

---

## CHAPTER ONE: INTRODUCTION TO SIWES PROGRAM

### 1.1 Background of the SIWES Program
The Students' Industrial Work Experience Scheme (SIWES) was established in 1973 by the Federal Government of Nigeria under the auspices of the Industrial Training Fund (ITF) through Decree No. 47 of 1971 (subsequently amended as the Industrial Training Amendment Act of 2011). The program was instituted as a strategic intervention to address a profound structural defect in the nation's post-secondary education system: the widening dichotomy between the theoretical instruction imparted within university lecture halls and the practical, operational competencies demanded by modern engineering, technological, and industrial enterprises.

Prior to the inception of SIWES, graduates of engineering, applied science, and technology disciplines across Nigerian tertiary institutions were routinely found deficient in hands-on technical skills, industrial tool handling, workshop safety protocols, and real-world system troubleshooting. While their theoretical foundations in mathematics, physical sciences, and circuit theory were rigorous, their inability to translate mathematical abstractions into functional physical hardware, production line operations, or scalable enterprise software architectures posed a severe impediment to industrial productivity and national economic development.

Recognizing that industrial growth is intrinsically tethered to the availability of an indigenous, technically adept workforce, the Federal Government conceptualized SIWES as a mandatory, credit-bearing component of undergraduate degree curricula in all Nigerian faculties of engineering and technology. For students pursuing the Bachelor of Engineering (B.Eng.) degree in Computer Engineering at the Federal University of Technology, Akure (FUTA), SIWES is undertaken at the 400-level for a continuous duration of six (6) calendar months. This prolonged duration immerses students directly into professional engineering workflows, bridging the transition from academic academia to high-stakes industrial practice.

### 1.2 The Industrial Training Fund (ITF)
The Industrial Training Fund (ITF) serves as the primary statutory body charged with the administrative oversight, financing, policy formulation, and standard enforcement of industrial training across Nigeria. Established under Decree No. 47 of 8th October 1971, the ITF operates under the Federal Ministry of Industry, Trade and Investment. Its statutory mandate encompasses:
1. Promoting and encouraging the acquisition of practical skills in industry and commerce with a view to generating a pool of indigenous trained manpower sufficient to meet the economic demands of the nation.
2. Formulating and enforcing training guidelines, curriculum standards, and supervisory monitoring protocols across participating employers.
3. Managing the National Training Fund, derived from a mandatory one percent (1%) payroll levy on all commercial employers having five (5) or more employees or an annual turnover of fifty million Naira (₦50,000,000) and above.
4. Disbursing SIWES allowances and training subsidies to eligible students and institutions upon the successful verification of their industrial attachments.
5. Establishing and maintaining Center of Excellence vocational facilities and industrial training centers throughout Nigeria to foster technological innovation and technical upskilling.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 1.1]                                      |
|                                                                       |
|  Figure 1.1: ITF Organizational Logo and SIWES Operational Framework  |
|  Description: High-resolution official insignia of the Industrial     |
|  Training Fund (ITF), accompanied by the multi-stakeholder operational|
|  framework connecting FUTA, the host employer (CWG Plc), and the NUC. |
+-----------------------------------------------------------------------+
```

### 1.3 Aims and Objectives of the SIWES Program
The overarching objective of the SIWES program is to expose undergraduate engineering students to industrial work situations they are likely to encounter upon graduation. Specifically, the program aims to:
- **Translate Theoretical Concepts into Industrial Practice:** Provide an avenue for students in higher institutions of learning to acquire industrial skills and experience in their approved course of study, thereby demystifying textbook abstractions through hands-on technical execution.
- **Exposure to Industrial Machinery and Tooling:** Familiarize students with specialized engineering equipment, instrumentation, industrial test benches, multi-layer printed circuit boards, high-voltage test racks, automated staging tools, and enterprise cloud software platforms that are typically unavailable in standard university laboratories.
- **Foster Professional Engineering Ethics and Communication:** Inculcate work ethics, professional discipline, laboratory safety standards, occupational hazard mitigation, technical report writing, and collaborative teamwork within multidisciplinary corporate environments.
- **Facilitate Direct Transition to Industry:** Transition students smoothly from the sheltered, academic environment of the university to the fast-paced, high-accountability world of work, enhancing their post-graduation employability and career readiness.
- **Strengthen Institutional-Industrial Synergies:** Enlist and strengthen employer involvement in the educational process of preparing students for employment in industry and commerce, establishing feedback loops through which curricula can be continuously modernized.

### 1.4 Regulatory Bodies Involved in SIWES Governance
The successful execution, accreditation, and administrative governance of the SIWES program rely on a multi-tiered regulatory framework comprising federal agencies, educational commissions, academic directorates, and private sector employers:

| Regulatory Stakeholder | Governance Function and Statutory Role | Impact on Internship Quality |
|---|---|---|
| **Industrial Training Fund (ITF)** | Policy formulation, fund allocation, supervisory inspections, and student welfare management. | Ensures host organizations adhere to national training standards and verifies intern logbooks. |
| **National Universities Commission (NUC)** | Academic curriculum accreditation, credit-load allocation, and institutional compliance monitoring. | Validates that SIWES remains a mandatory, credit-bearing requirement for engineering degree awards. |
| **Federal University of Technology, Akure (FUTA)** | Pre-attachment orientation, departmental placement vetting, institutional logbook issuance, and academic grading. | Conducts institutional supervision visits via faculty assessors to grade intern progress. |
| **Host Employer (CWG Plc)** | Provision of certified industry supervisors, technical training modules, workshop resources, and practical projects. | Immerses the intern into daily production, customer SLAs, enterprise software builds, and systems administration. |

### 1.5 Attachment Schedule and Dual-Rotation Plan
To satisfy the rigorous academic and practical requirements of the Department of Computer Engineering at FUTA, my six-month industrial attachment at Computer Warehouse Group (CWG) Plc (spanning 24th June 2026 to 18th December 2026) was strategically partitioned into two distinct, three-month operational rotations. This structure provided an equitable balance between hardware engineering, power automation, and modern enterprise software systems:

| Phase and Department | Operational Period | Core Technical Domains and Activities | Key Engineering Competencies Acquired |
|---|---|---|---|
| **Phase 1: Metering & Smart Energy Engineering** | 24 June 2026 – 28 August 2026 | Smart electricity energy meter assembly, mechanical coupling, lithium RTC battery socket seating, GPRS IoT daughterboard mounting, ESD protection protocols, mains energization (230V/415V), bench calibration, STS token keypad testing, MMS optical port mode switching, and statutory NEMSA certification. | Precision hardware integration, high-voltage test safety, optical infrared parameterization, cryptographic STS token entry, and regulatory compliance. |
| **Phase 2: IT Proximity Support, Infrastructure & Enterprise Software** | 01 September 2026 – 18 December 2026 | ITIL helpdesk operations, Cat6a TIA/EIA-568B structured cabling, 802.1Q VLAN segmentation, 42U data center server rack management, dual PDU feeds, Liebert CRAC cooling, automated Windows staging via `.ppkg` packages, Active Directory Domain Services (AD DS) administration, Group Policy Objects (GPOs), endpoint security monitoring, full-stack POS software engineering (CWG Retail Suite in Laravel 12 + React 19), and Microsoft Power Platform enterprise development (LeaveTrack PRJ-08). | Enterprise network engineering, server virtualization, directory security governance, full-stack database normalization (3NF), automated workflow modeling, and Power BI business intelligence analytics. |

---

## CHAPTER TWO: OVERVIEW OF COMPUTER WAREHOUSE GROUP (CWG) PLC

### 2.1 Corporate Background and History of CWG Plc
Computer Warehouse Group (CWG) Plc is a premier Pan-African information and communications technology (ICT) conglomerate headquartered in Lagos, Nigeria. Founded in 1992 by visionary entrepreneur Austin Okere as Computer Warehouse Limited, the organization commenced operations primarily as a computer hardware distribution and maintenance enterprise. Through strategic vision, technical excellence, and deep responsiveness to the rapid digitalization of the Nigerian financial sector, the company evolved into a full-scale systems integration, enterprise software development, cloud infrastructure, and energy automation powerhouse.

Over three decades of continuous innovation, CWG Plc expanded its regional footprint across Sub-Saharan Africa, establishing fully functional subsidiaries in Ghana (CWG Ghana Limited), Uganda (CWG Uganda Limited), and Cameroon (CWG Cameroon Limited). In February 2013, marking a historic milestone in Nigerian corporate history, CWG Plc was formally listed on the Nigerian Exchange (NGX) as the highest-capitalized technology stock on the bourse. 

Today, CWG Plc powers the mission-critical core banking applications, ATM switching fabrics, and data center operations for over sixty percent (60%) of Nigerian commercial banks. Furthermore, the company has diversified into automated smart electricity metering infrastructure, cloud computing, managed security services, and tailored enterprise resource planning (ERP) platforms across telecommunications, oil and gas, government, and consumer retail sectors.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 2.1]                                      |
|                                                                       |
|  Figure 2.1: Computer Warehouse Group (CWG) Plc Corporate Identity    |
|  Description: High-resolution corporate logo of Computer Warehouse    |
|  Group (CWG) Plc, illustrating brand colors, typography, and symbol.  |
+-----------------------------------------------------------------------+
```

### 2.2 Core Business Sectors, Divisions, and Subsidiaries
CWG Plc operates through specialized strategic business units (SBUs), each focused on a distinct vertical of modern information and energy technology:

| Operating Division | Core Technical Mandate and Specialization | Enterprise Solutions and Flagship Services |
|---|---|---|
| **Cloud & Infrastructure Services** | Architecture, deployment, and management of tier-3 and tier-4 data centers, hyper-converged virtualization, enterprise storage arrays, and hybrid cloud infrastructures. | Private cloud hosting, disaster recovery as a service (DRaaS), backup replication, and server rack management. |
| **ATM & Financial Automation** | End-to-end deployment, engineering maintenance, electronic journal harvesting, and hardware overhaul of Automated Teller Machines and point-of-sale terminals. | Wincor Nixdorf / Diebold Nixdorf ATM hardware fleet servicing, ATM cash cassette calibration, and switching integration. |
| **Software Systems & Enterprise Platforms** | Custom enterprise software engineering, core banking implementation, middleware development, and workflow automation. | Core banking deployment (Finacle), enterprise middleware, custom web portals, and Microsoft Power Platform business automation. |
| **Smart Metering & Energy Solutions** | Design, assembly, bench calibration, optical parameterization, and deployment of smart prepayment electricity meters for DISCOs. | STS-compliant single-phase and three-phase smart meters, Meter Management Systems (MMS), GPRS AMI architectures, and NEMSA testing. |
| **CWG Academy** | Corporate social responsibility and human capital development arm providing intensive practical ICT education to young engineering graduates. | Bootcamps covering enterprise networking, software engineering, cloud systems administration, and financial technologies. |

### 2.3 Corporate Vision, Mission, and Core Values (W-E-C-A-R-E)
- **Corporate Vision:** To be the premier technology solution provider in Africa, enabling economic growth, digital transformation, and business agility across enterprises.
- **Corporate Mission:** Enhancing our customers' business productivity through innovative, resilient, and cost-effective technological solutions delivered by passionate, highly skilled professionals.
- **Core Corporate Values (W-E-C-A-R-E):**
  - **W — Way of Life:** Integrity, transparency, and personal accountability are woven into the fabric of everyday corporate conduct.
  - **E — Excellence:** Uncompromising dedication to international best practices, technical precision, and premium service delivery.
  - **C — Customer Centricity:** Designing every software architecture, network layout, and metering solution around the specific operational needs of clients.
  - **A — Agility:** Swift adaptation to disruptive technologies, rapidly evolving market dynamics, and customer requirements.
  - **R — Respect:** Deep regard for employees, clients, regulatory standards, diversity, and individual perspectives.
  - **E — Execution:** Tenacious focus on delivering measurable, auditable results on time and within agreed service level agreements (SLAs).

### 2.4 Organizational Structure and Hierarchy
CWG Plc operates a matrix organizational hierarchy designed to promote technical synergy between functional departments and executive governance. The corporate governance structure is headed by the Board of Directors, which provides strategic oversight, risk governance, and fiduciary leadership.

Executive leadership is directed by the Group Managing Director / Chief Executive Officer, **Mr. Adewale Adeyipo**, supported by the Chief Operating Officer, **Mr. Afolabi Sobande**, the Chief Technology Officer, **Mr. Moruf Ireti Yusuf**, and the Group Head of Human Resources, **Mrs. Tinu Adeyemi**.

Below the executive board, operational departments execute day-to-day engineering deliverables. The **Information Technology & Business Innovation (IT & BI)** Department—in which my Phase 2 attachment took place—is led by **Mrs. Abimbola** (Direct Industry Supervisor) and **Mr. Moses Mornu** (Team Lead). The unit comprises specialized technical cells:
- **Enterprise Applications & Power Platform Cell:** Directed by Bayo, responsible for custom internal software, Microsoft Power Apps, Dataverse modeling, and automated workflows.
- **Data Center & Server Infrastructure Cell:** Directed by Mr. Matthew, managing server hardware, virtualization clusters, SAN storage, Liebert cooling, and dual PDU power infrastructure.
- **Network Operations & Security Cell:** Directed by Mr. Michael, overseeing structured cabling, Cisco switching, 802.1Q VLANs, firewall policies, and multi-SSID wireless networks.
- **Proximity Support & Client Systems Cell:** Responsible for laptop provisioning, Active Directory user management, EDR agent monitoring, and end-user SLA resolution.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 2.2]                                      |
|                                                                       |
|  Figure 2.2: CWG Plc Corporate Organogram and IT & BI Hierarchy       |
|  Description: Formal organizational organogram illustrating the line   |
|  of authority from the Board of Directors down to the IT & BI cells.  |
+-----------------------------------------------------------------------+
```

### 2.5 Contributions to Nigeria's Digital Economy and Technological Sovereignty
CWG Plc's strategic contributions to Nigeria's socio-economic and technological landscape are substantial:
1. **Critical Financial Infrastructure Backbone:** By deploying and maintaining core banking applications (such as Infosys Finacle) and over four thousand (4,000) ATMs across leading commercial banks (including First Bank, Zenith Bank, United Bank for Africa, and Access Bank), CWG underpins the daily financial transaction architecture of Nigeria's economy.
2. **National Energy Transition and Metering Rollouts:** In alignment with the Federal Government's National Mass Metering Programme (NMMP), CWG's Metering & Energy Solutions division supplies high-precision, tamper-evident smart electricity meters to major distribution companies (DISCOs) such as Eko Electricity Distribution Company (EKEDC) and Ikeja Electric (IE). This drives revenue protection, minimizes aggregate technical, commercial, and collection (ATC&C) losses, and ensures equitable billing for Nigerian electricity consumers.
3. **Indigenous Human Capital Development:** Through the CWG Academy, the company has trained and released into the Nigerian economy over two thousand (2,000) highly certified network engineers, systems administrators, cybersecurity analysts, and software developers, reversing the brain drain and fostering technological self-reliance.

## CHAPTER THREE: INDUSTRIAL WORK EXPERIENCE & TECHNICAL ACTIVITIES

### 3.1 SECTION A: METERING DEPARTMENT & ENERGY AUTOMATION (June – August 2026)

#### 3.1.1 Overview of Solid-State Energy Measurement Physics and Metering Topologies
Modern electrical energy distribution relies on solid-state electronic smart meters to quantify instantaneous power flow, cumulative active energy consumption, and grid power quality parameters. Unlike legacy electromechanical induction disc meters—which suffered from mechanical friction wear, calibration drift, and vulnerability to external mechanical tampering—solid-state energy meters utilize precision analog-to-digital converters (ADCs), specialized digital signal processing (DSP) application-specific integrated circuits (ASICs), and microcontrollers to calculate energy parameters mathematically.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.1]                                      |
|                                                                       |
|  Figure 3.1: Architecture of Modern Solid-State Electronic Meter     |
|  Description: High-level architectural block diagram illustrating the |
|  analog front-end (AFE), ADE7758 energy metering IC, MCU, RTC,       |
|  GPRS cellular daughterboard, STS keypad, LCD, and optical port.      |
+-----------------------------------------------------------------------+
```

The fundamental physics governing electrical power measurement dictates that instantaneous active power $p(t)$ is the mathematical product of instantaneous line voltage $v(t)$ and instantaneous line current $i(t)$:
$$p(t) = v(t) \cdot i(t)$$

For single-phase alternating current (AC) sinusoidal systems operating at 50 Hz, the root-mean-square (RMS) active power $P$ is expressed as:
$$P = V_{	ext{RMS}} \cdot I_{	ext{RMS}} \cdot \cos  arphi$$
where $\cos  arphi$ represents the power factor, and $ arphi$ is the phase angle difference between the voltage and current waveforms. 

In solid-state smart meters assembled at CWG Plc, voltage sensing is achieved through a high-precision metal-film resistive voltage divider network connected across the line and neutral conductors. Current sensing, conversely, employs two distinct engineering topologies depending on the meter rating:
1. **Single-Phase Domestic Meters (5(60)A or 5(100)A):** Utilize an ultra-low resistance, temperature-compensated Manganin electron-beam welded shunt resistor (typically with a resistance value of $350 \, \mu\Omega$). Manganin is chosen because its temperature coefficient of resistance is near zero ($ pprox \pm 10 	imes 10^{-6} \, 	ext{K}^{-1}$), ensuring measurement linearity regardless of ambient temperature fluctuations. The voltage drop $\Delta V = I \cdot R_{	ext{shunt}}$ across the shunt is directly proportional to line current.
2. **Three-Phase Commercial and Industrial Meters (3×230/400V, 10(100)A or CT-operated 1.5(6)A):** Utilize high-permeability toroidal current transformers (CTs) or Rogowski coils. Toroidal CTs provide galvanic isolation between the high-voltage mains and low-voltage digital processing electronics, preventing ground loops and protecting internal microcontrollers from lightning surges and utility transients.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.2]                                      |
|                                                                       |
|  Figure 3.2: Internal PCB Layout of Single and Three-Phase Meters    |
|  Description: Comparative engineering diagram showing the physical    |
|  layout of the analog sensing circuitry, MCU, relays, and connectors. |
+-----------------------------------------------------------------------+
```

The differential voltage signals from the sensing elements are routed into an Energy Metering IC (such as the Analog Devices ADE7758 or Cirrus Logic CS5463). The metering IC executes continuous simultaneous analog-to-digital conversions at a sampling rate exceeding 10 kHz, performs digital integration over time to compute active energy $E_{	ext{active}} = \int P \, dt$ (expressed in kilowatt-hours, kWh), reactive energy $E_{	ext{reactive}} = \int Q \, dt$ (expressed in kilovar-hours, kVARh), and outputs proportional high-frequency calibration pulses through an optical light-emitting diode (LED).

#### 3.1.2 Electrostatic Discharge (ESD) Protection Protocols and Workstation Grounding
A paramount engineering priority in the smart meter production line is the rigorous mitigation of Electrostatic Discharge (ESD). Modern smart meter printed circuit boards (PCBs) incorporate sensitive complementary metal-oxide-semiconductor (CMOS) microcontrollers, EEPROM memory chips, and radio-frequency (RF) communication transceivers. These semiconductor devices feature microscopic gate oxide insulation layers that can be permanently ruptured by electrostatic discharge potentials as low as 100 Volts. Because the human body can routinely accumulate triboelectric static charges exceeding 3,000 to 15,000 Volts through simple friction (such as walking across a synthetic floor or handling plastic packaging), unprotected human contact causes catastrophic dielectric breakdown or latent semiconductor defects.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.3]                                      |
|                                                                       |
|  Figure 3.3: ESD Grounding Station, Busbar, and Dissipative Workbench |
|  Description: Engineering schematic of the static-dissipative ESD     |
|  workstation showing wrist-strap bonding, 1MΩ resistor, and busbar.   |
+-----------------------------------------------------------------------+
```

To guarantee absolute semiconductor reliability, CWG Plc maintains an ESD-protected area (EPA) compliant with international standard IEC 61340-5-1. The workstation protocols strictly enforced during my attachment included:
- **Static-Dissipative Matting:** Every assembly workbench is covered with a dual-layer static-dissipative rubber mat. The top layer has a surface resistivity of $10^6$ to $10^9 \, \Omega/	ext{sq}$ to bleed static charges safely to ground, while the bottom conductive layer has a resistivity of $10^3$ to $10^5 \, \Omega/	ext{sq}$.
- **Continuous Wrist-Strap Grounding:** Assembly technicians must continuously wear conductive elastic wrist straps containing silver-plated woven nylon fibers. The wrist strap snaps into a coiled grounding cord incorporating an integrated $1 \, 	ext{M}\Omega \pm 10\%$ carbon-film safety resistor. This resistor serves a dual purpose: it slows the static charge dissipation rate to prevent spark ignition, while protecting the operator from electrical shock hazards in the event of accidental contact with 230V mains voltage.
- **Dedicated Copper Earth Busbar:** All dissipative mats, wrist-strap terminal sockets, and metal equipment chassis are bonded to a dedicated 25mm × 3mm electrolytic copper earth busbar. The busbar is bonded directly to the facility's low-impedance earthing rod system, with grounding loop resistance rigorously verified to be less than $1.0 \, \Omega$ using a digital ground resistance clamp meter.
- **Operator Apparel:** Technicians wear anti-static polyester/cotton smocks containing interwoven conductive carbon filament grids, alongside conductive heel grounders and anti-static nitrile gloves.

#### 3.1.3 Precision Mechanical Coupling, Terminal Lug Torque Specs, and Enclosure Assembly
The mechanical coupling of a smart electricity meter is a critical phase that bridges internal electronics with physical environmental protection. Smart electricity meters are installed in diverse outdoor and indoor operating environments across Nigeria, exposing them to high humidity, dust ingress, ambient temperatures up to 45°C, and structural vibration.

The meter enclosure is injection-molded from high-impact, ultraviolet-stabilized (UV), flame-retardant polycarbonate (compliant with UL94-V0 flammability ratings). The mechanical coupling procedure follows a rigorous step-by-step work instruction:
1. **Base Housing Preparation and Terminal Block Seating:** The heavy-duty terminal block—molded from reinforced polybutylene terephthalate (PBT) containing brass terminal inserts—is aligned and seated into the base casing. The brass terminal lugs feature dual M6 clamping screws designed to secure up to $25 \, 	ext{mm}^2$ copper or aluminum service entrance cables.
2. **Current Shunt and Wiring Harness Securing:** The Manganin current shunt is mechanically bolted to the terminal inserts. A calibrated digital torque screwdriver is mandatory for this operation. The clamping screws are torqued precisely to $2.8 \, 	ext{N}\cdot	ext{m}$ (within the allowable engineering tolerance of $2.5 - 3.0 \, 	ext{N}\cdot	ext{m}$). Under-torquing leads to high contact resistance ($R_{	ext{contact}}$), which under a full continuous load of 60A causes excessive Joule heating ($P_{	ext{loss}} = I^2 R$) that can melt terminal insulation and initiate electrical fires. Over-torquing strips the brass threads and compromises mechanical integrity.
3. **Motherboard and Display Alignment:** The primary digital controller PCB is slid into internal guide rails and secured with non-magnetic stainless steel screws. The liquid crystal display (LCD) assembly—utilizing an elastomeric conductive "zebra" connector strip—is secured against the PCB contact fingers, followed by the optical light pipes and silicone rubber STS keypad.
4. **Top Cover Latching and IP54 Gasket Compression:** The transparent polycarbonate top cover is lowered over the base assembly. An ethylene propylene diene monomer (EPDM) synthetic rubber gasket is compressed between the housing perimeter to achieve an Ingress Protection rating of IP54 (dust-protected and resistant to water splashing from all directions).

#### 3.1.4 Real-Time Clock (RTC) Lithium Battery Installation, Voltage Thresholding, and Time-of-Use Tariffs
Smart prepayment energy meters must maintain an uncorrupted, real-time astronomical calendar (recording seconds, minutes, hours, days, months, and leap years) independent of external electrical supply. The internal Real-Time Clock (RTC) is driven by a precision 32.768 kHz tuning-fork quartz crystal oscillator with internal temperature compensation to prevent clock drift across thermal cycles.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.4]                                      |
|                                                                       |
|  Figure 3.4: Lithium RTC Backup Battery (CR2032/CR2450) Seating      |
|  Description: Technical illustration of the coin-cell battery socket, |
|  polarization keying, and multimeter voltage threshold verification.  |
+-----------------------------------------------------------------------+
```

The RTC is powered during normal operation by the meter's internal regulated DC power supply. However, during power outages, load shedding, or warehouse storage, power seamlessly transfers to a dedicated onboard backup lithium coin cell battery (CR2032 or CR2450 manganese dioxide lithium chemistry, 3.0V nominal).

The battery installation procedure involves strict electrical qualification:
- **Voltage Threshold Verification:** Before insertion into the spring-tensioned coin cell socket, every battery is tested using a calibrated Fluke 115 true-RMS digital multimeter under an active load resistance of $100 \, 	ext{k}\Omega$. The open-circuit terminal voltage must measure $\ge 3.05 \, 	ext{V DC}$. Any cell exhibiting a terminal potential below $3.00 \, 	ext{V DC}$ is rejected immediately, as chemical self-discharge would fail to provide the statutory 10-year backup retention period mandated by Nigerian distribution utilities.
- **Polarization and Contact Seating:** The battery is inserted with positive (+) terminal orientation facing upward, engaging the gold-plated beryllium-copper spring contacts. Technicians inspect the seated cell under magnification to ensure zero contact skew, preventing micro-vibration dislodgement during transit.
- **Time-of-Use (TOU) and Tamper Timestamping Role:** The verified RTC maintains multi-tariff billing registers (Peak, Off-Peak, and Shoulder tariff bands) established by the Nigerian Electricity Regulatory Commission (NERC). Crucially, the RTC also records the exact date, hour, minute, and second of security tamper events (such as terminal cover removal, reverse energy flow, or magnetic interference), creating an indisputable audit trail for utility forensic investigators.

#### 3.1.5 GPRS Cellular IoT Daughterboard Mounting, SMA Antenna Matching, and Network Handshake
Smart meters deployed within an Advanced Metering Infrastructure (AMI) network require bidirectional cellular telecommunication capabilities to transmit interval load profiles, power quality metrics, and tamper alerts to the utility's central Head-End System (HES), while receiving remote firmware updates, credit top-ups, and disconnect/reconnect commands.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.5]                                      |
|                                                                       |
|  Figure 3.5: GPRS / Cellular IoT Daughterboard Mounting and Antenna  |
|  Description: Photographic and schematic illustration of the cellular |
|  modem daughterboard, SIM socket, micro-coaxial cable, and SMA port.  |
+-----------------------------------------------------------------------+
```

The wireless communication subsystem is implemented as an interchangeable cellular IoT daughterboard incorporating a quad-band GSM/GPRS modem (Quectel M95 or SIM800C module). The engineering assembly protocol requires:
1. **Daughterboard Header Insertion:** The daughterboard is aligned with dual 12-pin gold-plated board-to-board interconnect headers on the main motherboard, establishing DC power supply rails, UART serial data lines (TX, RX, RTS, CTS), and hardware reset lines. Nylon locking standoffs are snapped into place to mechanically secure the module against shock.
2. **SIM Card Seating:** An industrial-grade, temperature-hardened M2M micro-SIM card (rated for $-40^\circ	ext{C}$ to $+105^\circ	ext{C}$) provisioned with a static APN and private IP address is inserted into the push-push SIM socket.
3. **RF Antenna Coupling and Impedance Matching:** An ultra-thin micro-coaxial cable (U.FL connector) connects the modem's RF output to an external SubMiniature version A (SMA) 50-Ohm female bulk-head connector mounted through the meter housing. Alternatively, for compact urban installations, an internal planar inverted-F antenna (PIFA) etched directly onto an FR-4 PCB carrier is plugged into the socket. The characteristic impedance of the transmission line is strictly matched to $50 \, \Omega$ to minimize Voltage Standing Wave Ratio (VSWR $\le 1.5$), maximizing radiated power and avoiding RF reflections that could damage the power amplifier.
4. **Cellular Network Handshake Verification:** During bench testing, the modem is stimulated via serial AT commands to confirm network registration (`AT+CREG?`), signal quality index (`AT+CSQ` returning a received signal strength indication of at least 15/31), and GPRS packet network attachment (`AT+CGATT=1`).

#### 3.1.6 Mains Energization Bench Testing, High-Voltage Safety, and Optical Pulse Error Verification
Following mechanical assembly, the smart meters are transferred to the automated calibration and test facility. Here, meters are mounted on multi-position test racks (capable of accommodating 24 to 48 meters simultaneously) for high-voltage mains energization, power-on self-tests (POST), and metrological calibration.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.6]                                      |
|                                                                       |
|  Figure 3.6: Multi-Position Meter Test Bench Setup for Calibration    |
|  Description: Test bench setup showing 230V/415V power injection,     |
|  reference power standard, optical scanning heads, and error meters.  |
+-----------------------------------------------------------------------+
```

The test bench incorporates an ultrastable three-phase reference power standard (such as the MTE or Radian Research standard) with a measurement accuracy class of 0.05%. The bench applies programmable AC voltages ($230 \, 	ext{V} \pm 10\%$ for single-phase; $400/415 \, 	ext{V}$ line-to-line for three-phase) and currents ranging from basic current ($I_b = 5 \, 	ext{A}$) to maximum continuous current ($I_{	ext{max}} = 60 \, 	ext{A}$ or $100 \, 	ext{A}$) across power factors of $\cos  arphi = 1.0$ (unity) and $\cos  arphi = 0.5$ lagging (inductive).

The calibration process verifies the frequency of the optical calibration LED pulses, standardized at $1600 \, 	ext{imp/kWh}$ (single-phase) or $800 \, 	ext{imp/kWh}$ (three-phase). High-speed optical scanning heads mounted on magnetic articulated arms focus on each meter's calibration pulse LED. The test bench counts the pulse intervals against the high-precision reference standard to compute the active energy percentage error:
$$	ext{Percentage Error }  arepsilon =  rac{E_{	ext{meter}} - E_{	ext{reference}}}{E_{	ext{reference}}} 	imes 100\%$$

Under International Electrotechnical Commission (IEC) standard 62053-21 and Nigerian statutory regulations, a Class 1.0 smart meter must maintain an active measurement error margin strictly within $\pm 1.0\%$ across the rated operating range, and within $\pm 1.5\%$ at $\cos  arphi = 0.5$ inductive. Any meter exhibiting an error exceeding these thresholds undergoes digital calibration parameter adjustment via firmware or is rejected for circuit component auditing.

#### 3.1.7 Standard Transfer Specification (STS) Token Verification and Diagnostic Keypad Short Codes
Prepayment functionality is governed by the Standard Transfer Specification (STS)—the global open standard for prepayment metering systems codified under IEC 62055-41 and IEC 62055-51. Under STS, credit is transferred from the utility vending server to the consumer's meter via an encrypted 20-digit numerical token entered using the meter's 12-key silicone keypad.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.7]                                      |
|                                                                       |
|  Figure 3.7: STS Token Keypad Diagnostic Testing and Short Codes     |
|  Description: Engineering schematic of the STS token entry protocol, |
|  keypad matrix scanning, and short code diagnostic display sequence.  |
+-----------------------------------------------------------------------+
```

The 20-digit STS token encodes the transaction value, a unique Token Identifier (TID) based on minutes elapsed since the STS base date (1st January 1993, transitioning to the 2014 epoch), the meter's unique 11-digit serial number, and a cryptographic Message Authentication Code (MAC) generated using the Data Encryption Standard (DES) or Triple-DES algorithm with the utility's unique Vending Key (VK).

During assembly testing, technicians execute physical keypad matrix scanning tests and enter standard STS test tokens to verify cryptographic validation logic:
- **Keypad Matrix Continuity:** Every key (`0` through `9`, `Backspace/Clear`, and `Enter/Accept`) is pressed sequentially to verify contact bounce suppression and acoustic buzzer feedback.
- **Credit Test Token:** Entering the standard 20-digit test token `0000 0000 0001 5123 4567` verifies token acceptance, displaying `ACCEPT` on the LCD, incrementing the credit register, and energizing the internal 100A latching bistable relay.
- **Duplicate and Invalid Token Rejection:** Re-entering the identical token verifies that the TID lockout algorithm detects token reuse and displays `USED`, preventing replay attacks.
- **Keypad Diagnostic Short Codes:** Technicians enter diagnostic short codes to query internal sensor registers:

| Keypad Short Code | Displayed Register Value | Engineering Description and Verification Criteria |
|---|---|---|
| **`#001#`** | Cumulative Active Energy (kWh) | Displays total active forward energy accumulated since manufacturing date. Must match test bench baseline. |
| **`#002#`** | Instantaneous Voltage (V), Current (A), Frequency (Hz) | Sequentially displays grid electrical parameters. Voltage must read $230 \pm 5\,	ext{V}$, frequency $50.0 \pm 0.2\,	ext{Hz}$. |
| **`#003#`** | Instantaneous Active Power (kW) and Power Factor ($\cos  arphi$) | Displays real-time power dissipation and phase relationship. Verified against reference load standard. |
| **`#004#`** | Total Cumulative Reverse Active Energy (kWh) | Quantifies reverse power flow, indicating potential meter inversion tampering or unauthorized microgeneration. |
| **`#005#`** | Tamper Event Status Register Bitmask | Displays a hexadecimal bitmask detailing whether terminal cover, top cover, or magnetic sensors have tripped. |
| **`#008#`** | Meter Firmware Version and Checksum | Validates that the authorized, certified firmware build is flashed into microcontroller flash memory. |

#### 3.1.8 Optical Port Interfacing and Mode Switching via Meter Management System (MMS)
Smart meters feature a front-facing bidirectional optical communication port compliant with IEC 62056-21 (formerly IEC 1107). The optical port consists of an infrared light-emitting diode (transmitting at an 880 nm wavelength) and a matched phototransistor receiver positioned behind an optical circular aperture fitted with a ferromagnetic metal ring for magnetic probe attachment.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.8]                                      |
|                                                                       |
|  Figure 3.8: MMS Optical Probe Interface and Optical Port            |
|  Description: Photographic and schematic illustration of the optical  |
|  communication probe head attached magnetically to the smart meter.  |
+-----------------------------------------------------------------------+
```

The optical interface operates as an isolated serial data link allowing technicians to communicate with the meter using the proprietary **Meter Management System (MMS)** software running on industrial diagnostic laptops. The communication protocol initiates at a standardized baud rate of 300 baud with a 7-bit character length, even parity, and 1 stop bit (`300, 7, E, 1`), transmitting an optical sign-on request string (`/?!<CR><LF>`). Upon acknowledging the identification string from the meter, the protocol executes a dynamic baud rate negotiation, shifting up to 9600 baud for high-speed binary data transfer using the Device Language Message Specification (DLMS) / COSEM (Companion Specification for Energy Metering) protocol.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.9]                                      |
|                                                                       |
|  Figure 3.9: Mode Switching: Factory Staging to Utility Production   |
|  Description: State machine transition diagram illustrating the shift |
|  from unlocked Factory Mode to cryptographically sealed Utility Mode. |
+-----------------------------------------------------------------------+
```

A crucial engineering milestone performed during my rotation was **Operating Mode Switching**:
1. **Factory / Staging Mode:** Newly manufactured meters exist in an unlocked "Factory Mode" where energy registers can be cleared, calibration offsets can be adjusted in EEPROM, and diagnostic tests run without incrementing consumer billing ledgers.
2. **Transition Protocol:** Using the optical probe and authenticated administrative credentials within MMS, technicians issue the cryptographic `SET_MODE_DEPLOYMENT` instruction. The meter writes a persistent flag into secure non-volatile memory, irreversibly disabling register zeroing, locking the calibration coefficients, enabling the cryptographic STS vending keys, and activating anti-tamper latching circuits.
3. **Utility Production Mode:** The meter enters its field-ready state. In this mode, any physical violation automatically records an unerasable tamper event, and all energy consumption is strictly committed to legal billing registers.

#### 3.1.9 Anti-Tamper Detection Circuitry, Field Auditing, and Reverse Energy Flow Mitigation
In the Nigerian electricity distribution landscape, commercial non-technical losses resulting from energy theft and meter tampering represent an existential financial challenge to DISCOs. Consequently, smart meters incorporate sophisticated hardware anti-tamper sensing circuitry and firmware surveillance logic:
- **Terminal Cover Removal Detection:** A miniature micro-switch with gold-plated bifurcated contacts is mounted on the motherboard, spring-loaded against the terminal cover. The moment an unauthorized person unfastens the terminal cover screws, the switch opens. Even if the meter is entirely de-energized, the RTC battery powers the MCU interrupt line, capturing the exact timestamp into the tamper log, incrementing the tamper counter, flashing a warning icon on the LCD, and tripping the internal latching disconnect relay.
- **Enclosure Top-Cover Breach Sensor:** A secondary micro-switch or optical reflective sensor detects if the upper transparent housing is cracked or pried open.
- **Strong Magnetic Interference Detection:** Power thieves frequently place powerful neodymium super-magnets (magnetic flux density $B > 0.3 \, 	ext{Tesla}$) against the meter casing to saturate inductive current transformer cores or distort electronic circuits. Smart meters feature an onboard Hall-effect sensor or anisotropic magnetoresistive (AMR) IC. When a strong magnetic field is detected, the meter logs a magnetic tamper event, illuminates a warning LED, and instantly shifts into an anti-theft maximum current billing mode ($I_{	ext{billing}} = I_{	ext{max}} = 60	ext{A}$), penalizing the perpetrator.
- **Neutral Missing / Bypass Detection:** In conventional single-phase metering, lifting the neutral connection deprives the meter of voltage sensing, causing it to stop registering while current continues to flow. Smart meters employ dual-current sensing (monitoring both the phase shunt and a neutral current transformer). If the phase current $I_{	ext{phase}}$ and neutral current $I_{	ext{neutral}}$ diverge by more than a pre-set threshold ($|\Delta I| > 6.25\%$), the meter detects an earth leakage or neutral bypass theft and bills according to the higher current value.
- **Reverse Energy Flow Protection:** If an unauthorized person inverts the service input and output load conductors to run the meter backward, the MCU's directional power calculation algorithm detects the negative sign of active power ($	ext{Sign}(P) < 0$). Under utility configuration, the meter either treats reverse power as forward consumption (absolute value energy summation: $E_{	ext{total}} = \int |P| \, dt$) or locks out and disconnects power, rendering reversal futile.

#### 3.1.10 Quality Control (QC), NEMSA Act 2015 Certification, Wire Crimp Sealing, and Packaging
The final stage of the smart metering lifecycle is the rigorous Quality Control inspection and statutory legal metrology certification mandated under the **Nigerian Electricity Management Services Agency (NEMSA) Act 2015**. NEMSA is the federal regulatory body legally empowered to enforce technical standards, inspect electrical installations, and certify all electricity meters deployed across the Nigerian Electricity Supply Industry (NESI).

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.10]                                     |
|                                                                       |
|  Figure 3.10: NEMSA Quality Verification and Wire Crimp Lead Sealing  |
|  Description: High-resolution illustration of the legal metrology     |
|  certification process, serial-embossed crimping, and lead sealing.   |
+-----------------------------------------------------------------------+
```

Every meter batch undergoes a rigorous statutory compliance audit before dispatch:

| NEMSA Statutory Inspection Parameter | Regulatory Requirement / Standard | Measurement Methodology & Pass Criteria |
|---|---|---|
| **Metrological Accuracy Class** | IEC 62053-21 Class 1.0 | Active energy error must be within $\pm 1.0\%$ at unity power factor, and $\pm 1.5\%$ at $\cos  arphi = 0.5$ lag. |
| **High-Voltage Dielectric Withstand** | IEC 62052-11 Insulation Standard | $4 \, 	ext{kV AC}$ applied at 50 Hz for 60 seconds between shorted terminals and external housing; leakage current $< 5 \, 	ext{mA}$. |
| **Impulse Voltage Withstand** | IEC 62052-11 Lightning Surge Test | $6 \, 	ext{kV}$ crest impulse voltage ($1.2/50 \, \mu	ext{s}$ waveform) applied with positive and negative polarities. |
| **Power Consumption (Burden)** | IEC 62053-21 Efficiency Mandate | Voltage circuit active power burden $< 2.0 \, 	ext{W}$ and apparent burden $< 10 \, 	ext{VA}$; current circuit $< 2.5 \, 	ext{VA}$. |
| **Starting Current Sensitivity** | IEC 62053-21 Starting Threshold | Meter must register energy and pulse continuously at $0.004 \, I_b$ ($20 \, 	ext{mA}$ for a 5A base meter). |
| **No-Load Creep Condition** | Anti-Creeping Anti-Fraud Test | When voltage is $115\% \, V_n$ with zero current ($I = 0$), optical calibration pulse must emit no more than one pulse. |

Upon passing all automated electrical tests, authorized NEMSA inspectors and CWG QC supervisors perform the physical legal sealing:
- **Tamper-Evident Wire Crimp Sealing:** A multi-strand, high-tensile stainless steel sealing wire (clad in transparent fluoropolymer coating) is threaded through the interlocking eyelets of the meter top cover and terminal enclosure. 
- **Serial-Embossed Lead / Polycarbonate Seals:** A specialized mechanical wire crimping tool with hardened, engraved dies compresses a heavy-duty lead or polycarbonate sealing capsule over the twisted wire ends. The crimper embosses a unique, tamper-evident alphanumeric code identifying the specific NEMSA testing station, certifying inspector, and calendar year. Cutting or breaking this wire seal constitutes a federal offense under Nigerian law.
- **Batch Ledger Logging and Serialization:** The meter's unique 11-digit serial number, MAC address, IMEI of the GPRS modem, calibrated pulse constant, and test report checksum are scanned via a high-speed barcode imager. The data is committed to the utility production database and printed onto heavy-duty water-resistant external carton labels.
- **Palletization and Environmental Packaging:** The sealed meters are nested into custom anti-static thermoformed shock-absorbent trays, packaged into export-grade corrugated cardboard cartons (12 meters per carton), banded onto wooden shipping pallets with polyethylene stretch wrap, and transferred to the bonded logistics warehouse ready for delivery to distribution utilities.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.11]                                     |
|                                                                       |
|  Figure 3.11: Packaging, Barcode Serialization, and QA Batch Ledger  |
|  Description: Final packing station showing barcode scanning, carton  |
|  packaging, batch ledger documentation, and palletization for DISCOs. |
+-----------------------------------------------------------------------+
```

### 3.2 SECTION B: IT PROXIMITY SUPPORT, NETWORK INFRASTRUCTURE & SYSTEMS ADMINISTRATION (September 2026 – Present)

#### 3.2.1 ITIL Help Desk Operations, Ticket Resolution Workflow, and Proximity SLA Compliance
On 1st September 2026, my rotational training transitioned to the **Information Technology & Business Innovation (IT & BI)** Department at CWG Plc headquarters. Under the direct supervision of Mrs. Abimbola and Team Lead Mr. Moses Mornu, my daily responsibilities expanded into enterprise IT support, physical network infrastructure, Windows systems engineering, and directory services administration.

Enterprise technical support at CWG Plc is governed by the Information Technology Infrastructure Library (ITIL v4) framework, utilizing ManageEngine ServiceDesk Plus and Jira Service Management as central ticketing platforms. Internal support requests originating from executive management, corporate finance, software developers, human resources, and marketing are categorized according to severity and Service Level Agreements (SLAs):
1. **Priority 1 (Critical Outage - SLA: 15-minute response, 2-hour resolution):** Pertains to core data center switch failure, enterprise Active Directory domain controller unresponsiveness, VPN gateway crashes, or ERP system downtime affecting entire departments.
2. **Priority 2 (High Impact - SLA: 30-minute response, 4-hour resolution):** Affects departmental network segments, localized Wi-Fi access point degradation, or VIP executive hardware malfunction during executive meetings.
3. **Priority 3 (Medium Impact - SLA: 2-hour response, 8-hour resolution):** Involves individual laptop hardware faults, OS corruption, corrupted Outlook PST profiles, software installation requests, or VPN client reconfiguration.
4. **Priority 4 (Low Impact / Service Request - SLA: 4-hour response, 24-hour resolution):** New employee laptop staging, secondary monitor allocation, peripheral replacements, or group membership adjustments in Active Directory.

Proximity support technicians conduct rapid desk-side triage, utilizing diagnostic command-line tools (`ping`, `tracert`, `nslookup`, `netstat`, `sfc /scannow`, `dism /online /cleanup-image /restorehealth`), resolving hardware anomalies, replacing failed power supplies, and documenting root-cause analysis (RCA) in the ticketing knowledge base before ticket closure.

#### 3.2.2 Enterprise Structured Cabling, TIA/EIA-568B Standard, and Patch Panel Termination
A resilient physical layer (Layer 1 of the OSI model) forms the indispensable foundation of all enterprise networking. CWG Plc maintains a high-density, structured copper and optical fiber cabling plant designed to support 10 Gigabit Ethernet (10GBASE-T) backbones and Gigabit desktop drops across multi-story office wings.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.12]                                     |
|                                                                       |
|  Figure 3.12: OSI 7-Layer and TCP/IP 4-Layer Architectural Models     |
|  Description: Detailed reference diagram contrasting OSI 7 layers     |
|  with TCP/IP 4 layers, showing data encapsulation and protocol units. |
+-----------------------------------------------------------------------+
```

During my rotation under Mr. Michael (Networking Lead), I mastered the end-to-end design, pulling, termination, and certification of Category 6 (Cat6) and Category 6A (Cat6a) Unshielded Twisted Pair (UTP) and Shielded Twisted Pair (STP) cables. Cat6a cables operate at transmission frequencies up to 500 MHz, featuring tighter internal pair twists, a central longitudinal polyethylene spline (cross-filler) to isolate individual pairs, and heavy-duty outer jackets to eliminate Alien Near-End Crosstalk (ANEXT).

All modular RJ-45 terminations and patch panel terminations at CWG Plc strictly adhere to the **ANSI/TIA/EIA-568B** commercial wiring standard:

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.13]                                     |
|                                                                       |
|  Figure 3.13: Cat6/Cat6a Structured Cabling Pinout (TIA/EIA-568B)     |
|  Description: Color-coded wiring pinout diagram showing individual    |
|  wire positions (1 through 8) for straight-through RJ-45 modular jacks.|
+-----------------------------------------------------------------------+
```

| Pin Number | TIA/EIA-568B Wire Color Coding | Gigabit Ethernet (1000BASE-T) Function | Electrical Signal Designation |
|---|---|---|---|
| **Pin 1** | White / Orange Stripe | Transmit / Receive Pair 2 (+) | BI_DA+ (Bidirectional Data A+) |
| **Pin 2** | Solid Orange | Transmit / Receive Pair 2 (-) | BI_DA- (Bidirectional Data A-) |
| **Pin 3** | White / Green Stripe | Transmit / Receive Pair 3 (+) | BI_DB+ (Bidirectional Data B+) |
| **Pin 4** | Solid Blue | Transmit / Receive Pair 1 (+) | BI_DC+ (Bidirectional Data C+) |
| **Pin 5** | White / Blue Stripe | Transmit / Receive Pair 1 (-) | BI_DC- (Bidirectional Data C-) |
| **Pin 6** | Solid Green | Transmit / Receive Pair 3 (-) | BI_DB- (Bidirectional Data B-) |
| **Pin 7** | White / Brown Stripe | Transmit / Receive Pair 4 (+) | BI_DD+ (Bidirectional Data D+) |
| **Pin 8** | Solid Brown | Transmit / Receive Pair 4 (-) | BI_DD- (Bidirectional Data D-) |

In enterprise wiring closets, horizontal cable runs originating from work area wall plates terminate at rack-mounted 24-port or 48-port 110-type Insulation Displacement Contact (IDC) patch panels. Using an impact punch-down tool calibrated to its high-impact setting, individual twisted conductors are driven into phosphor-bronze V-shaped IDC slots, which slice through the outer wire insulation without nicking the copper core, establishing gas-tight, oxidation-resistant electrical bonds while shearing excess wire flush.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.14]                                     |
|                                                                       |
|  Figure 3.14: 24-Port Patch Panel, Brush Panels, and Cable Looming   |
|  Description: Front and rear view of the rack-mounted patch panel,    |
|  showing 1U brush management panels, Velcro ties, and cable dress.    |
+-----------------------------------------------------------------------+
```

To maintain optimal rack organization and airflow, horizontal 1U brush panels and D-ring cable management bars are installed between patch panels and switches. Cable bundles are secured using reusable hook-and-loop (Velcro) fasteners rather than nylon zip-ties, which can compress cable geometry, distort pair twisting, and induce Return Loss.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.15]                                     |
|                                                                       |
|  Figure 3.15: Hardware Tools: Crimper, Punch-Down, and Wire Mapper    |
|  Description: Photographic layout of tools used: ratcheting RJ-45     |
|  crimper, Fluke MicroScanner cable tester, and Patchsee tracer.       |
+-----------------------------------------------------------------------+
```

Every terminated link is qualified using a digital wire mapper and time-domain reflectometer (TDR) cable tester (such as the Fluke MicroScanner2). The tester checks for:
- **Wire Map Integrity:** Confirming pin-to-pin continuity across all 8 conductors with zero open circuits, short circuits, crossed pairs, or split pairs.
- **Length and Propagation Delay:** Verifying that total link distance does not exceed the statutory 90-meter permanent link (or 100-meter channel) limit.
- **Cable Tracing via Patchsee Light System:** In high-density server racks containing hundreds of black patch cords, Patchsee optical tracer cables containing internal dual plastic optical fibers are utilized. Connecting an LED light injection tool to one boot illuminates the opposite connector boot, enabling instantaneous trace identification without disrupting active network links.

#### 3.2.3 Layer-2/Layer-3 Switching, 802.1Q VLAN Trunking, and Multi-SSID Enterprise Wi-Fi Provisioning
Enterprise Local Area Networks (LANs) cannot operate as a flat, unsegmented broadcast domain. In a flat network, broadcast storms, ARP flooding, and malware lateral movement degrade performance and compromise corporate data confidentiality. At CWG Plc, network traffic is partitioned into logical broadcast domains using Virtual Local Area Networks (VLANs) implemented across Cisco Catalyst 3850 and 9300 series enterprise managed switches.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.16]                                     |
|                                                                       |
|  Figure 3.16: Cisco Managed Layer-2/Layer-3 Switches and SFP+ Modules |
|  Description: Cisco Catalyst enterprise switches showing 10G SFP+    |
|  fiber uplinks, RJ-45 PoE+ ports, and status LED indicator panels.    |
+-----------------------------------------------------------------------+
```

The enterprise network architecture employs a robust hierarchical VLAN segmentation scheme:

| VLAN ID | VLAN Name / Domain | IP Subnet Allocation | Default Gateway | Security Policy and Traffic Isolation Rules |
|---|---|---|---|---|
| **VLAN 10** | Corporate Management | `10.10.10.0/24` | `10.10.10.1` | Restricted to switch/router out-of-band management; SSH/HTTPS only. |
| **VLAN 20** | Corporate Staff LAN | `10.10.20.0/23` | `10.10.20.1` | Corporate employee laptops; 802.1X authenticated; access to internal ERP. |
| **VLAN 30** | Voice over IP (VoIP) | `10.10.30.0/24` | `10.10.30.1` | 3CX IP telephony; QoS DSCP EF (Expedited Forwarding) prioritized. |
| **VLAN 40** | Guest Wi-Fi | `172.16.40.0/22` | `172.16.40.1` | Client isolation enabled; direct internet egress; zero internal access. |
| **VLAN 50** | Data Center Servers | `10.10.50.0/24` | `10.10.50.1` | Physical servers, hypervisors, SAN storage; protected by stateful firewall. |

Switchports connected to end-user workstations are provisioned in **Access Mode** (`switchport mode access`, `switchport access vlan 20`), stripping 802.1Q tags upon egress so workstations receive untagged Ethernet frames. Furthermore, access ports feature:
- **Port Security:** Restricting each physical switchport to a maximum of two learned MAC addresses (`switchport port-security maximum 2`, `switchport port-security violation restrict`), preventing unauthorized rogue switches or hubs from expanding unmanaged networks.
- **Spanning Tree PortFast and BPDU Guard:** Enabling immediate transition to the forwarding state (`spanning-tree portfast`, `spanning-tree bpduguard enable`) to avoid 30-second STP listening/learning delays, while automatically err-disabling the port if an unauthorized switch injects BPDU frames.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.17]                                     |
|                                                                       |
|  Figure 3.17: Multi-SSID Enterprise Wi-Fi and 802.1Q VLAN Trunking    |
|  Description: Network topology showing Cisco Catalyst switches, trunk |
|  links carrying 802.1Q tagged frames to Cisco Aironet APs with SSIDs. |
+-----------------------------------------------------------------------+
```

Inter-switch links and uplinks connecting enterprise Cisco Aironet / Catalyst Wi-Fi Access Points (APs) operate in **Trunk Mode** (`switchport mode trunk`, `switchport trunk encapsulation dot1q`). Under the IEEE 802.1Q standard, a 4-byte tag (including a 12-bit VLAN Identifier, VID) is inserted into the Ethernet frame header between the Source MAC and EtherType fields. This allows a single physical Cat6a drop to carry traffic for multiple Service Set Identifiers (SSIDs) simultaneously:
- **`CWG-Corporate` SSID:** Broadcasts on 5 GHz band; uses WPA3-Enterprise with RADIUS / 802.1X machine certificate authentication; maps internally to VLAN 20.
- **`CWG-Voice` SSID:** Dedicated to mobile softphones and Wi-Fi handsets; maps to VLAN 30 with WMM (Wi-Fi Multimedia) Voice prioritization.
- **`CWG-Guest` SSID:** Uses captive portal web authentication; maps to VLAN 40 with strict peer-to-peer client isolation preventing guests from scanning neighboring devices.

#### 3.2.4 Cisco Packet Tracer Enterprise Network Simulation and Routing Topologies
To validate complex routing protocols and failover topologies prior to production implementation, network engineers at CWG Plc design and simulate multi-branch enterprise architectures using Cisco Packet Tracer and GNS3.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.18]                                     |
|                                                                       |
|  Figure 3.18: Cisco Packet Tracer Network Simulation Topology        |
|  Description: Detailed Packet Tracer schematic showing dual core      |
|  routers, Layer-3 distribution switches, OSPF areas, and WAN links.  |
+-----------------------------------------------------------------------+
```

During specialized training sessions led by Mr. Michael, I modeled an enterprise multi-site topology interconnecting CWG Lagos headquarters with regional branches in Abuja and Port Harcourt. The simulated design incorporated:
- **Core Layer-3 Routing:** Cisco 2911 series integrated services routers configured with Open Shortest Path First (OSPF v2) single-area routing (`router ospf 1`, `network 10.10.0.0 0.0.255.255 area 0`) providing sub-second path convergence.
- **Inter-VLAN Routing via Router-on-a-Stick:** Sub-interface creation with 802.1Q encapsulation (`interface GigabitEthernet0/0.20`, `encapsulation dot1Q 20`, `ip address 10.10.20.1 255.255.254.0`).
- **Dynamic Host Configuration Protocol (DHCP) Relay:** Configuring `ip helper-address 10.10.50.10` on router sub-interfaces to forward client UDP broadcast discover messages across subnet boundaries to the central Windows Server DHCP cluster.
- **Access Control Lists (ACLs):** Extended named ACLs deployed on distribution switches to enforce security perimeters, blocking Guest VLAN (`172.16.40.0/22`) hosts from establishing TCP connections to Server VLAN (`10.10.50.0/24`) databases while permitting outbound HTTP/HTTPS web traffic.

#### 3.2.5 Enterprise Data Center Facilities, 42U Server Racks, Dual PDU Feeds, and Environmental CRAC Cooling
The on-premise enterprise data center at CWG Plc houses the compute, storage, and networking clusters underpinning both internal corporate operations and hosted financial client platforms. The facility is engineered to Tier-3 specifications, guaranteeing 99.982% annual uptime with concurrent maintainability.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.19]                                     |
|                                                                       |
|  Figure 3.19: 42U Data Center Server Rack, Cage Nuts, and Looming    |
|  Description: High-density 42U server cabinet illustrating cage nut   |
|  chassis mounting, vertical PDU positioning, and cable looming.      |
+-----------------------------------------------------------------------+
```

Working under Mr. Matthew (Infrastructure Lead), I gained practical hands-on experience in data center physical engineering:
- **42U Server Cabinet Architecture:** Standard 19-inch EIA-310-D server racks measuring 42 rack units (42U, where $1\text{U} = 1.75 \text{ inches} = 44.45 \text{ mm}$) in height and 1000 mm in depth. Equipment mounting utilizes square-hole vertical rails fitted with zinc-plated spring-steel **cage nuts** (M6 threading). Mounting Dell PowerEdge chassis requires snapping cage nuts into exact vertical unit alignments using a cage nut insertion tool, followed by sliding tool-less ReadyRails into place.
- **Dual-Feed Power Redundancy (A & B Power Paths):** To eliminate single points of failure, every server rack is equipped with dual vertical intelligent Power Distribution Units (ePDUs) labeled PDU A and PDU B. PDU A is energized via an online double-conversion Uninterruptible Power Supply (UPS A) backed by Diesel Generator 1, while PDU B is energized via independent UPS B backed by Diesel Generator 2. Enterprise servers with redundant hot-pluggable power supplies connect Supply 1 to PDU A and Supply 2 to PDU B. If an entire power path collapses, the remaining supply assumes 100% of the electrical load seamlessly without service interruption.
- **Hot-Aisle / Cold-Aisle Containment:** Server racks are oriented face-to-face and back-to-back. Cold air discharged from the raised access floor plenum (24-inch void) enters the front perforated rack doors (Cold Aisle at 20°C to 22°C), passes through internal server chassis fans, absorbs thermal heat from CPUs and memory, and exhausts out the rear doors into the contained Hot Aisle (32°C to 35°C).
- **Liebert Precision Cooling (CRAC Units):** Environmental thermal management is controlled by Emerson Liebert Computer Room Air Conditioning (CRAC) units. These systems utilize variable-speed electronically commutated (EC) backward-curved centrifugal fans, dual scroll compressors, and chilled water / direct expansion (DX) coils to maintain strict temperature ($21^\circ\text{C} \pm 1^\circ\text{C}$) and relative humidity ($45\% \text{ to } 50\%$) envelopes. Precise humidity control prevents electrostatic discharge accumulation when air is too dry ($< 30\%$ RH) and prevents hygroscopic dust conductive bridge shorts when air is too humid ($> 60\%$ RH).

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.20]                                     |
|                                                                       |
|  Figure 3.20: Dual-Feed Power Distribution (PDU A/B) and CRAC Unit   |
|  Description: Technical diagram of data center power path redundancy  |
|  from dual UPS to rack PDUs, alongside Liebert precision cooling.     |
+-----------------------------------------------------------------------+
```

#### 3.2.6 Enterprise Server Architecture, Hardware RAID Redundancy, and IPMI/iDRAC Out-of-Band Management
Server hardware deployed within CWG data centers consists primarily of 1U and 2U Dell PowerEdge R640 and R740 rackmount servers powered by dual Intel Xeon Scalable processors, high-speed DDR4 registered ECC memory, and enterprise NVMe / SAS storage arrays.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.21]                                     |
|                                                                       |
|  Figure 3.21: Enterprise Server Hardware: Dell PowerEdge Chassis      |
|  Description: Internal anatomy of Dell PowerEdge R740 chassis showing |
|  dual CPU sockets, DIMM slots, hot-swap fans, PERC RAID, and iDRAC.   |
+-----------------------------------------------------------------------+
```

1. **Hardware RAID Controllers:** Storage reliability is enforced by Dell PowerEdge RAID Controllers (PERC H730P/H740P) featuring 8GB of non-volatile flash-backed cache (NV Cache). The storage architecture implements:
   - **RAID 1 (Mirrored Array):** Configured across dual 480GB enterprise SATA SSDs dedicated exclusively to the host Operating System / Type-1 Hypervisor. Provides complete disk mirroring; read throughput is doubled while write performance is maintained.
   - **RAID 5 / RAID 10 (Striped Arrays):** Configured across high-capacity enterprise 2.5-inch 12Gbps SAS hard drives for virtual machine datastores and database backups. RAID 10 combines disk striping (RAID 0) and disk mirroring (RAID 1), providing maximum I/O operations per second (IOPS) with fault tolerance capable of sustaining multiple concurrent drive failures across different mirror sets.
2. **Out-of-Band Remote Management via iDRAC9:** Enterprise servers incorporate an independent, dedicated processor running an embedded Linux OS—the **Integrated Dell Remote Access Controller (iDRAC9 Enterprise)**. Operating on an isolated out-of-band management network port with its own IP address, iDRAC allows infrastructure engineers to monitor server health, check thermal sensor readouts, review power consumption, execute remote power cycles (hard reboot, graceful shutdown), access remote virtual KVM consoles via HTML5, and mount virtual ISO installation media without requiring physical presence in the server room.
3. **Hypervisor Virtualization (Type-1 Bare-Metal):** Server workloads are virtualized using VMware ESXi 8.0 and Microsoft Hyper-V Server. In contrast to hosted Type-2 hypervisors (such as Oracle VirtualBox or VMware Workstation, which execute on top of a conventional consumer operating system), Type-1 bare-metal hypervisors install directly onto the physical server hardware. This direct hardware mediation delivers near-native CPU and memory performance, minimal latency, and robust resource isolation between production virtual machines.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.22]                                     |
|                                                                       |
|  Figure 3.22: Type-1 Bare-Metal vs Type-2 Hosted Hypervisors        |
|  Description: Architectural comparison illustrating hardware layer,   |
|  hypervisor abstraction, and guest OS execution across both models.   |
+-----------------------------------------------------------------------+
```

#### 3.2.7 Automated Corporate Fleet Provisioning using Windows Configuration Designer `.ppkg` Packages
A major responsibility during my proximity support rotation was the high-volume staging, deployment, and re-imaging of corporate laptops—primarily Dell Latitude (5420/5430 series) and HP EliteBook (840 G8/G9 series)—allocated to new employees, software developers, and executive staff.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.23]                                     |
|                                                                       |
|  Figure 3.23: Automated Windows 11 Staging via Custom `.ppkg` Package  |
|  Description: Workflow diagram of Windows Configuration Designer,     |
|  showing OEM image boot, OOBE intercept, USB `.ppkg` application.     |
+-----------------------------------------------------------------------+
```

Traditionally, manual operating system installation, application deployment, domain joining, and security hardening required up to 3 to 4 hours per machine. To optimize operational turnaround and enforce strict corporate baseline standardization, our IT support team deployed an automated provisioning workflow utilizing **Windows Configuration Designer** and custom Provisioning Packages (`.ppkg`).

The `.ppkg` staging architecture functions as an automated post-install payload applied during the Windows Out-of-Box Experience (OOBE):
1. **Packaging Configuration:** Using Windows Configuration Designer on an administrative staging workstation, an enterprise provisioning package (`CWG_Corporate_Staging_v4.2.ppkg`) was authored and cryptographically signed. The package encapsulates:
   - Automated computer renaming based on serial number and asset tag conventions (e.g., `CWG-LAP-%SERIAL%`).
   - Unattended joining to the on-premise Active Directory domain (`cwg.local`) using an encrypted domain-join service account.
   - Placement of the computer account into the designated organizational unit (`OU=Staged_Laptops,OU=Computers,DC=cwg,DC=local`).
   - Local administrator account generation with an enterprise randomized password, followed by automatic disabling of the built-in default Administrator.
   - Enforcement of BitLocker Drive Encryption (XTS-AES 256-bit encryption algorithm) requiring Trusted Platform Module (TPM 2.0) hardware attestation and backing up the 48-digit recovery key automatically to Active Directory and Microsoft Entra ID.
   - Silent, unattended installation of core corporate applications: Microsoft 365 Enterprise Apps (Word, Excel, PowerPoint, Outlook, Teams), CrowdStrike Falcon Sensor, Sophos Central Endpoint, ManageEngine Endpoint Central Agent, GlobalProtect VPN, and Google Chrome Enterprise.
   - Importation of CWG Private Root Certificate Authority (CA) certificates into the Windows Trusted Root Certification Authorities store.
   - Removal of consumer pre-installed OEM bloatware, consumer trials, and unapproved Windows Store applications.
2. **Execution Workflow:** Technicians boot a factory-fresh or freshly re-imaged laptop from its internal NVMe SSD into the initial Windows 11 OOBE language selection screen. Inserting a high-speed USB 3.2 flash drive containing the `.ppkg` file triggers Windows Setup to automatically detect the payload. Pressing the Windows key five times (or allowing auto-execution) prompts: *"Is this device for work or school?"* The technician selects the package, clicks *Yes, add it*, and removes the USB drive. The OS executes all silent installations, reboots twice, completes domain registration, enforces BitLocker, and presents the corporate domain login screen within 18 minutes—reducing technician touch time by over 85%.

#### 3.2.8 Computer Hardware Maintenance, Component Replacement, and Hardware Upgrades
Beyond software configuration, proximity support involves component-level hardware repair, diagnostic troubleshooting, and lifecycle upgrades across the corporate computer fleet.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.24]                                     |
|                                                                       |
|  Figure 3.24: Laptop Hardware Maintenance: RAM and NVMe SSD Upgrades  |
|  Description: Photographic sequence showing ESD mat work, base cover  |
|  removal, SO-DIMM RAM installation, and M.2 PCIe NVMe SSD swap.       |
+-----------------------------------------------------------------------+
```

Working at the hardware diagnostic workbench, I executed numerous physical repairs:
- **Random Access Memory (RAM) Upgrades:** Modern software development stacks and data analytics workloads frequently exceed base 8GB memory configurations, causing heavy page file thrashing and disk I/O bottlenecks. Technicians disconnect internal lithium-polymer battery packs, discharge residual capacitive charges by depressing the power button for 15 seconds, and unlatch dual DDR4/DDR5 Small Outline Dual In-line Memory Module (SO-DIMM) spring clips. Modules were upgraded to 16GB or 32GB dual-channel configurations (e.g., matching Kingston or Micron DDR4-3200MHz CL22 SO-DIMMs), followed by running UEFI Dell Pre-boot System Diagnostics (ePSA) memory tests to verify timing stability.
- **Storage Subsystem Upgrades:** Upgrading failing mechanical hard disk drives (HDDs) or legacy SATA M.2 SSDs to high-performance PCIe Gen3/Gen4 x4 M.2 NVMe Solid-State Drives (such as Samsung 980 Pro or Crucial P3). After seating the M.2 drive at a 30-degree angle and securing the captive screw, thermal conductive silicone pads and copper heatsink shields were installed to dissipate thermal throttling under sustained sequential transfers.
- **Thermal Overhaul and Repasting:** Laptops exhibiting thermal throttling, persistent high fan noise, or sudden thermal shutdown (temperatures exceeding 95°C under load) underwent complete thermal overhaul. The copper heat pipe and blower fan assembly was unbolted in reverse numerical sequence (4-3-2-1) to avoid micro-cracking the silicon die. Dried, degraded factory thermal interface material (TIM) was cleaned from the CPU/GPU die using 99.9% pure isopropyl alcohol (IPA) and lint-free microfiber swabs. A rice-grain bead of high-conductivity Arctic MX-4 carbon-based thermal paste (thermal conductivity $8.5 \, \text{W}/\text{m}\cdot\text{K}$) was applied to the bare die, and heatsink screws were torqued in ascending order (1-2-3-4) to guarantee uniform pressure distribution. Operating temperatures dropped by an average of 14°C to 18°C.
- **Lithium-Ion Battery Swelling and Replacement:** Diagnosed swollen laptop batteries causing trackpad distortion or chassis separation. Swollen lithium-ion cells pose severe chemical fire hazards; these units were carefully unfastened using non-magnetic ESD tweezers, isolated in fireproof LiPo safety bags, and replaced with genuine OEM battery packs, followed by BIOS battery health calibration.

#### 3.2.9 Microsoft Active Directory Domain Services (AD DS) Administration and OU Hierarchy
Microsoft Active Directory Domain Services (AD DS) serves as the centralized identity, authentication, and directory management platform for CWG Plc's enterprise ecosystem. Operating across redundant domain controllers (`DC1.cwg.local`, `DC2.cwg.local`), AD DS authenticates all user logons via the Kerberos v5 protocol and manages resource authorization.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.25]                                     |
|                                                                       |
|  Figure 3.25: Microsoft Active Directory Management Console (AD DS)   |
|  Description: Active Directory Users and Computers (ADUC) interface   |
|  showing the logical Organizational Unit (OU) structure and users.    |
+-----------------------------------------------------------------------+
```

Under the tutelage of Mr. Moses Mornu, I administered directory objects within the Active Directory Users and Computers (ADUC) management console. The directory structure is organized hierarchically into logical Organizational Units (OUs) reflecting corporate geography and departmental divisions:
```
DC=cwg,DC=local
├── OU=CWG_Corporate
│   ├── OU=Lagos_Headquarters
│   │   ├── OU=Departments
│   │   │   ├── OU=Executive_Management
│   │   │   ├── OU=Human_Resources
│   │   │   ├── OU=Finance_Accounting
│   │   │   ├── OU=IT_Business_Innovation
│   │   │   ├── OU=Software_Engineering
│   │   │   ├── OU=Metering_Energy
│   │   │   └── OU=Sales_Marketing
│   │   ├── OU=Security_Groups
│   │   │   ├── SG_All_Staff
│   │   │   ├── SG_IT_Admins
│   │   │   ├── SG_Finance_ReadWrite
│   │   │   └── SG_VPN_RemoteAccess
│   │   └── OU=Computers
│   │       ├── OU=Laptops
│   │       ├── OU=Desktops
│   │       └── OU=Servers
│   ├── OU=Abuja_Branch
│   └── OU=Regional_Subsidiaries (Ghana, Uganda, Cameroon)
```

Daily administrative tasks performed included:
- **User Provisioning:** Creating standardized user accounts following the corporate naming standard (`firstinitiallastname@cwg.local`), setting telephone numbers, departmental titles, email addresses, and populating the crucial `Manager` attribute (which maps the employee's direct line manager for automated workflow approvals).
- **Security Group Membership:** Assigning users to global and domain-local security groups to grant least-privilege Access Control Lists (ACLs) to departmental Network Attached Storage (NAS) file shares, printer pools, and application permissions.
- **Account Lifecycle and Credential Management:** Executing password resets for locked-out accounts, enforcing the *"User must change password at next logon"* flag, unlocking accounts locked by excessive failed Kerberos logon attempts, and disabling departing staff accounts while preserving mailbox archives for compliance.

#### 3.2.10 Group Policy Objects (GPOs) Deployment, Password Complexity, and Storage Device Hardening
Group Policy Objects (GPOs) provide the centralized policy engine through which system administrators enforce configuration standards, operating system settings, and security baselines across thousands of domain-joined Windows machines.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.26]                                     |
|                                                                       |
|  Figure 3.26: Group Policy Management Console (GPMC) Security Baseline|
|  Description: GPMC interface showing linked GPOs, security filtering, |
|  password policies, and removable storage lockdown configurations.    |
+-----------------------------------------------------------------------+
```

Using the Group Policy Management Console (GPMC), our IT team maintained and deployed enterprise security GPOs:

| Group Policy Object (GPO) | Target Scope / OU | Policy Setting and Registry Key | Security Objective and Enforcement |
|---|---|---|---|
| **`CWG-SEC-PasswordPolicy`** | Linked to Domain Root (`cwg.local`) | Minimum password length = 12 characters; Complexity enabled (uppercase, lowercase, numbers, symbols); Maximum password age = 90 days; History = 10 passwords remembered. | Prevents brute-force dictionary attacks; enforces regular credential rotation. |
| **`CWG-SEC-AccountLockout`** | Linked to Domain Root | Account lockout threshold = 5 invalid attempts; Lockout duration = 30 minutes; Reset counter after = 15 minutes. | Neutralizes automated online password spraying attacks across domain endpoints. |
| **`CWG-SEC-ScreenLockout`** | Linked to `OU=Computers` | `Interactive logon: Machine inactivity limit` = 600 seconds (10 minutes); Screen saver grace period = 0 seconds; Password required on resume. | Locks unattended employee laptops in shared office spaces, mitigating physical unauthorized access. |
| **`CWG-SEC-USB-RemovableStorage`** | Linked to `OU=Departments` (Except IT) | `User Configuration -> Administrative Templates -> System -> Removable Storage Access -> All Removable Storage classes: Deny all access` = Enabled. | Blocks USB flash drives and external hard drives, preventing corporate data exfiltration and malware ingress. |
| **`CWG-SEC-BitLocker-Enforcement`** | Linked to `OU=Laptops` | `Require BitLocker drive encryption without TPM: Disabled`; `Choose drive encryption method: XTS-AES 256-bit`; `Store recovery key in AD DS: Enabled`. | Renders stolen or misplaced laptop drives unreadable; secures corporate intellectual property. |

GPO replication across domain controllers was audited via Distributed File System Replication (DFSR) health checks, and policy application on client machines was verified using `gpupdate /force` and `gpresult /r /v` diagnostics.

#### 3.2.11 Enterprise Endpoint Detection and Response (EDR) Monitoring: Sophos Central and CrowdStrike Falcon
In response to modern advanced persistent threats (APTs), ransomware epidemics, and zero-day exploits, CWG Plc operates a defense-in-depth endpoint security architecture leveraging two leading Endpoint Detection and Response (EDR) platforms: **CrowdStrike Falcon** and **Sophos Central Intercept X**.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.27]                                     |
|                                                                       |
|  Figure 3.27: Enterprise Endpoint Security: Sophos & CrowdStrike Falcon|
|  Description: Cloud management console showing real-time EDR agent   |
|  health, threat detection telemetry, and quarantine actions.          |
+-----------------------------------------------------------------------+
```

Traditional signature-based antivirus engines fail against fileless malware, living-off-the-land binaries (LOLBins), and polymorphic ransomware. The EDR agents deployed across all corporate endpoints function differently:
- **CrowdStrike Falcon Sensor:** Operates as an ultra-lightweight kernel-level driver (less than 1% CPU utilization) that records all system events—including process execution, thread injection, registry modifications, network socket connections, and script execution (PowerShell, VBScript). This telemetry is streamed in real time to the CrowdStrike cloud threat graph. Using machine learning behavioral heuristics and Indicators of Attack (IOAs), Falcon detects malicious behavior (e.g., PowerShell attempting to download an encoded base64 payload into memory or invoking `vssadmin delete shadows`) and terminates the attacking process tree within milliseconds.
- **Sophos Central Intercept X:** Provides CryptoGuard anti-ransomware technology. When untrusted processes attempt rapid, unauthorized file encryption across user directories, Sophos intercepts the disk I/O, isolates the process, reverts encrypted files back to their uncorrupted pre-attack state using rollback cache snapshots, and alerts IT administrators.
- **Agent Health Auditing:** As part of daily proximity operations, technicians review the centralized EDR cloud dashboard to verify that all domain-joined endpoints maintain active, communicating agents with the latest sensor versions. Any machine exhibiting disconnected telemetry for more than 48 hours is quarantined from the corporate network until health is restored.

#### 3.2.12 IT Asset Management, Barcode Tagging, Physical Inventory Audits, and NIST 800-88 Decommissioning
Effective IT service delivery demands meticulous tracking of the physical location, operational health, assigned custodianship, and financial depreciation of all technological assets. CWG Plc enforces strict IT Asset Management (ITAM) and inventory control procedures.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.28]                                     |
|                                                                       |
|  Figure 3.28: IT Hardware Asset Inventory and Barcode Tagging        |
|  Description: Photographic evidence of metallic barcode asset tags,   |
|  handheld barcode scanner, inventory register, and secure store.      |
+-----------------------------------------------------------------------+
```

1. **Asset Tagging and Serialization:** Every hardware unit entering the organization—including laptops, desktops, monitors, Cisco switches, patch panels, server blades, and biometric access terminals—is affixed with a tamper-evident, anodized aluminum barcode asset tag (e.g., `CWG-AST-04892`). The asset tag number, manufacturer, model, serial number, processor specification, RAM capacity, storage capacity, MAC address, purchase order number, acquisition date, and assigned staff custodian are registered into the central ITAM database.
2. **Physical Inventory Stock Verification:** Bi-monthly physical store audits are conducted inside the secured IT inventory cage. Technicians systematically scan physical asset barcodes using laser handheld terminals, cross-referencing scanned data against the Active Directory computer container and accounting fixed asset ledgers to detect phantom assets, misplaced spares, or unreturned equipment.
3. **Hardware Decommissioning and NIST 800-88 Disk Sanitization:** When hardware assets reach the end of their operational lifecycle (typically 4 to 5 years), they undergo formal decommissioning to prevent corporate data leakage. Simple OS reformatting is inadequate, as forensic file recovery tools can easily reconstruct deleted files from raw drive sectors. In compliance with **NIST Special Publication 800-88 Revision 1 (Guidelines for Media Sanitization)**:
   - Functional SSDs and HDDs slated for redeployment or donation undergo cryptographic erasure and multi-pass overwrite (writing pseudo-random binary patterns across all addressable logical blocks).
   - Defective drives that fail overwrite verification are degaussed using high-intensity magnetic pulse degaussers and physically destroyed using a mechanical drive shredder, with certificates of destruction issued for corporate compliance audits.

### 3.3 SECTION C: SOFTWARE DEVELOPMENT AND ENTERPRISE SOLUTIONS

#### 3.3.1 Enterprise Software Development Methodologies: Agile Scrum Framework and CI/CD Pipelines
Enterprise software engineering at CWG Plc operates within modern iterative frameworks designed to maximize development velocity, software quality, and business alignment. Both major software initiatives undertaken during my industrial attachment—the **CWG Retail Suite** and the **LeaveTrack Enterprise Platform**—were managed using the **Agile Scrum** methodology.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.29]                                     |
|                                                                       |
|  Figure 3.29: Agile Scrum Engineering Lifecycle and CI/CD Pipeline    |
|  Description: Diagram showing sprint planning, daily standup, sprint  |
|  backlog, git feature branches, automated build, and code reviews.   |
+-----------------------------------------------------------------------+
```

Key engineering practices observed throughout development included:
- **Sprint Cycles and Backlog Grooming:** Development was organized into two-week sprints. Each sprint commenced with sprint planning meetings where business user stories were decomposed into granular technical tasks within Jira, estimated using story points, and assigned to developers.
- **Daily Standup Syncs:** 15-minute daily standups focused on three questions: *What was completed yesterday? What will be worked on today? What technical impediments or blockers exist?*
- **Git Branching Strategy (GitFlow):** Code repositories were maintained on GitHub. Developers were strictly prohibited from committing directly to the `main` production branch. Instead, feature branches (`feature/pos-barcode-listener`, `feature/leavetrack-dataverse-sync`) branched off `develop`. Merging required passing automated CI linting tests and receiving peer code review approvals from senior engineers.
- **Architectural Modularity and Clean Code:** Adhering strictly to enterprise software design patterns, including Model-View-Controller (MVC) separation, Single Responsibility Principle (SRP), and dependency injection. In the frontend React codebase, components were strictly refactored into modular subcomponents to maintain maintainability and eliminate bloated files.

#### 3.3.2 Major Project I: CWG Retail Suite (Full-Stack POS & Inventory Management Platform)

##### 3.3.2.1 Problem Analysis and Architectural Design: Decoupled Micro-Monolith (React 19 + Laravel 12)
Retail and inventory operations across modern commercial enterprises face severe challenges with traditional monolithic architectures: slow page loads, bloated server rendering, complex state synchronization across cash registers, and inventory race conditions during peak checkout periods. 

To address these limitations, I engineered the **CWG Retail Suite**—a high-performance, enterprise-grade Point of Sale (POS) and inventory management platform designed around a decoupled micro-monolith architectural pattern.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.30]                                     |
|                                                                       |
|  Figure 3.30: CWG Retail Suite Decoupled Architecture Diagram         |
|  Description: System architecture illustrating React 19 SPA, Axios,   |
|  Laravel 12 REST API, Sanctum Token Auth, SQLite/MySQL, and Printer.  |
+-----------------------------------------------------------------------+
```

The system architecture cleanly decouples the presentation and data tiers:
1. **Frontend Presentation Tier (React 19 SPA):** Engineered as a Single Page Application (SPA) leveraging React 19, Vite build tooling, React Router for client-side routing, and modern reactive state management. The UI delivers instantaneous user feedback without full-page reloads, featuring specialized keyboard event interceptors for hardware USB barcode scanners.
2. **Backend API Services Tier (Laravel 12 RESTful API):** Developed using PHP 8.3 and the Laravel 12 framework. The backend exposes stateless, high-performance RESTful JSON endpoints protected by Laravel Sanctum bearer token authentication. Business logic is organized into clean Controllers, Service classes, Form Request validators, and Eloquent ORM models.
3. **Data Persistence Tier (SQLite / MySQL):** Relational database optimized in Third Normal Form (3NF) with foreign key constraints, composite indexing on high-frequency query paths, and automated migration management.
4. **Hardware Interfacing Subsystem:** Direct integration with 80mm ESC/POS thermal receipt printers via browser-native print streams and USB human interface device (HID) barcode scanners.

##### 3.3.2.2 3NF Relational Database Schema Design and Key Constraints
A rigorous relational schema is imperative to prevent data redundancy, eliminate update anomalies, and maintain transactional integrity across inventory movements.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.31]                                     |
|                                                                       |
|  Figure 3.31: CWG Retail Suite 3NF Relational Database ERD            |
|  Description: Entity-Relationship Diagram showing users, categories,   |
|  products, transactions, transaction_items, stock_adjustments, logs.   |
+-----------------------------------------------------------------------+
```

The database design satisfies Third Normal Form (3NF), where every non-key attribute is non-transitively dependent on the primary key:

| Table Name | Primary Key | Foreign Keys & Target Tables | Key Attributes & Data Types | Database Purpose & Integrity Rules |
|---|---|---|---|---|
| **`users`** | `id` (BIGINT) | None | `name` (VARCHAR), `email` (VARCHAR, UNIQUE), `password` (VARCHAR), `role` (ENUM: 'admin', 'cashier'), `status` (ENUM: 'active', 'pending') | Authentication credentials, RBAC authorization, and account approval status. |
| **`categories`** | `id` (BIGINT) | None | `name` (VARCHAR), `slug` (VARCHAR, UNIQUE), `description` (TEXT) | Logical grouping of commercial products for quick POS filtering. |
| **`products`** | `id` (BIGINT) | `category_id` -> `categories(id)` | `name` (VARCHAR), `barcode` (VARCHAR, INDEX), `cost_price` (DECIMAL 10,2), `selling_price` (DECIMAL 10,2), `stock_quantity` (INTEGER), `low_stock_threshold` (INTEGER), `image_path` (VARCHAR) | Master inventory catalog. Barcode is indexed for sub-millisecond lookups. |
| **`transactions`** | `id` (BIGINT) | `user_id` -> `users(id)` | `invoice_number` (VARCHAR, UNIQUE), `total_amount` (DECIMAL 10,2), `payment_method` (ENUM: 'cash', 'card', 'transfer'), `amount_paid` (DECIMAL 10,2), `change_given` (DECIMAL 10,2), `created_at` (TIMESTAMP, INDEX) | Immutable financial transaction header recording sales events. |
| **`transaction_items`** | `id` (BIGINT) | `transaction_id` -> `transactions(id)` [CASCADE], `product_id` -> `products(id)` | `quantity` (INTEGER), `unit_price` (DECIMAL 10,2), `subtotal` (DECIMAL 10,2) | Line-item detail capturing product pricing at the exact instant of sale. |
| **`stock_adjustments`** | `id` (BIGINT) | `product_id` -> `products(id)`, `user_id` -> `users(id)` | `type` (ENUM: 'addition', 'subtraction'), `quantity` (INTEGER), `reason` (VARCHAR), `previous_stock` (INT), `new_stock` (INT) | Complete audit ledger tracking stock changes outside normal checkout sales. |
| **`activity_logs`** | `id` (BIGINT) | `user_id` -> `users(id)` | `action` (VARCHAR), `module` (VARCHAR), `ip_address` (VARCHAR), `details` (JSON) | System-wide security audit trail tracking logins, updates, and deletes. |

##### 3.3.2.3 Real-Time POS Checkout Engine, Barcode Scanning, and Atomic Transaction Processing
The Point of Sale checkout engine represents the primary operational interface for cashier staff. High retail throughput demands that scanning an item takes less than 100 milliseconds and that system crashes or network drops never leave the database in an inconsistent state.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.32]                                     |
|                                                                       |
|  Figure 3.32: POS Checkout Interface: Live Barcode & Cart State      |
|  Description: High-resolution screenshot of the POS screen showing    |
|  search/scanner input, cart items, price totals, and tender modal.   |
+-----------------------------------------------------------------------+
```

1. **Hardware Barcode Scanner Interception:** Hardware USB barcode scanners emulate rapid keyboard keystrokes terminating with an `Enter` key (`Key Code 13`). In the React frontend, an event listener hooks into the window `keydown` event. A time-delta threshold buffer distinguishes between slow manual human typing (> 50 ms between keystrokes) and high-speed scanner hardware input (< 20 ms between characters). When a barcode terminates, the frontend instantly locates the product in client memory or queries `GET /api/products/search?barcode={code}`, automatically incrementing the cart quantity or appending a new line item with zero cursor clicks.
2. **Reactive Cart State Machine:** The cart state is managed via React functional hooks (`useState`, `useReducer`), maintaining real-time computations of line subtotal, gross total, VAT calculations, and cash change:
   $$\text{Line Subtotal} = \text{Unit Selling Price} \times \text{Quantity}$$
   $$\text{Gross Total} = \sum_{k=1}^{n} \text{Subtotal}_k$$
   $$\text{Change Due} = \text{Amount Paid} - \text{Gross Total}$$
3. **Database Concurrency and Atomic Transactions:** In high-volume environments, two cashiers simultaneously scanning the last unit of an item can induce a race condition, leading to negative inventory balances. In the Laravel backend, checkout processing is wrapped inside an atomic database transaction (`DB::transaction`) utilizing pessimistic row-level locking (`lockForUpdate()`):
```php
public function processCheckout(CheckoutRequest $request) {
    return DB::transaction(function () use ($request) {
        $user = auth()->user();
        $totalAmount = 0;
        
        // 1. Generate unique invoice number
        $invoiceNumber = 'CWG-INV-' . strtoupper(Str::random(8)) . '-' . date('Ymd');
        
        // 2. Create Transaction Header
        $transaction = Transaction::create([
            'invoice_number' => $invoiceNumber,
            'user_id' => $user->id,
            'total_amount' => 0, // updated below
            'payment_method' => $request->payment_method,
            'amount_paid' => $request->amount_paid,
            'change_given' => max(0, $request->amount_paid - $request->total),
        ]);

        // 3. Process Line Items with Pessimistic Locking
        foreach ($request->items as $item) {
            $product = Product::where('id', $item['product_id'])->lockForUpdate()->firstOrFail();
            
            if ($product->stock_quantity < $item['quantity']) {
                throw new InsufficientStockException("Insufficient stock for: {$product->name}");
            }
            
            // Deduct physical inventory
            $product->decrement('stock_quantity', $item['quantity']);
            
            $subtotal = $product->selling_price * $item['quantity'];
            $totalAmount += $subtotal;
            
            TransactionItem::create([
                'transaction_id' => $transaction->id,
                'product_id' => $product->id,
                'quantity' => $item['quantity'],
                'unit_price' => $product->selling_price,
                'subtotal' => $subtotal,
            ]);
        }
        
        $transaction->update(['total_amount' => $totalAmount]);
        return response()->json(['success' => true, 'transaction' => $transaction->load('items.product')]);
    });
}
```
If an item has insufficient stock or an error occurs during processing, the entire transaction is automatically rolled back, guaranteeing absolute data consistency.

##### 3.3.2.4 ESC/POS 80mm Browser-Native Thermal Receipt Generation Subsystem
Upon checkout completion, cashiers must immediately issue printed physical receipts to customers. Traditional server-side PDF generation introduces severe latency (3 to 6 seconds) and requires bloated PDF rendering libraries. 

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.33]                                     |
|                                                                       |
|  Figure 3.33: ESC/POS 80mm Thermal Receipt Layout and Print Pipeline  |
|  Description: Technical layout of the 80mm thermal receipt showing    |
|  store branding, invoice number, tabular items, VAT, and cut command. |
+-----------------------------------------------------------------------+
```

To achieve sub-second receipt printing, I engineered a **browser-native 80mm thermal receipt generation engine**. The subsystem utilizes an isolated, hidden iframe formatted with specialized CSS `@media print` rules specifically tailored to standard 80mm (3.15-inch / 48-character monospace) thermal receipt rolls:
- **Monospace Typography:** Formatted in `font-family: 'Courier New', Courier, monospace` with zero margin and padding, ensuring strict character alignment across item columns.
- **Tabular Formatting:** Allocates fixed column widths: 22 characters for item name, 6 characters for quantity (`x2`), 10 characters for unit price, and 10 characters for subtotal.
- **Receipt Header and Legal Footer:** Dynamically injects CWG Retail Suite branding, physical store address, telephone contact, unique invoice barcode, cashier name, date/time timestamp, and statutory tax identification number (TIN).
- **Automated Guillotine Paper Cut:** Sends standardized ESC/POS hex control codes (`GS V 0` or `1D 56 00`) via raw print drivers to trigger the printer's internal cutter, presenting the severed receipt to the customer instantly.

##### 3.3.2.5 Product Catalogue Management, Dynamic Margin Calculations, and Image Upload Pipelines
Effective inventory management requires continuous catalog maintenance, image association, and real-time profitability auditing.

The product management module delivers:
- **Dynamic Profit Margin Computation:** When administrators input or adjust product cost and selling prices, a reactive UI badge instantly computes and displays the gross profit margin percentage:
  $$\text{Gross Profit Margin (\%)} = \left( \frac{\text{Selling Price} - \text{Cost Price}}{\text{Selling Price}} \right) \times 100\%$$
  The badge utilizes dynamic color-coding: green for healthy margins ($\ge 25\%$), amber for low margins ($10\% - 24.9\%$), and red for critical/negative margins ($< 10\%$), alerting managers against unprofitable pricing.
- **Secure Image Upload and Optimization Pipeline:** High-resolution product images uploaded via the UI undergo backend validation (enforcing MIME types `image/jpeg`, `image/png`, `image/webp` and max file size 2MB). Using PHP GD/Intervention Image, images are resized to a maximum resolution of 800×800 pixels, stripped of EXIF metadata to protect corporate privacy, and stored in protected storage with cryptographic SHA-256 filenames.

##### 3.3.2.6 Inventory Stock Adjustment Engine, Multi-Unit Tracking, and Discrepancy Auditing
Discrepancies inevitably arise between physical warehouse stock and system counts due to transit breakage, shrinkage, expiration, or vendor miscounts. Direct, unverified database editing destroys audit trails.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.34]                                     |
|                                                                       |
|  Figure 3.34: Inventory Adjustment and Discrepancy Audit Subsystem    |
|  Description: Interface showing stock adjustment modal, categorized   |
|  reasons (Breakage, Spoilage, Shrinkage), and immutable audit logs.  |
+-----------------------------------------------------------------------+
```

I engineered a formal **Stock Adjustment Subsystem**:
1. **Categorized Reason Codes:** Adjustments must be designated as an *Addition* or *Subtraction* and tagged with statutory reason codes: `Damaged in Transit / Breakage`, `Spoilage / Expiration`, `Theft / Shrinkage`, `Found Stock / Inventory Reconciliation`, or `Vendor Return`.
2. **Real-Time Projection Badge:** Before submission, the UI displays an interactive comparison badge showing: *Current Stock: 45 units -> Adjustment: -5 units -> Projected Stock: 40 units*.
3. **Immutable Audit Ledger:** Submitting an adjustment writes a permanent record into the `stock_adjustments` table recording the modifying staff ID, timestamp, prior stock, new stock, and justification, while simultaneously committing an entry into the security `activity_logs` table.

##### 3.3.2.7 Multi-Tab Financial Analytics and Business Intelligence Dashboard
Executive decision-makers require real-time visibility into sales velocities, inventory capital valuation, and gross margins without executing slow, ad-hoc database queries.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.35]                                     |
|                                                                       |
|  Figure 3.35: Multi-Tab Financial Analytics and Business Intelligence |
|  Description: Executive reporting dashboard showing 5 dedicated tabs: |
|  Sales Performance, Inventory Valuation, Profit & Loss, and Logs.    |
+-----------------------------------------------------------------------+
```

The system incorporates a high-performance **5-Tab Financial Reporting Suite**:
1. **Tab 1: Sales Performance:** Displays gross revenue, transaction volumes, average basket size, and hourly sales distribution. Cashiers and managers can toggle preset date filters: *Today, Yesterday, Last 7 Days, This Month, or Custom Date Range*.
2. **Tab 2: Inventory Capital Valuation:** Computes real-time working capital tied up in inventory across categories:
   $$\text{Total Cost Valuation} = \sum (\text{Stock Quantity}_i \times \text{Cost Price}_i)$$
   $$\text{Total Retail Valuation} = \sum (\text{Stock Quantity}_i \times \text{Selling Price}_i)$$
   $$\text{Potential Gross Profit} = \text{Total Retail Valuation} - \text{Total Cost Valuation}$$
3. **Tab 3: Profit & Loss (P&L) Ledger:** Calculates net realized gross profit across selected periods by joining transactions with product cost histories, factoring in recorded stock adjustments.
4. **Tab 4: Staff Activity & Audit Logs:** Displays a chronological audit stream tracking all user authentications, product creation, price alterations, and stock adjustments with client IP addresses.
5. **Tab 5: Low-Stock & Reorder Alerts:** Filters all products where `stock_quantity <= low_stock_threshold`, highlighting critically depleted items in red and providing a one-click CSV export to generate purchase reorder requisitions.

To ensure fast response times even with tens of thousands of transaction records, backend Eloquent queries employ eager loading (`Transaction::with('items.product')->whereBetween(...)`), eliminating $N+1$ query bottlenecks and maintaining API response latencies below 80 milliseconds.

##### 3.3.2.8 Role-Based Access Control, Cashier Interface Masking, and Security Protocols
Security and role segregation are paramount in retail operations:
- **Role Segregation (Admin vs Cashier):** Cashiers are restricted strictly to the POS checkout screen and their personal transaction shift summaries. Cashiers cannot view cost prices, profit margins, inventory valuation totals, or user management screens.
- **Cost Price Masking:** In cashier-facing API responses, sensitive fields (`cost_price`, `profit_margin`) are stripped by Laravel API Resources (`CashierProductResource`), preventing competitive intelligence theft or price disputes.
- **Account Self-Registration with Admin Approval:** New staff can register credentials via the portal, but accounts are created in a dormant `pending` status. Only a verified system administrator can approve the account, assign the operational role, and grant system access.

---

#### 3.3.3 Major Project II: LeaveTrack — Enterprise Operations Suite: Leave & Attendance Management System (PRJ-08)

##### 3.3.3.1 Problem Statement, Strategic Objectives, and Business Value Analysis
Across large enterprise organizations such as CWG Plc (employing hundreds of technical, administrative, and executive personnel across multiple geographic locations), managing employee leaves of absence via manual paper application forms, verbal requests, or disconnected email chains creates severe operational vulnerabilities:
1. **Uncoordinated Team Absences:** Department heads lack real-time visibility into overlapping leaves, resulting in simultaneous absences of critical engineering personnel and resulting SLA breaches.
2. **Untracked and Disputed Balances:** Without a centralized, immutable ledger, human resources personnel struggle to accurately compute accrued, taken, and remaining leave days, leading to employee disputes over leave carry-overs and entitlements.
3. **Lack of Compliance and Audit Trails:** Manual leave approvals leave no auditable historical log, complicating statutory compliance audits and annual financial leave liability accounting.

To resolve these enterprise challenges, under the supervision of Bayo (Enterprise Apps Lead) and Mrs. Abimbola, I spearheaded the technical design and end-to-end implementation of **LeaveTrack**—the **Leave & Attendance Management System (PRJ-08 • Track A — Enterprise Operations Suite)**. 

The primary business objectives achieved by LeaveTrack include:
- Enabling all corporate employees to submit leave requests and query their real-time remaining leave balances securely from desktop or mobile devices.
- Routing leave requests through a dynamic, multi-tier approval chain driven by enterprise directory reporting lines.
- Providing department managers with forward-looking team calendar visibility to prevent coverage conflicts.
- Providing Human Resources leadership with centralized policy administration, automated balance accruals, and audit-ready reporting.

##### 3.3.3.2 12-Week Delivery Lifecycle (Phases P1–P7) and Technical Milestones
LeaveTrack was engineered following the standardized 7-phase enterprise delivery roadmap prescribed for CWG IT projects:

| Delivery Phase | Operational Timeline | Technical Milestones and Engineering Deliverables |
|---|---|---|
| **Phase 1: Discovery & Requirements** | Weeks 1 – 2 | Documented CWG leave policies (Annual, Sick, Maternity, Study, Compassionate); drew relational ERD; defined approval rules; wireframed Canvas and Model-Driven screens. |
| **Phase 2: Data Layer Build (Dataverse)** | Weeks 3 – 4 | Implemented Dataverse tables with `Balances` tracking accrued/used/remaining per type; configured RBAC security roles (Employee, Manager, HR Admin); seeded sample hierarchy. |
| **Phase 3: Power Apps Core Build** | Weeks 5 – 7 | Developed responsive Power Apps Canvas portal (Leave Request with balance check, My Requests, My Balances); constructed Power Apps Model-Driven HR Console. |
| **Phase 4: Automation & Identity Integration** | Weeks 8 – 9 | Engineered Power Automate multi-tier approval state machine; integrated Microsoft Entra ID manager attribute; integrated Microsoft Graph API calendar sync. |
| **Phase 5: Power BI Reporting & Analytics** | Week 10 | Developed executive Power BI dashboards tracking departmental leave utilization, 30-day forward absence forecasts, and accrued organizational leave liabilities. |
| **Phase 6: Testing & Quality Assurance** | Week 11 | Executed rigorous UAT testing covering half-day deductions, public holiday boundary exclusions, and manager-on-leave delegation edge cases. |
| **Phase 7: ALM Deployment & Handover** | Week 12 | Packaged system as a Microsoft Power Platform Managed Solution; executed Dev -> Test -> Prod promotion; delivered user manuals and executive demo. |

##### 3.3.3.3 Enterprise Architecture & Technology Stack Alignment on Microsoft Power Platform
The LeaveTrack system was architected natively on the **Microsoft Power Platform** and the Microsoft 365 enterprise ecosystem, ensuring tight security integration, enterprise scalability, and seamless cross-platform operation.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.36]                                     |
|                                                                       |
|  Figure 3.36: LeaveTrack (PRJ-08) Enterprise System Architecture      |
|  Description: Architectural diagram showing Power Apps Canvas,        |
|  Model-Driven HR console, Dataverse, Power Automate, Entra ID, BI.   |
+-----------------------------------------------------------------------+
```

The technology stack mapping aligns as follows:
- **Presentation Layer (Power Apps):**
  - *Canvas Application:* Employee-facing responsive self-service portal designed for rapid mobile and web browser execution.
  - *Model-Driven Application:* Administrative, component-focused back-office console engineered for HR professionals and department directors.
- **Data Persistence Layer (Microsoft Dataverse):** Enterprise-grade, relational low-code data platform providing role-based security, rich data types, declarative business rules, and high-performance transactional capabilities.
- **Workflow & Automation Engine (Power Automate):** Cloud flows orchestrating event-driven approval routing, automated notifications, Entra ID manager discovery, and scheduled balance accrual jobs.
- **Analytics & Business Intelligence (Power BI):** Interactive dashboards ingesting Dataverse entities via DirectQuery to visualize workforce capacity and financial liabilities.
- **Identity & Security Layer (Microsoft Entra ID / Office 365):** Single Sign-On (SSO) authentication, role-based access control (RBAC), and automatic line-manager resolution via Azure Active Directory user attributes.
- **External Integration (Microsoft Graph API):** RESTful calendar API creating calendar events in Outlook to mark approved leaves automatically.

##### 3.3.3.4 Dataverse Relational Data Architecture, Entity Schemas, and Relationships
At the foundation of LeaveTrack is a normalized Dataverse relational data model. Six core tables were engineered with strict relational cardinality:

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.37]                                     |
|                                                                       |
|  Figure 3.37: LeaveTrack Relational Data Model (Dataverse ERD)        |
|  Description: ERD showing Employees, LeaveTypes, LeaveRequests,       |
|  Balances, Approvals, and PublicHolidays with 1:N relationships.     |
+-----------------------------------------------------------------------+
```

| Table Name (Logical Name) | Primary Column | Foreign Key Lookups | Core Attributes & Choice Data Types | Purpose and Relational Integrity Rules |
|---|---|---|---|---|
| **`Employees`** (`cwg_employee`) | `cwg_fullname` (String) | `cwg_manager_id` -> `cwg_employee` (Self-Lookup) | `cwg_email` (String, Unique), `cwg_jobtitle` (String), `cwg_department` (Choice), `cwg_employmentdate` (Date Only), `cwg_systemuser_id` (AAD User) | Master employee directory tracking corporate hierarchy and Entra ID identity mapping. |
| **`LeaveTypes`** (`cwg_leavetype`) | `cwg_typename` (String) | None | `cwg_defaultallowance` (Integer), `cwg_requiresdocumentation` (Yes/No), `cwg_allowshalfday` (Yes/No), `cwg_allowscarryover` (Yes/No), `cwg_maxcarryoverdays` (Integer) | Policy definitions for Annual, Sick, Maternity, Paternity, Study, and Compassionate leave. |
| **`Balances`** (`cwg_balance`) | `cwg_name` (String) | `cwg_employee_id` -> `Employees`, `cwg_leavetype_id` -> `LeaveTypes` | `cwg_leaveyear` (Integer), `cwg_accrueddays` (Decimal), `cwg_useddays` (Decimal), `cwg_pendingdays` (Decimal), `cwg_remainingdays` (Calculated Decimal) | The core balance ledger tracking accrued, taken, and available leave days per employee and type. |
| **`LeaveRequests`** (`cwg_leaverequest`) | `cwg_requestnumber` (Autonumber: `LR-{YYYY}-{0000}`) | `cwg_employee_id` -> `Employees`, `cwg_leavetype_id` -> `LeaveTypes` | `cwg_startdate` (Date Only), `cwg_enddate` (Date Only), `cwg_ishalfday` (Yes/No), `cwg_totalworkingdays` (Decimal), `cwg_reason` (Multiple Lines), `cwg_status` (Choice: Draft, Pending, Approved, Rejected, Cancelled), `cwg_attachment` (File) | Individual leave applications capturing requested dates and workflow approval state. |
| **`Approvals`** (`cwg_approval`) | `cwg_name` (String) | `cwg_leaverequest_id` -> `LeaveRequests`, `cwg_approver_id` -> `Employees` | `cwg_tier` (Choice: Line Manager, Dept Head, HR), `cwg_decision` (Choice: Pending, Approved, Rejected), `cwg_comments` (String), `cwg_decisiondate` (Date & Time) | Immutable audit log capturing each individual decision in the multi-tier approval chain. |
| **`PublicHolidays`** (`cwg_publicholiday`) | `cwg_holidayname` (String) | None | `cwg_holidaydate` (Date Only), `cwg_holidayyear` (Integer) | Calendar table storing statutory Nigerian public holidays to be excluded from leave calculations. |

##### 3.3.3.5 Power Apps Canvas Application Design: Employee Self-Service and Real-Time Balance Validation
The employee self-service portal was implemented as a Power Apps Canvas application optimized for both mobile smartphones and desktop web browsers.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.38]                                     |
|                                                                       |
|  Figure 3.38: LeaveTrack Canvas Application: Leave Request Interface  |
|  Description: Screenshot of the employee request screen showing type  |
|  dropdown, real-time balance badge, calendar pickers, and submit button.|
+-----------------------------------------------------------------------+
```

Key technical features engineered into the Canvas application include:
1. **Dynamic Real-Time Balance Check:** When an employee selects a leave type (e.g., *Annual Leave*), the application executes a Power Fx query against the `Balances` table to look up their current remaining entitlement:
```powerfx
Set(varCurrentBalance, 
    LookUp(cwg_balances, 
        cwg_employee_id.cwg_email = User().Email && 
        cwg_leavetype_id.cwg_leavetypeid = ddlLeaveType.Selected.cwg_leavetypeid &&
        cwg_leaveyear = Year(Today())
    ).cwg_remainingdays
);
```
2. **Business Day Calculation Excluding Weekends and Public Holidays:** Standard date subtraction (`DateDiff(StartDate, EndDate, Days) + 1`) incorrectly charges employees for weekends and statutory public holidays. To solve this, a complex Power Fx formula iterates through the selected date range, evaluates the day of the week, cross-references the `PublicHolidays` table, and computes the exact working days:
```powerfx
Set(varSelectedDays,
    With({
        DateRange: ForAll(
            Sequence(DateDiff(dpStartDate.SelectedDate, dpEndDate.SelectedDate, TimeUnit.Days) + 1),
            DateAdd(dpStartDate.SelectedDate, Value - 1, TimeUnit.Days)
        )
    },
    CountIf(
        DateRange,
        Weekday(Value, StartOfWeek.Monday) <= 5 && 
        !IsBlank(Value) &&
        IsEmpty(Filter(cwg_publicholidays, cwg_holidaydate = Value))
    ))
);
```
3. **Pre-Submission Validation Barrier:** If `varSelectedDays > varCurrentBalance`, the submission button is dynamically disabled, and an amber warning alert informs the employee that the requested duration exceeds their available balance, completely eliminating negative-balance submissions at the source.
4. **My Requests and Team Availability View:** A dedicated screen displays a gallery of the employee's historical requests with color-coded status badges, alongside a team calendar view highlighting upcoming approved absences across their department to foster collaborative coverage planning.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.39]                                     |
|                                                                       |
|  Figure 3.39: LeaveTrack Canvas Application: Requests & Team Calendar |
|  Description: Screenshot showing employee request history gallery,    |
|  status pills (Approved/Pending), and the 30-day team calendar view.  |
+-----------------------------------------------------------------------+
```

##### 3.3.3.6 Power Apps Model-Driven Application: HR Administration Console and Policy Management
While employees utilize the Canvas application for self-service, Human Resources administrators and departmental directors require a data-dense, back-office interface for policy governance, manual balance adjustments, and audit reviews. This was engineered as a **Power Apps Model-Driven Application**.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.40]                                     |
|                                                                       |
|  Figure 3.40: LeaveTrack Model-Driven Application: HR Console        |
|  Description: Model-driven interface illustrating Business Process   |
|  Flow (BPF) stages, balance adjustment grids, and policy editors.    |
+-----------------------------------------------------------------------+
```

The Model-Driven application incorporates:
- **Business Process Flow (BPF):** A structured, guided workflow (`Leave Request Resolution Process`) guiding administrators through four distinct stages: *1. Request Submission -> 2. Line Manager Review -> 3. HR Verification -> 4. Balance Committal and Closure*.
- **Comprehensive Entity Views and Dashboards:** Custom administrative views displaying *All Pending Requests*, *Expiring Leaves*, and *Staff Balances by Department*.
- **Balance Adjustment Sub-grid:** Allows HR administrators to apply statutory adjustments (e.g., granting study leave credits or executing year-end carry-over rollovers) with mandatory audit comments.

##### 3.3.3.7 Power Automate Multi-Tier Hierarchical Approval Workflow State Machine
The operational core of LeaveTrack is an automated event-driven workflow state machine engineered within **Power Automate**.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.41]                                     |
|                                                                       |
|  Figure 3.41: Power Automate Multi-Tier Approval Workflow Diagram    |
|  Description: Detailed cloud flow logic showing Dataverse trigger,    |
|  Entra ID manager discovery, approval actions, and ledger updates.   |
+-----------------------------------------------------------------------+
```

The workflow executes through a structured sequence of actions:
1. **Trigger:** The flow triggers automatically `When a row is added (Dataverse)` in the `LeaveRequests` table with status `Pending`.
2. **Dynamic Manager Discovery via Entra ID:** The flow extracts the applicant's email address and invokes the Office 365 Users connector (`Get manager (V2)`). This queries Microsoft Entra ID to identify the employee's direct line manager dynamically. If no manager is mapped in the directory, the flow automatically escalates the request to the central HR Operations queue.
3. **Multi-Tier Approval State Machine:**
   - **Tier 1 (Line Manager Approval):** The flow issues an interactive Microsoft Teams Adaptive Card and Outlook actionable email containing request details, employee tenure, remaining balance, and *Approve* / *Reject* buttons.
   - **Decision Branching:** If the Line Manager rejects the request with mandatory comments, the flow updates the request status to `Rejected`, notifies the employee via email, and terminates.
   - **Tier 2 (Department Head / HR Clearance):** If approved, and the requested duration exceeds 5 consecutive working days (or involves specialized leave categories like Maternity or Study leave), the flow routes an approval request to the Department Head, followed by final HR clearance.
4. **Atomic Balance Deduction and Ledger Commit:** Upon final approval:
   - The flow increments `cwg_useddays` and decrements `cwg_remainingdays` in the `Balances` table.
   - The request status in `LeaveRequests` transitions to `Approved`.
   - An immutable record is created in the `Approvals` table recording the approver's identity, timestamp, and comments.

##### 3.3.3.8 Entra ID Hierarchical Routing and Microsoft Graph API Automated Calendar Integration
Beyond internal Dataverse updates, modern enterprise workflows require external calendar synchronization to prevent meetings from being scheduled during approved absences.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.42]                                     |
|                                                                       |
|  Figure 3.42: Power Automate Graph API Calendar Integration Flow     |
|  Description: Flow diagram showing HTTP REST action invoking Graph    |
|  API `/v1.0/users/{id}/events` to add approved leave to Outlook.      |
+-----------------------------------------------------------------------+
```

To achieve this, I implemented an automated calendar injection flow:
1. **HTTP Action to Microsoft Graph API:** When a leave request attains the `Approved` state, Power Automate constructs an authenticated HTTP REST payload targeting the Microsoft Graph API endpoint:
   `POST https://graph.microsoft.com/v1.0/users/{employeeEmail}/events`
2. **Event Payload Construction:** The flow injects an all-day calendar event:
```json
{
  "subject": "On Leave: Annual Vacation",
  "body": {
    "contentType": "HTML",
    "content": "Employee is officially on approved annual leave. For urgent matters, contact the department cover staff."
  },
  "start": { "dateTime": "2026-10-12T00:00:00", "timeZone": "W. Central Africa Standard Time" },
  "end": { "dateTime": "2026-10-17T00:00:00", "timeZone": "W. Central Africa Standard Time" },
  "showAs": "oof",
  "isAllDay": true
}
```
Setting `"showAs": "oof"` (Out of Office) automatically updates the employee's Microsoft Teams presence status to *Out of Office*, declines conflicting incoming calendar invitations, and displays an automatic status banner across Outlook.

3. **Scheduled Monthly Balance Accrual Cloud Flow:** To support prorated annual leave entitlements, a recurring cloud flow executes at midnight on the 1st of every month (`Recurrence: Frequency = Month, Interval = 1`). The flow iterates through all active employees, calculates their monthly earned entitlement ($\text{Monthly Accrual} = \frac{\text{Annual Entitlement}}{12}$), increments `cwg_accrueddays`, and logs the balance update.

##### 3.3.3.9 Power BI Enterprise Analytics Dashboard: Departmental Absence Forecasting & Accrual Liability
To provide strategic workforce insights to executive leadership, I designed and deployed an executive analytics dashboard in **Power BI**. The dashboard connects directly to Microsoft Dataverse via DirectQuery, ensuring real-time reporting without manual data exports.

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.43]                                     |
|                                                                       |
|  Figure 3.43: Power BI Leave & Attendance Analytics Dashboard         |
|  Description: Executive dashboard visualizing leave utilization,      |
|  30-day absence forecast heatmap, and accrued leave liability metric. |
+-----------------------------------------------------------------------+
```

The Power BI dashboard delivers three vital analytical views:
1. **Departmental Leave Utilization Analysis:** Stacked bar charts and matrix tables visualizing leave days taken broken down by department, job grade, and leave type, enabling HR to identify departments with excessive unplanned sick leave or underutilized annual leave.
2. **30-Day Forward Team Absence Forecast Heatmap:** A forward-looking calendar matrix highlighting upcoming planned leaves across all operational units over the next 30 days, empowering project managers to identify team coverage bottlenecks before project sprints begin.
3. **Total Accrued Leave Financial Liability Calculation:** In financial accounting, unused accrued annual leave represents an accrued debt liability that the organization must pay out if an employee departs. Using Data Analysis Expressions (DAX), the dashboard computes this financial liability in real time across the enterprise:
```dax
Total Leave Liability = 
SUMX(
    cwg_balances,
    cwg_balances[cwg_remainingdays] * 
    RELATED(cwg_employee[cwg_daily_salary_rate])
)
```

##### 3.3.3.10 Security Governance, UAT Test Matrix, and Application Lifecycle Management (ALM) Handover
Enterprise software deployment demands stringent quality assurance and governance before production release:
- **Role-Based Security Configuration:** Configured three distinct Dataverse security roles:
  - *Employee Role:* Read and Write access to their own `LeaveRequests` and `Balances` (User-level access); Read-only access to `LeaveTypes` and `PublicHolidays`.
  - *Manager Role:* Read and Write access to requests submitted by direct reportees (Business Unit-level access); ability to update `Approvals`.
  - *HR Administrator Role:* Global Organization-level Read, Write, Append, and Delete privileges across all entities, with permissions to execute manual balance corrections.
- **User Acceptance Testing (UAT):** Conducted rigorous UAT test cases with real staff participants across edge-case scenarios:

| Test Case ID | Test Scenario and Input Data | Expected System Behavior | Actual Result & Status |
|---|---|---|---|
| **`TC-LT-01`** | Employee requests 3 days annual leave with 5 days balance available. | Working days correctly calculated as 3; request submitted; status = `Pending`. | Balance verified; manager alerted via Teams. **PASSED** |
| **`TC-LT-02`** | Employee attempts to request 10 days leave with only 4 days remaining. | Submission blocked; amber alert displays; submit button disabled. | Negative request prevented at UI layer. **PASSED** |
| **`TC-LT-03`** | Request spanning Friday to Tuesday including a statutory Public Holiday (Monday). | Weekend days (Sat/Sun) and public holiday (Mon) excluded; duration = 2 days. | Correctly calculated as 2 working days. **PASSED** |
| **`TC-LT-04`** | Line manager is currently on approved leave when reportee submits request. | Flow detects manager's active leave status and delegates approval to Dept Head. | Request escalated; zero SLA bottleneck. **PASSED** |
| **`TC-LT-05`** | Line manager clicks *Approve* in Outlook actionable card. | Status updates to `Approved`; balance deducted; event added to Outlook calendar. | Calendar sync and balance updated in < 5s. **PASSED** |

```
+-----------------------------------------------------------------------+
|  [SPACE RESERVED FOR FIGURE 3.44]                                     |
|                                                                       |
|  Figure 3.44: LeaveTrack Managed Solution ALM Deployment Lifecycle    |
|  Description: Pipeline diagram showing unmanaged development, managed |
|  solution export, and automated deployment from Dev -> Test -> Prod.  |
+-----------------------------------------------------------------------+
```

- **Application Lifecycle Management (ALM) Handover:** LeaveTrack was packaged as a **Power Platform Managed Solution** (`CWG_LeaveTrack_v1.0.0.zip`). Development occurred within an unmanaged sandbox environment (`CWG-Dev`), promoted to a dedicated User Acceptance Testing environment (`CWG-Test`), and finally deployed as a locked, managed solution into the production tenant (`CWG-Prod`). Comprehensive user guides were authored for employees and HR administrators, culminating in a successful live pilot deployment with the IT & BI team.

## CHAPTER FOUR: CONCLUSION, CHALLENGES ENCOUNTERED, AND RECOMMENDATIONS

### 4.1 Summary of Industrial Training Experience and Professional Growth
The six-month Students' Industrial Work Experience Scheme (SIWES) undertaken at Computer Warehouse Group (CWG) Plc from June to December 2026 has been an exceptionally transformative milestone in my academic, professional, and personal development as a computer engineering undergraduate. 

The intentional dual-rotation structure—spanning the **Metering & Energy Engineering Department** and the **IT Proximity Support, Network Infrastructure & Enterprise Software Systems Division**—provided a comprehensive synthesis of hardware engineering, electrical power automation, telecommunications, physical network design, directory systems administration, and modern enterprise software architecture. 

In the Metering rotation, I transitioned from theoretical circuit analysis to precision industrial manufacturing. Demystifying the physical measurement of active electrical energy, mastering electrostatic discharge (ESD) mitigation protocols, torque-controlled mechanical assembly, high-voltage mains energization, optical pulse calibration, STS cryptographic token validation, and legal metrology sealing under the statutory frameworks of the NEMSA Act 2015 instilled in me a deep appreciation for quality assurance and electrical safety.

In the IT Support and Infrastructure rotation, I gained invaluable practical mastery of enterprise networking, structured cabling to ANSI/TIA/EIA-568B specifications, Cisco switching and 802.1Q VLAN trunking, data center facilities management with dual PDU power redundancy and Liebert precision cooling, automated Windows staging via provisioning packages (`.ppkg`), Microsoft Active Directory domain administration, and endpoint security governance with CrowdStrike Falcon and Sophos Central.

Finally, in enterprise software engineering, spearheading the full-stack development of the **CWG Retail Suite** (utilizing Laravel 12, React 19, and 3NF relational modeling) and the **LeaveTrack Enterprise Platform** (utilizing the Microsoft Power Platform, Dataverse, Power Automate, and Power BI under the PRJ-08 specification) honed my competencies in scalable software design, concurrency control, automated business process modeling, and executive data analytics. The internship successfully bridged the gap between academic theory and real-world industrial practice.

### 4.2 Comprehensive Matrix of Technical Challenges Encountered and Engineering Resolutions
Throughout the six months of rigorous industrial training, numerous complex technical anomalies, edge cases, and engineering roadblocks were encountered. Tackling these challenges demanded deep analytical troubleshooting, theoretical reflection, collaborative consultation with industry mentors, and disciplined testing:

| Challenge ID & Domain | Problem Description and Observable Symptoms | Root Cause Analysis | Engineering Resolution and Preventive Measure |
|---|---|---|---|
| **`CH-01` (Metering)** | Smart meters failing optical pulse calibration on high-voltage test racks, exhibiting active energy error margins between $+2.8\%$ and $+4.1\%$ (exceeding Class 1.0 limit of $\pm 1.0\%$). | High-frequency electromagnetic switching noise from adjacent test bench isolation transformers coupling into unshielded analog front-end (AFE) sensing traces on the PCB. | Installed ferrite bead suppressors on the analog voltage divider inputs, shielded the current shunt twisted-pair leads, and recalibrated the ADE7758 digital gain registers via MMS optical commands. |
| **`CH-02` (Metering)** | Smart meters randomly resetting their astronomical calendar back to factory baseline (`1993-01-01`) during prolonged mains power-down. | Lithium backup RTC coin-cell batteries (CR2032) exhibiting micro-vibration dislodgement and contact resistance from oxidized phosphor-bronze spring fingers. | Replaced mechanical spring sockets with gold-plated dual-wipe battery clips, instituted a mandatory $100\,\text{k}\Omega$ active load voltage test ($\ge 3.05\,\text{V}$), and applied dielectric protective coating over contacts. |
| **`CH-03` (Networking)** | Newly crimped Cat6a patch cords failing Gigabit link negotiation on Cisco Catalyst switches, negotiating at only 100 Mbps (Fast Ethernet) or displaying intermittent packet drop. | Cable untwist during RJ-45 termination exceeded the 0.5-inch (12.7 mm) TIA/EIA standard, causing excessive Near-End Crosstalk (NEXT) and Return Loss on Pair 3 (Pins 3 and 6). | Re-terminated cable ends using a ratcheting precision crimper, maintaining pair twists strictly up to 3 mm from the copper contact blades; verified link with a Fluke MicroScanner2 wire mapper. |
| **`CH-04` (Data Center)** | Periodic high-temperature alarms ($> 26^\circ\text{C}$) triggered inside server rack 42U containment zones during mid-day peak compute loads. | Severe air bypass and thermal recirculation occurring because unpopulated 1U and 2U rack slots lacked blanking panels, allowing hot exhaust air to circulate back into the cold aisle intake. | Installed snap-in 1U/2U plastic blanking panels across all open rack spaces, sealed floor cable pass-through grommets, and calibrated the Liebert CRAC unit's variable-speed EC fan curves. |
| **`CH-05` (IT Support)** | Domain-joined corporate laptops occasionally failing user logon with the error: *"The trust relationship between this workstation and the primary domain failed."* | Laptops remained powered off or off the corporate network for over 90 days, causing their computer account password in Active Directory to desynchronize from the local LSA secrets cache. | Restored trust without re-imaging by connecting the laptop to the internal LAN and executing administrative PowerShell commands: `Test-ComputerSecureChannel -Repair -Credential (Get-Credential)`. |
| **`CH-06` (IT Support)** | Windows Configuration Designer `.ppkg` staging failing midway through unattended deployment with generic error code `0x80070005` (Access Denied). | The domain join service account embedded in the provisioning package lacked delegated permissions to create computer objects within the target `OU=Staged_Laptops`. | Re-delegated Active Directory permissions on the target OU using the Delegation of Control Wizard, granting the service account explicit *"Create and Delete Computer Objects"* rights. |
| **`CH-07` (Software: POS)** | Race conditions during peak checkout hours where two cashiers scanning the final unit of a stock item simultaneously caused inventory quantities to drop to negative values (`-1`). | Asynchronous, concurrent HTTP checkout requests executed separate `SELECT` and `UPDATE` SQL queries without pessimistic database locking, creating a race window. | Wrapped checkout processing in atomic Laravel database transactions (`DB::transaction`) and enforced pessimistic row-level locking (`Product::where(...)->lockForUpdate()->first()`). |
| **`CH-08` (Software: POS)** | Cashier staff able to inspect product cost prices and corporate gross profit margins by inspecting browser Developer Tools network responses. | Backend API endpoints utilized raw Eloquent models (`Product::all()`), serializing all database table columns into the public JSON response payload. | Implemented Laravel API Resource transformations (`CashierProductResource`) that dynamically strip `cost_price` and `profit_margin` attributes based on authenticated user roles. |
| **`CH-09` (Software: LeaveTrack)** | Employee leave request calculations incorrectly counted weekends and statutory Nigerian public holidays, deducting excess days from employee annual leave ledgers. | Initial Power Fx formula relied on simple date delta (`DateDiff(StartDate, EndDate, Days) + 1`), which is blind to calendar day types. | Engineered a complex iterative Power Fx formula generating a daily date sequence, filtering out `Weekday() > 5` (weekends) and cross-referencing the `PublicHolidays` Dataverse table. |
| **`CH-10` (Software: LeaveTrack)** | Power Automate approval flows failing with infinite loops or unhandled exceptions when an employee submitted a leave request while their direct line manager was also on leave. | The Entra ID `Get manager (V2)` action successfully resolved the manager's email, but the manager's out-of-office status halted the approval action indefinitely. | Added conditional branching in Power Automate that queries the manager's current leave status in Dataverse; if active, the flow automatically escalates the approval to the Department Head. |

### 4.3 Actionable Recommendations

#### 4.3.1 Recommendations for Host Organization: Computer Warehouse Group (CWG) Plc
Based on my six-month operational observations across departments, I submit the following strategic recommendations to management:
1. **Automate Meter Calibration Data Pipelines:** Currently, optical calibration results and NEMSA compliance logs on the test benches require manual batch ledger exports. Integrating test bench optical controllers directly into CWG's enterprise ERP via automated RESTful APIs would eliminate data entry transcription errors and provide real-time production throughput dashboards.
2. **Implement Cloud-Native Mobile Device Management (MDM):** While local `.ppkg` provisioning packages have revolutionized laptop staging speed, remote employees who rarely visit Lagos headquarters struggle to receive updated security baselines. Adopting Microsoft Intune and Windows Autopilot would allow zero-touch over-the-air provisioning, shipping factory-sealed laptops directly to remote staff with automated cloud configuration.
3. **Formalize Intern Project Mentorship Frameworks:** To sustain the extraordinary success of projects like CWG Retail Suite and LeaveTrack, CWG should institute a structured code-review and mentorship repository where intern project architectures are archived, documented, and promoted to internal production use across subsequent cohorts.

#### 4.3.2 Recommendations for Future SIWES Interns
To maximize the immense educational value of the industrial training scheme, future engineering interns should:
1. **Adopt a Proactive, Inquisitive Learning Stance:** Technical knowledge in industry is rarely spoon-fed. Interns must actively volunteer for challenging assignments, ask probing engineering questions, study hardware manuals, and shadow senior engineers during emergency troubleshooting sessions.
2. **Prioritize Practical Tool Mastery Alongside Theory:** Theoretical knowledge must be reinforced with physical tool competence. Interns should seek hands-on mastery of digital multimeters, oscilloscopes, cable crimpers, punch-down tools, command-line diagnostic utilities, and enterprise IDEs early in their placement.
3. **Maintain Rigorous Daily Engineering Logbooks:** Diligently documenting daily technical activities, wiring diagrams, circuit schematics, CLI commands, and software logic ensures an authentic, comprehensive technical report and solidifies operational learning.
4. **Cultivate Cross-Disciplinary Competencies:** Modern engineering challenges blur the boundaries between hardware, networking, and software. Computer engineering students should embrace both physical electronics (such as smart metering) and modern enterprise software stacks (such as React, Laravel, and cloud low-code platforms).

#### 4.3.3 Recommendations for Academic Institutions: FUTA & Department of Computer Engineering
To ensure that academic curricula remain deeply synchronized with modern industrial realities, I recommend:
1. **Incorporate Modern Enterprise Software Stacks into Lab Curricula:** Undergraduate programming courses should expand beyond basic C and Java syntax to incorporate modern full-stack web architectures (such as React, RESTful APIs, and relational database normalization), cloud low-code platforms (Microsoft Power Platform), and version control systems (Git/GitHub).
2. **Establish Dedicated Physical Networking and Cabling Laboratories:** The Department of Computer Engineering at FUTA should establish a dedicated hands-on networking laboratory equipped with physical patch panels, Cat6a punch-down blocks, enterprise switches, 19-inch racks, and cable certifiers, enabling students to master physical Layer-1 infrastructure before embarking on SIWES.
3. **Enhance Institutional SIWES Supervision Funding and Frequency:** Academic supervisors should be adequately resourced to conduct multiple, comprehensive physical inspection visits to host organizations, fostering closer collaborative research partnerships between university faculty and industrial technology leaders like CWG Plc.

#### 4.3.4 Recommendations for Industrial Training Fund (ITF) & National Universities Commission (NUC)
To optimize the nationwide impact and sustainability of the SIWES scheme, it is recommended that:
1. **Upward Review and Timely Disbursement of Student Allowances:** The current monthly student SIWES allowance has been severely eroded by inflationary economic pressures and transportation costs across commercial hubs like Lagos. The ITF should review student allowances upward to reflect prevailing living realities and ensure prompt electronic disbursement.
2. **Incentivize Private Sector Technology Hosts:** The Federal Government through the ITF should institute corporate tax credits, research grants, and national recognition awards for forward-thinking technology enterprises that invest significant resources into hosting, training, and mentoring engineering undergraduates.
3. **Establish a Centralized Digital SIWES Portal:** The ITF should modernize the administration of SIWES by replacing physical logbooks with a secure, centralized mobile and web portal where students submit weekly activity logs, industry-based supervisors verify entries digitally with biometric or SSO verification, and institutional assessors conduct paperless progress tracking.

---

## REFERENCES

- Adesola, O. G. (2025). *Technical Report on Students' Industrial Work Experience Scheme (SIWES) Undertaken at TotalEnergies Marketing Nigeria Limited*. Department of Computer Engineering, School of Electrical Systems Engineering, Federal University of Technology, Akure (FUTA).
- Analog Devices Inc. (2021). *ADE7758: Polyphase Multifunction Energy Metering IC with Per Phase Information*. Data Sheet Rev. E. Norwood, MA: Analog Devices Inc.
- ANSI/TIA/EIA. (2020). *Commercial Building Telecommunications Cabling Standard (ANSI/TIA-568.2-D)*. Telecommunications Industry Association, Arlington, VA.
- Cisco Systems Inc. (2023). *Cisco Catalyst 9300 Series Switches Architecture and Deployment Guide*. San Jose, CA: Cisco Press.
- David, T. D. (2026). *A Technical Report on the Students' Industrial Work Experience Scheme (SIWES II) Undertaken at CWG Plc, Lagos, Nigeria*. Department of Electrical/Electronics and Computer Engineering, Afe Babalola University, Ado-Ekiti (ABUAD).
- Federal Republic of Nigeria. (1971). *Industrial Training Fund Decree No. 47 of 1971 (as amended 2011)*. Federal Government Press, Lagos, Nigeria.
- Federal Republic of Nigeria. (2015). *Electricity Management Services Agency (NEMSA) Act 2015*. Federal Republic of Nigeria Official Gazette, No. 56, Vol. 102. Abuja, Nigeria.
- International Electrotechnical Commission. (2020). *Electricity Metering Equipment (a.c.) — Particular Requirements — Part 21: Static Meters for Active Energy (Classes 0,5, 1 and 2)*. IEC Standard 62053-21:2020. Geneva: IEC.
- International Electrotechnical Commission. (2021). *Electricity Metering — Data Exchange for Meter Reading, Tariff and Load Control — Part 21: Direct Local Data Exchange*. IEC Standard 62056-21. Geneva: IEC.
- International Electrotechnical Commission. (2022). *Electricity Metering — Payment Systems — Part 41: Standard Transfer Specification (STS) — Application Layer Protocol for One-Way Token Carrier Systems*. IEC Standard 62055-41. Geneva: IEC.
- Microsoft Corporation. (2026). *Microsoft Power Platform Technical Architecture and Dataverse Enterprise Modeling*. Microsoft Learn Documentation, Redmond, WA.
- National Institute of Standards and Technology (NIST). (2014). *Guidelines for Media Sanitization (NIST Special Publication 800-88, Revision 1)*. U.S. Department of Commerce, Washington, D.C.
- Otunba, A. B., & Popoola, J. J. (2023). *Bridging the Industry-Academia Divide in Nigerian Computer Engineering Education*. Nigerian Journal of Technology (NIJOTECH), 42(3), 312-325.
- Tanenbaum, A. S., & Wetherall, D. J. (2021). *Computer Networks (6th Edition)*. Boston, MA: Pearson Education.

---

## APPENDICES

### Appendix A: Metering Diagnostic Keypad Short Codes & Token Decryption Structure
```
+-----------------------------------------------------------------------------------------+
| SMART METER KEYPAD DIAGNOSTIC COMMAND MATRIX                                            |
+---------+------------------------------------+------------------------------------------+
| Code    | Description                        | Engineering Verification Expected        |
+---------+------------------------------------+------------------------------------------+
| #001#   | Cumulative Total Active Energy     | Displays kWh total since manufacture     |
| #002#   | Instantaneous Voltage, Current, Hz | V=230V +/-10%, I=load current, f=50.0Hz  |
| #003#   | Active Power and Power Factor      | kW load and cos phi phase relationship   |
| #004#   | Total Reverse Active Energy        | Identifies reverse energy flow tamper    |
| #005#   | Tamper Status Bitmask Register     | Hex status: Terminal/Top cover/Magnetic  |
| #008#   | Firmware Version and CRC Checksum  | Certified firmware build verification    |
+---------+------------------------------------+------------------------------------------+
```

### Appendix B: Structured Cabling TIA/EIA-568B Pinout Specification
```
+-----------------------------------------------------------------------------------------+
| ANSI/TIA/EIA-568B MODULAR RJ-45 CONNECTOR PINOUT ASSIGNMENTS                             |
+-----+-----------------------+-------------------------+---------------------------------+
| Pin | Wire Color Pattern    | 1000BASE-T Function     | Signal Name                     |
+-----+-----------------------+-------------------------+---------------------------------+
| 1   | White with Orange     | Transmit / Receive A+   | BI_DA+                          |
| 2   | Solid Orange          | Transmit / Receive A-   | BI_DA-                          |
| 3   | White with Green      | Transmit / Receive B+   | BI_DB+                          |
| 4   | Solid Blue            | Transmit / Receive C+   | BI_DC+                          |
| 5   | White with Blue       | Transmit / Receive C-   | BI_DC-                          |
| 6   | Solid Green           | Transmit / Receive B-   | BI_DB-                          |
| 7   | White with Brown      | Transmit / Receive D+   | BI_DD+                          |
| 8   | Solid Brown           | Transmit / Receive D-   | BI_DD-                          |
+-----+-----------------------+-------------------------+---------------------------------+
```

### Appendix C: LeaveTrack (PRJ-08) Dataverse Entity Schema & Attribute Definitions
```
+-----------------------------------------------------------------------------------------+
| LEAVETRACK ENTERPRISE DATAVERSE RELATIONAL ENTITY SCHEMA                                 |
+---------------------+-------------------+---------------------+-------------------------+
| Entity Logical Name | Primary Column    | Key Foreign Lookups | Core Attributes         |
+---------------------+-------------------+---------------------+-------------------------+
| cwg_employee        | cwg_fullname      | cwg_manager_id      | Email, Dept, Title      |
| cwg_leavetype       | cwg_typename      | None                | Allowance, Carryover    |
| cwg_balance         | cwg_name          | Employee, LeaveType | Accrued, Used, Remaining|
| cwg_leaverequest    | cwg_requestnumber | Employee, LeaveType | StartDate, EndDate, Days|
| cwg_approval        | cwg_name          | Request, Approver   | Tier, Decision, Comments|
| cwg_publicholiday   | cwg_holidayname   | None                | HolidayDate, Year       |
+---------------------+-------------------+---------------------+-------------------------+
```

### Appendix D: CWG Retail Suite Relational Schema DDL & API Endpoints
```
+-----------------------------------------------------------------------------------------+
| CWG RETAIL SUITE CORE RESTFUL API ROUTE ARCHITECTURE                                     |
+--------+---------------------------------------+----------------------------------------+
| Method | Endpoint URI                          | Controller Action & Access Policy      |
+--------+---------------------------------------+----------------------------------------+
| POST   | /api/auth/login                       | AuthController@login (Sanctum Token)   |
| GET    | /api/products                         | ProductController@index (RBAC masked)  |
| POST   | /api/products                         | ProductController@store (Admin Only)   |
| POST   | /api/checkout                         | CheckoutController@process (Atomic Tx) |
| GET    | /api/transactions                     | TransactionController@index (Filterable|
| POST   | /api/stock-adjustments                | StockAdjustmentController@store (Audit)|
| GET    | /api/reports/financial-summary        | ReportController@summary (5-Tab BI)    |
| GET    | /api/activity-logs                    | ActivityLogController@index (Audit)    |
+--------+---------------------------------------+----------------------------------------+
```

