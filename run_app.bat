@echo off
title Multi-Agent Startup Incubator
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File "%~dp0start_local.ps1"
pause
