@ECHO OFF
TIMEOUT 1 > NUL
ECHO (c) Microsoft Corporation. All rights reserved. &ECHO.
ECHO Initializing the server. Please wait... &ECHO.
TIMEOUT 1 > NUL
ECHO Press CTRL+C to terminate the server. &ECHO.
TIMEOUT 1 > NUL
server.py
ECHO Exiting...
TIMEOUT 3 > NUL
