@ECHO OFF
ECHO (c) Microsoft Corporation. All rights reserved. &ECHO.
ECHO The command has been executed, the data is being delivered to the server. Please wait. . .
TIMEOUT 1 > NUL
ECHO =========================================== &ECHO.
SET ip_address="IPv4 Address"
FOR /f "usebackq tokens=2 delims=:" %%f IN (`ipconfig ^| FINDSTR /c:%ip_address%`) DO ECHO Message from the server%%f: &ECHO.
TIMEOUT 1 > NUL
py -c "import comm_test; comm_test.response()" &ECHO.
ECHO ===========================================
ECHO Exiting. . .
TIMEOUT 3 > NUL
