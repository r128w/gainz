@echo off

:: directory for archive, help file, etc
set gainzdir="gainz"

set par1=%1

if "%par1%" EQU "help" goto help
if "%par1%" EQU "show" goto show
if "%par1%" EQU "edit" goto editIsReservedByBatch
if "%par1%" EQU "add"  goto add
if "%par1%" EQU "type" goto typeIsReservedByBatch

goto noCommand

:help
cls
type %gainzdir%\help.txt
goto:EOF

:show
py %gainzdir%\main.py show
goto:EOF

:add
py %gainzdir%\main.py add
goto:EOF

:editIsReservedByBatch
notepad %gainzdir%\archive.txt
goto:EOF

:typeIsReservedByBatch
py %gainzdir%\main.py type
goto:EOF

:noCommand
echo No command selected. Do you need "gainz help"?