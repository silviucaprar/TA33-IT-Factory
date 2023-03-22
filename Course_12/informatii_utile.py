"""
Background: este o modalitate prin car eputem sa dam un context generaltestelor noastre (nu functioneaza decat cu GIVEN)
Putem sa punem in background orice elemente de context care sunt valabile pentru toate scenariile din feature file
Daca vrem sa separam teste pe care le rulam pentru rulare individuala, putem sa ne folosim de conceputul de tag-uri
Tag-urile incep cu semnul @ si sunt urmate de free text (recomandat sa fie ceva sugestiv pentru scenariul in scop)
Un scenariu poate sa fie indentificat de mai multe tag-uri
In momentul rularii putem sa specificam tag-ul care ne intereseaza si se vor rula toate testele indentificate de acel tag

Scenario outline = o modalitate prin care putem sa rulam acelasi teste de mai multe ori cu mai multe perechi de valori de input
"""