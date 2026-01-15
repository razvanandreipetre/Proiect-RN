# 📡 Modulul de Achiziție și Generare Date

Acest modul este responsabil pentru interfațarea cu utilizatorul și captarea datelor de intrare (schițe) în timp real, transformându-le în tensori compatibili cu Rețeaua Neuronală.

## 1. Metoda de Generare/Achiziție Explictă

Datele nu sunt importate din surse statice, ci sunt **generate dinamic** prin interacțiunea utilizatorului cu interfața grafică (GUI) dezvoltată în LabVIEW.

**Fluxul de achiziție:**
1.  **Captură Evenimente:** Se utilizează o structură de tip *Event Structure* care monitorizează evenimentele mouse-ului (`Mouse Down`, `Mouse Move`, `Mouse Up`) pe controlul *Picture*.
2.  **Rasterizare Vectorială:** Coordonatele X/Y ale cursorului sunt transformate în timp real în linii grafice folosind funcțiile de desenare 2D din LabVIEW.
3.  **Conversie Bitmap:** La finalizarea desenului, imaginea din memoria controlului este extrasă și convertită într-o matrice de pixeli (Mapă de biți).
4.  **Salvare:** Imaginea brută este salvată în format `.png` în folderul `data/generated/` pentru a contribui la setul de date de antrenare.

## 2. Parametrii Folosiți

Deoarece achiziția este manuală (human-in-the-loop), parametrii sunt definiți de configurația interfeței de desen:

* **Senzor Virtual:** Mouse, Touchpad sau Stylus (în funcție de hardware-ul PC-ului).
* **Frecvența de Eșantionare:** Determinat de rata de refresh a Event Loop-ului (aprox. 10-20 ms per punct), suficient pentru a capta curbe fluide.
* **Rezoluție Spațială:**
    * *Canvas Desen:* 280x280 pixeli (pentru vizibilitate bună a utilizatorului).
    * *Output Final:* Downsampling la **28x28 pixeli** (pentru rețea).
* **Parametri "Pen" (Instrument de scris):**
    * *Width (Grosime):* Variabilă, setată experimental la **4-6 pixeli** (pentru a preveni întreruperile la redimensionare).
    * *Style:* Solid Line.
* **Zgomot (Noise):**
    * Nu se aplică zgomot electric (Gaussian).
    * **Zgomot inerent:** Variabilitatea biomecanică a utilizatorului (linii tremurate, cercuri imperfecte, centrări diferite). Acesta este un "feature" dorit, nu un bug.

## 3. Justificare Relevanță Date

Această metodă de achiziție este **critică** pentru succesul proiectului din următoarele motive:

1.  **Simulare Realistă:** Dacă am antrena rețeaua doar pe imagini perfecte de pe internet (logo-uri oficiale vectoriale), aceasta nu ar recunoaște niciodată o schiță făcută de mână ("Domain Gap"). Generând datele prin aceeași interfață prin care se va face testarea, garantăm că distribuția datelor de antrenare (`train`) este identică cu cea de testare (`test`).
2.  **Robustete:** Prin desenarea manuală a celor 40% din date, introducem imperfecțiuni naturale (unghiuri greșite, linii neînchise la Audi/BMW) care forțează rețeaua să învețe caracteristicile structurale profunde, nu doar să memoreze șabloane pixel-perfect.
3.  **Control Total:** Putem ajusta grosimea liniei și contrastul (Inversare Culori: Alb pe Negru) direct la sursă, eliminând nevoia unor algoritmi complecși de preprocesare ulterioară.
