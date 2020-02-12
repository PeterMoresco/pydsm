REM This script intalls some lybraries in a Windows computer that
REM are or intended to be used in this program and serves as
REM a reminder for later reference

@echo off
ECHO ================================================
ECHO ============ Instalando pacotes python =========
ECHO ================================================
python -m pip install --upgrade pip
python -m pip install numpy
python -m pip install progressbar
python -m pip install psutil
python -m pip install pandas
python -m pip install xlsxwriter
python -m pip install memory_profiler
python -m pip install pyfiglet
python -m pip install colorama
ECHO ================================================
ECHO =================== Finalizado =================
ECHO ================================================
