#!/bin/bash

echo ""
echo "🔍 Python3 kontrol ediliyor..."

if ! command -v python3 &> /dev/null; then
    echo ""
    echo "❌ Python3 bulunamadı."
    echo "   → https://www.python.org/downloads/ adresinden kur, sonra tekrar dene."
    echo ""
    read -p "Kapatmak için Enter'a bas..."
    exit 1
fi

echo "✅ Python3 bulundu: $(python3 --version)"
echo ""

cd "$(dirname "$0")"

if [ ! -f "conversations.json" ]; then
    echo "❌ conversations.json bulunamadı!"
    echo "   → Claude'dan export ettiğin ZIP'i aç"
    echo "   → conversations.json dosyasını bu klasöre koy"
    echo "   → Tekrar çift tıkla"
    echo ""
    read -p "Kapatmak için Enter'a bas..."
    exit 1
fi

echo "📂 conversations.json bulundu, dönüştürülüyor..."
echo ""

python3 claude_export_to_md.py conversations.json

echo ""
echo "✨ Tamamlandı! claude_md_export/ klasörüne bak."
echo ""
read -p "Kapatmak için Enter'a bas..."
