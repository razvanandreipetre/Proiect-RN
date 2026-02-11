## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | Petre Razvan-Andrei |
| **Grupa / Specializare** | [633AB / Informatică Industrială] |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | [https://github.com/razvanandreipetre/Proiect-RN] |
| **Acces Repository** | [Public] |
| **Stack Tehnologic** | [LabVIEW] |
| **Domeniul Industrial de Interes (DII)** | [ Automotive] |
| **Tip Rețea Neuronală** | [MLP] |

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 6 | Rezultat Final | Îmbunătățire | Status |
|--------|--------------|------------------|----------------|--------------|--------|
| Accuracy (Test Set) | ≥70% | [20%] | [24%] | [+24%] | [✗] |
| F1-Score (Macro) | ≥0.65 | [0.06] | [0.41] | [+0.35] | [✗] |
| Latență Inferență | [<50 ms] | [25 ms] | [18 ms] | [-7 ms] | [✓] |
| Contribuție Date Originale | ≥40% | [41%] | [68%] | - | [✓] |
| Nr. Experimente Optimizare | ≥4 | [3] | [5] | - | [✓] |

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [X] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [X] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [X] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [X] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [X] DA     |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.

---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

Programul dezvoltat se incadreaza in DII-ul de Automotive,deoarece prezinta o problema intalnita de persoane.Ca de exemplu,intr-ul loc de parcare,cand o masina intra in parcare,poate sa aiba defecte ale logo-ului/marcii.Utilizatorul,prin desenare,incearca sa deseneze logo-ul,iar programul prezice marca masinii daca trece de un prag de 70%.

### 2.2 Beneficii Măsurabile Urmărite

1. Reducerea timpului de detectie a logo-ului cu 50%
2. Detectarea logo-ului care se aseamana minim 70%
3. Reducerea timpului de recunoastere
4. Costul redus al programului

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
|---------------------------|--------------------------|--------------------------------|----------------------|
| Identificarea mașinilor cu logo-uri deteriorate sau ilizibile | Identificarea mașinilor cu logo-uri deteriorate sau ilizibile | Rețea Neuronală MLP (2HL) | Prag de predictibilitate > 70% |
| Eliminarea căutării manuale a mărcii în baze de date text | Recunoașterea automată a tiparului vizual din desen | Modul Invațare/Testare (.nnet) | < 1s timp de recunoaștere |
| Reducerea erorilor de înregistrare a vehiculelor în parcare | Reducerea erorilor de înregistrare a vehiculelor în parcare | Interfață UI (Drawing Canvas + Inference) | Reducerea timpului de inspecție cu 50% |

---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
|----------------|---------|
| **Origine date** | Dataset colectat manual |
| **Sursa concretă** | Google images |
| **Număr total observații finale (N)** | 48 |
| **Număr features** | 784(28x28) |
| **Tipuri de date** | Imagini |
| **Format fișiere** | PNG |
| **Perioada colectării/generării** | Noiembrie 2025 |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
|------|---------|
| **Total observații finale (N)** | [150] |
| **Observații originale (M)** | [102] |
| **Procent contribuție originală** | [68%] |
| **Tip contribuție** | [Date sintetice] |
| **Locație cod generare** | `src/data_acquisition/[Desenarea si salvarea unei imagini.vi]` |
| **Locație date originale** | `data/generated/` |

**Descriere metodă generare/achiziție:**

Datele originale au fost generate cu ajutorul unui vi de desenare a logo-urilor in diferite pozitii,cu diferite marimi ale pen-ului.Ca si parametri am folosit Pen width intre 5 si 25,si Line type solid/dash.Pentru problema sunt relevante deoarece logo-urile au fost desenate de catre utilizator si reflecta o apropriere de adevar in momentul in care utilizatorul foloseste reteaua neuronala in DII.

### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | [105] |
| Validation | 13.3% | [20] |
| Test | 16.6% | [25] |

**Preprocesări aplicate:**
- Redimensionare 280x280 si scalare 28x28
- Normalizare [0,1]
- Toate imaginile sunt negru pe fundal alb

**Referințe fișiere:** `data/README.md`, `config/preprocessing_params.txt`,`src/preprocessing/Desenarea si salarea unei imagini.vi`

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|-------|------------|---------------------------|-----------------|
| **Data Logging / Acquisition** | [LabVIEW] | Citirea si salvarea datelor+Conversia imaginilor in array si generarea fisierului de tip .bin | `src/data_acquisition/image to array.vi`,`src/data_acquisition/citire salvare date.vi` |
| **Neural Network** | [LabVIEW] | [Antrenarea retelei de tip MLP si generarea modelului .nnet] | `src/neural_network/invatare.vi` |
| **Web Service / UI** | [Labview Front Panel] | [ Interfață desenare imagine + predicție] | `src/app/main.vi` |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.png` *(sau `state_machine_v2.png` dacă actualizată în Etapa 6)*

**Stări principale și descriere:**

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
|-------|-----------|------------------|-----------------|
| `IDLE` | Așteptare input utilizator | Start aplicație | Input primit |
| `LOAD_IMAGE` | Realizează achiziția imaginii brute dintr-o cameră/senzor sau prin încărcarea unui fișier PNG | Tranziția din starea IDLE prin comanda de start. | Finalizarea încărcării matricii de pixeli în memorie. |
| `VALIDATE_IMAGE` | Verifică dacă imaginea îndeplinește criteriile minime | Existenta datelor brute disponibile | Determinarea validitatii |
| `Preprocess` | Redimensionare 28x28 si normalizare [0,1] | Imagine valida | Vector pregatit |
| `RN_INFERENCE` | Încarcă modelul antrenat (fișierul .nnet) și realizează calculul de clasificare prin straturile de neuroni. | Incarcare vector preprocesat | Generare probabilitate |
| `DISPLAY_RESULT` | [Afisare rezultat] | Decizie luată | Confirmare user |
| `STOP` | Oprire program | Rezultat afisat | Inchidere aplicatie. |

**Justificare alegere arhitectură State Machine:**

Utilizarea unei mașini de stări este esențială pentru acest studiu de caz deoarece permite interacțiunea în timp real. În timp ce utilizatorul desenează, sistemul poate trece rapid prin stările de PREPROCESS și INFERENCE , oferind un feedback vizual instantaneu în starea DISPLAY_RESULT.



## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

Input Layer:784 neuroni
Hidden Layer 1:150 neuroni
Hidden Layer 2:50 neuroni
Output Layer:5 neuroni(numele claselor)

**Justificare alegere arhitectură:**

Am ales o arhitectură de tip MLP cu două straturi ascunse (150-50 neuroni) deoarece oferă un raport optim între complexitatea de calcul și capacitatea de învățare pentru un set de date de dimensiuni reduse.

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
|----------------|----------------|---------------------|
| Learning Rate | Standard | Valoare standard in LABVIEW |
| Batch Size | 8 | Valoare optima pentru setul redus de imagini |
| Epochs(max) | 50000 | Limita superioara pentru retea ca sa treaca prin toate imaginile |
| Error goal | 0.05 | Prag de oprire pentru o acuratete cat mai mare |
| Early Stopping | Max time:600s | Oprire de siguranta la 10 minute |

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
|------|----------------------------|----------|----------|----------------|------------|
| **Baseline** | Configurația din Etapa 5 | [0.20%] | [0.19] | [1 min] | Referință |
| Exp 1 | [Crestere valori straturi de neuroni] | [24%] | [0.24] | [30 sec] | Acuratete usor crescuta,timp redus |
| Exp 2 | [crestere max time] | [28%] | [0.26] | [5 min] | Scadere error trend |
| Exp 3 | Batch size micsorat la 8 | [32%] | [0.30] | [2 min] | Grafic stabil |
| Exp 4 | Inversare culori | [36%] | [0.32] | [10 min] | Logo-uri vazute mai bine |
| Exp 5 | [Configuratie schimbata(cea actuala)] | [44%] | [0.41] | [10 min] | Optimizarea maxima atinsa |
| **FINAL** | [Configurația aleasă] | **[44%]** | **[0.40]** | [10 min] | **Modelul folosit în producție** |

**Justificare alegere model final:**

Configuratia straturilor de neuroni pe cele 2 straturi(150-50)este cea mai optima pentru reteaua reuronala.Numarul de epoci maxime(50000) si timpul maxim(10 minute) ofera timp suficient pentru a invata cat mai mult.Scaderea batch size-ului la 8 previne oscilatiile violente ale graficului,iar error goal de 0.05 permite retelei sa invete cat mai mult pana cand scade de acea valoare.


**Referințe fișiere:** `results/model3.bin`, `models/model3.nnet`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
|--------|---------|--------------|--------|
| **Accuracy** | [44%] | ≥70% | [✗] |
| **F1-Score (Macro)** | [0.41] | ≥0.65 | [✗] |
| **Precision (Macro)** | [0.42] | - | - |
| **Recall (Macro)** | [0.39] | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
|--------|-------------------|---------------------|--------------|
| Accuracy | [20%] | [44%] | [+24%] |
| F1-Score | [0.06] | [0.41] | [+0.35] |

**Referință fișier:** `results/metrici.png`,`src/generare metrici.vi`

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimizat.csv`

**Interpretare:**

| Aspect | Observație |
|--------|------------|
| **Clasa cu cea mai bună performanță** | [BMW] - Atinge un recall de 100% |
| **Clasa cu cea mai slabă performanță** | [Audi,Hyundai] - Recall [20%] |
| **Confuzii frecvente** | [Majoritatea claselor (Audi, Hyundai, Mercedes) sunt confundate frecvent cu BMW. Acest lucru se datorează probabil faptului că logo-ul BMW (un cerc cu secțiuni interioare) conține trăsături geometrice regăsite parțial și în celelalte logo-uri circulare] |
| **Dezechilibru clase** | [Deși numărul de mostre per clasă în setul de test este echilibrat (5 mostre/clasă), rețeaua prezintă o predispoziție către clasa BMW, sugerând că ponderile au fost optimizate excesiv pentru trăsăturile acestei mărci în timpul antrenării.] |

### 6.3 Analiza Top 5 Erori

| # | Input (descriere scurtă) | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Industrială |
|---|--------------------------|--------------|-------------|-----------------|------------------------|
| 1 | [Logo Audi] | [BMW] | [Audi] | [Rezoluția de 28x28 pixeli face ca inelele suprapuse să fie văzute de MLP ca o masă circulară centrală similară cu BMW] | [Înregistrarea eronată a mărcii în baza de date a parcării; necesită intervenție manuală.] |
| 2 | [Logo Hyundai] | [BMW] | [Hyundai] | [Predispoziția (bias) rețelei către clasa BMW (care are recall 100%) și similaritatea conturului exterior oval/circular.] | [Monitorizarea defectuoasă a fluxului de vehicule; alerte false pentru personalul de pază.] |
| 3 | [Logo Renault] | [Hyundai] | [Renault] | [Ambele logo-uri se bazează pe linii oblice/înclinate; MLP-ul nu distinge unghiurile specifice la rezoluție mică.] | [Scăderea încrederii operatorului în sistemul de asistență inteligent (SIA).] |
| 4 | [Logo Mercedes] | [BMW] | [Mercedes] | [Scăderea încrederii operatorului în sistemul de asistență inteligent (SIA).] | [Erori în procesul de sortare automată a vehiculelor în centrele logistice.] |
| 5 | [Schita Renault] | [Mercedes] | [Renault] | [Confuzia de linii oblice ale Renault confundate cu Y intors ale Mercedes-uui] | [Scăderea încrederii operatorului în sistemul de asistență inteligent (SIA).] |

### 6.4 Validare în Context Industrial

**Ce înseamnă rezultatele pentru aplicația reală:**

Acuratețea de 44% obținută  indică faptul că sistemul funcționează momentan ca un prototip de tip „Proof of Concept”, nu ca o soluție gata de producție. Într-un scenariu real de parcare, din 100 de vehicule cu logo-uri ilizibile pe care operatorul le schițează, modelul va identifica marca corectă pentru doar 44 dintre acestea. Restul de 56 de vehicule vor fi clasificate eronat (majoritatea fiind etichetate ca „BMW” din cauza bias-ului detectat în matricea de confuzie ), generând date incorecte în sistemul de monitorizare a traficului. Dacă estimăm că o căutare manuală a mărcii durează 2 minute, sistemul economisește 88 de minute de muncă, dar impune un timp suplimentar de corecție pentru cele 56 de erori, ceea ce confirmă necesitatea optimizării înainte de implementarea pe scară largă

**Pragul de acceptabilitate pentru domeniu:** [Acuratețe ≥70% pentru sisteme de asistență a operatorului uman.]  
**Status:** [Neatins (Diferență de −26% față de pragul minim).]  
**Plan de îmbunătățire (dacă neatins):** [Extinderea Dataset-ului: Creșterea numărului de observații de la $48$ la minim $500$ de imagini/schițe pentru a echilibra ponderile rețelei și a elimina „atracția” eronată către clasa BMW.
2.Data Augmentation: Generarea automată de variante ale schițelor (rotiri, translații, variații de grosime a liniilor) pentru a crește robustețea rețelei MLP.3.Optimizarea Arhitecturii: Testarea unei structuri cu 3 straturi ascunse sau trecerea la un model CNN (Convolutional Neural Network) dacă resursele hardware permit, pentru o mai bună capturare a trăsăturilor spațiale ale logo-urilor circulare.1.]

---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6

| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
|------------|---------------|-------------------|-------------|
| **Model încărcat** | `datatrain.nnet` | `model3.nnet` | [+24% accuracy] |
| **Threshold decizie** | [0.5 default] | [0.7] | [Minimizarea rezultatelor incerte; sistemul afișează marca doar dacă probabilitatea depășește 70%.] |
| **UI - feedback vizual** | [DA] | [ex: Bară precizie %] | [Informare operator pentru decizii] |
| **Logging** | [Doar predicție] | [Predicție + confidence] | [Ofera utilizatorului predictia daca depaseste pragul] |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

Screenshot-ul reprezinta interfata utilizatorului.Acesta deseneaza logo-ul,iar in dreapta,daca trece de pragul de 0.70 afiseaza rezultatul,daca nu,este afisat mesajul "Necunoscut.In chenarul de jos sunt clasele si scorul lor de predictie.

### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/interfata_test.mp4` *(GIF / Video / Secvență screenshots)*

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | [Utilizatorul deseneaza logo-ul cu mouse-ul in fereastra Picture] |
| 2 | Procesare | [Imagine redimensionata 28x28 si culorile inversate] |
| 3 | Inferență | [Programul calculeaza probabilitatile pentru cele 5 clase] |
| 4 | Decizie | [Daca scorul este sub 0.70,se afiseaza mesajul "Necunoscut"] |

**Latență măsurată end-to-end:** [aprox 200] ms  
**Data și ora demonstrației:** [11.02.2026, 16:44]

---

## 8. Structura Repository-ului Final

```
proiect-rn-[nume-prenume]/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── untrained_model.h5                  # Model schelet neantrenat (Etapa 4)
│   ├── trained_model.h5                    # Model antrenat baseline (Etapa 5)
│   ├── optimized_model.h5                  # Model FINAL optimizat (Etapa 6) ← FOLOSIT
│   └── final_model.onnx                    # (opțional) Export ONNX pentru deployment
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/citire salvare date.vi` | - | ✓ Creat | - | - |
| `src/neural_network/invatare.vi`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/generare metrici.vi`| - | - | - | ✓ Creat |
| `src/app/main.vi` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | - | - | - |
| `models/datatrain.nnet` | - | - | ✓ Creat | - |
| `models/model3.nnet` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimizat.csv` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/datatrain.bin` | - | - | ✓ Creat | - |
| `results/model3.bin` | - | - | - | ✓ Creat |
| `results/metrici.png` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python >= 3.8 (recomandat 3.10+)
pip >= 21.0
[sau LabVIEW >= 2020 pentru proiecte LabVIEW]
```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [URL_REPOSITORY]
cd proiect-rn-[nume-prenume]

# 2. Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# sau: venv\Scripts\activate    # Windows

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesare date (dacă rulați de la zero)
python src/preprocessing/data_cleaner.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Pasul 2: Antrenare model (pentru reproducere rezultate)
python src/neural_network/train.py --config config/optimized_config.yaml

# Pasul 3: Evaluare model pe test set
python src/neural_network/evaluate.py --model models/optimized_model.h5

# Pasul 4: Lansare aplicație UI
streamlit run src/app/main.py
# sau: python src/app/main.py (pentru Flask/FastAPI)
# sau: [instrucțiuni LabVIEW dacă aplicabil]
```

### 9.4 Verificare Rapidă 

```bash
# Verificare că modelul se încarcă corect
python -c "from src.neural_network.model import load_model; m = load_model('models/optimized_model.h5'); print('✓ Model încărcat cu succes')"

# Verificare inferență pe un exemplu
python src/neural_network/evaluate.py --model models/optimized_model.h5 --quick-test
```

### 9.5 Structură Comenzi LabVIEW (dacă aplicabil)

```
[Completați dacă proiectul folosește LabVIEW]
1. Deschideți [nume_proiect].lvproj
2. Rulați Main.vi
3. ...
```

---

## 10. Concluzii și Discuții

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
|--------------------------------|--------|----------|--------|
| [Reducerea timpului de detectie] | [50%] | [90%] | [✓] |
| [Timp de raspuns] | [<1 secunda] | [aprox. 200 ms] | [✓] |
| Accuracy pe test set | ≥70% | [44%] | [✗] |
| F1-Score pe test set | ≥0.65 | [0.41] | [✗] |
| [Cost implementare] | [Redus] | [Minim] | [✓] |

### 10.2 Ce NU Funcționează – Limitări Cunoscute

*[Fiți onești - evaluatorul apreciază identificarea clară a limitărilor]*

1. **Acuratete si F1 score redus** [Modelul nu a invatat corespunzator setul de date]
2. **Dataset mic** [Putine exemple]
3. **Confuzie intre clase** [Datorita acuratetii mici,se produc confuzii intre clase]
4. **Funcționalități planificate dar neimplementate:** [-]

### 10.3 Lecții Învățate (Top 5)

1. **[Lecție 1]:** [Datele insuficiente-retelele neuronale necesita sute de exemple per clasa,rezultand overfitting pe o clasa.]
2. **[Lecție 2]:** [Micsorarea imaginilor-imagini foarte mici si inghesuite->confuzie de clase]
3. **[Lecție 3]:** [Acuratete scazuta-erori in cod]
4. **[Lecție 4]:** [Threshold-ul mare pentru recunoasterea claselor(<0.70)]
5. **[Lecție 5]:** [De fiecare data am schimbat setarile,rezultand la rezultate diferite]

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**

As reincepe proiectul in Python,deoarece in Labview nu am reusit sa il implementez la target-ul impus din cauza complexitatii programului.Apoi as mari setul de date considerabil si as dedica timp foarte mult pentru antrenarea retelei.

### 10.5 Direcții de Dezvoltare Ulterioară

| Termen | Îmbunătățire Propusă | Beneficiu Estimat |
|--------|---------------------|-------------------|
| **Short-term** (1-2 săptămâni) | [Colectare date] | [Marirea datelor per clasa considerabil] |
| **Medium-term** (1-2 luni) | [Timp acordat antrenarii retelei] | [Antrenare extinsa peste 12 ore] |
| **Long-term** | [Finisarea si optimizarea programului] | [Functionalitate perfecta] |

---

## 11. Bibliografie

*[Minimum 3 surse cu DOI/link funcțional - format: Autor, Titlu, Anul, Link]*

1. [Abaza,B.], [Curs5_RN], [2025]. DOI: [link] sau URL: [link]
2. [Abaza,B.], [Laborator5_RN], [2025]. DOI: [link] sau URL: [link]
3. [Tarabuta,P.], [Hand-written digit recognition using an artificial neural network (ANN) and LabVIEW image processing], [2015]. DOI: [link] sau URL: [[link](https://forums.ni.com/t5/Student-Projects/Hand-written-digit-recognition-using-an-artificial-neural/ta-p/3513227)]
4. [Surse suplimentare dacă este cazul]

**Exemple format:**
- Abaza, B., 2025. AI-Driven Dynamic Covariance for ROS 2 Mobile Robot Localization. Sensors, 25, 3026. https://doi.org/10.3390/s25103026
- Keras Documentation, 2024. Getting Started Guide. https://keras.io/getting_started/

---

## 12. Checklist Final (Auto-verificare înainte de predare)

### Cerințe Tehnice Obligatorii

- [X] **Accuracy ≥70%** pe test set (verificat în `results/metrici.png`)
- [X] **F1-Score ≥0.65** pe test set
- [✓] **Contribuție ≥40% date originale** (verificabil în `data/generated/`)
- [✓] **Model antrenat de la zero** (NU pre-trained fine-tuning)
- [✓] **Minimum 4 experimente** de optimizare documentate (tabel în Secțiunea 5.3)
- [✓] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [✓] **State Machine** definit cu minimum 4-6 stări (Secțiunea 4.2)
- [✓] **Cele 3 module funcționale:** Data Logging, RN, UI (Secțiunea 4.1)
- [✓] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [✓] **README.md** complet (toate secțiunile completate cu date reale)
- [✓] **4 README-uri etape** prezente în `docs/` (etapa3, etapa4, etapa5, etapa6)
- [✓] **Screenshots** prezente în `docs/screenshots/`
- [✓] **Structura repository** conformă cu Secțiunea 8
- [X] **requirements.txt** actualizat și funcțional
- [X] **Cod comentat** (minim 15% linii comentarii relevante)
- [X] **Toate path-urile relative** (nu absolute: `/Users/...` sau `C:\...`)

### Acces și Versionare

- [✓] **Repository accesibil** cadrelor didactice RN (public sau privat cu acces)
- [X] **Tag `v0.6-optimized-final`** creat și pushed
- [X] **Commit-uri incrementale** vizibile în `git log` (nu 1 commit gigantic)
- [✓] **Fișiere mari** (>100MB) excluse sau în `.gitignore`

### Verificare Anti-Plagiat

- [✓] Model antrenat **de la zero** (weights inițializate random, nu descărcate)
- [✓] **Minimum 40% date originale** (nu doar subset din dataset public)
- [✓] Cod propriu sau clar atribuit (surse citate în Bibliografie)

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [DD.MM.YYYY]  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
