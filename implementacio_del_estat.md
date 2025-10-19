# Implementació de l'estat

## Càlcul del benefici

El benefici total es calcula com els ingressos dels dipòsits servits avui menys els costos de desplaçament, incorporant una penalització pel valor que es perd si es deixen peticions pendents un dia més per la rebaixa del preu aplicable l’endemà.

Cada petició equival a omplir un dipòsit d’una gasolinera; el camió té capacitat per a dos dipòsits, de manera que pot atendre fins a dues peticions per viatge. El preu base serà $P$ i té associat un factor de preu que el modifica en funció dels dies que la petició ha estat pendent. Aquest factor de preu es defineix com:

$$
f(d) = \begin{cases}
  1.02  \text{  si } d = 0 \\
  \max(0,1-0.02 \cdot d) \text{  si } d > 0
\end{cases}
$$

On $d$ és el nombre de dies que la petició ha estat pendent. Així, el preu efectiu per una petició pendent $d$ dies és $P \cdot f(d)$.

Per tant, si $S$ és el conjunt de peticions complertes avui (per a tota la flota de camions), els ingressos totals dels dipòsits servits avui es poden expressar com:

$$
I = \sum_{p \in S}^{n} P \cdot f(d_p)
$$

La distància sobre la quadrícula es calcula amb la mètrica Manhattan:

$$
d_1((x_1, y_1), (x_2, y_2)) = |x_1 - x_2| + |y_1 - y_2|
$$

La llargada total d'un viatge serà:

- Si se serveix una única gasolinera G des d'un centre C: $L = d(C, G) + d(G, C)$
- Si se serveixen dues gasolineres G1 i G2 des d'un centre C: $L = d(C, G1) + d(G1, G2) + d(G2, C)$

Si el cost per quilòmetre és $C_k$, el cost total $C$ per una quantitat de viatges $t$ de llargada $L$ serà:

$$
C = C_k \cdot \sum_{i=1}^{t} L_i
$$

Finalment, el benefici total $B$ es calcula com:

$$
B = I - C
$$

Per tal de minimitzar les penalitzacions i així maximitzar el benefici, definirem una funció que calculi aquesta penalització total, que podem fer servir per comparar diferents estats i com a ajuda a la nostra heurística:

- El preu d'una petició pendent $d$ dies és $P \cdot f(d)$.
- Si no s'atén avui la petició, demà el preu serà $P \cdot f(d+1)$, per tant la pèrdua potencial és: $ \Delta_ u = P \cdot (f(d) - f(d+1))$, on $u$ és la petició pendent.
- Si $U$ és el conjunt de peticions pendents avui, la penalització total $Pen$ es pot expressar com:
    $$
    Pen = \sum_{u \in U} P \cdot (f(d_u) - f(d_u + 1))
    $$

La funció de benefici total, doncs, quedaria:

$$
B_{total} = B - C - Pen
$$

## Possibles solucions inicials

1. Solució bàsica: __Assignar a cada camió les peticions més properes__ (de distància) fins a omplir la seva capacitat, _sense tenir en compte la penalització per peticions pendents._ Si un camió no pot atendre dues peticions (ja sigui per distància o per capacitat), només se li assigna una petició. Si un camió no pot atendre cap petició, torna al centre sense fer cap servei. Les peticions desateses es deixen pendents per al dia següent.
2. Solució complexa: Les peticions es prioritzen segons la seva __penalització potencial__ (pèrdua de preu per dia pendent). El camió atén primer les peticions amb la penalització més __alta__, sempre que estiguin dins de la seva capacitat i distància. Després, si és compatible per distància i capacitat, s'assigna la petició més propera geogràficament, i en cas d'empat, la que tingui més dies pendents, i en cas d'empat, la que impliqui menys distància de retorn al centre assignat al camió. Si això no és possible, el camió torna al centre havent atès la petició amb la penalització més alta. Si un camió no és compatible amb cap petició, retorna al seu centre sense fer cap servei. Les peticions desateses es deixen pendents per al dia següent.

## Possibles operadors

Per entendre-ho, cal recordar que:

- Cada centre té un __ÚNIC__ camió assignat.
- Cada camió té una capacitat màxima de 2 dipòsits per viatge.
- Cada petició només pot ser atesa per UN camió en un dia.
- Cada camió pot fer diversos viatges (v) en un dia fins a esgotar la seva capacitat, distància màxima o les peticions disponibles.
- Cada viatge comença i acaba al centre assignat al camió.  

Alguns possibles operadors per modificar l'estat actual són:

1. __Swap de centres per petició:__ Intercanviar les peticions assignades entre dos camions que pertanyen a diferents centres, és a dir, si el camió A del centre C1 té assignada la petició P1 i el camió B del centre C2 té assignada la petició P2, es poden intercanviar aquestes peticions entre els dos camions.
2. __Moure peticions d'un viatge a un altre:__ Transferir una petició d'un viatge d'un camió a un altre viatge del mateix camió, sempre que es compleixin les restriccions de capacitat i distància.
3. __Swap de peticions entre viatges:__ Intercanviar peticions entre dos viatges diferents, ja sigui del mateix camió o de camions diferents, sempre que es compleixin les restriccions de capacitat i distància.
4. __Reordenar ordre de servei en un viatge:__ Canviar l'ordre en què es serveixen les peticions dins d'un mateix viatge per optimitzar la distància recorreguda, si el camió atén dues peticions en un viatge.
5. __Reemparellar peticions dins d’un mateix camió:__ dividir un viatge amb dues aturades en dos viatges d’una aturada i recombinar-lo amb altres viatges d’una aturada del mateix camió, si això redueix la distància total recorreguda.
