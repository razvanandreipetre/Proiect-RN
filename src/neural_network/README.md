# 🧠 Modul Rețea Neuronală (Neural Network)

Acest director conține logica de definire, antrenare și inferență a Rețelei Neuronale Artificiale (RNA) utilizate pentru clasificarea logo-urilor auto.

## 1. Arhitectura Curentă

Modelul utilizat este de tip **Feed-Forward Multilayer Perceptron (MLP)**, complet conectat (Fully Connected). Această arhitectură a fost aleasă pentru echilibrul dintre viteza de inferență în LabVIEW și capacitatea de a învăța forme geometrice simple.

### Diagrama Straturilor:

1.  **Stratul de Intrare (Input Layer):**
    * **Dimensiune:** 784 neuroni.
    * **Explicație:** Corespunde imaginii de 28x28 pixeli linearizate (Flattened 1D array).
    * **Domeniu valori:** `[0, 1]` (Single Precision Float). Valoarea 1 reprezintă pixelul desenat (alb), 0 reprezintă fundalul (negru).

2.  **Straturi Ascunse (Hidden Layers):**
    * **Număr straturi:** 2.
    * **Funcție de Activare:** Sigmoid (pentru a introduce non-liniaritate și a menține valorile stabile între 0 și 1).
    * **Scop:** Extragerea trăsăturilor geometrice (linii, curbe, colțuri) din vectorul de pixeli.

3.  **Stratul de Ieșire (Output Layer):**
    * **Dimensiune:** 5 neuroni.
    * **Semnificație:** Fiecare neuron corespunde unei clase (Mărci Auto).
    * **Mapping Clase:**
        * Index 0: Audi
        * Index 1: BMW
        * Index 2: Hyundai
        * Index 3: Mercedes
        * Index 4: Renault
    * **Interpretare:** Neuronul cu valoarea (activarea) cea mai mare este considerat câștigător ("Winner takes all").

## 2. Implementare în LabVIEW

Logica este divizată în următoarele VI-uri (Virtual Instruments):

* **`Create NN.vi`**: Inițializează structura rețelei, alocă memoria pentru greutăți (weights) și bias-uri, și le randomizează inițial.
* **`invatare.vi` (Training Loop)**:
    * Încarcă fișierele binare `.bin` din `data/train`.
    * Execută algoritmul **Backpropagation** (Retropropagarea erorii).
    * Actualizează greutățile iterativ pentru a minimiza eroarea globală.
    * Salvează modelul antrenat în format `.nnet` .
* **`testare.vi` (Inference)**:
    * Încarcă modelul salvat.
    * Execută o propagare înainte (Forward Pass) pe o imagine nouă desenată de utilizator.
    * Returnează scorurile de încredere pentru fiecare clasă.

## 3. Hiperparametri de Antrenare

Configurația curentă pentru procesul de învățare:

* **Learning Rate (Rata de învățare):** 0.1 (Optimizat pentru stabilitate).
* **Momentum:** 0.8 (Pentru a accelera convergența și a evita minimele locale).
* **Epochs:** Configurat în interfața de antrenare (tipic 50-1000 iteratii).
* **Preprocesare Critică:** Inversarea culorilor (`1 - pixel`) este aplicată înainte de intrarea în rețea.

## 4. Formatul Modelului Salvat

Modelul este salvat într-un format proprietar/binar care conține:
1.  Topologia rețelei (număr straturi, număr neuroni).
2.  Matricele de greutăți (Weights) finale.
3.  Vectorii de bias.

Acest fișier este încărcat ulterior de modulul UI pentru a face predicții în timp real.
