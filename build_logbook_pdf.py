# Comprehensive SIWES Logbook Generator with explicit "WORK DONE DURING THE WEEK" section
# Incorporates all 12 operational weeks (Metering remainder + IT Support with SAP, M365, Network Printers & APs)
import os, subprocess

weeks_data = [
    # METERING REMAINDER WEEKS
    {
        "week_number": "Week 11",
        "period": "17th August 2026 – 21st August 2026",
        "unit": "Energy Automation & Meter Production",
        "section": "Metering Department",
        "badge_class": "badge-metering",
        "badge_text": "Metering & Energy Engineering",
        "job_done": "Mechanical Meter Coupling, Component Seating & Real-Time Clock Battery Integration",
        "work_done_summary": "During this week in the Metering Assembly Station, I carried out mechanical coupling of 240 single-phase smart prepaid electricity meters. The core work done encompassed matching physical outer casing serials with electronic PCB barcodes, installing long-life 3.6V Li-SOCl2 RTC lithium backup batteries to safeguard non-volatile memory during power outages, seating 4G/GPRS IoT cellular communication daughterboards onto the motherboards, inspecting all internal terminal shunts, tightening casing screws using electric torque screwdrivers calibrated to 1.2 Nm to guarantee IP54 ingress protection against dust and moisture, and documenting the batch in the physical Coupling Records Ledger.",
        "days": [
            ("Monday", "17/08/2026", "PCB & Enclosure Matching", "Conducted 100% serial integrity audit matching front cover nameplate serials with electronic PCB barcodes. Inspected internal current transformer terminations."),
            ("Tuesday", "18/08/2026", "Internal Battery & LCD Integration", "Installed long-life 3.6V Li-SOCl2 lithium backup batteries into PCB retention slots for real-time clock (RTC) retention. Mounted front intermediate housing ensuring clear LCD aperture seating."),
            ("Wednesday", "19/08/2026", "GPRS / Cellular Modem Coupling", "Mounted 4G/GPRS communication daughterboards onto meter motherboards. Fastened internal whip antenna leads and validated SIM card tray retention mechanism."),
            ("Thursday", "20/08/2026", "Torque-Calibrated Screw Fastening", "Secured outer transparent casing screws using calibrated electric torque screwdrivers (1.2 Nm) to ensure IP54/IP65 ingress protection against moisture and dust."),
            ("Friday", "21/08/2026", "Coupling Ledger Batch Reconciliation", "Recorded 240 assembled meter units into the physical Coupling Records Ledger; audited serial batch ranges and routed units to the Post-Test station.")
        ],
        "sketch_title": "Meter Coupling & Component Layout Hierarchy",
        "sketch": """[Outer Transparent Cover] --> [Front Nameplate (Serial # Audit)]
   |--> [Sealing Gasket (IP54 Enclosure Ingress Protection)]
   |--> [Metering PCB Motherboard + LCD Display Aperture]
   |--> [3.6V Li-SOCl2 RTC Backup Battery] + [GPRS/4G IoT Daughterboard]
   |--> [Bi-Stable Magnetic Disconnect Latch Relay (100A Rating)]
   |--> [Base Terminal Housing + Micro-switch Cover Tamper Sensor]""",
        "student_comment": "Learned the critical importance of serial number reconciliation between physical casing and PCB firmware identity to avoid utility billing discrepancies in the Meter Management System (MMS)."
    },
    {
        "week_number": "Week 12",
        "period": "24th August 2026 – 28th August 2026",
        "unit": "Quality Assurance & Post-Test Diagnostics",
        "section": "Metering Department",
        "badge_class": "badge-metering",
        "badge_text": "Metering & Energy Engineering",
        "job_done": "ESD Grounding Setup, Mains Energization, Keypad Verification & Factory-to-Deployment Mode Switching",
        "work_done_summary": "During this week in the Post-Test Inspection Station, I carried out functional testing and operational mode parameterization of coupled smart meters. Work done included setting up anti-static Electrostatic Discharge (ESD) wrist straps grounded to the common copper earth bar (< 1 MOhm) to prevent gate oxide puncture on CMOS/MCU chips, energizing meters at 230V AC / 50Hz nominal mains, sequentially testing all tactile keys on the 12-key elastomer keypad with diagnostic shortcodes (#001#, #002#, #003#), interfacing infrared optical read-heads to execute proprietary Meter Management Software (MMS) scripts that transitioned meters from Factory Mode to Deployment Mode, and generating 20-digit STS tokens to test relay disconnector tripping.",
        "days": [
            ("Monday", "24/08/2026", "ESD Workstation Grounding Setup", "Inspected ESD wrist straps, verified < 1.0 MOhm resistance path to common copper earth bar, and initiated static-safe post-test workbench procedures."),
            ("Tuesday", "25/08/2026", "Mains Energization & LCD Boot Diagnostics", "Connected coupled smart meters to 230V AC / 50Hz bench power supply; checked power-on self-test (POST) sequences, LCD segment illumination, and relay click."),
            ("Wednesday", "26/08/2026", "Elastomer Keypad Verification", "Sequentially entered diagnostic test shortcodes (#001# for Total Energy, #002# for Instantaneous Voltage, #003# for Current) to confirm audio-tactile elastomer keypad functionality."),
            ("Thursday", "27/08/2026", "MMS Optical Firmware Parameterization", "Coupled infrared optical probes to meter front read-heads; used Meter Management Software (MMS) to switch operational mode from Factory Mode to locked Deployment Mode."),
            ("Friday", "28/08/2026", "Relay Disconnector Operation & Token Acceptance", "Generated 20-digit STS test recharge credit tokens via test generator; loaded tokens via keypad to confirm token acceptance and internal latch relay disconnector trip/close.")
        ],
        "sketch_title": "Post-Test Bench Setup & MMS Mode State Machine",
        "sketch": """[Copper Earth Bar] <==== ESD Wrist Strap ====> [Test Technician]
                                                   |
[230V AC Mains Test Jig] ===> [Smart Energy Meter] <=== Optical Probe ===> [MMS Test Laptop]
                                       |
    State: FACTORY MODE ---------------> Transition Command -------------> State: DEPLOYMENT MODE
    (Open Calibration Access)        (Cryptographic Authorization)       (Commercial Anti-Tamper Armed)""",
        "student_comment": "Mastered the use of proprietary Meter Management Software (MMS) and optical read-heads. Understood how ESD grounding prevents latent dielectric breakdown in microcontroller gates."
    },
    {
        "week_number": "Week 13",
        "period": "31st August 2026 – 4th September 2026",
        "unit": "Statutory Certification, Sealing & Packaging",
        "section": "Metering to IT Systems Handover",
        "badge_class": "badge-metering",
        "badge_text": "Metering & Energy Engineering",
        "job_done": "NEMSA Regulatory Compliance Audit, Tamper-Evident Wire Sealing & Palletized Warehouse Transfer",
        "work_done_summary": "During this week at the Final Packaging & Regulatory Certification Station, I performed statutory quality compliance checks and anti-tamper sealing on 300 tested meters. Work done included conducting visual surface audits and cleaning grease/fingerprint residue with anti-static solution, affixing internal QC Pass stickers over enclosure joints, applying statutory Nigerian Electricity Management Services Agency (NEMSA) regulatory certification labels pursuant to the NEMSA Act 2015, threading stainless steel sealing wire through enclosure sealing lugs, crimping serialized poly-carbonate NEMSA seals, affixing CWG holographic warranty security seals, boxing units with user manuals, and reconciling packaging ledgers.",
        "days": [
            ("Monday", "31/08/2026", "Finished Cosmetic & Housing Audit", "Inspected 300 tested meters for cosmetic flaws, stripped terminal screws, or missing terminal cover screws. Cleaned surface grease using anti-static fluid."),
            ("Tuesday", "01/09/2026", "QC Pass & Statutory NEMSA Sticker Application", "Affixed internal QC Pass guarantee stickers over enclosure seam joints; applied official statutory NEMSA (Nigerian Electricity Management Services Agency Act 2015) compliance labels."),
            ("Wednesday", "02/09/2026", "Serialized NEMSA Poly-carbonate Wire Sealing", "Threaded high-tensile stainless steel sealing wire through meter terminal lugs and casing lugs; crimped serialized NEMSA tamper-evident seals using calibrated sealing pliers."),
            ("Thursday", "03/09/2026", "CWG Holographic Sealing & User Manual Insertion", "Affixed CWG Plc corporate holographic tamper-evident warranty seals; inserted user operating manuals, STS quick-start guides, and wiring schematics into product cartons."),
            ("Friday", "04/09/2026", "Packaging Ledger Audit & Departmental Handover", "Completed batch ledger documentation reconciling 300 meter serials with NEMSA seal serials; transferred palletized batch to warehouse store. Prepared for rotation to IT Support.")
        ],
        "sketch_title": "NEMSA & CWG Tamper-Evident Multi-Tier Sealing Scheme",
        "sketch": """+-----------------------------------------------------------------+
| [Internal QC Seal] -> Validates manufacturing & optical calibration
| [NEMSA Sticker]   -> Statutory compliance (NEMSA Act 2015 grid mandate)
| [Wire Crimp Seal] -> Poly-carbonate serialized security wire through lugs
| [CWG Hologram]    -> Factory warranty authentication seal over casing seam
+-----------------------------------------------------------------+
          |=========> Protective Box Packaging with Foam Cushioning
          |=========> User Manual + STS Token Card Enclosure
          |=========> Palletized Warehouse Transfer for Utility Dispatch""",
        "student_comment": "Learned the legal and technical necessity of statutory NEMSA verification for grid-connected metering equipment in Nigeria, and how multi-tier physical security seals deter meter tampering."
    },

    # IT SUPPORT WEEKS (FROM SEP 7 ONWARDS — ROTATION TO IT & BI)
    {
        "week_number": "Week 14 (IT Week 1)",
        "period": "7th September 2026 – 11th September 2026",
        "unit": "IT Support & Enterprise Systems",
        "section": "IT & Business Innovation (IT & BI)",
        "badge_class": "badge-itsupport",
        "badge_text": "IT Support & Client Systems",
        "job_done": "IT Department Orientation, Network Printer Setup with User PIN Security, Wireless APs & Environs, SAP GUI & M365 Setup",
        "work_done_summary": "During my first full week in the IT & Business Innovation Department, I received orientation under Mrs. Abimbola and Mr. Moses Mornu and tackled core enterprise client systems. Work done included deploying and configuring departmental Multi-Function Network Printers (MFPs) over TCP/IP, configuring 'User Code Authentication' / Secure PIN passwords for staff on the printer web management console to prevent uncollected print wastage and safeguard sensitive payroll/financial prints, performing physical installation and coverage survey of enterprise Wireless Access Points (APs) taking into account environmental wall/pillar attenuation, installing the SAP GUI desktop client and configuring the SAP Logon Pad (Application Server, SID, System Number 00), and provisioning Microsoft 365 apps including Microsoft Teams, Outlook profile configuration with Exchange Online Autodiscover, and SharePoint Online document library sync.",
        "days": [
            ("Monday", "07/09/2026", "IT Departmental Orientation & Tool Handover", "Reported to IT & BI Department. Received briefing from Mrs. Abimbola and Team Lead Mr. Moses Mornu on corporate IT policy, ticketing SLAs, and proximity desk assignments."),
            ("Tuesday", "08/09/2026", "Network Printer Setup & User PIN Authentication", "Configured enterprise Ricoh/HP Multi-Function Printers (MFPs) on the network (Port 9100 Raw); configured departmental User Code / PIN password authentication tables in the printer web interface and client driver preferences to enforce secure print release."),
            ("Wednesday", "09/09/2026", "Wireless Access Points (APs) & Environs Survey", "Assisted in deploying ceiling-mount enterprise Access Points (APs); surveyed environmental physical obstructions (reinforced concrete walls, glass partitions), verified 802.3at PoE+ power from switchports, and tested 2.4 GHz vs 5 GHz coverage."),
            ("Thursday", "10/09/2026", "SAP GUI Installation & Logon Pad Configuration", "Installed SAP GUI client on 6 finance workstations; configured SAP Logon Pad with server parameters (Application Server IP, System ID 'PRD', Instance '00'); performed connection tests and unlocked locked user accounts using transaction SU01."),
            ("Friday", "11/09/2026", "Microsoft 365 (Teams, Outlook & SharePoint) Staging", "Configured Microsoft 365 collaboration apps for new staff: automated Outlook profile creation via Autodiscover, resolved cached Exchange mode settings, configured Microsoft Teams desktop client, and mapped departmental SharePoint Online document libraries.")
        ],
        "sketch_title": "Enterprise Secure Print Architecture & SAP / M365 Client Topology",
        "sketch": """[User Laptop] ---> Prints Document with User PIN ---> [Network Print Server / MFP Port 9100]
                                                            | (Job Held in Secure Memory)
[Staff Physical Presence] ---> Enters User PIN at Printer Console ---> [Job Releases & Prints]

[Corporate Desktop] ===> [SAP GUI / Logon Pad] ===> [SAP Application Server (PRD / Port 3200)]
                    ===> [M365 Suite] ========> [Exchange Online / Teams / SharePoint Online]""",
        "student_comment": "Gained tremendous practical insight into enterprise user security. Learned how User Code PIN accounting on network MFPs eliminates print waste and confidentiality breaches, and mastered SAP Logon Pad configuration."
    },
    {
        "week_number": "Week 15 (IT Week 2)",
        "period": "14th September 2026 – 18th September 2026",
        "unit": "IT Support & Proximity Operations",
        "section": "Enterprise IT Infrastructure",
        "badge_class": "badge-itsupport",
        "badge_text": "IT Support & Proximity",
        "job_done": "IT Proximity Helpdesk Incident Resolution, Outlook OST Repair, Printer Spooler Troubleshooting & Retail Suite Architecture Kickoff",
        "work_done_summary": "During this week in the IT Support & Proximity Unit, I resolved daily enterprise helpdesk incident tickets and initiated software project planning. Work done included participating in the review of the IT Service Management (ITSM) ticketing queue, resolving 12 corporate desktop support tickets (clearing corrupted local print spooler queues, resolving Outlook OST data file corruption by regenerating OST files in %localappdata%, re-authenticating Microsoft Authenticator MFA prompts, and fixing network drive mappings), participating in the software architecture kickoff meeting for the CWG Retail Suite (Point of Sale & Inventory), drafting the relational Entity-Relationship Diagram (ERD), scaffolding the Laravel 12 backend with Sanctum authentication, and setting up the Vite-powered React frontend repository on GitHub.",
        "days": [
            ("Monday", "14/09/2026", "Proximity Unit Orientation & ITSM Workflow", "Managed enterprise IT service desk incident queue. Handled Severity 3 user tickets covering application crashes, forgotten user PIN codes on printers, and Teams audio device routing."),
            ("Tuesday", "15/09/2026", "Corporate User Incident Handling & Outlook OST Fix", "Resolved 8 Level-1 user tickets: diagnosed Windows print spooler crashes (`spoolsv.exe`), cleared queue in `System32\\spool\\printers`, and repaired corrupted Outlook `.ost` data files."),
            ("Wednesday", "16/09/2026", "CWG Retail Suite Architecture & ERD Review", "Participated in software development kickoff meeting for CWG Retail Suite (POS & Inventory). Reviewed system requirements and drafted relational Entity-Relationship Diagram (ERD)."),
            ("Thursday", "17/09/2026", "Laravel 12 API Scaffold & Sanctum Setup", "Installed Laravel 12 backend framework; configured Laravel Sanctum tokenized authentication and structured database connection parameters for MySQL in .env."),
            ("Friday", "18/09/2026", "Initial React Frontend Scaffolding & Git Tracking", "Scaffolded modern React frontend client using Vite; initialized Git version control repository on GitHub with branch protection rules.")
        ],
        "sketch_title": "ITSM Escalation & Client-Server System Architecture",
        "sketch": """[User Incident / Ticket] ---> [Level-1 Proximity Dispatch] ---> [Level-2 Desktop Support]
                                                                          |
                                  [CWG Retail Suite Web Client (React 19)]
                                                  | (RESTful JSON via HTTP)
                                  [Laravel 12 API Server + Sanctum Token Auth]
                                                  | (Eloquent ORM)
                                  [MySQL Relational Database Engine (Port 3306)]""",
        "student_comment": "Gained clear perspective on enterprise helpdesk operations and corporate incident escalation. Successfully initialized the foundational full-stack decoupled architecture for CWG Retail Suite."
    },
    {
        "week_number": "Week 16 (IT Week 3)",
        "period": "21st September 2026 – 25th September 2026",
        "unit": "IT Support & Software Engineering",
        "section": "Infrastructure & Systems Development",
        "badge_class": "badge-software",
        "badge_text": "Software & IT Systems",
        "job_done": "Enterprise VPN/MFA Support, Database Schema Normalization & Hardware RAM/NVMe Upgrades",
        "work_done_summary": "During this week across IT Proximity and Software Development, I resolved enterprise user identity issues and developed core backend APIs. Work done included configuring secure remote VPN tunnels (Zscaler Private Access and Cisco AnyConnect) for remote executives, enrolling multi-factor authentication (MFA) devices via Microsoft Authenticator, designing and running normalized database migrations in Third Normal Form (3NF) for users, products, sales, and line items, writing tokenized authentication controllers using Bcrypt password hashing, and disassembling two corporate laptops to upgrade failing mechanical HDDs to high-speed 512GB M.2 NVMe SSDs.",
        "days": [
            ("Monday", "21/09/2026", "Remote VPN & MFA Configuration", "Assisted corporate staff with Zscaler / Cisco AnyConnect secure remote VPN configurations and registered Microsoft Authenticator Multi-Factor Authentication (MFA) tokens."),
            ("Tuesday", "22/09/2026", "Database Migrations & Relational Schema (3NF)", "Designed and executed Laravel migrations in 3rd Normal Form: `users`, `products`, `sales`, `sale_items`, and `stock_adjustments` tables with foreign key constraints."),
            ("Wednesday", "23/09/2026", "Sanctum Token Authentication & Breeze Integration", "Implemented user login, password hash verification (Bcrypt), and token issuance endpoints (`POST /api/login`) with role validation attributes."),
            ("Thursday", "24/09/2026", "Hardware RAM/SSD Laptop Diagnostic", "Diagnosed 2 malfunctioning corporate HP laptops: replaced faulty DDR4 SODIMM RAM modules, upgraded failing HDD to 512GB NVMe SSD, and verified BIOS hardware recognition."),
            ("Friday", "25/09/2026", "Product Creation API & Route Testing", "Developed `ProductController.php` with validation rules; created API endpoint for product catalogue management and tested JSON responses via automated test suite.")
        ],
        "sketch_title": "Database Relational Schema (3NF) Topology",
        "sketch": """+---------------+       +------------------+       +-------------------+
|     USERS     |<----->|      SALES       |<----->|    SALE_ITEMS     |
| id, name,     | 1   M | id, user_id,     | 1   M | id, sale_id,      |
| role, status  |       | total, payment   |       | product_id, qty   |
+---------------+       +------------------+       +---------+---------+
                                                             | M
                                                             | 1
                                                   +---------v---------+
                                                   |     PRODUCTS      |
                                                   | id, sku, name,    |
                                                   | sell_price, unit  |
                                                   +-------------------+""",
        "student_comment": "Understood the practical intersection between hardware maintenance (SSD/RAM staging) and software data integrity (database normalization and token security)."
    },
    {
        "week_number": "Week 17 (IT Week 4)",
        "period": "28th September 2026 – 2nd October 2026",
        "unit": "IT Support & Network Infrastructure",
        "section": "Enterprise Networking & Workstation Maintenance",
        "badge_class": "badge-itsupport",
        "badge_text": "IT Support & Networking",
        "job_done": "Structured Cabling, Patch Panel Termination, Wireless AP RF Optimization & Printer User Code Audits",
        "work_done_summary": "During this week in the Network Infrastructure & Facilities Unit, I carried out structured cabling, wireless access point optimization, and printer security audits. Work done included performing an audit of server rack patch panels on the 2nd floor, tracing unmanaged drop cables, terminating 12 new solid-copper Cat6 cables into 24-port patch panels following the TIA/EIA-568B pinout standard, conducting cable continuity and near-end crosstalk tests with an electronic wire tester, auditing network printer user code tables to remove decommissioned staff accounts, and surveying corporate Wi-Fi Access Points (APs) to adjust transmit power and reduce co-channel interference across office wings.",
        "days": [
            ("Monday", "28/09/2026", "Data Center Patch Panel Audit", "Audited server rack patch panels on the 2nd floor data room; re-labeled Cat6a drop cables and documented port assignments to distribution switches."),
            ("Tuesday", "29/09/2026", "Cat6 Structured Cabling & RJ-45 Crimping", "Terminated 12 new Cat6 solid copper patch cables according to the TIA/EIA-568B standard; verified pinout continuity, wire-map, and near-end crosstalk with digital cable tester."),
            ("Wednesday", "30/09/2026", "Departmental Switch Patching & Port Security", "Assisted Senior Network Engineer in patching workstation drops to departmental switch ports; verified link speed negotiation (1 Gbps) and audited printer static IP reservations."),
            ("Thursday", "01/10/2026", "Public Holiday: National Independence Day", "Statutory National Holiday (Nigeria Independence Day). Conducted scheduled remote server health checks and UPS power status monitoring."),
            ("Friday", "02/10/2026", "Wireless Access Point (AP) RF Optimization", "Surveyed corporate Wireless Access Points (APs); adjusted channel allocation (channels 1, 6, 11 on 2.4 GHz) and verified smooth roaming between ground floor and executive suites.")
        ],
        "sketch_title": "TIA/EIA-568B Color Code & Enterprise Switch Patching",
        "sketch": """TIA/EIA-568B Pinout Standard:
Pin 1: White/Orange | Pin 2: Orange      | Pin 3: White/Green | Pin 4: Blue
Pin 5: White/Blue   | Pin 6: Green       | Pin 7: White/Brown | Pin 8: Brown
                       |
[Wall Data Outlet RJ-45] ===Cat6 Drop===> [24-Port Patch Panel] ===Patch Cord===> [Switch Port (PoE Enabled for AP)]""",
        "student_comment": "Mastered precision RJ-45 crimping under TIA/EIA-568B. Gained real-world appreciation for structured cable dressing and cable management in high-density rack enclosures."
    },
    {
        "week_number": "Week 18 (IT Week 5)",
        "period": "5th October 2026 – 9th October 2026",
        "unit": "IT Hardware Support & Maintenance",
        "section": "PC Diagnostics, Component Upgrades & Thermal Servicing",
        "badge_class": "badge-itsupport",
        "badge_text": "Hardware Support & Maintenance",
        "job_done": "Laptop Hardware Diagnostics, RAM & NVMe SSD Upgrades, Heatsink Thermal Servicing & Preventive Maintenance",
        "work_done_summary": "During this week in Hardware Support, I carried out comprehensive physical maintenance, diagnostic testing, and performance upgrades across 8 corporate Dell Latitude laptops. Work done included running Dell ePSA pre-boot hardware diagnostics to evaluate memory and disk health, unseating sluggish mechanical HDDs and installing high-speed 512GB PCIe NVMe M.2 2280 SSDs under UEFI/GPT partitioning to eliminate 100% disk usage bottlenecks, upgrading SO-DIMM RAM from 8GB single-channel to 16GB dual-channel (3200 MHz) on multitasking workstations, disassembling cooling heatsinks to clean dust clogs from copper radiator fins using compressed air, removing degraded thermal compound with 99% isopropyl alcohol, applying fresh non-conductive thermal paste to CPU/GPU dies to lower operating temperatures by 16°C, executing 30-minute system burn-in stress tests, and updating the IT Hardware Asset Maintenance Register.",
        "days": [
            ("Monday", "05/10/2026", "Hardware Diagnostics & Bottleneck Assessment", "Received 5 sluggish staff laptops; executed Dell ePSA Pre-boot System Assessment (F12) to test memory cells, battery health, and SMART drive status; confirmed 100% disk queue bottlenecks caused by 5400 RPM mechanical HDDs."),
            ("Tuesday", "06/10/2026", "High-Speed PCIe NVMe M.2 SSD Installation", "Under ESD wrist-strap grounding, disassembled laptop lower chassis and unseated mechanical SATA HDDs; installed 512GB PCIe Gen3 x4 NVMe M.2 2280 SSDs secured with M2x3mm screws; initialized GPT partitions under UEFI; reduced system boot time from 185s to 14s."),
            ("Wednesday", "07/10/2026", "SO-DIMM RAM Upgrades & Dual-Channel Memory Verification", "Upgraded memory on 4 workstations from 8GB to 16GB; aligned DDR4 SO-DIMM notches with 260-pin socket keys at 45° and pressed down until retaining spring clips locked; verified 3200 MHz bus frequency and 128-bit dual-channel symmetric memory interleaving in BIOS."),
            ("Thursday", "08/10/2026", "Thermal Heatsink Servicing, Dust Clearing & Repasting", "Serviced 3 thermally throttled executive laptops; unfastened copper heat pipe assemblies in cross-pattern order; cleaned dried thermal paste residue with 99% isopropyl alcohol and lint-free wipes; blew out dust from cooling fans; applied fresh thermal compound, lowering CPU temperatures by 16°C."),
            ("Friday", "09/10/2026", "System Stress Testing, Benchmarking & Staff Handover", "Executed 30-minute burn-in stress tests using Windows Memory Diagnostic and Prime95 to verify system stability under heavy computing load; confirmed zero BSOD or thermal trip events; logged hardware serials and upgraded specs in IT Asset Register; handed over machines to staff.")
        ],
        "sketch_title": "Laptop Hardware Upgrade & Thermal Dissipation Architecture",
        "sketch": """[Disassembled Laptop Lower Chassis (ESD Grounded)]
       |
       +--> [SO-DIMM Slot 1: 8GB DDR4] + [SO-DIMM Slot 2: 8GB DDR4] ===> Dual-Channel 16GB (3200 MHz)
       |
       +--> [M.2 2280 PCIe Gen3 x4 Slot] ===> 512GB NVMe SSD Installed (Sequential Read: ~3,500 MB/s)
       |
       +--> [Copper Heatpipe & Fan Blower] ===> Dust Cleaned + Fresh Thermal Paste (-16°C Thermal Relief)
       |
       +--> [Dell ePSA Pre-Boot Diagnostics] ===> Memory, Storage, Thermal & Fan: ALL PASS [100% Healthy]""",
        "student_comment": "Gained practical, hands-on competence in laptop hardware maintenance, component upgrades, and thermal dissipation principles. Learned how simple hardware bottlenecks like mechanical HDDs and single-channel RAM severely degrade workplace productivity, and mastered safe handling of sensitive surface-mount electronics under strict electrostatic discharge (ESD) precautions."
    },
    {
        "week_number": "Week 19 (IT Week 6)",
        "period": "12th October 2026 – 16th October 2026",
        "unit": "Software Engineering & Enterprise Solutions",
        "section": "Core POS Engine & Inventory Architecture",
        "badge_class": "badge-software",
        "badge_text": "Software Engineering",
        "job_done": "Product Inventory Normalization, Stock Adjustments Engine & Role-Based Middleware Security",
        "work_done_summary": "During this week in the Software Engineering team, I built the inventory tracking and access control layers of the CWG Retail Suite. Work done included refactoring ProductController to support Route Model Binding and soft deactivation via `is_active` flags, decoupling stock quantities into an independent `inventories` table, developing `StockAdjustmentController.php` with audit reason tagging (`restock`, `damaged`, `audit`), implementing atomic database transactions to guarantee stock consistency during concurrent operations, authoring PHPUnit automated feature tests, and writing role-based middleware that strictly bars cashiers from viewing cost prices, supplier margins, and administrative settings.",
        "days": [
            ("Monday", "12/10/2026", "Product Deactivation & Route Model Binding", "Refactored `ProductController` to use Laravel Route Model Binding; added soft-delete `is_active` flag to archive products safely without breaking historical sales data."),
            ("Tuesday", "13/10/2026", "Decoupled Inventories Table Migration", "Separated stock quantity into dedicated `inventories` table with 1-to-1 product relationship; migrated existing product inventory data seamlessly."),
            ("Wednesday", "14/10/2026", "Stock Adjustment Controller & Audit Routing", "Implemented `StockAdjustmentController.php` supporting stock audit reasons (`damaged`, `restock`, `inventory_audit`); built transaction logging for stock movements."),
            ("Thursday", "15/10/2026", "Multi-Product Automated Feature Tests", "Authored Pest/PHPUnit automated test suites (`StockAdjustmentTest.php`) verifying inventory increments, boundary conditions, and negative stock prevention."),
            ("Friday", "16/10/2026", "Role Middleware & Cashier Restrictions", "Created custom `EnsureUserHasRole` middleware; ensured cashiers are strictly barred from viewing product cost prices, margin data, or store settings.")
        ],
        "sketch_title": "Inventory Audit Logging & Role Gate State Model",
        "sketch": """Request -> [Role Middleware Check]
             |--> Role == Cashier  ---> Returns: sell_price, sku, name (cost_price HIDDEN)
             |--> Role == Owner/Mgr --> Returns: cost_price, profit_margin, full_audit
                                    |
[Stock Adjustment] ---> [DB Transaction Lock] ---> [Adjust Inventory Qty] ---> [Log Audit Event]""",
        "student_comment": "Learned professional test-driven development (TDD) using automated PHPUnit assertions. Successfully protected sensitive business financial metrics using server-side role middleware."
    },
    {
        "week_number": "Week 20 (IT Week 7)",
        "period": "19th October 2026 – 23rd October 2026",
        "unit": "Software Engineering & Enterprise Solutions",
        "section": "POS Checkout, Thermal Printing & Sales Engine",
        "badge_class": "badge-software",
        "badge_text": "Software Engineering",
        "job_done": "POS Checkout Interface, Barcode SKU Search, 80mm Thermal Receipt Generator & Sales History",
        "work_done_summary": "During this week in Software Development, I focused on client-side checkout and peripheral hardware integration. Work done included engineering the Point of Sale (POS) user interface in React with real-time barcode scanning, search auto-complete, and cart quantity capping, building an atomic cash tender dialog with automated change calculation, styling an 80mm browser-native thermal receipt print layout using CSS `@media print` rules for thermal printers, creating a paginated Sales History table with multi-parameter date range filters, seeding 14 authentic Nigerian retail products, and building an inventory Restock intake station.",
        "days": [
            ("Monday", "19/10/2026", "POS Interface Grid & Real-Time Cart State", "Built React POS component with live category filtering, rapid barcode/SKU search, responsive product grid, and stock-capped cart line item management."),
            ("Tuesday", "20/10/2026", "Atomic Cash Checkout & Change Calculator", "Engineered checkout settlement modal supporting Cash, Card, and Bank Transfer tender options with automated change calculation and transactional concurrency locking."),
            ("Wednesday", "21/10/2026", "Browser-Native 80mm Thermal Receipt Engine", "Implemented browser-native 80mm thermal receipt print stylesheet (`@media print`); styled store header, cashier credentials, line items, VAT, and barcode footer."),
            ("Thursday", "22/10/2026", "Sales History Table & Date Range Filter Presets", "Created sales audit table with filtering by payment method and date presets (Today, 7D, 30D); integrated receipt reprint modal."),
            ("Friday", "23/10/2026", "Database Seeding & Restock Intake Station", "Seeded 14 authentic Nigerian retail products with images; developed Restock & Adjustment station with reason-tagged adjustments and visual stock badges.")
        ],
        "sketch_title": "80mm POS Thermal Receipt Layout Structure",
        "sketch": """+---------------------------------------+
|          CWG PROVISIONS STORE         |
|  12 Ogui Road, Abeokuta, Ogun State   |
|  Tel: +234 803 123 4567 | RC: 123456  |
|---------------------------------------|
| Receipt #: RCP-2026-0042              |
| Date: 2026-10-21 14:32 | Cashier: John|
|---------------------------------------|
| Item              Qty   Price   Total |
| MAMADOR OIL 5L      1   14,500 14,500 |
| DANO MILK 800G      2    4,200  8,400 |
|---------------------------------------|
| TOTAL AMOUNT:               NGN 22,900|
| TENDERED (CASH):            NGN 25,000|
| CHANGE DUE:                  NGN 2,100|
|---------------------------------------|
| Thank you for shopping with CWG Store |
+---------------------------------------+""",
        "student_comment": "Built an authentic, high-speed retail checkout flow with strict inventory synchronization. Designed pixel-perfect 80mm thermal receipt layouts that print without browser margins."
    },
    {
        "week_number": "Week 21 (IT Week 8)",
        "period": "26th October 2026 – 30th October 2026",
        "unit": "Software Engineering & Enterprise Solutions",
        "section": "Financial Reports & High-Performance Optimization",
        "badge_class": "badge-software",
        "badge_text": "Software Engineering",
        "job_done": "Financial Reports Engine, SQL B-Tree Indexing, React-Toastify Popups & Activity Audits",
        "work_done_summary": "During this week in Software Engineering, I executed critical database query optimizations and built enterprise analytical reporting tools. Work done included eliminating sequential N+1 query loops across sales lookups, applying compound B-Tree indexes on `sales(created_at, payment_method)` and projecting specific SQL columns to dramatically accelerate database response, developing the 5-tab Reports module (Financial Sales, Inventory Valuation, Stock Health, Product Velocity, and User Staff Audits) with CSV and PDF export, organizing 30-day adaptive sales charts, integrating React-Toastify notifications, and incorporating real-world metering work instructions into the IT technical report.",
        "days": [
            ("Monday", "26/10/2026", "Database Performance & SQL B-Tree Indexing", "Eliminated sequential N+1 query loops; added compound B-Tree indexes on `sales(created_at, payment_method)` and projected columns at SQL level for instant response times."),
            ("Tuesday", "27/10/2026", "Financial Analysis Layout & 5 Report Subtabs", "Constructed comprehensive Reports module: Financial Sales, Inventory Valuation, Stock Level Deficits, Product Velocity, and User Staff Audits with CSV/PDF export."),
            ("Wednesday", "28/10/2026", "Adaptive 30-Day Sales Chart & SweetAlert2 Modals", "Organized 30-day/90-day daily sales revenue chart with collision-free interval ticks; replaced old browser alerts with modern themed dialogs and React-Toastify notifications."),
            ("Thursday", "29/10/2026", "Staff Activity Audit Log & Admin Layer Isolation", "Organized admin-only pages under dedicated `pages/admin` directory; added staff event timeline capturing sales transactions, logins, and inventory restock operations."),
            ("Friday", "30/10/2026", "IT Technical Report Metering Instructions Update", "Incorporated physical manufacturing work instructions from the metering factory (Coupling, Post-Test ESD Safety, and NEMSA Packaging) into the comprehensive IT Report.")
        ],
        "sketch_title": "SQL Query Optimization: Before vs After B-Tree Indexing",
        "sketch": """BEFORE OPTIMIZATION:
  Query: SELECT * FROM sales WHERE created_at BETWEEN ? AND ?
  Execution: Full Table Scan (ALL) -> 5,000+ rows traversed -> High Server Latency (1,800ms)

AFTER B-TREE INDEXING:
  Schema: INDEX sales_created_payment_idx (created_at, payment_method)
  Execution: Range Index Scan (range) -> Directly fetches matched pointer rows -> Sub-10ms response""",
        "student_comment": "Learned the deep technical mechanics of database query optimization, compound B-tree index execution plans, and architectural modularity in enterprise web development."
    },
    {
        "week_number": "Week 22 (IT Week 9)",
        "period": "2nd November 2026 – 6th November 2026",
        "unit": "IT Support, Proximity & Systems Deployment",
        "section": "Enterprise IT Operations",
        "badge_class": "badge-itsupport",
        "badge_text": "IT Support & Systems Deployment",
        "job_done": "Laptop Hardware Staging, Windows OS Provisioning (.ppkg), Essential Software Deployment & Active Directory Domain Integration",
        "work_done_summary": "During this week in the IT Support & Systems Staging Lab, I conducted complete lifecycle preparation and deployment of enterprise laptop hardware for onboarding staff. Work done included unboxing and inspecting 5 Dell Latitude 5440 laptops, configuring UEFI BIOS settings (Secure Boot, TPM 2.0, battery management), performing clean Windows 11 Enterprise installation over GPT partition tables, executing automated staging via Windows Configuration Designer provisioning packages (.ppkg) that injected Wi-Fi profiles, root certificates, and OEM drivers, deploying the enterprise application stack (Microsoft 365, Zscaler VPN, CrowdStrike Falcon), joining devices to the `cwg.local` Active Directory domain, escrowing BitLocker keys to AD, and completing employee handover.",
        "days": [
            ("Monday", "02/11/2026", "New Laptop Unboxing & Hardware POST Verification", "Unboxed batch of 5 brand new corporate enterprise laptops (Dell Latitude 5440); verified battery health, verified UEFI BIOS firmware settings, secure boot, and TPM 2.0 status."),
            ("Tuesday", "03/11/2026", "Windows 11 Enterprise Clean OS Installation", "Configured UEFI bootable flash drives with official Windows 11 Enterprise media; partitioned NVMe SSD storage (GPT scheme) and completed OS base installation."),
            ("Wednesday", "04/11/2026", "Automated Staging via Provisioning Packages (.ppkg)", "Connected corporate provisioning package (.ppkg) generated with Windows Configuration Designer: automatically injected Wi-Fi profiles, corporate root CA certificates, and OEM drivers."),
            ("Thursday", "05/11/2026", "Essential Enterprise Software & Security Suite Installation", "Installed corporate software stack: Microsoft 365 Enterprise Apps (Word, Excel, Outlook, Teams), Zscaler Private Access VPN, CrowdStrike Falcon EDR antivirus, and Google Chrome Enterprise."),
            ("Friday", "06/11/2026", "Domain Joining, Active Directory Staging & User Profile Handover", "Joined newly staged laptops to `cwg.local` Active Directory domain; moved computer objects into `OU=Workstations,OU=CWG-Staff`; tested domain login, BitLocker drive encryption escrow to AD, and handed over to onboarding employee.")
        ],
        "sketch_title": "Complete Laptop Staging & Active Directory Onboarding Workflow",
        "sketch": """[New Laptop Hardware] ===> [UEFI / Secure Boot / TPM 2.0 Verification]
                                    |
[Clean Windows 11 Enterprise Install (GPT Partition Scheme)]
                                    |
[Custom .ppkg Provisioning] ---> Injects Wi-Fi, Root CA, Asset OEM Drivers
                                    |
[Software Suite Deployment] ---> M365 Apps, Zscaler VPN, CrowdStrike EDR
                                    |
[Active Directory Domain Join] -> cwg.local Domain -> GPO Policy Enforcement
                                    |
[BitLocker 256-bit Encryption] -> Recovery Key Escrowed to Active Directory
                                    |
[Final Quality Check & Physical Handover to Onboarding Corporate Staff]""",
        "student_comment": "Acquired comprehensive practical mastery in end-to-end enterprise laptop staging, automated provisioning with .ppkg packages, essential enterprise security deployment, and Active Directory domain enrollment."
    },
    {
        "week_number": "Week 23 (IT Week 10)",
        "period": "9th November 2026 – 13th November 2026",
        "unit": "Enterprise Solutions & Power Platform",
        "section": "IT & Business Innovation",
        "badge_class": "badge-software",
        "badge_text": "Enterprise Apps & Cloud",
        "job_done": "LeaveTrack (PRJ-08) Kickoff, Dataverse Relational Data Modeling, Canvas App UI & Public Holiday Logic",
        "work_done_summary": "During this week in the Enterprise Applications Cell under Bayo and Mrs. Abimbola, I initiated development on LeaveTrack (PRJ-08 • Track A — Enterprise Operations Suite). Work done included reviewing CWG's HR leave entitlement policies across 6 leave categories (Annual, Sick, Maternity, Paternity, Study, Compassionate), designing the normalized Microsoft Dataverse relational schema across 6 core tables (`cwg_employee`, `cwg_leavetype`, `cwg_balance`, `cwg_leaverequest`, `cwg_approval`, `cwg_publicholiday`), configuring RBAC security roles (Employee, Manager, HR Admin), populating statutory Nigerian public holidays, building the responsive Power Apps Canvas portal with real-time balance lookup formulas, and implementing date calculations that dynamically exclude weekends and public holidays.",
        "days": [
            ("Monday", "09/11/2026", "LeaveTrack (PRJ-08) Architecture & HR Policy Review", "Reviewed project specification PRJ-08 for Leave & Attendance Management System. Mapped corporate HR leave rules, annual accrual formulas, and multi-tier approval policies."),
            ("Tuesday", "10/11/2026", "Microsoft Dataverse Table Architecture & Schemas", "Created Dataverse tables: `Employees`, `LeaveTypes`, `LeaveRequests`, `Balances`, `Approvals`, and `PublicHolidays`; defined autonumbering (`LR-{YYYY}-{0000}`) and choice columns."),
            ("Wednesday", "11/11/2026", "Security Roles & Public Holiday Calendar Seeding", "Configured Dataverse RBAC security roles (User-level access for Employees, BU-level for Managers, Global for HR); seeded statutory 2026 Nigerian public holidays into `PublicHolidays`."),
            ("Thursday", "12/11/2026", "Power Apps Canvas Interface & Dynamic Balance Lookups", "Engineered responsive Power Apps Canvas request screen; implemented Power Fx formulas querying `Balances` to display real-time remaining leave days dynamically upon type selection."),
            ("Friday", "13/11/2026", "Working Days Logic & Pre-Submission Validation Barrier", "Authored Power Fx iterative sequence formula calculating working days strictly excluding weekends and public holidays; added pre-submission validation preventing requests exceeding available balance.")
        ],
        "sketch_title": "LeaveTrack Dataverse Relational Schema (PRJ-08 Data Layer)",
        "sketch": """[cwg_employee] 1 ----- M [cwg_balance] M ----- 1 [cwg_leavetype]
       |                      |
       | 1                    | (tracks: accrued, used, remaining)
       v M                    v
[cwg_leaverequest] 1 --- M [cwg_approval]
       |                   (Tier: Manager -> Dept Head -> HR)
       v
[cwg_publicholiday] -> Excluded from duration calculation""",
        "student_comment": "Learned low-code enterprise data modeling on Microsoft Dataverse. Mastered complex Power Fx iterative date arithmetic to exclude statutory public holidays from employee leave balances."
    },
    {
        "week_number": "Week 24 (IT Week 11)",
        "period": "16th November 2026 – 20th November 2026",
        "unit": "Cloud Automation, Identity & Analytics",
        "section": "IT & Business Innovation",
        "badge_class": "badge-software",
        "badge_text": "Cloud Automation & BI",
        "job_done": "Power Automate Hierarchical Approvals, Entra ID Manager Routing, Graph API Calendar Sync & Power BI Analytics",
        "work_done_summary": "During this week culminating on 19th–20th November 2026, I completed the backend workflow automation, identity integration, calendar synchronization, and executive business intelligence dashboards for LeaveTrack (PRJ-08). Work done included building a Power Automate cloud flow triggered by Dataverse row additions, integrating Microsoft Entra ID via the Office 365 Users connector (`Get manager (V2)`) to dynamically discover applicant line managers, designing interactive Teams Adaptive Cards for one-click manager approvals, invoking Microsoft Graph API (`POST /v1.0/users/{id}/events`) to automatically write approved leaves into Outlook calendars with out-of-office status, constructing an executive Power BI analytics dashboard computing departmental absence trends and total organization-wide accrued leave liability, and executing formal User Acceptance Testing (UAT).",
        "days": [
            ("Monday", "16/11/2026", "Power Automate Cloud Flow & Entra ID Manager Lookup", "Created automated cloud flow triggered on `LeaveRequests` creation; used Office 365 Users connector to resolve applicant's direct manager dynamically from Microsoft Entra ID directory attributes."),
            ("Tuesday", "17/11/2026", "Multi-Tier Approval State Machine & Teams Adaptive Cards", "Engineered interactive Microsoft Teams Adaptive Card approval prompts with comments; built conditional escalation branching for leaves > 5 days routing to Department Head and HR."),
            ("Wednesday", "18/11/2026", "Microsoft Graph API Automated Outlook Calendar Sync", "Configured HTTP action targeting Graph API (`/v1.0/users/{id}/events`) to inject approved leave blocks into employee Outlook calendar (`showAs: 'oof'`); built monthly balance accrual cloud flow."),
            ("Thursday", "19/11/2026", "Power BI Executive Dashboard & Organization Liability", "Engineered Power BI dashboard connecting to Dataverse via DirectQuery; built DAX measures computing total accrued leave financial liability and 30-day forward team absence heatmap."),
            ("Friday", "20/11/2026", "User Acceptance Testing (UAT), ALM Packaging & Documentation", "Executed 5 UAT test scenarios (half-days, holiday boundaries, manager-on-leave delegates); packaged system as Managed Solution (`CWG_LeaveTrack_v1.0.0.zip`); finalized technical documentation.")
        ],
        "sketch_title": "LeaveTrack Multi-Tier Approval & Graph API Integration Architecture",
        "sketch": """[Leave Request Submitted] ---> [Dataverse Trigger]
                                      |
[Entra ID Manager Lookup] ---> [Teams Adaptive Card Prompt]
                                      |
                      +---------------+---------------+
                      | (Approved)                    | (Rejected)
                      v                               v
[Balance Ledger Deduction]            [Notify Employee via Email]
                      |
[Microsoft Graph API Call] ---> Creates Outlook Event (showAs: 'oof')
                      |
[Power BI Dashboard] ---------> Live Org Liability & Absence Heatmap""",
        "student_comment": "Successfully delivered PRJ-08 LeaveTrack enterprise platform. Mastered enterprise cloud orchestration with Power Automate, Microsoft Graph API calendar integration, and Power BI DAX financial modeling."
    }
]

def generate_html(weeks):
    pages_html = []
    
    for w in weeks:
        rows_html = []
        for day, date, nature, details in w["days"]:
            rows_html.append(f"""
            <tr>
              <td class="col-day">{day}<small>{date}</small></td>
              <td class="col-nature">{nature}</td>
              <td class="col-details">{details}</td>
            </tr>
            """)
        
        table_rows = "".join(rows_html)
        
        page = f"""
        <div class="logbook-page">
          <div class="doc-header">
            <div>
              <div class="doc-title-main">COMPUTER WAREHOUSE GROUP (CWG) PLC</div>
              <div class="doc-title-sub">STUDENT INDUSTRIAL WORK EXPERIENCE SCHEME (SIWES) — TECHNICAL LOGBOOK</div>
            </div>
            <div class="doc-header-meta">
              <strong>TRAINING RECORD</strong><br>
              CWG Infrastructure & Engineering
            </div>
          </div>

          <div class="info-bar">
            <div class="info-item">
              <span>Section / Department</span>
              <strong>{w["section"]}</strong>
            </div>
            <div class="info-item">
              <span>Operational Unit</span>
              <strong><span class="section-badge {w["badge_class"]}">{w["badge_text"]}</span></strong>
            </div>
            <div class="info-item">
              <span>Training Period</span>
              <strong>{w["period"]}</strong>
            </div>
            <div class="info-item" style="text-align: right;">
              <span>Logbook Week</span>
              <strong style="color: #1e3a8a; font-size: 13px;">{w["week_number"]}</strong>
            </div>
          </div>

          <div class="weekly-project-box">
            <div class="box-tag">WORK DONE DURING THE WEEK:</div>
            <div class="box-title">{w["job_done"]}</div>
            <div class="box-desc">{w["work_done_summary"]}</div>
          </div>

          <table class="daily-table">
            <thead>
              <tr>
                <th style="width: 13%;">Day / Date</th>
                <th style="width: 25%;">Nature of Work Done</th>
                <th style="width: 62%;">Detailed Technical Activities & Engineering Description</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>

          <div class="bottom-section">
            <div class="sketch-panel">
              <div class="panel-header">WEEKLY TECHNICAL ILLUSTRATION / CIRCUIT / LOGIC DIAGRAM: {w["sketch_title"]}</div>
              <pre class="ascii-sketch">{w["sketch"]}</pre>
            </div>
            
            <div class="feedback-panel">
              <div class="feedback-box">
                <div class="panel-header">STUDENT'S WEEKLY REFLECTION & TECHNICAL COMPETENCY:</div>
                <div class="student-comment-text">"{w["student_comment"]}"</div>
              </div>
              <div class="feedback-box">
                <div class="panel-header">INDUSTRY-BASED SUPERVISOR'S APPRAISAL & SIGNATURE:</div>
                <div class="signature-line"></div>
                <div class="signature-caption">Supervisor Signature, Stamp & Date</div>
              </div>
            </div>
          </div>
        </div>
        """
        pages_html.append(page)
    
    all_pages = "\n".join(pages_html)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CWG Plc - SIWES Technical Logbook (Weeks 11 to 24 (Up to Nov 19/20))</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 8mm 10mm 8mm 10mm;
  }}
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    margin: 0;
    padding: 0;
    background: #f1f5f9;
    font-size: 9.5px;
  }}
  .logbook-page {{
    background: #ffffff;
    width: 100%;
    max-width: 210mm;
    min-height: 280mm;
    margin: 0 auto 12mm auto;
    padding: 10mm 12mm;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  @media print {{
    body {{
      background: #ffffff;
    }}
    .logbook-page {{
      box-shadow: none;
      margin: 0;
      padding: 4mm 6mm;
      width: 100%;
      height: 100%;
      page-break-after: always;
    }}
  }}

  /* Header */
  .doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 2.5px solid #1e3a8a;
    padding-bottom: 5px;
    margin-bottom: 6px;
  }}
  .doc-title-main {{
    font-size: 15px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: 0.5px;
  }}
  .doc-title-sub {{
    font-size: 9px;
    font-weight: 700;
    color: #2563eb;
    margin-top: 1px;
    letter-spacing: 0.3px;
  }}
  .doc-header-meta {{
    text-align: right;
    font-size: 8px;
    color: #64748b;
    line-height: 1.25;
  }}

  /* Info Bar */
  .info-bar {{
    display: grid;
    grid-template-columns: 1.2fr 1.3fr 1.3fr 1fr;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 5px 8px;
    margin-bottom: 7px;
    gap: 6px;
  }}
  .info-item span {{
    display: block;
    font-size: 7.5px;
    text-transform: uppercase;
    color: #64748b;
    font-weight: 700;
  }}
  .info-item strong {{
    font-size: 9.5px;
    color: #0f172a;
  }}
  .section-badge {{
    display: inline-block;
    padding: 1.5px 5px;
    border-radius: 3px;
    font-size: 8.5px;
    font-weight: 700;
  }}
  .badge-metering {{
    background: #dbeafe;
    color: #1e40af;
    border: 1px solid #bfdbfe;
  }}
  .badge-itsupport {{
    background: #e0e7ff;
    color: #3730a3;
    border: 1px solid #c7d2fe;
  }}
  .badge-software {{
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
  }}

  /* Weekly Project Box */
  .weekly-project-box {{
    background: #f0fdf4;
    border-left: 3.5px solid #16a34a;
    border-top: 1px solid #bbf7d0;
    border-right: 1px solid #bbf7d0;
    border-bottom: 1px solid #bbf7d0;
    border-radius: 0 4px 4px 0;
    padding: 5px 8px;
    margin-bottom: 7px;
  }}
  .box-tag {{
    font-size: 7.5px;
    font-weight: 800;
    color: #15803d;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 1px;
  }}
  .box-title {{
    font-size: 10px;
    font-weight: 700;
    color: #14532d;
    margin-bottom: 2px;
  }}
  .box-desc {{
    font-size: 8.5px;
    color: #166534;
    line-height: 1.3;
  }}

  /* Daily Table */
  .daily-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 7px;
    font-size: 8.5px;
  }}
  .daily-table th {{
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 4px 6px;
    border: 1px solid #1e3a8a;
    font-size: 8px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  .daily-table td {{
    padding: 4.5px 6px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
    line-height: 1.3;
  }}
  .daily-table tr:nth-child(even) {{
    background: #f8fafc;
  }}
  .col-day {{
    font-weight: 700;
    color: #0f172a;
    white-space: nowrap;
  }}
  .col-day small {{
    display: block;
    font-weight: normal;
    color: #64748b;
    font-size: 7.5px;
  }}
  .col-nature {{
    font-weight: 600;
    color: #1e40af;
  }}
  .col-details {{
    color: #334155;
  }}

  /* Bottom Section: Sketch & Feedback */
  .bottom-section {{
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 8px;
    margin-top: 2px;
  }}
  .sketch-panel, .feedback-box {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 5px 7px;
  }}
  .panel-header {{
    font-size: 7.5px;
    font-weight: 800;
    text-transform: uppercase;
    color: #1e3a8a;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2px;
    margin-bottom: 3px;
    letter-spacing: 0.3px;
  }}
  .ascii-sketch {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7.5px;
    line-height: 1.25;
    color: #0f172a;
    background: #f8fafc;
    border: 1px dashed #cbd5e1;
    border-radius: 3px;
    padding: 4px;
    margin: 0;
    white-space: pre;
    overflow-x: auto;
  }}
  .feedback-panel {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 6px;
  }}
  .feedback-box {{
    flex: 1;
  }}
  .feedback-box span {{
    display: block;
    font-size: 7px;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 1px;
  }}
  .student-comment-text {{
    color: #1e293b;
    font-style: italic;
    line-height: 1.25;
  }}
  .signature-line {{
    margin-top: 8px;
    border-bottom: 1px dotted #94a3b8;
    height: 8px;
  }}
  .signature-caption {{
    font-size: 7.5px;
    color: #64748b;
    text-align: center;
    margin-top: 1px;
  }}
</style>
</head>
<body>
{all_pages}
</body>
</html>
"""
    return full_html

html_output = generate_html(weeks_data)
with open('SIWES_TECHNICAL_LOGBOOK.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Generated SIWES_TECHNICAL_LOGBOOK.html with explicit WORK DONE DURING THE WEEK successfully.")

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_abs = os.path.abspath('SIWES_TECHNICAL_LOGBOOK.html')
pdf_abs = os.path.abspath('SIWES_TECHNICAL_LOGBOOK_REPORT.pdf')

cmd = [
    edge_path,
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_abs}',
    html_abs
]

res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Edge conversion exit code: {res.returncode}")
if os.path.exists(pdf_abs):
    print(f"SUCCESS! Updated PDF at {pdf_abs} with size {os.path.getsize(pdf_abs)} bytes.")
else:
    print("PDF generation failed.")
