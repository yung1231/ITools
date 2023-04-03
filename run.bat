@echo off
setlocal

echo --- Start IDAPython ---

set ida_path=D:\IDA_Pro_7.5\idat64.exe
set script_path=D:\idapython\opcode_extract.py
set target_dir=D:\dummy
set save_dir=D:\save_dir

if not exist "%benign_dir%" (
    mkdir "%benign_dir%"
    echo Create %benign_dir% dir
) else (
    echo %benign_dir% directory already exists.
)

for %%f in ("%target_dir%\*") do (
    %ida_path% -A -S"%script_path% %%~nxf %benign_dir%" "%%~ff"
    del "%%~dpnf.i64"
)

echo --- End IDAPython ---

endlocal