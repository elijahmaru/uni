import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_auc_score,
    roc_curve,
    classification_report,
    confusion_matrix,
)
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from category_encoders import TargetEncoder
from textblob import TextBlob

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
df_clean_original = pd.read_csv("dataSet.csv", sep=",")
print(df_clean_original.head())
print("\nИнформация о данных:")
df_clean_original.info()
print(df_clean_original.describe())
print(f"Количетсво пропусков\n{df_clean_original.isnull().sum()}")
print(f"Количество дубликатов: {df_clean_original.duplicated().sum()}")
print(
    df_clean_original[
        "performance_category"
    ].value_counts()  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
)
sns.countplot(x="performance_category", data=df_clean_original)
plt.title("Распределение целевой переменной")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df_clean_original["final_exam_score"], kde=True)
plt.title("Распределение итоговых оценок")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df_clean_original["study_hours_per_day"])
plt.title("Boxplot study_hours_per_day")
plt.show()

numeric_cols = df_clean_original.select_dtypes(include=["int64", "float64"]).columns
plt.figure(figsize=(18, 10))
corr = df_clean_original[numeric_cols].corr()
sns.heatmap(corr, cmap="coolwarm")
plt.title("Корреляционная матрица")
plt.show()


def contaminate_data(df: pd.DataFrame) -> pd.DataFrame:
    df_dirty = df.copy()
    np.random.seed(RANDOM_STATE)
    for col in df_dirty.columns:
        if col != "performance_category":
            mask = np.random.random(len(df_dirty)) < 0.3
            df_dirty.loc[mask, col] = np.nan
    dup_rows = df_dirty.sample(frac=0.05, random_state=RANDOM_STATE)
    df_dirty = pd.concat([df_dirty, dup_rows], ignore_index=True)
    df_dirty = df_dirty.sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
    numeric_cols = df_dirty.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        outlier_idx = np.random.choice(
            df_dirty.index, size=int(0.05 * len(df_dirty)), replace=False
        )
        df_dirty.loc[outlier_idx, col] = df_dirty[col].max() * np.random.uniform(
            2, 5, size=len(outlier_idx)
        )
    cat_cols = df_dirty.select_dtypes(include=["object"]).columns
    mistakes = {
        "Engineering": ["enginering", "engeniring"],
        "Arts": ["art"],
        "Medical": ["medicl", "medcal"],
        "Low": ["lOw", "lo"],
        "High": ["hgh", "hig", "hi"],
    }
    for col in cat_cols:
        for correct, wrong_list in mistakes.items():
            for wrong in wrong_list:
                df_dirty[col] = df_dirty[col].replace(wrong, correct)
        rows_perturb = np.random.choice(
            df_dirty.index, size=int(0.1 * len(df_dirty)), replace=False
        )
        for idx in rows_perturb:
            if (
                isinstance(df_dirty.loc[idx, col], str)
                and len(df_dirty.loc[idx, col]) > 2
            ):
                s = list(df_dirty.loc[idx, col])
                pos1, pos2 = np.random.choice(len(s), 2, replace=False)
                s[pos1], s[pos2] = s[pos2], s[pos1]
                df_dirty.loc[idx, col] = "".join(s)
    comments = [
        "Не занемается и плохо учится",
        "Абсолютно не заинтересован в учёбе",
        "Много прогуливал",
        "Попал в универ только потомучто папа знаект декана",
    ]
    df_dirty["teacher_comment"] = np.random.choice(comments, size=len(df_dirty))
    return df_dirty


df_dirty = contaminate_data(df_clean_original)
df_dirty.to_csv("dataSetDirty.csv", index=False)
print(f"Загрязнённый датасет сохранён, размер: {df_dirty.shape}")

df = pd.read_csv("dataSetDirty.csv")
print("Первые 5 строк:")
df.head()
print("\nИнформация о данных:")
df.info()
missing = df.isnull().sum()
missing[missing > 0].sort_values(ascending=False).plot(kind="bar", figsize=(12, 4))
plt.title("Количество пропущенных значений по признакам")
plt.show()
print(f"Дубликатов строк: {df.duplicated().sum()}")
sns.countplot(data=df, x="performance_category")
plt.title("Распределение целевой переменной (до очистки)")
plt.show()


# Задача 3: Очистка данных
def clean_data(df: pd.DataFrame):
    df_clean = df.copy()
    initial_len = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    print(f"Удалено дубликатов: {initial_len - len(df_clean)}")

    cat_cols = df_clean.select_dtypes(include=["object"]).columns.drop(
        ["teacher_comment"], errors="ignore"
    )
    num_cols = df_clean.select_dtypes(include=[np.number]).columns

    # Заполнение пропусков в категориальных модой
    for col in cat_cols:
        mode_val = df_clean[col].mode()
        if len(mode_val) > 0:
            df_clean[col].fillna(mode_val[0], inplace=True)
        else:
            df_clean[col].fillna("missing", inplace=True)

    # Приведение к нижнему регистру
    for col in cat_cols:
        df_clean[col] = df_clean[col].astype(str).str.lower().str.strip()

    # Исправление опечаток
    corrections = {
        "enginering": "engineering",
        "engeniring": "engineering",
        "art": "arts",
        "medicl": "medical",
        "medcal": "medical",
        "lOw": "low",
        "lo": "low",
        "hgh": "high",
        "hig": "high",
        "hi": "high",
    }
    for col in cat_cols:
        df_clean[col] = df_clean[col].replace(corrections)

    # Винсоризация выбросов
    for col in num_cols:
        upper = df_clean[col].quantile(0.99)
        lower = df_clean[col].quantile(0.01)
        df_clean[col] = df_clean[col].clip(lower, upper)

    # Заполнение пропусков в числовых медианой
    for col in num_cols:
        df_clean[col].fillna(df_clean[col].median(), inplace=True)
    return df_clean


df_cleaned = clean_data(df)

invalid_mask = ~df_cleaned["performance_category"].isin(["high", "low", "medium"])
if invalid_mask.any():
    print(f"Удалено {invalid_mask.sum()} строк с некорректным значением y")
    df_cleaned = df_cleaned[~invalid_mask]

assert df_cleaned.isnull().sum().sum() == 0, "Остались пропуски в данных!"
assert df_cleaned["y"].notna().all(), "Целевая переменная содержит NaN!"

print("Очистка завершена, NaN отсутствуют.")
df_cleaned.head()


# Задача 4: Feature engineering
def build_features(df: pd.DataFrame):
    df_feat = df.copy()
    if "attendance_percentage" in df_feat.columns:
        df_feat["is_high_attendance"] = (df_feat["attendance_percentage"] > 85).astype(
            int
        )
    df_feat["social_vs_study"] = df_feat["social_media_hours"] / (
        df_feat["study_hours_per_day"]
    )
    df_feat["stress_sleep_ratio"] = df_feat["stress_level"] / (
        df_feat["sleep_hours"] + 1
    )
    df_feat["usesAi"] = df_feat["ai_tool_usage_hours"]
    if "teacher_comment" in df_feat.columns:
        df_feat["teacher_words"] = df_feat["teacher_comment"].apply(
            lambda x: len(str(x).split())
        )
        df_feat["comment_has_positive"] = (
            df_feat["customer_comment"]
            .str.contains("заинтересован|вежлив|подумает", case=False, na=False)
            .astype(int)
        )
        df_feat["comment_has_negative"] = (
            df_feat["customer_comment"]
            .str.contains("отказ|не заинтересован|не берёт", case=False, na=False)
            .astype(int)
        )

        def sentiment_score(text):
            try:
                return TextBlob(str(text)).sentiment.polarity
            except:
                return 0.0

        df_feat["comment_sentiment"] = df_feat["customer_comment"].apply(
            sentiment_score
        )
        df_feat = df_feat.drop(columns=["customer_comment"])

    df_feat["log_duration"] = np.log1p(df_feat["study_hours_per_day"])
    return df_feat


df_featured = build_features(df_cleaned)
print(f"Размер после feature engineering: {df_featured.shape}")
df_featured.head()

X = df_featured.drop(columns=["performance_category"])
y = df_featured["performance_category"].map({"high": 2,"medium": 1, "low": 0})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE
)

num_cols = X_train.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()

numeric_transformer = RobustScaler()
categorical_transformer = TargetEncoder(
    cols=cat_cols, smoothing=10, handle_missing="value"
)

preprocessor = ColumnTransformer(
    [("num", numeric_transformer, num_cols), ("cat", categorical_transformer, cat_cols)]
)
# ================================
# Ячейка 7: Базовая модель (без балансировки)
# ================================
pipeline_vanilla = Pipeline([
    ('preprocessor', preprocessor),
    ('clf', LogisticRegression(max_iter=1000, random_state=RANDOM_STATE))
])
pipeline_vanilla.fit(X_train, y_train)
y_pred_proba = pipeline_vanilla.predict_proba(X_test)[:,1]
auc_base = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC без балансировки: {auc_base:.4f}")
# ================================
# Ячейка 8: С SMOTE
# ================================
smote_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=RANDOM_STATE)),
    ('clf', LogisticRegression(max_iter=1000, random_state=RANDOM_STATE))
])
smote_pipeline.fit(X_train, y_train)
y_pred_smote = smote_pipeline.predict_proba(X_test)[:,1]
auc_smote = roc_auc_score(y_test, y_pred_smote)
print(f"ROC-AUC с SMOTE: {auc_smote:.4f}")
# ================================
# Ячейка 9: Подбор гиперпараметров и финальная модель
# ================================
final_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=RANDOM_STATE)),
    ('clf', LogisticRegression(random_state=RANDOM_STATE, max_iter=1000))
])

param_grid = {
    'smote__k_neighbors': [3, 5, 7],
    'clf__C': [0.1, 1.0, 10.0]
}

grid = GridSearchCV(final_pipeline, param_grid, cv=StratifiedKFold(5), scoring='roc_auc', n_jobs=-1)
grid.fit(X_train, y_train)

print(f"Лучшие параметры: {grid.best_params_}")
print(f"Лучший ROC-AUC на кросс-валидации: {grid.best_score_:.4f}")
best_model = grid.best_estimator_
y_pred_final = best_model.predict_proba(X_test)[:,1]
auc_final = roc_auc_score(y_test, y_pred_final)
print(f"Финальный ROC-AUC на тесте: {auc_final:.4f}")
# ================================
# Ячейка 10: Матрица ошибок и важность признаков
# ================================
y_pred_class = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred_class)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Коэффициенты модели
preprocessor_fitted = best_model.named_steps['preprocessor']
X_train_trans = preprocessor_fitted.transform(X_train)
coefs = best_model.named_steps['clf'].coef_[0]
feature_names = num_cols + [f"target_enc_{c}" for c in cat_cols]
importance = pd.DataFrame({'feature': feature_names[:len(coefs)], 'coef': coefs})
importance = importance.reindex(importance.coef.abs().sort_values(ascending=False).index)
plt.figure(figsize=(10,6))
sns.barplot(data=importance.head(15), x='coef', y='feature', palette='viridis')
plt.title('Топ-15 признаков по модулю коэффициента')
plt.tight_layout()
plt.show()
