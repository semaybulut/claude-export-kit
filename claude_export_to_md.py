#!/usr/bin/env python3
"""
Claude Conversations JSON → Markdown Converter
Kullanım: python3 claude_export_to_md.py conversations.json
Çıktı: Her conversation için ayrı .md dosyası (output/ klasörüne)
"""

import json
import os
import sys
from datetime import datetime, timezone


def sanitize_filename(name: str) -> str:
    """Dosya adı için güvenli string."""
    if not name or not name.strip():
        return "untitled"
    safe = "".join(c if c.isalnum() or c in " -_" else "_" for c in name)
    return safe.strip()[:80]


def format_timestamp(iso_str: str) -> str:
    """ISO timestamp → okunabilir format."""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return iso_str[:16] if iso_str else ""


def extract_text_from_content(content_blocks: list) -> str:
    """
    Content bloklarından sadece text kısımlarını çıkar.
    tool_use / tool_result bloklarını atla.
    """
    parts = []
    for block in content_blocks:
        btype = block.get("type", "")
        if btype == "text":
            text = block.get("text", "").strip()
            if text:
                parts.append(text)
        # tool_use ve tool_result atlanıyor (internal mechanics)
    return "\n\n".join(parts)


def conversation_to_markdown(conv: dict) -> str:
    """Tek bir conversation dict'ini Markdown string'e çevirir."""
    title = conv.get("name") or "Untitled Conversation"
    created = format_timestamp(conv.get("created_at", ""))
    updated = format_timestamp(conv.get("updated_at", ""))
    messages = conv.get("chat_messages", [])

    lines = []
    lines.append(f"# {title}")
    lines.append(f"\n> **Oluşturulma:** {created}  |  **Son güncelleme:** {updated}")
    lines.append(f"> **Mesaj sayısı:** {len(messages)}")
    lines.append("\n---\n")

    for msg in messages:
        sender = msg.get("sender", "unknown")
        ts = format_timestamp(msg.get("created_at", ""))
        content_blocks = msg.get("content", [])

        # Content bloklarından text çıkar
        text = extract_text_from_content(content_blocks)

        # Fallback: direkt text field
        if not text:
            text = msg.get("text", "").strip()

        if not text:
            continue  # boş mesajı atla

        if sender == "human":
            lines.append(f"### 🧑 Sen  `{ts}`\n")
        else:
            lines.append(f"### 🤖 Claude  `{ts}`\n")

        lines.append(text)
        lines.append("\n---\n")

    return "\n".join(lines)


def main():
    # --- Input dosyası ---
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        # Default: aynı klasörde conversations.json
        input_path = "conversations.json"

    if not os.path.exists(input_path):
        print(f"❌ Dosya bulunamadı: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        print("❌ Beklenmedik format: JSON root bir liste olmalı.")
        sys.exit(1)

    # --- Output klasörü ---
    output_dir = os.path.join(os.path.dirname(input_path), "claude_md_export")
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n📂 {len(data)} conversation bulundu.\n")

    for i, conv in enumerate(data):
        title = conv.get("name") or "untitled"
        date_str = conv.get("created_at", "")[:10]  # YYYY-MM-DD
        safe_name = sanitize_filename(title)
        filename = f"{date_str}_{safe_name}.md"
        out_path = os.path.join(output_dir, filename)

        md_content = conversation_to_markdown(conv)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        msg_count = len(conv.get("chat_messages", []))
        print(f"  ✅ [{i+1}/{len(data)}] {filename}  ({msg_count} mesaj)")

    print(f"\n✨ Tamamlandı → {output_dir}/\n")


if __name__ == "__main__":
    main()
