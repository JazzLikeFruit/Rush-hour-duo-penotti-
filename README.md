# Rush hour

Rush Hour is een spel waarbij jouw rode auto vast staat op een bord met andere auto's. Het doel is om alle auto's weg te schuiven tot je met je rode auto naar de uitgang kan rijden.
Hierbij staat vast dat elke auto alleen kan bewegen in de orientatie waar deze al in stond, en dat ze niet gedraaid kunnen worden. Ook is het net als in het echte verkeer onmogelijk om door andere auto's heen te rijden, en kunnen ze alleen tegen elkaar aan rijden. 

Dit probleem lijkt simpel te zijn om op te lossen, maar naarmate het bord groter wordt en er meer auto's in de weg staan wordt het steeds complexer!  

Wij hebben 6 algoritmen geschreven die deze puzzel op kunnen lossen. Elk algoritme zal het aantal stappen weergeven dat het heeft gekost om tot een winnende oplossing te komen. Wij hebben bepaald dat elke beweging die in 1x gemaakt kan worden over meerdere stukken grid 1 move is, in tegenstelling tot andere uitvoeringen die we gevonden hebben waarbij een beweging over 1 stuk grid equivalent is aan 1 move.

## Aan de slag

De code is in dit project geschreven in python. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn te installeren via pip d.m.v. de command `pip install -r requirements.txt`


## Gebruik

De spelborden kunnen worden opgelost door de volgende command te runnen: `python main.py`. Dit opent een interface waarin een spelbord en een algoritme gekozen kunnen worden om het spel mee op te lossen. Als het algoritme klaar is met runnen zal het winnende bord en het aantal stappen dat het over de oplossing deed weergegeven worden. Als een van de eerste drie spelborden gekozen is, kan er als er gevraagd wordt naar het algoritme ook `all` als input gegeven worden, waarbij alle algoritmen uitgevoerd worden. Op het moment dat deze optie gekozen wordt bij een groter bord bestaat de kans dat het programma vastloopt.

## Structuur

De volgende lijst beschrijft de belangerijkste mappen en documenten binnen deze directory:
- **code**  
    - **algorithms**  
        de folder algorithms bevat alle programma's met daarin de algoritmen die gebruikt kunnen worden om rush hour op te lossen  
        - **breadth_first_prooning.py**  
            dit algoritme gaat op de welbekende breadth-first manier op zoek naar een oplossing. D.m.v. de pruning worden alleen borden die nog niet zijn voorgekomen in de queue gezet, wat de executie en de runtime sterk verbeterd vergeleken met een versie zonder pruning. Dit algoritme kan niet gebruikt worden voor spelborden hoger dan spelbord 4.
        - **breath_first.py**
            deze file bevat een implementatie van de breadth-fist algoritme. De runtime van deze code is te langzaam om in een redelijke tijd met een oplossing voor de boarden t             komen. De eerste algoritme werd met behulp van deze code geschreven. 
        - **end_point.py**  
            het end point algoritme begint met kijken of de rode auto geblokkeerd is door andere auto's. Als dit het geval is zoekt het algoritme door alle auto's heen die ertoe leiden dat de rode auto vast staat. De auto's die aan het eind van deze blokkade kunnen bewegen, worden dan weggeschoven, tot uiteindelijk de rode auto kan bewegen richting de uitgang.  
            Door de deterministische natuur van dit algoritme is het nodig om te gebruiken in conjunctie met een random algoritme. De verhouding waarin deze gebruikt worden kan worden bepaald door een threshold waarde mee te geven als het algoritme wordt uitgevoerd, met een threshold van 0 betekenend dat alleen het random algoritme uitgevoerd wordt, en een threshold van 1 betekenend dat alleen het end point algoritme wordt uitgevoerd. Vooralsnog lijkt een threshold van 0.7 voor de meest optimale oplossing te zorgen.  
        - **random_algorithm.py**  
            het random algoritme kiest een random auto en een random aantal stappen uit om de auto te verplaatsen, en voert deze stappen uit tot het spel gewonnen is.  
        - **short_path.py**  
            het short path algoritme slaat elke configuratie van het bord per stap op. Zodra een stap ertoe leidt dat het volledige bord op een eerder verschenen configuratie uitkomt, wordt het spel teruggezet naar de eerste stap waar deze configuratie voor is gekomen.  
        - **unique_moves.py**  
            het unique moves algoritme slaat elke configuratie van het bord per stap op. Elke move die gezet wordt mag niet leiden tot een bordconfiguratie die al is voorgekomen in een eerdere zet. Hierdoor moet elke zet leiden tot een nieuw spelbord.  

    - **classes**  
        de folder classes bevat de bestanden met de auto en bord objecten om de game te kunnen laden  
        - **board.py**  
            het board object maakt een grid aan gebaseert op de naam van de inputfile, en vult deze met lege plekken en auto's gebaseerd op de coordinaten van de auto's.  
        - **cars.py**  
            het cars object slaat per auto de orientatie, naam, lengte en de positie van de auto op het bord op.  

- **data**  
    de data folder bevat de input bestanden die de coordinaten van de auto's per spelbord bevatten.  

- **endpoint_optimum.py**  
    dit programma bevat code om het endpoint algoritme in conjunctie met het random algoritme uit te voeren voor alle spelborden. Er wordt gevraagd om een threshold min en max als het programma gerund wordt, wat de range bepaald van de thresholds die gebruikt worden. Er wordt ook gevraagd om het aantal herhalingen per run dat uitgevoerd moet worden.  

- **main.py**  
    main.py bevat het programma waarin een spelbord en een algoritme gekozen kunnen worden om uit te voeren. Er verschijnt een menu waar eerst het spelbord gekozen kan worden, en daarna het algoritme om dit bord mee op te lossen. 

## Auteurs

- Nina Borsboom
- Shewen Davelaar
- Joris Bruil
