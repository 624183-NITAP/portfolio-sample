# Sai Ram Tummuri — Personal Engineering & Quantum Computing Portfolio

[![NIT Andhra Pradesh](https://img.shields.io/badge/NIT%20Andhra%20Pradesh-B.Tech%20ECE%20(2024--2028)-1e3a8a?style=for-the-badge&logo=googlescholar&logoColor=white)](https://www.nitandhra.ac.in)
[![CGPA](https://img.shields.io/badge/CGPA-8.0%2F10-10b981?style=for-the-badge)](public/assets/resume/sai_ram_tummuri_resume.html)
[![National Rank 13](https://img.shields.io/badge/IISc%20%C3%97%20Qiskit-Rank%2013%20Nationwide-f59e0b?style=for-the-badge&logo=ibm&logoColor=white)](https://github.com/624183-NITAP)
[![Top 8% Nationwide](https://img.shields.io/badge/ATF%202025-Top%208%25%20Nationwide-8b5cf6?style=for-the-badge)](https://github.com/624183-NITAP)

> *"Exploring the Intersection of Electronics, Semiconductor Technology & Quantum Computing."*

A premium, interactive personal portfolio website built for **Sai Ram Tummuri** — undergraduate in **Electronics and Communication Engineering (ECE)** at the **National Institute of Technology Andhra Pradesh (NIT AP)**.

---

## ⚡ Core Architectural Foundation: Two Distinct Technical Domains

This website is engineered around two separate technical domains with distinct visual identities, navigation hierarchies, simulators, projects, and credential registries:

```text
/
├── Home & Dual-Portal Launchpad
├── About & Verified Academic Ledger
│
├── DOMAIN 01 — ECE ENGINEERING (Gold & Emerald Cleanroom Theme)
│   ├── Semiconductor Technology & Microfabrication
│   │   └── Interactive 8-Stage Silicon Wafer Cleanroom Simulator
│   ├── Embedded Systems & Industrial IoT Telemetry (CoE-DMA Siemens)
│   ├── Digital Electronics & Computer Architecture
│   │   └── Interactive 8-Bit Breadboard Computer Bus Simulator
│   ├── Signal Processing & Communication Systems
│   │   └── Live Real-Time HTML5 Canvas Oscilloscope & Spectrum Analyzer
│   ├── Verified ECE Projects Gallery (Filterable)
│   └── ECE Technical Skills Matrix
│
├── DOMAIN 02 — QUANTUM COMPUTING (Deep Void Violet & Cyan Hilbert Theme)
│   ├── Quantum Information Science Profile
│   ├── Quantum Technologies & Stack
│   │   └── Interactive 2-Qubit Circuit & 3D Rotating Bloch Sphere Simulator
│   ├── Verified Quantum Certifications Gallery (IBM Quantum, CeNSE IISc, WISER)
│   ├── National Quantum Achievements Timeline (Rank 13 IISc, ATF Stage-2)
│   ├── Quantum Projects & Research Case Studies (QEC, Grover, VQC)
│   └── Long-Term Quantum Research Agenda
│
├── Professional Experience & Campus Leadership Timeline
├── Engineering Collaboration Docket (Dynamic Ticket & AJAX Dispatch)
├── Cleanroom & Lab Logbook (Persistent Peer Blackboard)
└── Official Resume Viewer & Modal System
```

---

## 🔬 Key Interactive Features

### 1. 🎛️ Procedural Web Audio Engine (Pure Web Audio API)
- **Zero MP3 / external audio dependencies** — synthesized on-the-fly using the browser's native `AudioContext`.
- **Mode 1: Cleanroom Laminar Airflow & 60Hz Carrier Hum**: Procedural pink noise passed through a biquad lowpass filter (~160Hz) with subtle 60Hz harmonic hum.
- **Mode 2: Quantum Coherence & Wavefunction Chirp**: Procedurally generated 432Hz harmonic sine wave with slow LFO vibrato.
- **Mode 3: Mute**: Silence with animated sound wave status indicator.
- **Relay Click Chimes**: Synthesized feedback on gate toggles and docket submission.

### 2. 🧮 Interactive 2-Qubit Circuit & 3D Canvas Bloch Sphere
- Direct in-browser simulation of 2-qubit Hilbert space transformations ($|q_0 q_1\rangle$).
- Clickable gates: Hadamard ($H$), Pauli-X (Bit-flip), Pauli-Z (Phase-flip), and $CNOT$ entangling gate.
- Real-time computation of state vector:
  $$|\psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$$
- Live probability distribution bars ($|\alpha|^2, |\beta|^2, |\gamma|^2, |\delta|^2$).
- HTML5 Canvas projection of the 3D rotating Bloch Sphere showing state vector $\vec{r} = (\langle X \rangle, \langle Y \rangle, \langle Z \rangle)$.

### 3. 🧪 8-Stage Semiconductor Cleanroom Fabrication Simulator
- Interactive process step-through:
  1. Wafer Cleaning (RCA-1 / RCA-2)
  2. Thermal Oxidation (Deal-Grove $\text{SiO}_2$ growth)
  3. Photolithography (UV 365nm mask alignment & resist development)
  4. Etching (Wet BOE vs Reactive Ion Etching RIE)
  5. Thin-Film Deposition (PVD Magnetron Sputtering & CVD)
  6. Doping & Ion Implantation
  7. Metallization & Rapid Thermal Annealing (RTA)
  8. Chemical Mechanical Planarization (CMP) & Metrology
- Highlights verified training at **SPARC–NanoX, IIT Hyderabad** and **CeNSE, IISc Bengaluru**.

### 4. 📟 Live Signal Processing Oscilloscope (Canvas 2D)
- Continuous mathematical wave renderer ($A \sin(2\pi f t)$).
- Switchable waveform modes: Sine Wave, Square Wave, AM Modulated Carrier.
- Real-time Gaussian noise injection and low-pass filter toggles with frequency slider ($1.0 - 10.0\text{ Hz}$).

### 5. 💻 Interactive 8-Bit Breadboard Computer Bus Simulator
- Step-through single-pulse clock sequencer modeling discrete 74LS TTL logic ICs.
- Step-by-step visual bus transfers between Program Counter (PC), Memory Address Register (MAR), RAM, Instruction Register (IR), ALU, and Accumulator.
- Interactive glowing 8-bit LED data bus strip.

### 6. 📋 Engineering Collaboration Docket & Dispatch Terminal
- Configurable inquiry parameters: Domain (Semiconductor, IoT, Quantum, Internship), Urgency, and Message.
- Real-time carbon-spec slip preview with dynamic Ticket ID (`SRT-LAB-XXXX`), dynamic timestamp, estimated SLA response window, and sawtooth jagged cut edge.
- Live submission powered by FormSubmit AJAX directly to `tummurisairam@gmail.com`.
- Thermal docket print preview engine (`window.print()`).

### 7. 📌 Cleanroom & Lab Logbook (Persistent Peer Blackboard)
- Wafer-pinned laboratory blackboard with category tags (*Peer Review*, *Research Note*, *Collaboration*, *Welcome*).
- Persistent across browser reloads using `localStorage`.
- Visitors can pin custom notes with randomized rotation angles.

### 8. 🖼️ Client-Side Photo & Certificate Swapper
- Cleanroom badge portrait frame with client-side image uploader.
- Dedicated Certificate Viewer modal with **"Upload My Scan"** tool: Sai Ram can upload scanned certificates or photos directly in the browser; images are cached in `localStorage` and automatically displayed across all certificate cards.

---

## 🎓 Verified Personal Information & Credentials

| Category | Verified Details |
| :--- | :--- |
| **Full Name** | Tummuri Naga Veera Venkata Sairam (Sai Ram Tummuri) |
| **Institution** | National Institute of Technology Andhra Pradesh (NIT AP) |
| **Degree** | B.Tech — Electronics & Communication Engineering (2024–2028) |
| **CGPA** | **8.0 / 10** |
| **Class XII** | Board of Intermediate Education, AP — **94.0%** (Jan 2024) |
| **Class X** | Board of Secondary Education, AP — **87.67%** (2022) |
| **Location** | Ainavilli, Andhra Pradesh, India |
| **Email** | [tummurisairam@gmail.com](mailto:tummurisairam@gmail.com) • [624183@student.nitandhra.ac.in](mailto:624183@student.nitandhra.ac.in) |
| **Phone** | +91 91828 55181 |
| **LinkedIn** | [linkedin.com/in/sairamtummuri](https://www.linkedin.com/in/sairamtummuri/) |
| **GitHub** | [github.com/624183-NITAP](https://github.com/624183-NITAP) |

### 🏆 Verified Achievements & Honors
- **Rank 13 Nationwide**: IISc × Qiskit Fall Fest 2025 (*Eigen Trails / IISc Bengaluru & IBM Quantum*)
- **Top 8% Nationwide**: ATF 2025 Stage-2 Coding Assessment Qualification
- **Qiskit Global Summer School 2025**: IBM Quantum (Quantum Algorithms & Error Mitigation)
- **Foundations of Quantum Error Correction**: IBM Quantum (Stabilizer Codes & Syndrome Measurement)
- **CeNSE Summer School 2026**: Centre for Nano Science and Engineering, IISc Bengaluru
- **WISER Summer School 2026**: Advanced Semiconductor Physics & Research
- **SPARC–NanoX Semiconductor Fabrication Workshop**: IIT Hyderabad, Dept. of EE (Oct–Nov 2026)
- **Internet of Things (IoT) Intern**: CoE-DMA, NIT Warangal & Siemens (June–July 2026)
- **Executive Member**: ECE Association, NIT Andhra Pradesh
- **Joint Secretary**: Brindavanam Club, NIT Andhra Pradesh

---

## 📁 Directory Structure

```text
portfolio-sample/
├── index.html                           # Master unified portfolio application
├── ece.html                             # Dedicated ECE Engineering landing page
├── quantum.html                         # Dedicated Quantum Computing landing page
├── README.md                            # Comprehensive documentation
├── LICENSE                              # Open-source license
├── public/
│   └── assets/
│       ├── profile/
│       │   └── avatar.svg               # Vector monogram & microchip avatar
│       ├── ece/
│       │   ├── semiconductor/
│       │   │   └── wafer-fab.svg        # Silicon wafer & cleanroom schematic
│       │   ├── embedded/
│       │   │   └── iot-internship.svg   # Industrial IoT ESP32/Node-RED diagram
│       │   ├── digital-electronics/
│       │   │   ├── breadboard-computer.svg # 8-bit computer architecture
│       │   │   └── error-detection.svg  # Parity logic gate schematic
│       │   └── signal-processing/
│       │       └── matlab-signal.svg    # Oscilloscope & FFT spectrum graphic
│       ├── quantum/
│       │   └── certificates/
│       │       ├── qiskit-summer-school-2025.svg
│       │       ├── iisc-qiskit-fallfest-2025.svg
│       │       ├── ibm-foundations-qec.svg
│       │       ├── cense-iisc-2026.svg
│       │       ├── wiser-summer-school-2026.svg
│       │       └── techobytes-iith-quantum.svg
│       └── resume/
│           └── sai_ram_tummuri_resume.html # Clean printable resume
```

---

## 🚀 Quick Start & Local Development

No Node.js runtime or build step required. The application runs immediately in any modern web browser.

### 1. Clone the Repository
```bash
git clone https://github.com/624183-NITAP/portfolio-sample.git
cd portfolio-sample
```

### 2. Launch Local Server
You can simply double-click `index.html` to open it in your browser, or start a local Python HTTP server:

```bash
python -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

---

## 🌐 Deploy to GitHub Pages / Vercel / Netlify

### GitHub Pages (Recommended)
1. Push this repository to your GitHub account (`https://github.com/624183-NITAP/portfolio-sample`).
2. Navigate to **Settings &rarr; Pages**.
3. Under **Branch**, select `main` and root folder `/`.
4. Click **Save**. Your site will be live at:
   `https://624183-nitap.github.io/portfolio-sample/`

---

## 🛠️ Tech Stack & Architecture

- **Markup & Semantics**: Semantic HTML5 with ARIA accessibility labels
- **Styling**: Tailwind CSS (CDN) with customized quantum and silicon color palettes
- **Typography**: Fraunces (Headings), Plus Jakarta Sans (Body), Space Mono & JetBrains Mono (Code & Schematics)
- **Vector Graphics**: Custom high-fidelity inline & standalone SVG schematics
- **Interactive Audio**: Web Audio API (procedural synthesis, zero external sound files)
- **Canvases**: HTML5 Canvas 2D (Oscilloscope) and 3D Vector Math (Bloch Sphere)
- **State Management**: Native ES6+ with `localStorage` for notes, portrait, and certificate caching
- **Form Handling**: FormSubmit AJAX API with instant client-side SLA calculation

---

&copy; 2026 **Sai Ram Tummuri**. National Institute of Technology Andhra Pradesh.
