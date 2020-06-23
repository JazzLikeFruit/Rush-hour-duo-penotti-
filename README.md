# Rush hour

Rush Hour is een spel waarbij jouw rode auto vast staat op een bord met andere auto's. Het doel is om alle auto's weg te schuiven tot je met je rode auto naar de uitgang kan rijden.
Hierbij staat vast dat elke auto alleen kan bewegen in de orientatie waar deze al in stond, en dat ze niet gedraaid kunnen worden. Ook is het net als in het echte verkeer onmogelijk om door andere auto's heen te rijden, en kunnen ze alleen tegen elkaar aan rijden. 

Dit probleem lijkt simpel te zijn om op te lossen, maar naarmate het bord groter wordt en er meer auto's in de weg staan wordt het steeds complexer!

## Aan de slag

De code is in dit project geschreven in python. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn te installeren via pip met de volgende command:  
`pip install -r requirements.txt`


## Gebruik

De code kan gerunt worden door aanroepen van van:
`python main.py`

## Structuur

De volgende lijst beschrijft de belangerijkste mappen en documenten binnen deze directory:
- code  
    - algorithms  
        de folder algorithms bevat alle programma's met daarin de algoritmen die gebruikt kunnen worden om rush hour op te lossen  
        - breadth_first.py  
            breadth first gaat met de welbekende breadth first methode de mogelijke oplossingen door. Door de hoeveelheid geheugen die dit algoritme inneemt is het alleen functioneel om te gebruiken bij de 6x6 borden.  
        - breadth_first_prooning.py  
            description  
        - end_point.py  
            het end point algoritme begint met kijken of de rode auto geblokkeerd is door andere auto's. Als dit het geval is zoekt het algoritme door alle auto's heen die ertoe leiden dat de rode auto vast staat. De auto's die aan het eind van deze blokkade kunnen bewegen, worden dan weggeschoven, tot uiteindelijk de rode auto kan bewegen richting de uitgang.  
            Door de deterministische natuur van dit algoritme is het nodig om te gebruiken in conjunctie met een random algoritme. De verhouding waarin deze gebruikt worden kan worden bepaald door een threshold waarde mee te geven als het algoritme wordt uitgevoerd, met een threshold van 0 betekenend dat alleen het random algoritme uitgevoerd wordt, en een threshold van 1 betekenend dat alleen het end point algoritme wordt uitgevoerd.  
        - random_algorithm.py  
            het random algoritme kiest een random auto en een random aantal stappen uit om de auto te verplaatsen, en voert deze stappen uit tot het spel gewonnen is.  
        - short_path.py  
            het short path algoritme slaat elke configuratie van het bord per stap op. Zodra een stap ertoe leidt dat het volledige bord weer op een eerdere configuratie uitkomt, wordt het spel teruggezet naar de eerste stap waar deze configuratie voor is gekomen.  
        - unique_moves.py  
            het unique moves algoritme slaat elke configuratie van het bord per stap op. Elke move die gezet wordt mag niet leiden tot een bordconfiguratie die al is voorgekomen in een eerdere zet. Hierdoor moet elke zet leiden tot een nieuw spelbord.  

    - classes  
        de folder classes bevat de auto en board objecten om de game te kunnen laden  
        - board.py  
            het board object maakt een grid aan gebaseert op de naam van de inputfile, en vult deze met lege plekken en auto's gebaseerd op de coordinaten van de auto's.  
        - cars.py  
            het cars object slaat per auto de orientatie, naam, lengte en de positie van de auto op het bord op.  

- data  
    de data folder bevat de bestanden die de coordinaten van de auto's per spelbord bevatten.  

- endpoint_optimum.py  
    dit programma bevat code om het endpoint algoritme in conjunctie met het random algoritme uit te voeren voor alle spelborden. Er wordt gevraagd om een threshold min en max als het programma gerund wordt, wat de range bepaald van de thresholds die gebruikt worden. Er wordt ook gevraagd om het aantal herhalingen per run dat uitgevoerd moet worden.  

- main.py  
    main.py bevat het programma waarin een spelbord en een algoritme gekozen kunnen worden om uit te voeren. 

## Auteurs

- Nina
- Shewen Davelaar
- Joris
