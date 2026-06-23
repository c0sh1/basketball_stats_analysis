# Proyecto Final — Módulo 1 (Análisis y Visualización de Datos)

Esto es vuestra primera carta de presentación de cara a empresas. No es un ejercicio más: es algo que vais a poder enseñar en una entrevista, y la presentación final es una presentación a cliente de verdad. Así que hay que currárselo: producto bien hecho, repo ordenado y una historia que se entienda sin abrir un notebook.

## La idea

Coger un dataset real de Kaggle que os interese, hacerle todo el trabajo de datos con Python (limpieza y EDA) en un Jupyter, y convertirlo en un producto presentable: un dashboard en Power BI, o una app en Streamlit, con un repositorio de GitHub bien documentado.

La pregunta que guía todo es siempre la misma: ¿qué problema útil resuelven estos datos y a quién le sirve? Si lo tenéis claro, tenéis proyecto. Si no, seguid buscando dataset.

## Qué tiene que llevar

Todo lo del Módulo 1:

- Una idea clara con su pregunta, y dos datasets: el principal y un plan B por si el primero falla.
- Repositorio en GitHub con estructura ordenada, README y requirements.txt.
- Commits hechos poco a poco según vais avanzando, no todo el último día.
- Preprocesamiento en Python: nulos, tipos, duplicados, outliers, y alguna columna nueva si aporta.
- EDA con gráficos y conclusiones escritas (un gráfico sin conclusión no cuenta).
- Producto final en Power BI o en Streamlit, el que os tire más.
- README documentado: qué es, qué problema resuelve, los datos, el proceso y los hallazgos.
- Presentación orientada a cliente: producto y valor, sin enseñar notebooks ni código.

Es análisis y visualización. Aquí lo que se evalúa es que sepáis entender unos datos, limpiarlos, sacarles conclusiones y contarlas bien.

## Elegir el dataset (esto se hace hoy)

La fuente principal es Kaggle (kaggle.com/datasets), y de respaldo tenéis Google Dataset Search, datos.gob.es y HuggingFace.

Antes de venir a que os lo valide, comprobad vosotros que sirve para un EDA. Si falla algo de esto, probablemente no valga:

- Volumen suficiente: como referencia, más de 1.000 filas y varias columnas.
- Mezcla de tipos: que tenga columnas numéricas y categóricas, que es lo que permite un EDA con chicha (distribuciones, comparativas, correlaciones).
- Una pregunta detrás: que se intuya un problema real, no un listado sin sentido.
- Ni trivial ni imposible: que haya algo que limpiar, pero que no esté tan roto que sea inviable.
- Columnas que entendáis: que sepáis qué significa cada una.
- Uso permitido y con el enlace a la fuente claro.

El plan B no es opcional. Buscad un segundo dataset de otro proyecto distinto por si el principal resulta malo (pocos datos, mal estructurado, columnas vacías). Os ahorra perder días.

## El flujo de trabajo

1. Crear el repo en GitHub y dejarlo en local con GitHub Desktop. README inicial con el título y la idea, y primer commit.
2. Cargar y explorar el dataset crudo: shape, info(), describe(), nulos, tipos, primeras filas.
3. Preprocesar: nulos, tipos correctos, duplicados, outliers, normalizar texto y alguna columna nueva si suma. De aquí sale un processed.csv limpio.
4. EDA: distribuciones, relaciones entre variables, correlaciones, segmentaciones. Cada gráfico con su conclusión.
5. Montar el producto (Power BI o Streamlit) leyendo ese processed.csv.
6. Documentar el README con los hallazgos y cómo se ejecuta.
7. Preparar la presentación.

Una idea que os ayuda: el notebook hace el trabajo sucio y deja un CSV limpio; el producto solo lee ese CSV. Así el dashboard o la app siempre tira, aunque luego no toquéis el notebook.

## El producto: Power BI o Streamlit

Elegís uno, el que os tire más:

- Power BI: si os va lo visual y de negocio sin escribir código. Dashboards potentes a base de arrastrar y soltar.
- Streamlit: si os tira más Python y queréis una app interactiva hecha por vosotros, con filtros y lógica propia.

En los tres casos los datos salen del processed.csv de vuestro notebook.

## GitHub poco a poco (con GitHub Desktop)

Vamos a trabajar con GitHub Desktop, que es lo más cómodo y no os pelea con comandos. El repo lo podéis crear de dos formas: desde la web de GitHub y luego clonarlo en GitHub Desktop, o directamente en GitHub Desktop con File > New repository y después Publish repository.

A partir de ahí la rutina es siempre la misma: cada vez que termináis algo, abrís GitHub Desktop, veis los cambios, escribís abajo a la izquierda un resumen de lo que habéis hecho, le dais a "Commit to main" y luego a "Push origin" para subirlo.

Nada de dejarlo todo para el último día con un único commit. Quiero ver vuestro avance. El historial debería parecerse a esto:

- Estructura inicial del repo y README
- Dataset crudo y enlace a la fuente
- Carga y exploración inicial del dataset
- Limpieza de nulos, tipos y duplicados
- Tratamiento de outliers y columnas nuevas
- EDA univariante con conclusiones
- EDA bivariante y correlaciones
- Dashboard / app con los gráficos clave
- README con los hallazgos

Acostumbraos a esto ya, porque en una empresa nadie sube todo de golpe. El repo cuenta vuestra historia de trabajo, y eso también lo miramos.

## El README

Es la portada del proyecto, lo primero que miramos los profes. Tiene que llevar:

- Título y una frase de qué es y qué resuelve.
- El problema o la pregunta de negocio.
- Los datos: fuente con su enlace a Kaggle, número de filas y columnas, y qué representan.
- El proceso: qué limpieza hicisteis y por qué tomasteis esas decisiones.
- Los hallazgos clave, de tres a cinco, cada uno con su gráfico.
- Cómo se ejecuta: requirements.txt y cómo abrir el notebook o lanzar la app.
- Capturas del producto final.

## La presentación (estilo cliente)

Imaginad que se lo presentáis a una empresa que os ha contratado para analizar esos datos. Vendéis el producto y el valor, no el código.

Lo que sí hay que hacer: empezar por el problema y por a quién le importa. Enseñar el producto final funcionando, con una demo en vivo. Contar tres o cuatro hallazgos y, sobre todo, el "y esto qué": qué decisión permite tomar cada uno. Cerrar con el valor, en qué ayuda al negocio y qué se podría ampliar más adelante.

Lo que no hay que hacer: enseñar el notebook, celdas de código o df.head(). Nada de "primero importé pandas, luego hice un dropna", que al cliente eso no le importa. Y gráficos sueltos sin contar qué significan, tampoco.

Una regla sencilla para repasar la presentación: si una frase no la entendería el director de una empresa que no sabe Python, cambiadla.

## Estructura de repositorio recomendada

```
mi-proyecto-m1/
├── README.md                 qué es, problema, datos, hallazgos, cómo ejecutar
├── requirements.txt
├── data/
│   ├── raw/                  dataset original de Kaggle
│   └── processed/            processed.csv (datos limpios)
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_preprocesamiento.ipynb
│   └── 03_eda.ipynb
├── app/                      streamlit  (si elegís Streamlit)
│   └── app.py
├── powerbi/                  .pbix y capturas  (si elegís Power BI)
└── img/                      capturas para el README
```

## Checklist

Arranque (hoy):

- [ ] Idea de proyecto definida con su pregunta de negocio
- [ ] Dataset principal encontrado y pasado por el filtro EDA (con enlace)
- [ ] Dataset plan B encontrado (con enlace)
- [ ] Repositorio de GitHub creado y abierto en GitHub Desktop, con README inicial

Datos:

- [ ] Carga y exploración inicial del dataset
- [ ] Preprocesamiento (nulos, tipos, duplicados, outliers)
- [ ] Columnas nuevas si aportan
- [ ] processed.csv generado

Análisis:

- [ ] EDA univariante con conclusiones
- [ ] EDA bivariante y correlaciones con conclusiones
- [ ] Tres a cinco hallazgos clave identificados

Producto y entrega:

- [ ] Producto final funcionando (Power BI o Streamlit)
- [ ] README documentado con hallazgos y capturas
- [ ] Commits hechos poco a poco a lo largo del proyecto
- [ ] Presentación a cliente preparada (producto y valor, sin código)

## Cómo se evalúa

Orientativo, sobre 10:

- Repo y uso de GitHub (estructura, README, commits poco a poco): 2
- Preprocesamiento (limpieza correcta y justificada): 2
- EDA (gráficos con conclusiones que aportan): 2
- Producto final (dashboard o app cuidado y que funciona): 2
- Presentación a cliente (clara, con valor y sin código): 2

## Fechas

Arrancamos hoy. La validación del dataset, esta semana, cuanto antes mejor. La presentación final es el [02/07/2026].

Y aprovechad para subir también a GitHub proyectos anteriores del bootcamp, que suman experiencia y dejan vuestro perfil más completo.
