@echo off
chcp 65001 >nul
echo.
echo Checking Python3...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Python bulunamadi.
        echo    - https://www.python.org/downloads/ adresinden kur
        echo    - Kurulum sirasinda "Add Python to PATH" kutusunu mutlaka isaretle
        echo    - Sonra bu dosyaya tekrar cift tikla
        echo.
        pause
        exit /b 1
    )
    set PYTHON=python3
) else (
    set PYTHON=python
)

echo Python bulundu.
echo.

if not exist "conversations.json" (
    echo [ERROR] conversations.json bulunamadi!
    echo    - Claude.ai - Settings - Privacy - Export Data
    echo    - Gelen maildeki linke tikla, ZIP indir
    echo    - ZIP'i ac, conversations.json'i bu klasore koy
    echo    - Tekrar cift tikla
    echo.
    pause
    exit /b 1
)

echo conversations.json bulundu, donusturuluyor...
echo.

%PYTHON% claude_export_to_md.py conversations.json

echo.
echo Tamamlandi! claude_md_export klasorune bak.
echo.
pause
