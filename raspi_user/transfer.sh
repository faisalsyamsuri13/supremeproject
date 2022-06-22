sleep 0.25
python -c "import writer"
sleep 0.5
echo 'Initializing...'
echo ''
sleep 1
echo 'Contacting the server, please wait...'
echo ''
sleep 1
python -c "import comm; comm.response()"
sleep 1
python -c "import client"
sleep 0.5
echo ''
echo 'Exiting...'
sleep 3
