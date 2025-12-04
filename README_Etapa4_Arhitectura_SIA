# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Petre Razvan-Andrei 
**Link Repository GitHub:** https://github.com/razvanandreipetre/Proiect-RN
**Data:** 04.12.2025 
---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**



##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Recunoastere rapida a schitei unui logo | Clasificare imagine schita logo in sub o secunda | RN Module + UI |
| Validarea calitatii desenului de intrare | Detectarea imaginilor neclare cu >95% rata de validare | Data Acquisition+Preprocessing Module |
| Instruirea persoanelor in viziune artificiala | Demonstratie LABVIEW de a clasifica imagini | NN Module + UI |

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.

#### Tipuri de contribuții acceptate (exemple din inginerie):

Alegeți UNA sau MAI MULTE dintre variantele de mai jos și **demonstrați clar în repository**:

| **Tip contribuție** | **Exemple concrete din inginerie** | **Dovada minimă cerută** |
|---------------------|-------------------------------------|--------------------------|
| **Date generate prin simulare fizică** | • Traiectorii robot în Gazebo<br>• Vibrații motor cu zgomot aleator calibrat<br>• Consumuri energetice proces industrial simulat | Cod Python/LabVIEW funcțional + grafice comparative (simulat vs real din literatură) + justificare parametri |
| **Date achiziționate cu senzori proprii** | • 500-2000 măsurători accelerometru pe motor<br>• 100-1000 imagini capturate cu cameră montată pe robot<br>• 200-1000 semnale GPS/IMU de pe platformă mobilă<br>• Temperaturi/presiuni procesate din Arduino/ESP32 | Foto setup experimental + CSV-uri produse + descriere protocol achiziție (frecvență, durata, condiții) |
| **Etichetare/adnotare manuală** | • Etichetat manual 1000+ imagini defecte sudură<br>• Anotat 500+ secvențe video cu comportamente robot<br>• Clasificat manual 2000+ semnale vibrații (normal/anomalie)<br>• Marcat manual 1500+ puncte de interes în planuri tehnice | Fișier Excel/JSON cu labels + capturi ecran tool etichetare + log timestamp-uri lucru |
| **Date sintetice prin metode avansate** | • Simulări FEM/CFD pentru date dinamice proces | Cod implementare metodă + exemple before/after + justificare hiperparametri + validare pe subset real |

#### Declarație obligatorie în README:

Scrieți clar în acest README (Secțiunea 2):

### Contribuția originală la setul de date:

**Total observații finale:** N=50 imagini
**Observații originale:** M=50(100%)

**Tipul contribuției:**
[ ] Date generate prin simulare fizică  
[x] Date achiziționate cu senzori proprii  
[x] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Deși setul de date inițial este mic (50 de imagini PNG), contribuția originală constă în preprocesarea tuturor imaginilor in program prin redimensionare 28x28 pixeli.Aceste imagini au fost obținute prin descarcare de pe internet,apoi prin redimensionare de catre utilizator.

**Locația codului:** `data/processed`
**Locația datelor:** `data/raw`
```
**Dovezi:**
- Grafic comparativ: `docs/generated_vs_real.png`
- Setup experimental: `docs/acquisition_setup.jpg` (dacă aplicabil)
- Tabel statistici: `docs/data_statistics.csv`


#### Exemple pentru "contribuție originală":
-Simulări fizice realiste cu ecuații și parametri justificați  
-Date reale achiziționate cu senzori proprii (setup documentat)  
-Augmentări avansate cu justificare fizică (ex: simulare perspective camera industrială)  


#### Atenție - Ce NU este considerat "contribuție originală":

- Augmentări simple (rotații, flips, crop) pe date publice  
- Aplicare filtre standard (Gaussian blur, contrast) pe imagini publice  
- Normalizare/standardizare (aceasta e preprocesare, nu generare)  
- Subset dintr-un dataset public (ex: selectat 40% din ImageNet)
```

---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)


### Justificarea State Machine-ului ales:

Am ales arhitectura de Clasificare Imagini deoarece proiectul se bazeaza pe o intrare discreta de date(imagini neprocesate).Obiectivul este de a recunoaste cat mai precis un logo la desenarea acestuia de catre utilizator.

Stările principale sunt:
1.IDLE: Sistemul așteaptă o acțiune a utilizatorului.
2.LOAD_IMAGE: Achiziționează imaginea  (fie dintr-o cameră/senzor, fie dintr-un fișier local PNG).
3.VALIDATE_IMAGE: Verifică calitatea minimă a imaginii (ex: rezoluție, prezența elementelor).
4.PREPROCESS: Aplică transformările necesare (Redimensionare la 28×28 px, Normalizare [0,1]), pregătind tensorul de intrare.
5.RN_INFERENCE: Încărcă modelul (VI-ul RN) și realizează clasificarea.
6.DISPLAY_RESULT:In timpul desenului utilizatorului,programul afișează clasa prezisă (Marca auto) și probabilitatea.
7.STOP:Se opreste programul

Tranzițiile critice sunt:
-VALIDATE_IMAGE → ERROR_IMAGE_QUALITY: Când imaginea nu trece de verificarea de calitate (ex: fundal neașteptat, imagine complet neagră).
-ERROR_IMAGE_QUALITY → STOP: După afișarea unui mesaj de eroare, sistemul trebuie să se opreasca.

Starea ERROR este esențială pentru că gestioneaza input-rile neconforme ale utilizatorului(imagine slab calitativa,fisiere corupte etc.).

---

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

Toate cele 3 module trebuie să **pornească și să ruleze fără erori** la predare. Nu trebuie să fie perfecte, dar trebuie să demonstreze că înțelegeți arhitectura.

| **Modul** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
|-----------|----------------------------------|-------------|----------------------------------------------|
| **1. Data Logging / Acquisition** | Vi2.vi | VI-ul de preprocesare ruleaza si redimensioneaza toate imaginile la o dimensiune de 28x28 pixeli |
| **2. Neural Network Module** | Vi4.vi | Arhitectura RN este definita si compilata in LABVIEW. |
| **3. Web Service / UI** | Untitled1.vi | Interfata porneste,primeste o imagine si afiseaza o clasificare. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [X] Cod rulează fără erori: Vi2.vi
- [ ] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [X] Include minimum 40% date originale în dataset-ul final
- [X] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [X] Arhitectură RN definită și compilată fără erori
- [X] Model poate fi salvat și reîncărcat
- [ ] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [X] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [ ] Includeți un screenshot demonstrativ în `docs/screenshots/`

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [X] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [X] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [X] Cod generare/achiziție date funcțional și documentat
- [ ] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [X] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [X] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [ ] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [X] Cod rulează fără erori (Vi2.vi)
- [X] Produce minimum 40% date originale din dataset-ul final
- [ ] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [ ] Documentație în `src/data_acquisition/README.md` cu:
  - [ ] Metodă de generare/achiziție explicată
  - [ ] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [ ] Justificare relevanță date pentru problema voastră
- [ ] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [X] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [ ] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [X] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [ ] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [ ] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)

---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`

