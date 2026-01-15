import os
import shutil
import random
from pathlib import Path
from sklearn.model_selection import train_test_split

# --- CONFIGURARE ---
# Căile către foldere (relative la locul unde rulezi scriptul sau absolute)
RAW_COLLECTED_DIR = Path(r'C:\Users\razva\Desktop\PROIECT RN\Lab5\dataraw') 
RAW_GENERATED_DIR = Path(r'C:\Users\razva\Desktop\PROIECT RN\Lab5\datagenerat')
OUTPUT_BASE_DIR = Path('data')

# Proporții
TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

# Clasele tale (numele folderelor)
CLASSES = ['Audi', 'BMW', 'Mercedes', 'Renault', 'Hyundai']

def split_dataset():
    # 1. Curățăm folderele vechi de train/val/test pentru a nu amesteca datele
    for split in ['train', 'validation', 'test']:
        split_path = OUTPUT_BASE_DIR / split
        if split_path.exists():
            shutil.rmtree(split_path)
            print(f"Sters folder vechi: {split_path}")

    # 2. Iterăm prin fiecare clasă pentru a păstra stratificarea
    total_images_count = 0
    
    for class_name in CLASSES:
        # Colectăm toate imaginile pentru clasa curentă din ambele surse
        all_images = []
        
        # Din collected
        src_col = RAW_COLLECTED_DIR / class_name
        if src_col.exists():
            all_images.extend([p for p in src_col.glob('*') if p.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp']])
            
        # Din generated
        src_gen = RAW_GENERATED_DIR / class_name
        if src_gen.exists():
            all_images.extend([p for p in src_gen.glob('*') if p.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp']])

        print(f"Clasa {class_name}: {len(all_images)} imagini găsite.")
        
        if not all_images:
            print(f"ATENȚIE: Nu s-au găsit imagini pentru {class_name}!")
            continue

        # 3. Calculăm split-ul
        # Prima împărțire: Train vs (Val + Test)
        train_imgs, temp_imgs = train_test_split(
            all_images, 
            train_size=TRAIN_RATIO, 
            random_state=42, 
            shuffle=True
        )
        
        # A doua împărțire: Val vs Test (din ce a rămas)
        # Deoarece Val și Test sunt egale (15% fiecare), împărțim temp la jumătate (0.5)
        val_imgs, test_imgs = train_test_split(
            temp_imgs, 
            test_size=0.5, 
            random_state=42, 
            shuffle=True
        )

        # 4. Copiem fișierele în destinație
        splits = {
            'train': train_imgs,
            'validation': val_imgs,
            'test': test_imgs
        }

        for split_name, images in splits.items():
            dest_dir = OUTPUT_BASE_DIR / split_name / class_name
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            for img_path in images:
                shutil.copy(img_path, dest_dir / img_path.name)
        
        total_images_count += len(all_images)

    print("-" * 30)
    print(f"PROCES COMPLET. Total imagini procesate: {total_images_count}")
    print(f"Verifică folderele: {OUTPUT_BASE_DIR}/train, /validation, /test")

if __name__ == "__main__":
    # Verificăm dacă avem librăria sklearn instalată
    try:
        import sklearn
        split_dataset()
    except ImportError:
        print("Eroare: Nu ai instalat scikit-learn.")
        print("Instalează folosind comanda: pip install scikit-learn")