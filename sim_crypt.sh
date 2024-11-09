echo "$ ./sim_crypt.py init mAsterPasswrd"
python3 sim_crypt.py init mAsterPasswrd
sleep 5

echo
echo "$ ./sim_crypt.py put mAsterPasswrd www.fer.hr neprobojnAsifrA"
python3 sim_crypt.py put mAsterPasswrd www.fer.hr neprobojnAsifrA
sleep 5

echo
echo "$ ./sim_crypt.py put wrong www.netflix.hr sifra"
python3 sim_crypt.py put wrong www.netflix.hr sifra
sleep 5

echo
echo "$ ./sim_crypt.py get mAsterPasswrd www.fer.hr"
python3 sim_crypt.py get mAsterPasswrd www.fer.hr
sleep 5

echo
echo "$ ./sim_crypt.py get wrongPasswrd www.fer.hr"
python3 sim_crypt.py get wrongPasswrd www.fer.hr
sleep 5

echo
echo "$ ./sim_crypt.py put mAsterPasswrd www.google.com novaSifra"
python3 sim_crypt.py put mAsterPasswrd www.google.com novaSifra
sleep 5

echo
echo "$ ./sim_crypt.py get mAsterPasswrd www.google.com"
python3 sim_crypt.py get mAsterPasswrd www.google.com
sleep 5

echo
echo "$ ./sim_crypt.py put mAsterPasswrd www.google.com druganovaSifra"
python3 sim_crypt.py put mAsterPasswrd www.google.com druganovaSifra
sleep 5

echo
echo "$ ./sim_crypt.py get mAsterPasswrd www.google.com"
python3 sim_crypt.py get mAsterPasswrd www.google.com
sleep 5