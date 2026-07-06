# Multi-Agent Startup Incubator - Local Server Runner

Clear-Host
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "     Multi-Agent Startup Incubator Server Runner     " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host ""

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot

# 1. Detect Python
$PythonPath = "python"
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    # Check default AppData Local path
    $LocalPython = "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
    if (Test-Path $LocalPython) {
        $PythonPath = $LocalPython
        Write-Host "[Python] Local AppData'da Python 3.11 bulundu." -ForegroundColor Green
    } else {
        Write-Host "[HATA] Sisteminizde Python bulunamadı!" -ForegroundColor Red
        Write-Host "Lütfen Python 3.10+ kurun ve PATH'e ekleyin." -ForegroundColor Yellow
        Read-Host "Kapatmak için Enter'a basın..."
        exit
    }
} else {
    Write-Host "[Python] Sistemde Python bulundu." -ForegroundColor Green
}

# 2. Virtual Environment check
$VenvPath = Join-Path $ProjectRoot "venv"
if (!(Test-Path $VenvPath)) {
    Write-Host "[Venv] Sanal ortam bulunamadı. Oluşturuluyor..." -ForegroundColor Yellow
    & $PythonPath -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[HATA] Sanal ortam oluşturulamadı!" -ForegroundColor Red
        Read-Host "Kapatmak için Enter'a basın..."
        exit
    }
    Write-Host "[Venv] Sanal ortam başarıyla oluşturuldu." -ForegroundColor Green
}

# 3. Activate Virtualenv
Write-Host "[Venv] Sanal ortam aktif ediliyor..." -ForegroundColor Cyan
. "$VenvPath\Scripts\Activate.ps1"

# 4. Install/Upgrade requirements
Write-Host "[Deps] Bağımlılıklar kontrol ediliyor..." -ForegroundColor Cyan
python -m pip install --upgrade pip -q
python -m pip install -r backend/requirements.txt -q
Write-Host "[Deps] Tüm bağımlılıklar güncel." -ForegroundColor Green

# 5. Open Browser
Write-Host "[Browser] http://127.0.0.1:8000 adresi tarayıcıda açılıyor..." -ForegroundColor Green
Start-Process "http://127.0.0.1:8000"

# 6. Start Uvicorn Server
Write-Host "[Server] FastAPI Uvicorn sunucusu başlatılıyor..." -ForegroundColor Cyan
Write-Host "Durdurmak için CTRL+C tuşlarına basın." -ForegroundColor Yellow
Write-Host "----------------------------------------------------"
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
