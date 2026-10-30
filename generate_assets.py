import os

def create_svg(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {path}")

# 1. Avatar SVG
avatar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="avatarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4" />
      <stop offset="50%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#f59e0b" />
    </linearGradient>
    <pattern id="microgrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(139, 92, 246, 0.12)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="url(#avatarGrad)" rx="24"/>
  <rect width="400" height="400" fill="url(#microgrid)" rx="24"/>
  
  <!-- Silicon Wafer / Quantum Orbit Rings -->
  <circle cx="200" cy="180" r="140" fill="none" stroke="rgba(6, 182, 212, 0.2)" stroke-dasharray="6 6"/>
  <circle cx="200" cy="180" r="115" fill="none" stroke="rgba(139, 92, 246, 0.3)" stroke-width="1.5"/>
  <circle cx="200" cy="180" r="90" fill="rgba(15, 23, 42, 0.8)" stroke="url(#accentGrad)" stroke-width="2.5"/>
  
  <!-- Quantum Orbit Ellipses -->
  <ellipse cx="200" cy="180" rx="130" ry="45" fill="none" stroke="rgba(6, 182, 212, 0.4)" stroke-width="1.5" transform="rotate(-25 200 180)"/>
  <ellipse cx="200" cy="180" rx="130" ry="45" fill="none" stroke="rgba(245, 158, 11, 0.4)" stroke-width="1.5" transform="rotate(35 200 180)"/>
  
  <!-- Central Microchip Icon -->
  <rect x="160" y="140" width="80" height="80" rx="8" fill="#111827" stroke="#8b5cf6" stroke-width="2"/>
  <rect x="175" y="155" width="50" height="50" rx="4" fill="#1e1b4b" stroke="#06b6d4" stroke-width="1.5"/>
  
  <!-- Chip Pins -->
  <path d="M170 140 V130 M185 140 V130 M200 140 V130 M215 140 V130 M230 140 V130" stroke="#f59e0b" stroke-width="2"/>
  <path d="M170 220 V230 M185 220 V230 M200 220 V230 M215 220 V230 M230 220 V230" stroke="#f59e0b" stroke-width="2"/>
  <path d="M160 150 H150 M160 165 H150 M160 180 H150 M160 195 H150 M160 210 H150" stroke="#06b6d4" stroke-width="2"/>
  <path d="M240 150 H250 M240 165 H250 M240 180 H250 M240 195 H250 M240 210 H250" stroke="#06b6d4" stroke-width="2"/>
  
  <!-- Monogram Initials SRT -->
  <text x="200" y="186" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="22" fill="#ffffff" text-anchor="middle" letter-spacing="1">SRT</text>
  
  <!-- Bottom Identification Plate -->
  <rect x="40" y="325" width="320" height="50" rx="10" fill="rgba(17, 24, 39, 0.9)" stroke="rgba(255, 255, 255, 0.1)"/>
  <text x="200" y="348" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" fill="#ffffff" text-anchor="middle">SAI RAM TUMMURI</text>
  <text x="200" y="364" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="10" fill="#06b6d4" text-anchor="middle" letter-spacing="1">ECE @ NIT AP • SEMICONDUCTOR &amp; QUANTUM</text>
</svg>"""

# 2. Qiskit Global Summer School 2025 Certificate SVG
qiskit_cert_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a051b" />
      <stop offset="50%" stop-color="#140b2e" />
      <stop offset="100%" stop-color="#050212" />
    </linearGradient>
    <linearGradient id="goldBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" />
      <stop offset="50%" stop-color="#06b6d4" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
  </defs>
  <rect width="800" height="560" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="760" height="520" rx="12" fill="none" stroke="url(#goldBorder)" stroke-width="2"/>
  <rect x="28" y="28" width="744" height="504" rx="8" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  
  <!-- Quantum Circuit Watermark Background -->
  <g stroke="rgba(139, 92, 246, 0.1)" stroke-width="1">
    <line x1="80" y1="120" x2="720" y2="120"/>
    <line x1="80" y1="160" x2="720" y2="160"/>
    <line x1="80" y1="200" x2="720" y2="200"/>
    <line x1="80" y1="240" x2="720" y2="240"/>
  </g>
  
  <!-- Issuer Header -->
  <g transform="translate(60, 60)">
    <rect x="0" y="0" width="38" height="38" rx="8" fill="#6929c4"/>
    <text x="19" y="25" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="18" fill="#ffffff" text-anchor="middle">IBM</text>
    <text x="50" y="25" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="20" fill="#ffffff">IBM Quantum</text>
    <text x="210" y="25" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="14" fill="#a78bfa">| Qiskit Global Community</text>
  </g>
  <rect x="630" y="55" width="110" height="28" rx="14" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4"/>
  <text x="685" y="74" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#06b6d4" text-anchor="middle">VERIFIED 2025</text>
  
  <!-- Certificate Title -->
  <text x="400" y="165" font-family="'Fraunces', serif" font-weight="700" font-size="28" fill="#f8fafc" text-anchor="middle">Certificate of Completion</text>
  <text x="400" y="195" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="14" fill="#94a3b8" text-anchor="middle">This is proudly presented to</text>
  
  <!-- Recipient -->
  <text x="400" y="248" font-family="'Fraunces', serif" font-weight="700" font-size="34" fill="#a78bfa" text-anchor="middle">Sai Ram Tummuri</text>
  <line x1="240" y1="262" x2="560" y2="262" stroke="#6929c4" stroke-width="2"/>
  
  <!-- Description -->
  <text x="400" y="295" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="13" fill="#cbd5e1" text-anchor="middle">For successfully completing the rigorous two-week intensive training program in</text>
  <text x="400" y="325" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="18" fill="#38bdf8" text-anchor="middle">Qiskit Global Summer School 2025</text>
  <text x="400" y="350" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="12" fill="#94a3b8" text-anchor="middle">Quantum Algorithms • Quantum Error Mitigation • Quantum Circuit Simulation • PennyLane &amp; Qiskit SDK</text>
  
  <!-- Security Seal & Signatures -->
  <g transform="translate(400, 435)">
    <circle cx="0" cy="0" r="38" fill="rgba(105, 41, 196, 0.3)" stroke="#a78bfa" stroke-width="2" stroke-dasharray="4 2"/>
    <circle cx="0" cy="0" r="30" fill="#140b2e" stroke="#06b6d4" stroke-width="1.5"/>
    <text x="0" y="-4" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="8" fill="#a78bfa" text-anchor="middle">IBM QUANTUM</text>
    <text x="0" y="8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="10" fill="#38bdf8" text-anchor="middle">OFFICIAL</text>
    <text x="0" y="18" font-family="'Plus Jakarta Sans', sans-serif" font-weight="600" font-size="7" fill="#ffffff" text-anchor="middle">SEAL</text>
  </g>
  
  <!-- Footer signatories -->
  <g transform="translate(140, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">IBM Quantum Team</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">Global Education Lead</text>
  </g>
  
  <g transform="translate(500, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">National Institute of Tech</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">Andhra Pradesh, India</text>
  </g>
  
  <text x="400" y="515" font-family="'Space Mono', monospace" font-size="9" fill="#475569" text-anchor="middle">CREDENTIAL ID: QGSS25-SRT-NITAP-VERIFIED • ISSUED JULY 2025</text>
</svg>"""

# 3. IISc x Qiskit Fall Fest 2025 (Rank 13)
iisc_cert_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" width="100%" height="100%">
  <defs>
    <linearGradient id="iiscBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b132b" />
      <stop offset="50%" stop-color="#1c2541" />
      <stop offset="100%" stop-color="#080c1a" />
    </linearGradient>
  </defs>
  <rect width="800" height="560" fill="url(#iiscBg)" rx="16"/>
  <rect x="20" y="20" width="760" height="520" rx="12" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <rect x="28" y="28" width="744" height="504" rx="8" fill="none" stroke="rgba(245, 158, 11, 0.2)" stroke-width="1"/>
  
  <!-- Header -->
  <g transform="translate(60, 55)">
    <circle cx="20" cy="20" r="20" fill="#d97706"/>
    <text x="20" y="26" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="14" fill="#ffffff" text-anchor="middle">IISc</text>
    <text x="50" y="20" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="16" fill="#ffffff">Indian Institute of Science, Bengaluru</text>
    <text x="50" y="36" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="12" fill="#fbbf24">Eigen Trails × Qiskit Fall Fest 2025</text>
  </g>
  <rect x="610" y="55" width="130" height="30" rx="15" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b"/>
  <text x="675" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="11" fill="#fcd34d" text-anchor="middle">🏆 RANK 13</text>
  
  <text x="400" y="165" font-family="'Fraunces', serif" font-weight="700" font-size="28" fill="#ffffff" text-anchor="middle">Certificate of Merit &amp; Excellence</text>
  <text x="400" y="195" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="14" fill="#94a3b8" text-anchor="middle">Conferred upon</text>
  
  <text x="400" y="248" font-family="'Fraunces', serif" font-weight="700" font-size="34" fill="#fbbf24" text-anchor="middle">Sai Ram Tummuri</text>
  <text x="400" y="275" font-family="'Plus Jakarta Sans', sans-serif" font-weight="600" font-size="12" fill="#cbd5e1" text-anchor="middle">NIT Andhra Pradesh</text>
  
  <text x="400" y="315" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="13" fill="#e2e8f0" text-anchor="middle">For outstanding national performance and securing</text>
  <text x="400" y="348" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="22" fill="#f59e0b" text-anchor="middle">RANK 13 NATIONWIDE</text>
  <text x="400" y="375" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="12" fill="#94a3b8" text-anchor="middle">In the competitive IISc × Qiskit Fall Fest 2025 Quantum Algorithm &amp; Circuit Optimization Challenge</text>
  
  <g transform="translate(140, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Eigen Trails Lead</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">IISc Bengaluru</text>
  </g>
  <g transform="translate(500, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Qiskit Advocate</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">IBM Quantum</text>
  </g>
  
  <text x="400" y="515" font-family="'Space Mono', monospace" font-size="9" fill="#475569" text-anchor="middle">CREDENTIAL: IISC-QFEST25-RANK13-SRT • VERIFIED HACKATHON</text>
</svg>"""

# 4. CeNSE Summer School 2026 (IISc Bengaluru)
cense_cert_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" width="100%" height="100%">
  <defs>
    <linearGradient id="censeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#022c22" />
      <stop offset="50%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#021f18" />
    </linearGradient>
  </defs>
  <rect width="800" height="560" fill="url(#censeBg)" rx="16"/>
  <rect x="20" y="20" width="760" height="520" rx="12" fill="none" stroke="#10b981" stroke-width="2"/>
  <rect x="28" y="28" width="744" height="504" rx="8" fill="none" stroke="rgba(16, 185, 129, 0.2)" stroke-width="1"/>
  
  <g transform="translate(60, 55)">
    <rect x="0" y="0" width="40" height="40" rx="8" fill="#10b981"/>
    <text x="20" y="26" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="16" fill="#ffffff" text-anchor="middle">CeNSE</text>
    <text x="52" y="20" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="16" fill="#ffffff">Centre for Nano Science and Engineering</text>
    <text x="52" y="36" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="12" fill="#6ee7b7">Indian Institute of Science (IISc), Bengaluru</text>
  </g>
  <rect x="620" y="55" width="120" height="30" rx="15" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
  <text x="680" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#6ee7b7" text-anchor="middle">SUMMER 2026</text>
  
  <text x="400" y="165" font-family="'Fraunces', serif" font-weight="700" font-size="28" fill="#ffffff" text-anchor="middle">Certificate of Training</text>
  <text x="400" y="195" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="14" fill="#94a3b8" text-anchor="middle">Presented to</text>
  <text x="400" y="248" font-family="'Fraunces', serif" font-weight="700" font-size="34" fill="#34d399" text-anchor="middle">Sai Ram Tummuri</text>
  
  <text x="400" y="300" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="13" fill="#e2e8f0" text-anchor="middle">For successful participation in the advanced cleanroom &amp; microfabrication modules at</text>
  <text x="400" y="332" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="20" fill="#10b981" text-anchor="middle">CeNSE Summer School 2026</text>
  <text x="400" y="362" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="12" fill="#a7f3d0" text-anchor="middle">Semiconductor Fabrication Protocols • Cleanroom Safety • Lithography • Thin-Film Characterization</text>
  
  <g transform="translate(140, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Chairperson, CeNSE</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">IISc Bengaluru</text>
  </g>
  <g transform="translate(500, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Program Coordinator</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">Summer School 2026</text>
  </g>
  <text x="400" y="515" font-family="'Space Mono', monospace" font-size="9" fill="#475569" text-anchor="middle">CREDENTIAL: IISC-CENSE-2026-SRT-FAB • CLEANROOM ACCREDITATION</text>
</svg>"""

# 5. SPARC-NanoX Semiconductor Fabrication Workshop / Internship SVG
wafer_fab_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="cleanroomBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="siliconGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="50%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#cleanroomBg)" rx="16"/>
  
  <!-- Silicon Wafer Disc Graphic -->
  <circle cx="300" cy="180" r="120" fill="#1e1e24" stroke="url(#siliconGrad)" stroke-width="4"/>
  <path d="M 400 110 A 120 120 0 0 0 200 110" stroke="#fbbf24" stroke-width="1" fill="none" opacity="0.3"/>
  <path d="M 415 150 A 120 120 0 0 0 185 150" stroke="#fbbf24" stroke-width="1" fill="none" opacity="0.3"/>
  <path d="M 420 190 A 120 120 0 0 0 180 190" stroke="#fbbf24" stroke-width="1" fill="none" opacity="0.3"/>
  <path d="M 410 230 A 120 120 0 0 0 190 230" stroke="#fbbf24" stroke-width="1" fill="none" opacity="0.3"/>
  
  <!-- Wafer Flat Notch -->
  <line x1="280" y1="300" x2="320" y2="300" stroke="#f59e0b" stroke-width="4"/>
  
  <!-- Microchip dies on wafer -->
  <g fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="1">
    <rect x="250" y="140" width="30" height="30" rx="2"/>
    <rect x="290" y="140" width="30" height="30" rx="2"/>
    <rect x="330" y="140" width="30" height="30" rx="2"/>
    <rect x="250" y="180" width="30" height="30" rx="2"/>
    <rect x="290" y="180" width="30" height="30" rx="2" fill="rgba(16, 185, 129, 0.4)" stroke="#10b981" stroke-width="2"/>
    <rect x="330" y="180" width="30" height="30" rx="2"/>
  </g>
  
  <!-- Info Overlay -->
  <rect x="30" y="320" width="540" height="60" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.1)"/>
  <text x="50" y="345" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="14" fill="#fbbf24">SPARC–NanoX Semiconductor Fabrication Workshop</text>
  <text x="50" y="365" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="11" fill="#94a3b8">IIT Hyderabad • Dept. of Electrical Engineering • Photolithography &amp; Thin Films</text>
</svg>"""

# 6. Breadboard Computer Schematic SVG
breadboard_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="pcbBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#022c22" />
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#pcbBg)" rx="16"/>
  <rect x="20" y="20" width="560" height="360" rx="10" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="8 4"/>
  
  <!-- 8-Bit Bus Traces -->
  <line x1="80" y1="200" x2="520" y2="200" stroke="#34d399" stroke-width="6"/>
  <text x="300" y="194" font-family="'Space Mono', monospace" font-size="10" fill="#a7f3d0" text-anchor="middle">MAIN 8-BIT DATA BUS</text>
  
  <!-- Modular Blocks -->
  <!-- Clock -->
  <rect x="60" y="60" width="90" height="80" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="105" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#ffffff" text-anchor="middle">CLOCK GEN</text>
  <text x="105" y="115" font-family="'Space Mono', monospace" font-size="9" fill="#fbbf24" text-anchor="middle">NE555 Timer</text>
  <line x1="105" y1="140" x2="105" y2="200" stroke="#f59e0b" stroke-width="2"/>
  
  <!-- Registers -->
  <rect x="180" y="60" width="100" height="80" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="230" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#ffffff" text-anchor="middle">REGISTER A</text>
  <text x="230" y="115" font-family="'Space Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">74LS173 D-FF</text>
  <line x1="230" y1="140" x2="230" y2="200" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- ALU -->
  <rect x="310" y="60" width="110" height="80" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
  <text x="365" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#ffffff" text-anchor="middle">8-BIT ALU</text>
  <text x="365" y="115" font-family="'Space Mono', monospace" font-size="9" fill="#c084fc" text-anchor="middle">74LS283 Adder</text>
  <line x1="365" y1="140" x2="365" y2="200" stroke="#a855f7" stroke-width="2"/>
  
  <!-- RAM / MAR -->
  <rect x="440" y="60" width="100" height="80" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
  <text x="490" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#ffffff" text-anchor="middle">RAM 16x8</text>
  <text x="490" y="115" font-family="'Space Mono', monospace" font-size="9" fill="#f472b6" text-anchor="middle">74LS189</text>
  <line x1="490" y1="140" x2="490" y2="200" stroke="#ec4899" stroke-width="2"/>
  
  <!-- Lower section: Instruction Register & Control ROM -->
  <rect x="180" y="250" width="240" height="90" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="300" y="285" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" fill="#ffffff" text-anchor="middle">CONTROL LOGIC &amp; MICROCODE</text>
  <text x="300" y="305" font-family="'Space Mono', monospace" font-size="10" fill="#34d399" text-anchor="middle">EEPROM / Diode Matrix • Step Sequencer</text>
  <line x1="300" y1="250" x2="300" y2="200" stroke="#10b981" stroke-width="2"/>
</svg>"""

create_svg("public/assets/profile/avatar.svg", avatar_svg)
create_svg("public/assets/quantum/certificates/qiskit-summer-school-2025.svg", qiskit_cert_svg)
create_svg("public/assets/quantum/certificates/iisc-qiskit-fallfest-2025.svg", iisc_cert_svg)
create_svg("public/assets/quantum/certificates/cense-iisc-2026.svg", cense_cert_svg)
create_svg("public/assets/ece/semiconductor/wafer-fab.svg", wafer_fab_svg)
create_svg("public/assets/ece/digital-electronics/breadboard-computer.svg", breadboard_svg)
print("Base SVGs created successfully!")

# 7. IBM Foundations of Quantum Error Correction SVG
ibm_qec_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" width="100%" height="100%">
  <defs>
    <linearGradient id="qecBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110e2e" />
      <stop offset="50%" stop-color="#1f1b4e" />
      <stop offset="100%" stop-color="#09061c" />
    </linearGradient>
  </defs>
  <rect width="800" height="560" fill="url(#qecBg)" rx="16"/>
  <rect x="20" y="20" width="760" height="520" rx="12" fill="none" stroke="#8b5cf6" stroke-width="2"/>
  <rect x="28" y="28" width="744" height="504" rx="8" fill="none" stroke="rgba(139, 92, 246, 0.2)" stroke-width="1"/>
  
  <g transform="translate(60, 55)">
    <rect x="0" y="0" width="38" height="38" rx="8" fill="#6929c4"/>
    <text x="19" y="25" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="18" fill="#ffffff" text-anchor="middle">IBM</text>
    <text x="50" y="25" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="20" fill="#ffffff">IBM Quantum</text>
    <text x="210" y="25" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="14" fill="#a78bfa">| Advanced Technical Curriculum</text>
  </g>
  <rect x="620" y="55" width="120" height="30" rx="15" fill="rgba(139, 92, 246, 0.2)" stroke="#8b5cf6"/>
  <text x="680" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#c084fc" text-anchor="middle">ACCREDITED</text>
  
  <text x="400" y="165" font-family="'Fraunces', serif" font-weight="700" font-size="28" fill="#ffffff" text-anchor="middle">Foundations of Quantum Error Correction</text>
  <text x="400" y="195" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="14" fill="#94a3b8" text-anchor="middle">Awarded to</text>
  <text x="400" y="248" font-family="'Fraunces', serif" font-weight="700" font-size="34" fill="#c084fc" text-anchor="middle">Sai Ram Tummuri</text>
  
  <text x="400" y="300" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="13" fill="#e2e8f0" text-anchor="middle">Demonstrating thorough theoretical comprehension and implementation proficiency in</text>
  <text x="400" y="332" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="20" fill="#a855f7" text-anchor="middle">Quantum Stabilizer Codes &amp; Syndrome Measurement</text>
  <text x="400" y="362" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="12" fill="#d8b4fe" text-anchor="middle">3-Qubit Bit/Phase Flip Codes • Shor 9-Qubit Code • Fault-Tolerant Circuit Design • Noise Mitigation</text>
  
  <g transform="translate(140, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">QEC Curriculum Board</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">IBM Quantum</text>
  </g>
  <g transform="translate(500, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">NIT Andhra Pradesh</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">Academic Verification</text>
  </g>
  <text x="400" y="515" font-family="'Space Mono', monospace" font-size="9" fill="#475569" text-anchor="middle">CREDENTIAL: IBM-QEC-FOUNDATION-SRT-2025 • VERIFIED SPECIALIZATION</text>
</svg>"""

# 8. WISER Summer School 2026 SVG
wiser_cert_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" width="100%" height="100%">
  <defs>
    <linearGradient id="wiserBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1026" />
      <stop offset="50%" stop-color="#2d1b40" />
      <stop offset="100%" stop-color="#120917" />
    </linearGradient>
  </defs>
  <rect width="800" height="560" fill="url(#wiserBg)" rx="16"/>
  <rect x="20" y="20" width="760" height="520" rx="12" fill="none" stroke="#ec4899" stroke-width="2"/>
  <rect x="28" y="28" width="744" height="504" rx="8" fill="none" stroke="rgba(236, 72, 153, 0.2)" stroke-width="1"/>
  
  <g transform="translate(60, 55)">
    <rect x="0" y="0" width="40" height="40" rx="8" fill="#db2777"/>
    <text x="20" y="26" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="16" fill="#ffffff" text-anchor="middle">W</text>
    <text x="52" y="20" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="16" fill="#ffffff">WISER Summer School 2026</text>
    <text x="52" y="36" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="12" fill="#f472b6">Advanced Scientific Research &amp; Semiconductor Physics</text>
  </g>
  <rect x="620" y="55" width="120" height="30" rx="15" fill="rgba(236, 72, 153, 0.2)" stroke="#ec4899"/>
  <text x="680" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#f472b6" text-anchor="middle">SCHOLAR 2026</text>
  
  <text x="400" y="165" font-family="'Fraunces', serif" font-weight="700" font-size="28" fill="#ffffff" text-anchor="middle">Certificate of Participation</text>
  <text x="400" y="195" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="14" fill="#94a3b8" text-anchor="middle">Awarded to</text>
  <text x="400" y="248" font-family="'Fraunces', serif" font-weight="700" font-size="34" fill="#f472b6" text-anchor="middle">Sai Ram Tummuri</text>
  
  <text x="400" y="300" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="13" fill="#e2e8f0" text-anchor="middle">In recognition of successful participation in interdisciplinary research workshops at</text>
  <text x="400" y="332" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="20" fill="#ec4899" text-anchor="middle">WISER Summer School 2026</text>
  <text x="400" y="362" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="12" fill="#fbcfe8" text-anchor="middle">Advanced Semiconductor Materials • Quantum Nanostructures • Research Methodologies</text>
  
  <g transform="translate(140, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Academic Director</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">WISER Consortium</text>
  </g>
  <g transform="translate(500, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Coordinator</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">Research Committee</text>
  </g>
  <text x="400" y="515" font-family="'Space Mono', monospace" font-size="9" fill="#475569" text-anchor="middle">CREDENTIAL: WISER-2026-SRT-HONORS • VERIFIED ATTENDANCE</text>
</svg>"""

# 9. Techobytes & E-Cell IIT Hyderabad Quantum Workshop
techobytes_cert_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" width="100%" height="100%">
  <defs>
    <linearGradient id="tbBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09182b" />
      <stop offset="50%" stop-color="#142c47" />
      <stop offset="100%" stop-color="#071322" />
    </linearGradient>
  </defs>
  <rect width="800" height="560" fill="url(#tbBg)" rx="16"/>
  <rect x="20" y="20" width="760" height="520" rx="12" fill="none" stroke="#0ea5e9" stroke-width="2"/>
  <rect x="28" y="28" width="744" height="504" rx="8" fill="none" stroke="rgba(14, 165, 233, 0.2)" stroke-width="1"/>
  
  <g transform="translate(60, 55)">
    <circle cx="20" cy="20" r="20" fill="#0284c7"/>
    <text x="20" y="26" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="14" fill="#ffffff" text-anchor="middle">IITH</text>
    <text x="52" y="20" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="16" fill="#ffffff">E-Cell IIT Hyderabad &amp; Techobytes</text>
    <text x="52" y="36" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="12" fill="#7dd3fc">National Hands-on Quantum Computing Workshop</text>
  </g>
  <rect x="620" y="55" width="120" height="30" rx="15" fill="rgba(14, 165, 233, 0.2)" stroke="#0ea5e9"/>
  <text x="680" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#7dd3fc" text-anchor="middle">CERTIFIED</text>
  
  <text x="400" y="165" font-family="'Fraunces', serif" font-weight="700" font-size="28" fill="#ffffff" text-anchor="middle">Certificate of Training</text>
  <text x="400" y="195" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="14" fill="#94a3b8" text-anchor="middle">Presented to</text>
  <text x="400" y="248" font-family="'Fraunces', serif" font-weight="700" font-size="34" fill="#38bdf8" text-anchor="middle">Sai Ram Tummuri</text>
  
  <text x="400" y="300" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="13" fill="#e2e8f0" text-anchor="middle">For active participation and practical circuit simulation execution in the</text>
  <text x="400" y="332" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="20" fill="#0284c7" text-anchor="middle">Quantum Computing &amp; Qiskit Workshop</text>
  <text x="400" y="362" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="12" fill="#bae6fd" text-anchor="middle">Conducted by Techobytes Technologies in collaboration with E-Cell, IIT Hyderabad</text>
  
  <g transform="translate(140, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Convener, E-Cell</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">IIT Hyderabad</text>
  </g>
  <g transform="translate(500, 440)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#475569" stroke-width="1"/>
    <text x="80" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" fill="#e2e8f0" text-anchor="middle">Technical Lead</text>
    <text x="80" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#64748b" text-anchor="middle">Techobytes Technologies</text>
  </g>
  <text x="400" y="515" font-family="'Space Mono', monospace" font-size="9" fill="#475569" text-anchor="middle">CREDENTIAL: IITH-TECHOBYTES-QC-SRT • WORKSHOP CERTIFICATE</text>
</svg>"""

# 10. IoT CoE-DMA Siemens & NIT Warangal Internship SVG
iot_internship_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="iotBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#042f2e" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#iotBg)" rx="16"/>
  <rect x="20" y="20" width="560" height="360" rx="12" fill="none" stroke="#0d9488" stroke-width="2"/>
  
  <!-- IoT Topology Gateway Diagram -->
  <circle cx="300" cy="180" r="45" fill="#134e4a" stroke="#2dd4bf" stroke-width="2"/>
  <text x="300" y="176" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#ffffff" text-anchor="middle">ESP32 / Pico</text>
  <text x="300" y="192" font-family="'Space Mono', monospace" font-size="9" fill="#5eead4" text-anchor="middle">IoT Gateway</text>
  
  <!-- Satellite nodes -->
  <!-- Sensor Node 1 -->
  <circle cx="150" cy="110" r="30" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="150" y="114" font-family="'Space Mono', monospace" font-size="9" fill="#38bdf8" text-anchor="middle">Sensors</text>
  <line x1="175" y1="125" x2="260" y2="160" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 2"/>
  
  <!-- MQTT Broker -->
  <circle cx="450" cy="110" r="30" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="450" y="114" font-family="'Space Mono', monospace" font-size="9" fill="#f59e0b" text-anchor="middle">MQTT</text>
  <line x1="425" y1="125" x2="340" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 2"/>
  
  <!-- Node-RED Flow -->
  <circle cx="300" cy="275" r="30" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="300" y="279" font-family="'Space Mono', monospace" font-size="9" fill="#f87171" text-anchor="middle">Node-RED</text>
  <line x1="300" y1="225" x2="300" y2="245" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4 2"/>
  
  <!-- Bottom Plate -->
  <rect x="40" y="325" width="520" height="50" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(45, 212, 191, 0.3)"/>
  <text x="60" y="347" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" fill="#2dd4bf">IoT Intern — CoE-DMA, NIT Warangal &amp; Siemens</text>
  <text x="60" y="363" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#94a3b8">June – July 2026 • Industrial IoT, ESP32, MQTT Broker, Node-RED Automation</text>
</svg>"""

# 11. MATLAB Signal Detection SVG
matlab_signal_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="matlabBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18181b" />
      <stop offset="100%" stop-color="#27272a" />
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#matlabBg)" rx="16"/>
  <rect x="30" y="30" width="540" height="270" rx="8" fill="#09090b" stroke="#3f3f46" stroke-width="1"/>
  
  <!-- Grid Lines -->
  <g stroke="#27272a" stroke-width="1">
    <line x1="30" y1="90" x2="570" y2="90"/>
    <line x1="30" y1="150" x2="570" y2="150"/>
    <line x1="30" y1="210" x2="570" y2="210"/>
    <line x1="120" y1="30" x2="120" y2="300"/>
    <line x1="210" y1="30" x2="210" y2="300"/>
    <line x1="300" y1="30" x2="300" y2="300"/>
    <line x1="390" y1="30" x2="390" y2="300"/>
    <line x1="480" y1="30" x2="480" y2="300"/>
  </g>
  
  <!-- Signal Sine Waves -->
  <!-- Carrier & Modulated wave -->
  <path d="M 40 165 Q 65 110, 90 165 T 140 165 T 190 165 T 240 165 T 290 165 T 340 165 T 390 165 T 440 165 T 490 165 T 540 165" fill="none" stroke="#06b6d4" stroke-width="2.5"/>
  <path d="M 40 165 Q 55 130, 70 165 T 100 165 T 130 165 T 160 165 T 190 165 T 220 165 T 250 165 T 280 165 T 310 165 T 340 165 T 370 165 T 400 165 T 430 165 T 460 165 T 490 165 T 520 165 T 550 165" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3"/>
  
  <text x="50" y="60" font-family="'Space Mono', monospace" font-size="11" fill="#06b6d4">CH1: S(t) Filtered Signal [MATLAB DSP]</text>
  <text x="50" y="80" font-family="'Space Mono', monospace" font-size="10" fill="#f59e0b">CH2: Noise-Corrupted Carrier Wave</text>
  
  <rect x="40" y="325" width="520" height="50" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(6, 182, 212, 0.3)"/>
  <text x="60" y="347" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" fill="#38bdf8">Signal Detection &amp; Analysis using MATLAB</text>
  <text x="60" y="363" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#94a3b8">FFT Spectral Analysis • SNR Optimization • Threshold Signal Detection Algorithms</text>
</svg>"""

# 12. Error Detection Digital Logic SVG
error_detection_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="edBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#edBg)" rx="16"/>
  <rect x="20" y="20" width="560" height="360" rx="12" fill="none" stroke="#6366f1" stroke-width="2"/>
  
  <!-- Logic Gates XOR tree diagram -->
  <g transform="translate(100, 70)">
    <!-- Inputs -->
    <text x="-40" y="30" font-family="'Space Mono', monospace" font-size="11" fill="#cbd5e1">D0 - D3</text>
    <line x1="20" y1="20" x2="80" y2="20" stroke="#818cf8" stroke-width="2"/>
    <line x1="20" y1="40" x2="80" y2="40" stroke="#818cf8" stroke-width="2"/>
    
    <!-- XOR Gate 1 -->
    <rect x="80" y="10" width="70" height="50" rx="6" fill="#312e81" stroke="#a5b4fc" stroke-width="1.5"/>
    <text x="115" y="40" font-family="'Space Mono', monospace" font-size="14" fill="#ffffff" text-anchor="middle">XOR</text>
    
    <!-- Line to Parity bit -->
    <line x1="150" y1="35" x2="230" y2="80" stroke="#818cf8" stroke-width="2"/>
    <line x1="150" y1="125" x2="230" y2="80" stroke="#818cf8" stroke-width="2"/>
    
    <!-- XOR Gate 2 -->
    <rect x="80" y="100" width="70" height="50" rx="6" fill="#312e81" stroke="#a5b4fc" stroke-width="1.5"/>
    <text x="115" y="130" font-family="'Space Mono', monospace" font-size="14" fill="#ffffff" text-anchor="middle">XOR</text>
    
    <!-- Output Parity Checker -->
    <rect x="230" y="60" width="80" height="50" rx="6" fill="#4338ca" stroke="#c7d2fe" stroke-width="2"/>
    <text x="270" y="90" font-family="'Space Mono', monospace" font-size="13" fill="#ffffff" text-anchor="middle">PARITY</text>
    
    <line x1="310" y1="85" x2="380" y2="85" stroke="#34d399" stroke-width="3"/>
    <circle cx="395" cy="85" r="14" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="395" y="90" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="11" fill="#ffffff" text-anchor="middle">OK</text>
  </g>
  
  <rect x="40" y="325" width="520" height="50" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(99, 102, 241, 0.3)"/>
  <text x="60" y="347" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" fill="#818cf8">Error Detection System using Digital Logic</text>
  <text x="60" y="363" font-family="'Plus Jakarta Sans', sans-serif" font-weight="400" font-size="10" fill="#94a3b8">Parity Generator &amp; Checker • Combinational TTL Logic Gates • Circuit Verification</text>
</svg>"""

create_svg("public/assets/quantum/certificates/ibm-foundations-qec.svg", ibm_qec_svg)
create_svg("public/assets/quantum/certificates/wiser-summer-school-2026.svg", wiser_cert_svg)
create_svg("public/assets/quantum/certificates/techobytes-iith-quantum.svg", techobytes_cert_svg)
create_svg("public/assets/ece/embedded/iot-internship.svg", iot_internship_svg)
create_svg("public/assets/ece/signal-processing/matlab-signal.svg", matlab_signal_svg)
create_svg("public/assets/ece/digital-electronics/error-detection.svg", error_detection_svg)
print("All extended SVGs created successfully!")
