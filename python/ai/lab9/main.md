

# 1. Импорт библиотек

```python
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
    MinMaxScaler,
    RobustScaler
)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import label_binarize
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

from sklearn.metrics import RocCurveDisplay


df = pd.read_csv('dataSet.csv')

# Первые 5 строк
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df['performance_category'].value_counts())
sns.countplot(x='performance_category', data=df)
plt.title('Распределение целевой переменной')
plt.show()
plt.figure(figsize=(8,5))

sns.histplot(df['final_exam_score'], kde=True)

plt.title('Распределение итоговых оценок')
plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(x=df['study_hours_per_day'])

plt.title('Boxplot study_hours_per_day')
plt.show()
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

plt.figure(figsize=(18,10))

corr = df[numeric_cols].corr()

sns.heatmap(corr, cmap='coolwarm')

plt.title('Корреляционная матрица')
plt.show()
```

# 2. Генерация «грязных» данных

```python
df_dirty = df.copy()

np.random.seed(42)

missing_indices = np.random.choice(df_dirty.index, 100)

df_dirty.loc[missing_indices, 'sleep_hours'] = np.nan

duplicates = df_dirty.sample(20)

df_dirty = pd.concat([df_dirty, duplicates])

outlier_indices = np.random.choice(df_dirty.index, 20)

df_dirty.loc[outlier_indices, 'study_hours_per_day'] = 50

text_noise_indices = np.random.choice(df_dirty.index, 20)

for idx in text_noise_indices:
    df_dirty.loc[idx, 'gender'] = ' MAle '


plt.show()
```

# 3. Очистка данных

```python
def clean_data(df_clean):

    # Удаление дубликатов
    df_clean = df_clean.drop_duplicates()

    # Обработка пропусков
    numeric_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    # Очистка текстовых данных
    cat_cols = df_clean.select_dtypes(include=['object']).columns

    for col in cat_cols:
        df_clean[col] = df_clean[col].str.lower().str.strip()

    # Исправление ошибок
    corrections = {
        'male ': 'male',
        ' male': 'male',
        ' maLe ': 'male'
    }

    for col in cat_cols:
        df_clean[col] = df_clean[col].replace(corrections)

    # Обработка выбросов
    Q1 = df_clean['study_hours_per_day'].quantile(0.25)
    Q3 = df_clean['study_hours_per_day'].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df_clean = df_clean[
        (df_clean['study_hours_per_day'] >= lower) &
        (df_clean['study_hours_per_day'] <= upper)
    ]

    return df_clean
df_clean = clean_data(df_dirty)
print(df_clean.isnull().sum())
print(df_clean.duplicated().sum())
```

---

# 4. Feature Engineering
```python
df_clean['study_focus_ratio'] = (
    df_clean['study_hours_per_day'] *
    df_clean['focus_score']
)

df_clean['stress_sleep_ratio'] = (
    df_clean['stress_level'] /
    (df_clean['sleep_hours'] + 1)
)
df_clean['is_high_attendance'] = (
    df_clean['attendance_percentage'] > 85
).astype(int)
df_clean['social_vs_study'] = (
    df_clean['social_media_hours'] /
    (df_clean['study_hours_per_day'] + 1)
)
```

# 5. Подготовка данных
```python
label_encoders = {}

cat_cols = df_clean.select_dtypes(include=['object']).columns

for col in cat_cols:

    encoder = LabelEncoder()

    df_clean[col] = encoder.fit_transform(df_clean[col])

    label_encoders[col] = encoder
X = df_clean.drop('performance_category', axis=1)
y = df_clean['performance_category']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
standard_scaler = StandardScaler()

X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)
robust_scaler = RobustScaler()

X_train_robust = robust_scaler.fit_transform(X_train)
X_test_robust = robust_scaler.transform(X_test)
log_model = LogisticRegression(max_iter=1000)

log_model.fit(X_train_standard, y_train)
rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf_model.fit(X_train, y_train)
```


# 7. Оценка качества моделей


```python
y_pred_log = log_model.predict(X_test_standard)
print(classification_report(y_test, y_pred_log))

print('Accuracy:', accuracy_score(y_test, y_pred_log))
print('Precision:', precision_score(y_test, y_pred_log, average='weighted'))
print('Recall:', recall_score(y_test, y_pred_log, average='weighted'))
print('F1-score:', f1_score(y_test, y_pred_log, average='weighted'))

y_pred_rf = rf_model.predict(X_test)
print(classification_report(y_test, y_pred_rf))
print('Accuracy:', accuracy_score(y_test, y_pred_rf))
print('Precision:', precision_score(y_test, y_pred_rf, average='weighted'))
print('Recall:', recall_score(y_test, y_pred_rf, average='weighted'))
print('F1-score:', f1_score(y_test, y_pred_rf, average='weighted'))


classes = np.unique(y_test)

y_test_bin = label_binarize(y_test, classes=classes)
```
# 16. Прогнозирование
```python
new_students = pd.DataFrame({
    'student_id': [5001, 5002],
    'age': [20, 18],
    'gender': ['male', 'female'],
    'city_type': ['urban', 'rural'],
    'study_hours_per_day': [7, 2],
    'deep_work_sessions': [5, 1],
    'assignment_completion_rate': [90, 40],
    'attendance_percentage': [95, 60],
    'social_media_hours': [1, 6],
    'doomscrolling_before_sleep': [0, 1],
    'notification_distractions': [2, 8],
    'ai_tool_usage_hours': [2, 0.5],
    'gaming_hours': [1, 5],
    'stress_level': [3, 9],
    'motivation_level': [9, 3],
    'focus_score': [8, 2],
    'procrastination_index': [2, 9],
    'mental_state': ['good', 'bad'],
    'sleep_hours': [8, 4],
    'caffeine_intake': [1, 5],
    'physical_activity_hours': [2, 0],
    'internet_quality': [9, 4],
    'family_support': [9, 3],
    'financial_stress': [2, 8],
    'learning_style': ['visual', 'reading'],
    'career_goal': ['engineer', 'artist'],
    'productivity_after_midnight': [5, 2],
    'revision_efficiency': [9, 3],
    'burnout_risk': [2, 8],
    'consistency_score': [9, 2],
    'final_exam_score': [85, 40]
})
for col in cat_cols:
    new_students[col] = label_encoders[col].transform(new_students[col])
predictions = rf_model.predict(new_students)

print(predictions)