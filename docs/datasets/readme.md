
##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Senzori
* **Modul de achiziție:** ✓ Senzori reali / ☐ Simulare / ☐ Fișier extern / ☐ Generare programatică
* **Perioada / condițiile colectării:** Noiembrie 2025

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 50
* **Număr de caracteristici (features):** 1
* **Tipuri de date:** ☐ Numerice / ☐ Categoriale / ☐ Temporale / ✓ Imagini
* **Format fișiere:** ☐ CSV / ☐ TXT / ☐ JSON / ✓ PNG / ☐ Altele: [...]

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
|-------------------|---------|-------------|---------------|--------------------|
| imagine logo | imagini | px | imagini logo-uri | 280x280(sau rezolutia initiala) |
| Clase | Categorii |  | marca de masina | Audi,BMW,Mercedes,Renault,Hyundai |

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

* 5 clase a cate 10 imagini fiecare
* Analiza dimensiunilor imaginii (Verificare uniformitate).

### 3.2 Analiza calității datelor

* Identificarea siglelor care seamana foarte mult
* Dectectarea imaginilor cu rezolutie diferita sau fundal diferit

### 3.3 Probleme identificate

* Dimensiuni initiale diferite


---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* Fiecare imagine a fost redimensionata ca sa aiba 28x28 pixeli pentru a putea fi trecuta mult mai usor in program.Am folosit functiile IMAQ Create,IMAQ Resample si IMAQ ImageToArray.

### 4.2 Transformarea caracteristicilor

* Normalizarea valorilor pixelilor: Scalarea valorilor pixelilor din intervalul [0,255] în intervalul [0,1], împărțind la 255.


### 4.3 Structurarea seturilor de date

* 70–80% – train
* 10–15% – validation
* 10–15% – test

**Principii respectate:**
* Stratificare pentru clasificare
* Fără scurgere de informație (data leakage)
* Statistici calculate DOAR pe train și aplicate pe celelalte seturi

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train/val/test în foldere dedicate
* Parametrii de preprocesare în `config/preprocessing_config.*` (opțional)

---

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & transformate
* `data/train/`, `data/validation/`, `data/test/` – seturi finale
* `src/preprocessing/` – codul de preprocesare
* `data/README.md` – descrierea dataset-ului

---

##  6. Stare Etapă (de completat de student)

- [✓] Structură repository configurată
- [✓] Dataset analizat (EDA realizată)
- [✓] Date preprocesate
- [ ] Seturi train/val/test generate
- [✓] Documentație actualizată în README + `data/README.md`
