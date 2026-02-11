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
| Recunoastere rapida a schitei unui logo | Clasificare imagine schita logo in sub o secunda | Modul RN |
| Validarea calitatii desenului de intrare | Detectarea imaginilor neclare înainte de clasificare | Modul achiziție |
| Instruirea persoanelor in viziune artificiala | Demonstratie LABVIEW de a clasifica imagini | Interfață utilizator |

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

### Contribuția originală la setul de date:

**Total observații finale:** N=85 imagini
**Observații originale:** M=35(41,18%)

**Tipul contribuției:**
[ ] Date generate prin simulare fizică  
[x] Date achiziționate cu senzori proprii  
[x] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Datele au fost generate cu ajutorul VI-ului din data/generated prin desen si reprezinta 41,18% din totalul de date care trebuiesc preprocesate.

**Locația codului:** `data/generated`
**Locația datelor:** `data/raw`

---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)


### Justificarea State Machine-ului ales:

Am ales arhitectura de Clasificare Imagini deoarece proiectul se bazeaza pe o intrare discreta de date(imagini neprocesate).Obiectivul este de a recunoaste cat mai precis un logo la desenarea acestuia de catre utilizator.

### Stările principale sunt:
  1.**IDLE**: Sistemul așteaptă o acțiune a utilizatorului.
  2.**LOAD_IMAGE**: Achiziționează imaginea  (fie dintr-o cameră/senzor, fie dintr-un fișier local PNG).
  3.**VALIDATE_IMAGE**: Verifică calitatea minimă a imaginii (ex: rezoluție, prezența elementelor).
  4.**PREPROCESS**: Aplică transformările necesare (Redimensionare la 28×28 px, Normalizare [0,1]), pregătind tensorul de intrare.
  5.**RN_INFERENCE**: Încărcă modelul (VI-ul RN) și realizează clasificarea.
  6.**DISPLAY_RESULT**:In timpul desenului utilizatorului,programul afișează clasa prezisă (Marca auto) și acuratețea cea mai mare.
  7.**STOP**:Se opreste programul

### Tranzițiile critice sunt:
-**VALIDATE_IMAGE → ERROR_IMAGE_QUALITY:** Când imaginea nu trece de verificarea de calitate (ex: fundal neașteptat, imagine complet neagră).
-**ERROR_IMAGE_QUALITY → STOP:** După afișarea unui mesaj de eroare, sistemul trebuie să se opreasca.

Starea ERROR este esențială pentru că gestioneaza input-rile neconforme ale utilizatorului(imagine slab calitativa,fisiere corupte etc.).

---

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

Toate cele 3 module trebuie să **pornească și să ruleze fără erori** la predare. Nu trebuie să fie perfecte, dar trebuie să demonstreze că înțelegeți arhitectura.

| **Modul** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
|-----------|----------------------------------|-------------|----------------------------------------------|
| **1. Data Logging / Acquisition** | procesare imagini.vi + redimensionare imagini.vi | VI-ul de preprocesare ruleaza si redimensioneaza toate imaginile la o dimensiune de 28x28 pixeli |
| **2. Neural Network Module** | citire salvare date.vi + invatare.vi | Arhitectura RN este definita si compilata in LABVIEW. |
| **3. Web Service / UI** | testare.vi | Interfata porneste,primeste o imagine si afiseaza o clasificare. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [X] Cod rulează fără erori: redimensionare imagini.vi
- [X] Generează fișiere binare(.bin) în format compatibil cu preprocesarea din Etapa 3
- [X] Include minimum 40% date originale în dataset-ul final
- [X] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [X] Arhitectură RN definită și compilată fără erori
- [X] Model poate fi salvat și reîncărcat
- [X] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [X] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [X] Includeți un screenshot demonstrativ în `docs/screenshots/`

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [X] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [X] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [X] Cod generare/achiziție date funcțional și documentat
- [X] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [X] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [X] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [X] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [X] Cod rulează fără erori (redimensionare imagini.vi)
- [X] Produce minimum 40% date originale din dataset-ul final
- [X] Fisier binar(.bin) generat în format compatibil cu preprocesarea din Etapa 3
- [X] Documentație în `src/data_acquisition/README.md` cu:
  - [X] Metodă de generare/achiziție explicată
  - [X] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [X] Justificare relevanță date pentru problema voastră
- [X] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [X] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [X] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [X] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [X] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [X] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)

---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`

