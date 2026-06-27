import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score, precision_score
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("🚀 TRAINING MODEL PREDIKSI JLPT N4 - 10.000 DATA")
print("   dengan 5 Skenario Split Data")
print("=" * 70)

# ============================================
# LOAD DATA DARI FILE CSV (10.000 RESPONDEN)
# ============================================
print("\n📊 Memuat dataset dari file...")

try:
    df = pd.read_csv('dataset_jlpt_10000.csv')
    print(f"✅ Berhasil memuat data: {len(df)} responden")
    print(f"   Kolom: {list(df.columns)}")
    print(f"   Status Siap: {(df['status'] == 'Siap').sum()}")
    print(f"   Status Belum Siap: {(df['status'] == 'Belum Siap').sum()}")
except FileNotFoundError:
    print("\n❌ File 'dataset_jlpt_10000.csv' tidak ditemukan!")
    print("   Jalankan generate_dataset.py terlebih dahulu.")
    exit()

# ============================================
# PREPARE DATA
# ============================================
X = df[['kanji', 'kosakata', 'grammar', 'reading']]
y = df['status'].map({'Siap': 1, 'Belum Siap': 0})

# ============================================
# SKENARIO SPLIT DATA
# ============================================
split_scenarios = {
    '90/10': {'test_size': 0.10, 'train_size': 0.90},
    '80/20': {'test_size': 0.20, 'train_size': 0.80},
    '70/30': {'test_size': 0.30, 'train_size': 0.70},
    '60/40': {'test_size': 0.40, 'train_size': 0.60},
    '50/50': {'test_size': 0.50, 'train_size': 0.50},
}

# Model yang akan diuji
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=6),
    'Random Forest': RandomForestClassifier(n_estimators=200, random_state=42, max_depth=8)
}

# ============================================
# SIMPAN HASIL SEMUA SKENARIO
# ============================================
all_results = []

print("\n" + "=" * 70)
print("📊 HASIL TRAINING SEMUA SKENARIO")
print("=" * 70)

best_overall = None
best_overall_score = 0
best_overall_scenario = ""
best_overall_model = ""

for scenario_name, split_config in split_scenarios.items():
    print("\n" + "=" * 70)
    print(f"📌 SKENARIO {scenario_name} (Train: {split_config['train_size']*100:.0f}% / Test: {split_config['test_size']*100:.0f}%)")
    print("=" * 70)
    
    # Split data sesuai skenario
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=split_config['test_size'], random_state=42, stratify=y
    )
    
    print(f"\n   Training: {len(X_train)} responden")
    print(f"   Testing: {len(X_test)} responden")
    
    scenario_results = []
    
    for model_name, model in models.items():
        print(f"\n   🤖 Training {model_name}...")
        
        # Training
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        # Metrics
        akurasi = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        
        # Cross validation
        cv_scores = cross_val_score(model, X, y, cv=5)
        
        print(f"      ✅ Akurasi: {akurasi * 100:.2f}%")
        print(f"      ✅ F1-Score: {f1:.4f}")
        print(f"      ✅ Recall: {recall:.4f}")
        print(f"      ✅ Precision: {precision:.4f}")
        print(f"      ✅ Cross-val: {cv_scores.mean() * 100:.2f}% (+/- {cv_scores.std() * 100:.2f}%)")
        
        # Simpan hasil
        result = {
            'scenario': scenario_name,
            'train_size': split_config['train_size'],
            'test_size': split_config['test_size'],
            'model': model_name,
            'akurasi': akurasi,
            'f1_score': f1,
            'recall': recall,
            'precision': precision,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std()
        }
        scenario_results.append(result)
        all_results.append(result)
        
        # Cek model terbaik overall
        if f1 > best_overall_score:
            best_overall_score = f1
            best_overall = model
            best_overall_model = model_name
            best_overall_scenario = scenario_name
    
    # Tampilkan ringkasan skenario
    print(f"\n   📊 RINGKASAN SKENARIO {scenario_name}:")
    print("   " + "-" * 50)
    for r in scenario_results:
        print(f"   {r['model']}: Akurasi={r['akurasi']*100:.2f}%, F1={r['f1_score']:.4f}, Recall={r['recall']:.4f}")

# ============================================
# SIMPAN MODEL TERBAIK
# ============================================
print("\n" + "=" * 70)
print("🏆 MODEL TERBAIK KESELURUHAN")
print("=" * 70)
print(f"\n   Model: {best_overall_model}")
print(f"   Skenario: {best_overall_scenario}")
print(f"   F1-Score: {best_overall_score:.4f}")

joblib.dump(best_overall, 'model_jlpt.pkl')
print("\n✅ Model terbaik tersimpan sebagai 'model_jlpt.pkl'")

# ============================================
# TABEL PERBANDINGAN SEMUA SKENARIO
# ============================================
print("\n" + "=" * 70)
print("📊 TABEL PERBANDINGAN SEMUA SKENARIO")
print("=" * 70)

# Buat DataFrame untuk perbandingan
df_results = pd.DataFrame(all_results)

# Pivot table untuk perbandingan per model
pivot_akurasi = df_results.pivot(index='scenario', columns='model', values='akurasi')
pivot_f1 = df_results.pivot(index='scenario', columns='model', values='f1_score')
pivot_recall = df_results.pivot(index='scenario', columns='model', values='recall')
pivot_precision = df_results.pivot(index='scenario', columns='model', values='precision')

print("\n📊 Perbandingan Akurasi (%):")
print(pivot_akurasi.round(4) * 100)

print("\n📊 Perbandingan F1-Score:")
print(pivot_f1.round(4))

print("\n📊 Perbandingan Recall:")
print(pivot_recall.round(4))

print("\n📊 Perbandingan Precision:")
print(pivot_precision.round(4))

# ============================================
# REKOMENDASI SKENARIO TERBAIK
# ============================================
print("\n" + "=" * 70)
print("💡 REKOMENDASI")
print("=" * 70)

# Cari skenario terbaik untuk setiap model
for model_name in models.keys():
    model_data = df_results[df_results['model'] == model_name]
    best_scenario = model_data.loc[model_data['f1_score'].idxmax()]
    print(f"\n   📌 {model_name}:")
    print(f"      Skenario terbaik: {best_scenario['scenario']}")
    print(f"      F1-Score: {best_scenario['f1_score']:.4f}")
    print(f"      Akurasi: {best_scenario['akurasi']*100:.2f}%")
    print(f"      Recall: {best_scenario['recall']:.4f}")
    print(f"      Precision: {best_scenario['precision']:.4f}")

# ============================================
# TEST PREDIKSI DENGAN MODEL TERBAIK
# ============================================
print("\n" + "=" * 70)
print("🔮 TEST PREDIKSI DENGAN MODEL TERBAIK")
print("=" * 70)

test_cases = [
    [85, 80, 75, 82],  # Skor tinggi → Siap
    [45, 50, 40, 48],  # Skor rendah → Belum
    [70, 65, 55, 60],  # Skor sedang → Siap
    [60, 60, 60, 60],  # Skor batas (total 72) → Siap
    [30, 30, 30, 30],  # Skor sangat rendah (total 36) → Belum
    [90, 85, 70, 65],  # Kanji tinggi, reading rendah
    [55, 50, 60, 65],  # Grammar & reading tinggi
    [40, 45, 50, 55],  # Semua sedang rendah
]

print("\n   Hasil Prediksi:")
print("   " + "-" * 60)
for test in test_cases:
    pred = best_overall.predict([test])[0]
    total_poin = sum(test) * 0.3
    hasil = "✅ SIAP" if pred == 1 else "❌ BELUM SIAP"
    print(f"   {test} → {hasil} (Total: {total_poin:.0f} poin)")

print("\n" + "=" * 70)
print("🎉 TRAINING SELESAI!")
print("=" * 70)

# ============================================
# SIMPAN HASIL KE FILE CSV
# ============================================
df_results.to_csv('hasil_training_all_scenarios.csv', index=False)
print("\n📊 Hasil training tersimpan sebagai 'hasil_training_all_scenarios.csv'")