import html

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. FIX JS UNICODE
script_start = text.find("<script>")
if script_start != -1:
    head = text[:script_start]
    script = text[script_start:]
    
    # We must unescape HTML entities FIRST so we can manipulate the string
    script = html.unescape(script)
    script = script.replace("₹", "\\u20B9")
    script = script.replace("·", "\\u00B7")
    
    # Also fix the text replacement in the table JS template
    # Wait, the table uses `&#x20b9;` literal because JS sets innerHTML. That's fine! 
    # But wait, earlier we tried to fix tooltips which use `₹` and `·`. Those were unescaped above!
    
    # 2. Add Live Clock logic
    if "// ── BOOT" in script:
        script = script.replace(
            "// ── BOOT ───────────────────────────────────────────",
            "// ── BOOT ───────────────────────────────────────────\n" +
            "    setInterval(() => {\n" +
            "      const d = new Date();\n" +
            "      const el = document.getElementById('liveClock');\n" +
            "      if(el) el.textContent = 'Live System Time: ' + d.toLocaleTimeString();\n" +
            "    }, 1000);\n"
        )
    
        # 3. Add AI Explain Logic
        script = script.replace(
            "<td><span class=\"badge ${rk}\">${c.risk}</span></td>",
            "<td><span class=\"badge ${rk}\">${c.risk}</span>" +
            "${c.risk === 'HIGH' ? `<button class='btn btn-ghost' style='padding: 2px 8px; font-size: 11px; margin-left: 8px; border: 1px solid #cbd5e1;' onclick='explainClaim(\"${c.id}\")'>&#x1F916; AI Explain</button>` : ''}" +
            "</td>"
        )
        
        script = script.replace(
            "// ── BOOT",
            "// ── AI FUNCTION ────────────────────────────────────\n" +
            "    async function explainClaim(id) {\n" +
            "      const m = document.getElementById('aiModal');\n" +
            "      const t = document.getElementById('aiText');\n" +
            "      m.style.display = 'flex';\n" +
            "      t.innerHTML = '<i>Generating AI Fraud Analysis...</i>';\n" +
            "      try {\n" +
            "        const r = await fetch('http://localhost:8000/explain/' + id);\n" +
            "        const d = await r.json();\n" +
            "        let txt = d.analysis || 'Error analyzing claim.';\n" +
            "        txt = txt.replace(/\\*\\*(.*?)\\*\\*/g, '<b>$1</b>');\n" +
            "        txt = txt.replace(/`(.*?)`/g, '<code style=\"background:#f1f5f9;padding:2px 4px;border-radius:4px;color:#0f172a;\">$1</code>');\n" +
            "        txt = txt.replace(/\\n/g, '<br>');\n" +
            "        t.innerHTML = txt;\n" +
            "      } catch(e) { t.innerHTML = '<span style=\"color:red\">Failed to connect to AI engine. Is the backend running?</span>'; }\n" +
            "    }\n" +
            "    function closeAiModal() { document.getElementById('aiModal').style.display='none'; }\n\n" +
            "// ── BOOT"
        )
    
    # Re-encode non-ascii (if any snuck in) back to html entities for safe ASCII writing
    script = script.encode("ascii", "xmlcharrefreplace").decode("ascii")
    text = head + script

# 4. Insert Live Clock in Navbar
navbar_actions = text.find('<div class="navbar-actions">')
if navbar_actions != -1:
    clock_html = '<div id="liveClock" style="font-size:12px;color:#64748b;font-weight:600;margin-right:16px;background:#f8fafc;padding:6px 12px;border-radius:6px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:6px;">&#x23F0; Live System Time: --</div>'
    text = text[:navbar_actions] + clock_html + text[navbar_actions:]

# 5. Insert AI Modal HTML
modal_html = """
<div id="aiModal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(15,23,42,0.4);z-index:9999;align-items:center;justify-content:center;backdrop-filter:blur(4px);">
  <div style="background:#ffffff;padding:2rem;border-radius:12px;max-width:550px;width:90%;box-shadow:0 25px 50px -12px rgba(0,0,0,0.25);border:1px solid #e2e8f0;animation: fadeUp 0.3s ease-out forwards;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;border-bottom:1px solid #f1f5f9;padding-bottom:1rem;">
      <h3 style="margin:0;color:#1e293b;font-family:Inter,sans-serif;font-size:1.25rem;display:flex;align-items:center;gap:8px;font-weight:700;">
        <span style="background:#eff6ff;padding:8px;border-radius:8px;font-size:1.2rem;display:flex;">&#x1F916;</span> AI Fraud Investigator
      </h3>
      <button onclick="closeAiModal()" style="background:none;border:none;font-size:1.8rem;color:#94a3b8;cursor:pointer;line-height:1;border-radius:6px;padding:4px 8px;transition:0.2s;">&times;</button>
    </div>
    <div id="aiText" style="color:#475569;line-height:1.7;font-size:0.95rem;font-family:Inter,sans-serif;"></div>
  </div>
</div>
"""
body_end = text.find("</body>")
if body_end != -1:
    text = text[:body_end] + "\n" + modal_html + "\n" + text[body_end:]

# Also fix the broken HTML entity in "Last loaded" logic if it had "&middot;" instead of "&#183;"
text = text.replace("&middot;", "&#183;")

text_safe = text.encode("ascii", "xmlcharrefreplace").decode("ascii")

with open("index.html", "w", encoding="ascii") as f:
    f.write(text_safe)
print("UI Successfully Patched!")
