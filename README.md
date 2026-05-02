# Claude Export Kit
English description below.

Claude sohbetlerini JSON'dan temiz Markdown dosyalarına dönüştürür.
Mac, Windows ve Linux desteklenir.

---

## MAC KURULUM (bir kere)

1. Bu klasörü istediğin bir yere koy (örn. Documents/claude-export/)
2. Terminal'i aç (Spotlight → "Terminal"), şunu yapıştır:

   chmod +x ~/Documents/claude-export/run.command

## MAC KULLANIM (her export'ta)

1. Claude.ai → Sol alt profil → Settings → Privacy → Export Data
2. Gelen maildeki linke tıkla → ZIP indir
3. ZIP'i aç → conversations.json çıkar
4. conversations.json dosyasını bu klasöre at (eskisinin üzerine yaz)
5. run.command dosyasına çift tıkla
6. claude_md_export/ klasöründe sohbetler .md olarak hazır

---

## WINDOWS KURULUM (bir kere)

1. Python'u kur: https://www.python.org/downloads/
   !! Kurulum sırasında "Add Python to PATH" kutusunu işaretle !!
2. Bu klasörü istediğin bir yere koy (örn. Belgeler/claude-export/)

## WINDOWS KULLANIM (her export'ta)

1. Claude.ai → Sol alt profil → Settings → Privacy → Export Data
2. Gelen maildeki linke tıkla → ZIP indir
3. ZIP'i aç → conversations.json çıkar
4. conversations.json dosyasını bu klasöre at (eskisinin üzerine yaz)
5. run.bat dosyasına çift tıkla
6. claude_md_export/ klasöründe sohbetler .md olarak hazır

---

## GEREKSİNİM

- Python 3 kurulu olmalı
- Kontrol: Terminal/CMD → python3 --version
- Kurulum: https://www.python.org/downloads/

## NOT

Claude'un resmi exportu bazı sohbetleri eksik getirebilir — bu Anthropic'in bilinen bir limitasyonudur.

---
## ENGLISH

# Claude Export Kit

Converts Claude chats from JSON to clean Markdown files.
Supports Mac, Windows, and Linux.

---

## MAC SETUP (one-time)

1. Place this folder anywhere you like (e.g., Documents/claude-export/)
2. Open Terminal (Spotlight → "Terminal") and paste the following:

   chmod +x ~/Documents/claude-export/run.command

## MAC USAGE (for every export)

1. Claude.ai → Profile (bottom left) → Settings → Privacy → Export Data
2. Click the link in the email you receive → Download the ZIP
3. Extract the ZIP → locate conversations.json
4. Move conversations.json into this folder (overwrite the old one)
5. Double-click the run.command file
6. Your chats are ready as .md files in the claude_md_export/ folder

---

## WINDOWS SETUP (one-time)

1. Install Python: https://www.python.org/downloads/
   !! Make sure to check the "Add Python to PATH" box during installation !!
2. Place this folder anywhere you like (e.g., Documents/claude-export/)

## WINDOWS USAGE (for every export)

1. Claude.ai → Profile (bottom left) → Settings → Privacy → Export Data
2. Click the link in the email you receive → Download the ZIP
3. Extract the ZIP → locate conversations.json
4. Move conversations.json into this folder (overwrite the old one)
5. Double-click the run.bat file
6. Your chats are ready as .md files in the claude_md_export/ folder

---

## REQUIREMENTS

- Python 3 must be installed
- Check: Terminal/CMD → python3 --version
- Installation: https://www.python.org/downloads/

## NOTE

Claude's official export may sometimes result in missing chats — this is a known limitation of Anthropic.
