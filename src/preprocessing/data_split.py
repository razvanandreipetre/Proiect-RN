import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

# --- CONFIGURARE ---

# Calea către folderul principal unde ai toate imaginile (dataupdate)
# Folosim r'' pentru a evita erorile de la backslash pe Windows
RAW_DATA_DIR = Path(r'C:\Users\razva\Desktop\PROIECT RN\dataupdate') 

# Folderul unde se va crea structura finală (train/val/test)
OUTPUT_BASE_DIR = Path('data')

# Proporții (70% Train, 15% Validation, 15% Test)
TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

# Clasele tale (trebuie să corespundă cu numele folderelor din dataupdate)
CLASSES = ['Audi', 'BMW', 'Mercedes', 'Renault', 'Hyundai']

def split_dataset():
    print(f"Sursă date: {RAW_DATA_DIR}")
    print(f"Destinație: {OUTPUT_BASE_DIR.absolute()}")
    print("-" * 30)

    # 1. Curățăm folderele vechi de train/val/test pentru a porni de la zero
    for split in ['train', 'validation', 'test']:
        split_path = OUTPUT_BASE_DIR / split
        if split_path.exists():
            shutil.rmtree(split_path)
            print(f" [INFO] Șters folder vechi: {split_path}")

    total_images_processed = 0
    
    # 2. Iterăm prin fiecare clasă
    for class_name in CLASSES:
        source_class_dir = RAW_DATA_DIR / class_name
        
        # Verificăm dacă folderul clasei există
        if not source_class_dir.exists():
            print(f" [!] ATENȚIE: Folderul sursă pentru '{class_name}' nu există la calea: {source_class_dir}")
            continue

        # Colectăm toate imaginile (ignoram case sensitivity la extensii)
        images = [
            p for p in source_class_dir.glob('*') 
            if p.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp']
        ]

        count = len(images)
        print(f"Clasa {class_name}: {count} imagini găsite.")
        
        if count == 0:
            continue

        # 3. Calculăm split-ul
        # Dacă ai foarte puține imagini (<3), train_test_split poate da eroare, așa că le punem toate la train
        if count < 3:
            train_imgs = images
            val_imgs = []
            test_imgs = []
            print(f"   -> Prea puține imagini pentru split. Toate mutate în TRAIN.")
        else:
            # Prima împărțire: Train vs (Restul = Val + Test)
            train_imgs, temp_imgs = train_test_split(
                images, 
                train_size=TRAIN_RATIO, 
                random_state=42, 
                shuffle=True
            )
            
            # A doua împărțire: Val vs Test (din restul de 30%)
            # Deoarece 15% este jumătate din 30%, facem split 0.5
            val_imgs, test_imgs = train_test_split(
                temp_imgs, 
                test_size=0.5, 
                random_state=42, 
                shuffle=True
            )

        # 4. Copiem fișierele în destinație
        splits_mapping = {
            'train': train_imgs,
            'validation': val_imgs,
            'test': test_imgs
        }

        for split_name, imgs_list in splits_mapping.items():
            dest_dir = OUTPUT_BASE_DIR / split_name / class_name
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            for img_path in imgs_list:
                try:
                    shutil.copy(img_path, dest_dir / img_path.name)
                except Exception as e:
                    print(f"Eroare la copiere {img_path.name}: {e}")
        
        total_images_processed += count

    print("-" * 30)
    print(f"PROCES COMPLET.")
    print(f"Total imagini procesate: {total_images_processed}")
    print(f"Structura a fost creată în folderul: {OUTPUT_BASE_DIR.absolute()}")

if __name__ == "__main__":
    try:
        import sklearn
        split_dataset()
    except ImportError:
        print("Eroare: Nu ai instalat librăria scikit-learn.")
        print("Instalează folosind comanda în terminal: pip install scikit-learn")