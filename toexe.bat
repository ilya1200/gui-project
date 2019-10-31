
echo Installing PyInstaller
pip install PyInstaller
if %errorlevel% NEQ 0 (
echo --- Failed to install PyInstaller ---
exit /b %errorlevel%
)
echo Building the executable from source python files
PyInstaller --onefile -n gui --distpath . start.py
echo --- Successfully built the executable ---
