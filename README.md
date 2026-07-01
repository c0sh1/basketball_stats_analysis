# 🏀 Basketball Stats Analysis
### ¿Es la NBA la liga de baloncesto más dominante del mundo, o hay talento de élite repartido por otras ligas internacionales?

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📋 Descripción del proyecto

Análisis exploratorio de estadísticas de baloncesto de **53,949 registros** que abarca **49 ligas** de todo el mundo entre **1999 y 2020**, incluyendo la NBA, Euroleague, ACB, NBL australiana y muchas más.

El objetivo es responder si la NBA es realmente la liga más dominante del mundo o si el talento de élite está repartido por otras ligas internacionales, utilizando una métrica de rendimiento normalizada por minutos jugados.

---

## ❓ Preguntas de negocio

1. ¿Es la NBA realmente la mejor liga del mundo en términos de rendimiento?
2. ¿Están los mejores jugadores del mundo en la NBA?
3. ¿Qué países producen más talento en el baloncesto mundial?
4. ¿Qué equipos han sido históricamente los más dominantes?
5. ¿Son las estadísticas brutas comparables entre ligas?

---

## 🔍 Hallazgos clave

- **Las estadísticas brutas no son comparables entre ligas** — la NBA juega el doble de minutos que las ligas internacionales (1,295 vs 663 minutos de media), lo que infla artificialmente sus números. Por eso se desarrolló la métrica `performpermin` (PTS+REB+AST+STL+BLK por minuto jugado).

- **Ajustado por minutos, los equipos internacionales superan a los NBA** — los Top 5 equipos internacionales (BAR/Eurocup, LIM/FIBA-Europe-Cup, HAPJ/Euroleague) tienen un `performpermin` de entre 0.85 y 0.95, frente al 0.74-0.78 de los mejores equipos NBA (GSW, DEN, PHX).

- **El mejor jugador histórico por rendimiento por minuto es Giannis Antetokounmpo** — con 1.666 performpermin en su mejor temporada, muy por encima de la media.

- **El talento no está concentrado solo en EEUU** — países como Nigeria, la República Democrática del Congo y Camerún producen jugadores con un rendimiento por minuto superior al promedio de Estados Unidos.

- **Los equipos NBA más dominantes históricamente** son GSW (2000-2001), SAC (2015-2016) y WAS (2018-2019), medidos por rendimiento promedio de su plantilla a lo largo de todas las temporadas.

---

## 📊 Dataset

- **Fuente:** [Basketball Stats by Season — Kaggle](https://www.kaggle.com/)
- **Registros:** 53,949
- **Ligas:** 49 (NBA + ligas internacionales)
- **Temporadas:** 1999-2000 a 2019-2020
- **Columnas:** 30 (estadísticas de juego, datos físicos, draft, nacionalidad)

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| Python 3.11 | Lenguaje principal |
| Pandas | Procesamiento de datos |
| Scikit-learn | KNN Imputer para valores nulos |
| Matplotlib / Seaborn | Visualizaciones en el EDA |
| Plotly | Gráficas interactivas (radar chart) |
| Streamlit | Dashboard interactivo |
| GitHub | Control de versiones |

---

## 📁 Estructura del proyecto

```
basketball_stats_analysis/
├── Data/
│   ├── stats_by_season.csv          ← dataset original
│   └── stsbyseasonclean.csv         ← dataset procesado
├── Notebook/
│   ├── data_process.ipynb           ← limpieza y preprocesamiento
│   └── EDA.ipynb                    ← análisis exploratorio
├── Streamlit_app/
│   ├── assets/
│   │   └── banner.jpg
│   ├── pages/
│   │   ├── 1_NBA_vs_Internacional.py
│   │   ├── 2_Top_Jugadores.py
│   │   ├── 3_Top_Equipos.py
│   │   └── 4_Talento_por_Pais.py
│   └── home.py
├── requirements.txt
└── README.md
```

---

## 🚀 Cómo ejecutarlo en local

```bash
# 1 — Clona el repositorio
git clone https://github.com/c0sh1/basketball-stats-analysis.git

# 2 — Instala las dependencias
pip install -r requirements.txt

# 3 — Ejecuta el dashboard
cd Streamlit_app
streamlit run home.py
```

---

## 🌐 Dashboard en producción

👉 [Ver dashboard en Streamlit Cloud](https://basketballstatsanalysis-6rwwjegrmk3ilbvdwonkbu.streamlit.app)


---

## 👤 Autor

Proyecto desarrollado como parte de un bootcamp de Data Analytics.

---

## 📄 Licencia

MIT License
