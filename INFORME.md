<style>
/* Estils globals del document */
body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 9pt;
  text-align: justify;
  line-height: 1.4;
}

/* Paràgrafs justificats */
p {
  text-align: justify;5
  font-size: 9pt;
}

/* Estils per a les llistes amb la mateixa mida que el text normal */
ul, ol, code{
  font-size: 9pt;
  line-height: 1.4;
}

li {
  font-size: 9pt;
  line-height: 1.4;
}

/* Títols més petits */
h1 {
  font-size: 12pt;
  text-align: left;
}

h2 {
  font-size: 10pt;
  text-align: left;
}

h3 {
  font-size: 9pt;
  text-align: left;
}

h4 {
  font-size: 9pt;
  text-align: left;
}

/* Contenidor principal per a la fila d'imatges */
.image-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
  align-items: flex-start;
  width: 100%;
}

/* Cada columna que conté una imatge i el seu text */
.image-column {
  flex: 0 1 48%;
  min-width: 280px;
  max-width: 450px;              /* LÍMIT: Màxim 450px d'amplada */
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}

/* Quan només hi ha UNA imatge */
.image-row:has(.image-column:only-child) .image-column {
  max-width: 600px;              /* LÍMIT: Una sola imatge màx 600px */
  flex: 0 1 auto;
}

/* Imatge única */
.image-row:has(.image-column:only-child) .image-column img {
  width: 100%;
  max-width: 600px;              /* LÍMIT: Max 600px per imatge única */
  max-height: 500px;             /* LÍMIT: Max 500px d'alçada */
  height: auto;
  object-fit: contain;
}

/* Estils per a la imatge (múltiples imatges) */
.image-column img {
  width: 100%;
  max-width: 450px;              /* LÍMIT: Max 450px per imatge */
  max-height: 400px;             /* LÍMIT: Max 400px d'alçada */
  height: auto;
  display: block;
  object-fit: contain;
}

/* Estils per al peu de foto */
.image-column .caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
  width: 100%;
}

/* Estil per a la separació de pàgines en PDF */
.page-break {
  page-break-before: always;
  break-before: page;
}

/* Bloc imatge-esquerra / text-dreta */
.media-row {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
  margin: 1rem 0;
}

.media-image {
  flex: 0 0 38%;
  max-width: 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.media-image img {
  width: 100%;
  height: auto;
  display: block;
}

.media-image .caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
}

.media-text {
  flex: 1 1 0;
  min-width: 240px;
}

/* ============================================
   CONTENIDOR DE TAULES AMB PEU DE TAULA
   ============================================ */
.table-container {
  width: 100%;
  margin: 1.5rem 0;
  overflow-x: auto;
  page-break-inside: avoid;
}

/* Estils per a les taules */
.table-container table {
  width: 100%;
  max-width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
  margin: 0 auto;
  background-color: #fff;
}

/* Capçalera de taula */
.table-container thead {
  background-color: #e0e0e0;
  font-weight: bold;
}

.table-container th {
  padding: 8px 6px;
  text-align: center;
  border: 1px solid #888;
  font-size: 7pt;
}

/* Files de dades */
.table-container td {
  padding: 6px 5px;
  text-align: center;
  border: 1px solid #aaa;
  font-size: 7pt;
}

/* Files alternades (zebra striping) */
.table-container tbody tr:nth-child(even) {
  background-color: #f5f5f5;
}

/* Peu de taula (caption) */
.table-container .table-caption {
  margin-top: 0.5rem;
  font-size: 8pt;
  text-align: center;
  color: #555;
  font-style: italic;
}

/* Estil alternatiu: caption sobre la taula */
.table-container .table-title {
  margin-bottom: 0.5rem;
  font-size: 9pt;
  text-align: center;
  font-weight: bold;
  color: #333;
}

/* Millores per a impressió/PDF */
@media print {
  .table-container {
    page-break-inside: avoid;
  }

  .table-container table {
    border: 1px solid #000;
  }

  .table-container th,
  .table-container td {
    border: 1px solid #666;
  }

  .image-column {
    page-break-inside: avoid;
  }

  /* Límits més restrictius per a PDF */
  .image-column img {
    max-height: 350px;
  }

  .image-row:has(.image-column:only-child) .image-column img {
    max-height: 450px;
  }
}

@page {
  @bottom-center {
    content: "Pàgina " counter(page) " de " counter(pages);
    font-size: 8pt;
    color: #555;
  }
}

</style>

## 0. Taula de continguts

- [0. Taula de continguts](#0-taula-de-continguts)
- [1. Introducció](#1-introducció)
- [2. Objectius i metodologia](#2-objectius-i-metodologia)
- [3. Implementació en Python](#3-implementació-en-python)
- [4. Experimentació](#4-experimentació)
  - [4.1 Experiment 1: Selecció d'Operadors](#41-experiment-1-selecció-doperadors)
  - [4.2 Experiment 2: Estratègia d'Inicialització](#42-experiment-2-estratègia-dinicialització)
  - [4.3 Experiment 3: Calibratge de Simulated Annealing](#43-experiment-3-calibratge-de-simulated-annealing)
  - [4.4 Experiment 4: Escalabilitat Temporal](#44-experiment-4-escalabilitat-temporal)
    - [4.4.1 Plantejament del problema](#441-plantejament-del-problema)
    - [4.4.2 Mètode](#442-mètode)
    - [4.4.3 Resultats](#443-resultats)
    - [4.4.4 Conclusions](#444-conclusions)
  - [4.5 Experiment 5: Consolidació de Centres](#45-experiment-5-consolidació-de-centres)
  - [4.6 Experiment 6: Sensibilitat al Cost per Km](#46-experiment-6-sensibilitat-al-cost-per-km)
  - [4.7 Experiment 7: Variació de l'Horari Laboral](#47-experiment-7-variació-de-lhorari-laboral)
  - [4.8 Experiment 8: Validació de Resultats (Experiment Especial)](#48-experiment-8-validació-de-resultats-experiment-especial)
- [5. Conclusions](#5-conclusions)

<div class="page-break"></div>

## 1. Introducció

## 2. Objectius i metodologia

## 3. Implementació en Python

## 4. Experimentació

### 4.1 Experiment 1: Selecció d'Operadors

### 4.2 Experiment 2: Estratègia d'Inicialització

### 4.3 Experiment 3: Calibratge de Simulated Annealing

### 4.4 Experiment 4: Escalabilitat Temporal

En problemes de distribució amb múltiples centres i clients (gasolineres), la **qualitat de la solució** i el **temps de computació** depenen de l'**algorisme de cerca local utilitzat** i de la **mida del problema**. S'observa que tant Hill Climbing (HC) com Simulated Annealing (SA) poden trobar solucions, però poden *comportar-se diferent* segons l'escala del problema. Aquest experiment té com a objectiu avaluar com **la mida del problema afecta el rendiment temporal i la qualitat de les solucions obtingudes per ambdós algorismes**, per tal d'identificar quin algorisme és més adequat per a problemes de diferents escales.

#### 4.4.1 Plantejament del problema

Ens plantegem la següent qüestió de recerca:
Com **afecta la mida del problema** (nombre de centres i gasolineres) al temps d'execució i a la qualitat de les solucions obtingudes per algorismes de cerca local (Hill Climbing i Simulated Annealing)?

També ens plantegem:

- Quin algorisme (HC o SA) és més eficient en termes de temps d'execució?
- Quin algorisme proporciona millors solucions (major benefici)?
- Com escala el temps d'execució amb la mida del problema?
- Els paràmetres de SA es mantenen adequats en augmentar la mida del problema

Per a respondre aquestes qüestions, plantegem les següents hipòtesis:

- $H_0$: No hi ha diferències significatives en la qualitat de les solucions obtingudes per HC i SA a mesura que augmenta la mida del problema.
- $H_{1_a}$: Simulated Annealing proporciona solucions de millor qualitat (major benefici) que Hill Climbing.
- $H_{1_b}$: Hill Climbing és significativament més ràpid que Simulated Annealing.
- $H_{1_c}$: El temps d'execució creix de manera no lineal amb la mida del problema per ambdós algorismes.

#### 4.4.2 Mètode

Per a resoldre aquesta qüestió, farem un estudi experimental amb mesures repetides, utilitzant la proporció ``(centres:gasolineres)`` per a diferents mides del problema. Seleccionarem mides creixents per avaluar l'impacte de la mida del problema en el rendiment dels algorismes. Aquestrs mides seran múltiples de $(10:100)$, com ara: $(20:200)$, $(30:300)$, $(40:400)$, fins a $(100:1000)$.

Executatrem 3 rèpliques per cada combinació algorisme-mida (amb seeds diferents: 1234, 1235, 1236), per tant, el total d'experiments serà:

- 10 mides del problema (de $(10:100)$ a $(100:1000)$)
- 2 algorismes (HC i SA)
- 3 rèpliques per combinació

Total experiments: $10 \times 2 \times 3 = 64$ experiments

Per a cada experiment, seguirem els següents passos:

1. Generació de gasolineres i centres amb seed controlada per reproducibilitat
2. Creació de l'estat inicial utilitzant inicialització greedy (seleccionada als experiments 1 i 2)
3. Aplicació de l'algorisme de cerca (HC o SA)
4. Mesura del temps d'execució (en mil·lisegons) i càlcul del benefici obtingut
5. Repetició del procés per a les 3 rèpliques

Les variables usades en aquest experiment són:

Variables independents:

- Mida del problema: Nombre de centres de distribució (i corresponent nombre de gasolineres en proporció $10:100$)
- Algorisme de cerca: Hill Climbing (HC) vs Simulated Annealing (SA)

Variables dependents:

- Temps d'execució: Temps en mil·lisegons necessari per trobar la solució
- Qualitat de la solució: Benefici obtingut (ingressos - costos - penalitzacions) en euros

Variables controlades:

- Inicialització: Greedy
- Funció heurística: Mateixa per ambdós algorismes
- Operadors: ``swapCentres`` i ``mourePeticio``
- Paràmetres del problema:
  - km màxims per camió: $640$
  - Viatges màxims per camió: $5$
  - Valor del dipòsit: $1000€$
  - Cost per km: $2€/km$
  - Multiplicitat (camions per centre): $1$

#### 4.4.3 Resultats

<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>Centres</th>
        <th>Gasolineres</th>
        <th>HC Temps (ms)</th>
        <th>SA Temps (ms)</th>
        <th>HC Benefici (€)</th>
        <th>SA Benefici (€)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>10</td>
        <td>100</td>
        <td>4.71 ± 1.40</td>
        <td>176.80 ± 43.77</td>
        <td>78,905.33 ± 5,364.21</td>
        <td>78,905.33 ± 5,364.21</td>
      </tr>
      <tr>
        <td>20</td>
        <td>200</td>
        <td>5.50 ± 0.90</td>
        <td>262.60 ± 14.92</td>
        <td>146,541.33 ± 11,717.81</td>
        <td>146,541.33 ± 11,717.81</td>
      </tr>
      <tr>
        <td>30</td>
        <td>300</td>
        <td>12.94 ± 1.82</td>
        <td>397.87 ± 10.57</td>
        <td>227,730.67 ± 2,310.00</td>
        <td>227,730.67 ± 2,310.00</td>
      </tr>
      <tr>
        <td>40</td>
        <td>400</td>
        <td>17.07 ± 0.58</td>
        <td>541.66 ± 16.92</td>
        <td>305,804.00 ± 8,281.67</td>
        <td>305,804.00 ± 8,281.67</td>
      </tr>
      <tr>
        <td>50</td>
        <td>500</td>
        <td>30.80 ± 1.56</td>
        <td>715.54 ± 27.89</td>
        <td>379,674.67 ± 4,586.52</td>
        <td>379,674.67 ± 4,586.52</td>
      </tr>
      <tr>
        <td>60</td>
        <td>600</td>
        <td>27.63 ± 4.18</td>
        <td>973.33 ± 67.50</td>
        <td>458,681.33 ± 11,162.71</td>
        <td>458,681.33 ± 11,162.71</td>
      </tr>
      <tr>
        <td>70</td>
        <td>700</td>
        <td>26.99 ± 10.53</td>
        <td>1,069.85 ± 50.40</td>
        <td>535,348.00 ± 17,466.36</td>
        <td>535,348.00 ± 17,466.36</td>
      </tr>
      <tr>
        <td>80</td>
        <td>800</td>
        <td>34.17 ± 6.99</td>
        <td>1,083.88 ± 73.85</td>
        <td>622,076.00 ± 13,773.39</td>
        <td>622,076.00 ± 13,773.39</td>
      </tr>
      <tr>
        <td>90</td>
        <td>900</td>
        <td>35.45 ± 7.39</td>
        <td>1,181.71 ± 52.65</td>
        <td>701,654.67 ± 19,625.70</td>
        <td>701,654.67 ± 19,625.70</td>
      </tr>
      <tr>
        <td>100</td>
        <td>1,000</td>
        <td>36.86 ± 7.79</td>
        <td>1,312.00 ± 87.17</td>
        <td>766,644.00 ± 19,266.81</td>
        <td>766,644.00 ± 19,266.81</td>
      </tr>
    </tbody>
  </table>
  <div class="table-caption">
    Taula 1: Resultats de l'experiment d'escalabilitat. Comparació del temps d'execució (ms) i benefici (€) entre Hill Climbing (HC) i Simulated Annealing (SA) segons la mida del problema. Valors mostren mitjana ± desviació estàndard de 3 rèpliques amb seeds 1234, 1235 i 1236.
  </div>
</div>

Ambdós algorismes obtenen solucions de qualitat idèntica en totes les mides del problema, amb beneficis que oscil·len entre 78905€ (10 centres) i 766644€ (100 centres). Les desviacions estàndard també són equivalents, indicant que la inicialització greedy utilitzada ja proporciona solucions d'alta qualitat. En aquest context, SA no aconsegueix escapar dels òptims locals trobats per HC per millorar els resultats.

Anàlisi del temps d'execució segons l'algorisme:

<div class="image-row">
  <div class="image-column">
    <img src="./experiments/resultats/4/experiment_escalabilitat_log.png" alt="Gràfic de Temps d'Execució vs Mida del Problema">
    <div class="caption">Figura n: Log-temps d'execució (ms) en funció de la mida del problema per Hill Climbing (HC) i Simulated Annealing (SA).
    </div>
  </div>
</div>

Les dues línies (HC en blau i SA en taronja) són aproximadament paral·leles en escala logarítmica. Això indica que ambdós algorismes tenen la mateixa complexitat temporal $O(n)$. Si un algorisme creixés quadràticament i l'altre linealment, les línies divergirien progressivament. La distància vertical constant entre les dues línies confirma que SA és consistentment 35-40 vegades més lent que HC en tot el rang de mides. En escala logarítmica, una diferència constant vertical representa un factor multiplicatiu constant.

No obstant això, Hill Climbing resulta clarament preferible en aquest context específic, ja que proporciona solucions de qualitat idèntica a les de Simulated Annealing amb un temps d'execució entre 35 i 40 vegades inferior. És rellevant destacar que la diferència temporal entre ambdós algorismes es manté com un factor multiplicatiu constant al llarg de tot el rang de mides analitzat, evidenciant que no es tracta d'una diferència de complexitat algorítmica sinó d'un cost base inherent a SA. Extrapolant els resultats observats, per a un problema de 200 centres de distribució s'esperarien temps d'execució aproximats de 70-75 mil·lisegons per a Hill Climbing i al voltant de 2500 mil·lisegons per a Simulated Annealing, mantenint la mateixa proporció temporal i qualitat de solució, la qual cosa reforça la idoneïtat de HC per a aplicacions que requereixin respostes ràpides sense comprometre la qualitat dels resultats obtinguts.

L'aplanament de HC entre 30-70 centres és interessant i suggereix que l'algorisme convergeix més ràpidament en problemes de mida mitjana, possiblement per característiques específiques de les instàncies generades o perquè l'espai de cerca té menys òptims locals a explorar.

Anàlisi segons la mida del problema:

<div class="image-row">
  <div class="image-column">
    <img src="./experiments/resultats/4/experiment_escalabilitat.png" alt="Gràfic de Temps d'Execució vs Mida del Problema">
    <div class="caption">Figura n+1: Gràfcs varis en funció de la mida del problema per Hill Climbing (HC) i Simulated Annealing (SA).</div>
  </div>
</div>

Aquest conjunt de gràfics proporciona una anàlisi completa i multidimensional dels resultats experimentals

**Gràfic 1:** Temps d'execució vs Mida del problema (superior esquerre)

- La línia blava (HC) es manté gairebé plana, oscillant entre 5-37 ms en tot el rang
- La línia taronja (SA) mostra un creixement lineal pronunciat, de ~177 ms a ~1,312 ms
- Les barres d'error (desviació estàndard) són petites en HC i més grans en SA

Hill Climbing és extremadament ràpid i estable, mentre que SA presenta un cost temporal molt superior que creix de manera consistent. L'escala del gràfic fa que HC sembli quasi constant, demostrant la seva eficiència.

**Gràfic 2:** Benefici vs Mida del problema (superior dret)

- Les dues línies són perfectament superposades - només es veu la línia taronja de SA
- Creixement lineal del benefici: de ~79000€ (10 centres) a ~767000€ (100 centres)
- Les barres d'error són idèntiques per ambdós algorismes
- El benefici augmenta proporcionalment amb la mida del problema

Aquí es demostra que HC i SA obtenen **exactament les mateixes solucions**. No hi ha cap avantatge de SA en qualitat, la qual cosa invalida completament el seu cost temporal addicional. El creixement lineal del benefici amb la mida indica que la qualitat escala bé.

**Gràfic 3:** Ràtio de temps SA/HC (inferior esquerre)

- La línia roja discontinua marca la igualtat (SA = HC)
- El ràtio oscil·la entre $23x$ (50 centres) i $47x$(20 centres)
- Variabilitat notable: el ràtio no és constant
- Pic a 20 centres (~47x) i vall a 50 centres (~23x)

Aquesta variabilitat en el ràtio suggereix que la velocitat relativa dels algorismes depèn parcialment de les característiques específiques de cada instància del problema. Tot i això, SA sempre és almenys 23 vegades més lent, confirmant la seva inferioritat en eficiència. El valor mitjà de 35-40x es manté com a referència.

**Gràfic 4:** Diferència de benefici SA - HC (inferior dret)

- La línia està **perfectament centrada en zero** (diferència = $0€$)
- No hi ha cap desviació visible de la línia horizontal
- Tots els punts coincideixen exactament amb zero

#### 4.4.4 Conclusions

Respecte a $H_{1_a}$ (qualitat de solucions):

**Rebutgem la hipòtesi**. Tant HC com SA proporcionen solucions de qualitat idèntica, amb una diferència mitjana de 0€. Els beneficis obtinguts són exactament els mateixos en totes les mides del problema analitzades (des de 78905€ amb 10 centres fins a 766644€ amb 100 centres), demostrant que la inicialització greedy utilitzada ja situa les solucions en òptims locals d'alta qualitat que SA no aconsegueix superar.

Respecte a $H_{1_b}$ (temps d'execució):

**Acceptem la hipòtesi**. HC és significativament més ràpid que SA, amb una diferència de 35-40 vegades més, en promig. Per exemple, amb 100 centres, HC triga ``36.86 ms`` mentre que SA necessita ``1.312 ms``, representant un factor multiplicatiu constant al llarg de tot el rang de mides analitzat. Aquesta diferència es manté estable independentment de la mida del problema.

Respecte a $H_{1_c}$ (escalabilitat):

**Rebutgem parcialment la hipòtesi inicial de creixement no lineal**. El temps d'execució creix de manera aproximadament lineal $O(n)$ amb la mida del problema, observant-se increments de 7.8x per HC i 7.4x per SA quan la mida augmenta 10 vegades (de 10 a 100 centres). Aquest comportament és millor del previst i indica una excel·lent escalabilitat per ambdós algorismes, tot i que el cost base de SA el fa impràctic per a problemes grans malgrat la seva complexitat lineal.

***

Per a aquest problema d'optimització de rutes amb inicialització greedy, Hill Climbing és clarament superior a Simulated Annealing: ofereix solucions de qualitat idèntica amb un temps d'execució 35-40 vegades inferior, major estabilitat i predictibilitat, i excel·lent escalabilitat. Els resultats suggereixen que la combinació d'inicialització greedy i operadors locals utilitzats proporciona un paisatge de cerca amb pocs òptims locals profunds, limitant l'avantatge teòric de SA per escapar-ne.

### 4.5 Experiment 5: Consolidació de Centres

### 4.6 Experiment 6: Sensibilitat al Cost per Km

### 4.7 Experiment 7: Variació de l'Horari Laboral

### 4.8 Experiment 8: Validació de Resultats (Experiment Especial)

## 5. Conclusions
