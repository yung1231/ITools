@echo off
setlocal EnableDelayedExpansion

echo --- Start IDAPython ---
echo.

set ida_path=D:\IDA_Pro_7.5\idat64.exe
set script_path=D:\idapython\opcode_extract.py
set target_dir=D:\dummy
set save_dir=D:\save_dir

if not exist "%save_dir%" (
    mkdir "%save_dir%"
    echo [+] Create %save_dir% dir
) else (
    echo [+] %save_dir% directory already exists.
)

echo [+] Start analysis.
set count=0

for %%f in ("%target_dir%\*") do (
    %ida_path% -A -S"%script_path% %%~nxf %save_dir%" "%%~ff"
    del "%%~dpnf.i64"
    set /a count+=1
    echo Processed !count! files.
)

echo.
echo --- End IDAPython ---

pause

endlocal