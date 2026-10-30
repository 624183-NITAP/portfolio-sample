with open("index.html", "r", encoding="utf-8") as f:
    full_html = f.read()

# Generate ece.html - A dedicated landing experience for ECE Engineering
ece_html = full_html.replace(
    "<title>Sai Ram Tummuri | Electronics &amp; Semiconductor Engineering &amp; Quantum Computing</title>",
    "<title>ECE Engineering &amp; Semiconductor Technology | Sai Ram Tummuri (NIT AP)</title>"
)
# In ece.html, default domain filter to ece
ece_html = ece_html.replace("setDomainFilter('all')", "setDomainFilter('ece')")

with open("ece.html", "w", encoding="utf-8") as f:
    f.write(ece_html)
print(f"Generated ece.html ({len(ece_html)} bytes)")

# Generate quantum.html - A dedicated landing experience for Quantum Computing
quantum_html = full_html.replace(
    "<title>Sai Ram Tummuri | Electronics &amp; Semiconductor Engineering &amp; Quantum Computing</title>",
    "<title>Quantum Computing &amp; Quantum Error Correction | Sai Ram Tummuri (NIT AP)</title>"
)
# In quantum.html, default domain filter to quantum
quantum_html = quantum_html.replace("setDomainFilter('all')", "setDomainFilter('quantum')")

with open("quantum.html", "w", encoding="utf-8") as f:
    f.write(quantum_html)
print(f"Generated quantum.html ({len(quantum_html)} bytes)")

