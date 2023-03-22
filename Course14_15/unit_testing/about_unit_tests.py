"""
In testare se pot defini mai multe niveluri de testare in functie de procentajul de finalizare a aplicatiei.

1. Unit testing
2. Component testing
3. Integration testing
4. System testing
5. Acceptance testing

1. Unit testing - a nu se confunda cu libraruia unittest
- cel mai detaliat nivel de testare care presupune testarea celor mai mici bucati functionale dintr-o app software.
De regula: functii care testeaza alte functii.
Pentru a rula fisiere de teste unitare se foloseste libraria pytest
pip install pytest

Pentru rulare:
1. Rularea intregului pachet de teste: pytest <nume_pachet>
2. Rularea unui fisier specific prin scrierea adresei la care se afla:
pytest <adresa_fisier/nume_fisier.py>
3. Mutarea in folderul in care se afla fisierul
cd <adresa_fisier> si rulare <pytest nume_fisiere>

2. Component testing - testarea modulelor individuale din aplicatie.
3. Component Integration testing
- legarea componentelor intre ele si definirea comunicarii intre componente
System integration testing
- legarea sistemelor intre ele si definirea comunicarii intre sisteme

4. System testing - testarea functionalitatilor end to end
5. Acceptance testing - nivel de testare care presupune verificarea functionalitatii aplicatiei din perspectiva clientului
- alpha testing - testarea facuta de catre testari la sediul dezvoltatorului pentru a face o ultima verificare a produsului
- beta testing - testare facuta la sediul clientului, pe environmentul clientului.
"""