echo "Dodavanje korisnika sgros"
echo "$ ./usermgmt add sgros"
python3 usermgmt.py add sgros

echo
echo "Dodavanje korisnika mjau"
echo "$ ./usermgmt add mjau"
python3 usermgmt.py add mjau

echo
echo "Dodavanje korisnika mk"
echo "$ ./usermgmt add mk"
python3 usermgmt.py add mk

echo
echo "Dodavanje korisnika krivo - različite šifre"
echo "$ ./usermgmt add krivo"
python3 usermgmt.py add krivo

echo
echo "Mijenjanje šifre za korisnika sgros"
echo "$ ./usermgmt passwd sgros"
python3 usermgmt.py passwd sgros

echo
echo "Mijenjanje šifre kod sljedećeg logiranja za korisnika mk"
echo "$ ./usermgmt forcepass mk"
python3 usermgmt.py forcepass mk

echo
echo "Brisanje korisnika mjau"
echo "$ ./usermgmt del mjau"
python3 usermgmt.py del mjau

echo
echo "Logiranje korisnika sgros"
echo "$ ./login sgros"
python3 login.py sgros

echo
echo "Logiranje korisnika mjau"
echo "$ ./login mjau"
python3 login.py mjau

echo
echo "Logiranje korisnika mk"
echo "$ ./login mk"
python3 login.py mk