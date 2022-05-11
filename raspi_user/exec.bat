@ECHO OFF
ECHO (c) Microsoft Corporation. All rights reserved. &ECHO.
ECHO The command has been executed, the data is being delivered to the server. Please wait. . .
ECHO =========================================== &ECHO.
SET ip_address="IPv4 Address"
FOR /f "usebackq tokens=2 delims=:" %%f IN (`ipconfig ^| FINDSTR /c:%ip_address%`) DO ECHO Message from the server%%f: &ECHO.
py -c "import comm_test; comm_test.response()" &ECHO.
ECHO ===========================================
TIMEOUT /t 3
