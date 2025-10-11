# Planificació setmanal pràctica:
## Primera setmana: Presa de contacte amb el problema i implementació de l’estat (10 a 19 d’octubre)

El primer que haureu de fer és reflexionar sobre el problema que descriu l’enunciat i plantejar-vos les mateixes preguntes que us fèieu en els problemes de la primera sessió de pràctiques:

- **Quins elements intervenen en el problema?**
- **Quin és l’espai de cerca?**
- **Quina mida té l’espai de cerca?**
- **Què és un estat inicial?**
- **Quines condicions compleix un estat final?**
- **Quins operadors permeten modificar els estats?**
- **Quin factor de ramificació tenen els operadors de canvi d’estat?**

A partir de les respostes a aquestes preguntes, us podeu plantejar què necessitareu per implementar la pràctica amb les classes de l’AIMA.  
Fixeu-vos que vosaltres **no heu d’implementar els algoritmes**, sinó que heu d’identificar i implementar els elements que aquests necessiten.  
Aquests elements són els que s’han explicat a classe de teoria: **estat**, **operadors de cerca** i **funció heurística**.

---

### Representació de l’estat

Un primer exercici consisteix a pensar **quina estructura de dades** heu d’implementar per representar l’estat.  
És fonamental pensar la representació tenint en compte **l’eficiència espacial i temporal**, ja que la cerca generarà una gran quantitat d’estats.

A partir d’aquest plantejament previ, hauríeu de començar a plantejar-vos **la implementació de la classe que representa l’estat**.  
La implementació de l’estat inclou decidir **quina estructura de dades és més adequada** per representar els elements del problema.  
Com ja s’ha esmentat, aquesta representació hauria de ser **eficient**, ja que l’exploració generarà un gran nombre d’estats.

Per guanyar **eficiència espacial**, és una bona idea declarar com a **estàtiques** les parts de la representació que no canvien, de manera que es comparteixin entre totes les instàncies.

---

### Generació de la solució inicial

Haureu d’implementar **constructors** que generin la solució inicial.  
L’enunciat demana que busqueu **almenys dues estratègies** per generar-la.

Heu de pensar en diversos aspectes sobre com generar aquesta solució inicial, com ara **quin és el cost** de generar-la i **com n’és de bona**.

De cara als experiments, és interessant observar **com influeix la qualitat de la solució inicial** en el resultat de la cerca.  
Per exemple, podeu utilitzar una estratègia que generi **solucions molt dolentes** i una altra que, **segons algun criteri, sigui millor**, i analitzar si el nombre de passos fins a arribar a la solució final i la seva qualitat són diferents.

---

### Implementació dels operadors de cerca

Dins de la implementació de l’estat també s’inclou **la implementació dels operadors de cerca**.  
Heu d’analitzar **quin conjunt d’operadors és més convenient**.

Observeu que el **factor de ramificació** és important, perquè influeix directament en el temps necessari per trobar la solució.  

També heu de tenir en compte que uns operadors que no generin prou alternatives poden donar lloc a **solucions pitjors**, ja que no permetrien explorar correctament l’espai de cerca.

Penseu bé **quines operacions** es poden fer dins del problema.  
De vegades en calen diverses per poder accedir a tot l’espai de cerca, i també pot haver-hi **conjunts alternatius d’operadors**.

## Segona setmana: Implementació de les classes per a l’AIMA (del 20 al 26 d’octubre)

A aquestes alçades ja hauríeu de tenir implementat l’estat del problema juntament amb els seus operadors i les estratègies d’inici de la cerca.

Ara necessiteu implementar la resta de classes que l’AIMA utilitza per resoldre el problema.

Implementar la classe que genera els estats successors és senzill: només heu de generar, per a un estat, tots els estats accessibles possibles. Com que ja tindreu implementats els operadors, només cal decidir com es fa la generació dels nodes aplicant-los. L’ordre en què es generen és indiferent, només cal assegurar-se que per a cada node es generin tots els successors accessibles. Recordeu que l’estratègia per generar els nodes ha de ser diferent per a **Hill Climbing** i per a **Simulated Annealing**.  
Per a Hill Climbing haureu de generar totes les possibles aplicacions dels operadors a l’estat actual, mentre que per a Simulated Annealing haureu d’escollir a l’atzar un operador i generar només un successor aplicant aquest operador amb paràmetres també aleatoris.

Amb això n’hi ha prou, ja que és l’algoritme de cerca el que s’encarregarà de fer l’exploració i decidir quins nodes s’expandeixen.

La classe que comprova si s’ha arribat a un estat final és la més senzilla de totes. En el cas de la cerca local, no és possible saber si s’ha arribat a l’estat final, per tant, la funció que implementa aquesta classe ha de retornar sempre **fals**. Podeu copiar aquesta classe de qualsevol dels exemples de cerca local que teniu, ja que totes són iguals.

La classe en què haureu de pensar més és la que calcula la **funció heurística**.

Heu de reflexionar sobre què mesuren les funcions heurístiques que descriu l’enunciat i decidir com es calculen a partir de l’estat.

Recordeu que les funcions heurístiques que implementeu s’han de **minimitzar**. Penseu també que la diferència entre **maximitzar** i **minimitzar** és simplement un canvi de signe.

---

## Tercera setmana: Experiments (del 24 al 29 d’octubre i del 6 al 9 de novembre)

Durant aquesta setmana hauríeu de tenir ja una implementació funcional de la pràctica i començar a fer **experiments**.

Heu de pensar en els diferents escenaris que es poden plantejar amb els elements que teniu.  
Tingueu en compte que l’objectiu dels experiments és obtenir informació que us permeti respondre a les preguntes que planteja l’enunciat.  
Tingueu també en compte que un mateix experiment pot proporcionar informació per a diverses preguntes.

Seguiu l’ordre dels experiments que teniu a l’enunciat; això us permetrà anar prenent decisions sobre els diferents elements del problema i establir-les per a experiments posteriors.

Per ajustar els paràmetres del **Simulated Annealing**, escolliu valors extrems i proveu-ne els efectes.  
A partir d’aquests valors podeu anar ajustant-los explorant punts intermedis fins a trobar un valor que considerareu adequat segons l’objectiu del problema.  
Tingueu en compte el significat dels paràmetres per guiar-vos en la vostra exploració.

Feu **suposicions** sobre com haurien de ser les solucions de cada experiment i comproveu els resultats que obteniu.  
Compareu si aquests resultats corresponen amb les vostres intuïcions i intenteu justificar el resultat.

Tingueu present que, per poder extreure conclusions fonamentades, haureu d’executar cada experiment **diverses vegades**.  
Per tal de comparar, haureu d’executar els algoritmes amb les mateixes dades; per això podeu fixar les **llavors del generador de nombres aleatoris** quan creeu les dades.

Podeu il·lustrar la **significativitat dels resultats** que obtingueu utilitzant els coneixements adquirits a l’assignatura d’estadística.  
També podeu utilitzar **gràfics** per mostrar el que succeeix als experiments.

No us oblideu d’anar escrivint la **documentació** a mesura que aneu fent els experiments.

## Quarta setmana: La documentació final (del 10 al 14 de novembre)

En aquesta setmana hauríeu de tenir els resultats dels experiments i escriure la documentació.

Una cosa que heu de tenir present és que la documentació ha de ser un reflex del vostre treball, ja que és el que servirà perquè qualifiquem la vostra pràctica. Una mala documentació significa una mala nota.

La documentació ha d’incloure:

- La descripció/justificació de la implementació de l’estat  
- La descripció/justificació dels operadors que heu triat  
- La descripció/justificació de les estratègies per trobar la solució inicial  
- La descripció/justificació de les funcions heurístiques  
- Per a cada experiment:
  - Condicions de cada experiment  
  - Resultats de l’experiment  
  - Què esperàveu i què heu obtingut  
  - Comparacions  
  - Comentaris addicionals que us semblin adequats  
- Comparació entre els resultats obtinguts amb Hill Climbing i Simulated Annealing (no oblideu explicar com heu ajustat els paràmetres per a aquest últim algoritme).  
- Respostes raonades a les preguntes de l’enunciat.

