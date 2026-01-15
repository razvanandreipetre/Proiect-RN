# 🖥️ Modul Interfață Utilizator (UI Application)

Acest director conține punctul de intrare (Entry Point) al aplicației SIA. Interfața grafică permite utilizatorului să interacționeze cu Rețeaua Neuronală în timp real.

## 1. Fișierul Principal

* **Nume fișier:** `testare.vi`
* **Locație:**  `src/app/` .
* **Dependențe:** Necesită ca `procesare imagine.vi` și `citire salvare date.vi` să fie accesibile în ierarhia proiectului.

## 2. Instrucțiuni de Lansare (Launch Commands)

Deoarece aplicația este dezvoltată în mediul LabVIEW, lansarea se face urmând acești pași stricți:

### Pasul 1: Deschiderea Proiectului
1.  Navigați în directorul rădăcină al repository-ului.
2.  Deschideți fișierul principal: **`testare.vi`**.

### Pasul 2: Rularea Aplicației
1.  Pe Panoul Frontal al `testare.vi`, localizați bara de instrumente superioară.
2.  Apăsați butonul **Run** (Săgeata Albă) sau folosiți scurtătura tastaturii: `Ctrl + R`.

### Pasul 3: Utilizare
1.  **Desenare:** Folosiți mouse-ul pentru a desena un logo în zona albă "Picture".
    * *Audi:* 4 cercuri.
    * *BMW:* Cerc cu cruce.
    * *Hyundai:* Oval cu H.
    * *Mercedes:* Cerc cu 3 linii (Y inversat).
    * *Renault:* Romb.
2.  **Inference:** Clasificarea se face automat (în timp real) sau la apăsarea butonului, în funcție de configurație.
3.  **Rezultat:** Priviți indicatorul "Rezultat" și imaginea de referință afișată în dreapta.
4.  **Reset:** Apăsați butonul "Refresh" (dacă este disponibil) sau desenați peste pentru a începe o nouă inferență.

## 3. Configurare Interfață

Pentru rezultate optime, asigurați-vă că pe Panoul Frontal sunt setate următoarele valori înainte de rulare:
* **Pen Width:** 4-6 (pentru o grosime a liniei optimă).
* **Pen Style:** Solid.
* **Calea Modelului:** Asigurați-vă că controlul de cale (Path Control) din stânga sus indică corect către fișierul `.nnet` sau folderul de date antrenate.

## 4. Troubleshooting (Depanare)

* **Eroare "SubVI missing":** Asigurați-vă că nu ați mutat fișierele `src/preprocessing/procesare imagine.vi` sau `src/neural_network/citire salvare date.vi` din locurile lor originale.
* **Rezultat "Necunoscut" constant:** Verificați dacă ați desenat suficient de mare și central. Verificați graficul "image 28x28" pentru a vedea dacă desenul este capturat corect (Alb pe fundal Negru).
