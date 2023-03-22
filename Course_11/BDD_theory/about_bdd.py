"""
BDD = Behaviour Driven Development

O abordare de software development in centrul careia stau scenariile de testare bazate pe asteptarile functionale ale clientului pentru aplicatie

Atunci cand dezvoltam o aplicatie cu BDD lucrurile se vor desfasura in felul urmator:
1. Definim scenariile de testare intr-un limbaj comun(engleza), care sa fie inteles de catre toti participantii si persoanele implicate in proiect.
Scenariile de testare vor fi scrise intr-un limbaj numit Gherkin
2. Definim testele automate care sa acopere scenariile definite mai sus.
Rulam testele si asteptare este ca acestea sa fie failed --> deoarece codul nuu a fost scris.
3. Scriem codul care sa implementeze aplicatia plecand de la testele automate scris anterior. Rulam din nou testele, care de aceasta data vot fi passed (asta daca nu intalnim un bug)
4. Daca sunt teste failed, atunci o sa raportam buguri, care ulterior or s afie fixate si apoi o sa reluam procesul de rulare a testetlor.
5. Repetam pasul 4 pana cand toate testele sunt passed.

AVANTAJE:
1. Oricine se va uita pe suita noastra de teste automate, va intelege usor ce am testat si ce functionalitati ale aplicatiei au fost acoperite
2. Focusul/atentia se muta pe scenariile de testare, astfel incat sansele de a asigura calitatea aplicatiei cresc.

BDD este o abordare derivata din TDD (Test Driven Development)

TDD = o abordare de software development in centrul careia stau testele automate scris pt testarea aplicatiei
Atunci cand dezvoltam o aplicatie cu TDD lucrurile se vor desfasura astfel:
1. Definim testele automate care sa acopere functionalitatile de business cerute de catre client.
....

Diferenra dintre TDD si BDD este ca la BDD se pune acentul pe scenarii (adica se pleaca de la scenarii), iar la TDD se pune accentul pe teste (adica se pleaca de la teste)
BDD are in plus fata de TDD descrierea scenariilor de business in limbajul gerkin salavate in niste fisiere numite feature files.

In python BDD-ul este implementat prin intermediul librariei behave


Un feature file este format din urmatoarele componente:

1. Feature to be tested = O functionalitate mai mare compusa din mai multe subfunctionalitati
2. Scenario = Un use case / o actiune sau un set de actiuni pe care utilizatorul le face pentru a obtine un anumit rezultat
3. Scenario steps = Intructiuni/ actiuni individuale pe care utilizatorul le face pentru a obtine un anumit rezultat

Echivalentul in Jira (Test management tool) al componentelor feature file
Feature = Epic
Scenario = Story
Scenario steps = Story description

Acceptance criteria = conditii pe care trebuie sa le indeplineasca un scenariu pentru ca acesta sa fie considerat passed

Gherkin = un limbaj descriptiv care este folosit pentru maparea testelor automate cu o descriere de business usor de inteles (de catre toti participantii la proiect)

Se bazeaza pe cateva cuvinte cheie:
feature = o functionalitate majora care poate fi testata
scenario= un scenariu specific ...
secenaroi outline = un scenariu mai complex cu mai multe variante de input
given = contextul in care se desfasoara actiune
when = actiunile pe care le face utilizatorul
then = rezultatul pe care ne asteptam sa il primim atunci cand efectuam actiunile de mai sus
background = pasii de tipul given care sunt valabili pentru mai multe scenarii (pentru a evita duplicarea codului)
"""




