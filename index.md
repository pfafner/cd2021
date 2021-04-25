# Introducción a la Ciencia de Datos 2021

Este es un curso introductorio a la ciencia de datos, con énfasis principalmente en los fundamentos matemáticos y estadísticos de los principales algoritmos de aprendizaje automáticos y reconocimiento de patrones. El tema central del curso es el estudio de métodos para obtener información útil a partir de datos. Al final del curso, los estudiantes comprederán, tanto en la teoría como en la práctica, las etapas necesarias para producir un estudio o análisis de datos, desde la concepción de un problema, hasta la generación de un informe técnico de análisis. Para aprovechar de mejor manera el curso, es recomendable que los estudiantes estén familiarizados con temas de álgebra lineal, cálculo, estadística matemática, y tener conocimientos de al menos un lenguaje de programación (*e.g.* Python, R, Matlab, C++, u otros).


# Programa del curso
<div id='id-programa'/>

[Programa del curso](programa/Programa-cd2021.pdf){:target="_blank"}

### Horario
<div id='id-horario'/>

* Lunes y jueves, 15:40 a 17:20 horas.  Laboratorio: a definir.

### Office Hours
<div id='id-office'/>

* Viernes de 16:00 a 17:00 horas, o por solicitud del estudiante. También pueden enviar sus dudas por correo electrónico.


# Material del curso
<div id='id-material'/>

  **No.**  | **Fecha**    | **Tópicos**                                                         | **Actividades**
  -------- | ------------ | ------------------------------------------------------------------- |  -------------------------------------
  01       | 11.01.2021   | Introducción <br/> [Aula 01](aulas/aula01.pdf){:target="_blank"}    | [(I. Carmichael, J.S. Marron) Data Science vs. Statistics: Two Cultures?](lecturas/carmichael_marron.pdf){:target="_blank"} 
  02       | 14.01.2021   | Probabilidad <br/> [Aula 02](aulas/aula02.pdf){:target="_blank"}    | Ejemplos corregidos. <br/> [(K.-L. Chung) A Course in Probability Theory](http://library.lol/main/6B122D4F68618DB5F1893F0296CB2491){:target="_blank"}  
  03       | 18.01.2021   | Proba. condicional <br/> Variables aleatorias <br/> [Aula 03](aulas/aula03.pdf){:target="_blank"}  | Lefebvre, capítulo 2, pp. 27--54. <br/> [(M. Lefebvre) Basic Probability with Applications](http://library.lol/main/F3B9314CA31E0289D5FCD6EEDA01308A){:target="_blank"}
  L1a      | 21.01.2021   |                                                                     | **[Lista de ejercicios 1, parte A](listas/lista01a.pdf){:target="_blank"}** <br/> *Entregar sólo ejercicios: 1, 7, 8, 11, 12.* Se entregarán junto con la parte B.
  04       | 21.01.2021   | Variables aleatorias <br/> [Aula 04](aulas/aula04.pdf){:target="_blank"} |  Lefebvre, sección 3.1, pp. 55--60  
  05       | 25.01.2021   | Variables aleatorias discretas. Resúmenes de distribuciones. <br/> [Aula 05](aulas/aula05.pdf){:target="_blank"} | **Obs.** Versión actualizada del Aula 05 con lo que vimos el jueves 28. <br/> Lefebvre, sección 3.2, pp. 61--69
  06       | 28.01.2021   | Variables aleatorias continuas. Resúmenes de distribuciones. <br/> [Aula 06](aulas/aula06.pdf){:target="_blank"} | Material sobre v.a. continuas y resúmenes de distribuciones. <br/> Lefebvre, sección 3.3, pp. 70--80
  07       | 30.01.2021   | Ejemplos de distribuciones. <br/> [Aula 07](aulas/aula07.pdf){:target="_blank"} | Material sobre distribuciones.  <br/> Lefebvre, capítulos 3 y 4 (el 4 es sobre multivariadas).
  L1b      | 30.01.2021   |                                                                     |  **[Lista de ejercicios 1, parte B](listas/lista01b.pdf){:target="_blank"}** <br/> *Entregar sólo ejercicios: 1, 2, 4, 5.* <br/> **Fecha de entrega: Lunes 8 de febrero.**
  08       | 01.02.2021   | Técnicas de visualización. Análisis de componentes principales. <br/> [Aula 08](aulas/aula08.pdf){:target="_blank"} | 
  09       | 04.02.2021   | Análisis de componentes principales <br/> [Aula 09](aulas/aula09.pdf){:target="_blank"} | 
  10       | 08.02.2021   | Interpretación de PCA. Errores comunes. Ejemplos y aplicaciones. <br/> [Aula 10](aulas/aula10.pdf){:target="_blank"} | **Obs!** Abajo aparecen los enlaces al material sobre Python y Pandas. <br/> *Agradezcan a JLo por las referencias!*
  11       | 11.02.2021   | Escalamiento multidimensional <br/> [Aula 11](aulas/aula11.pdf){:target="_blank"} | Material sobre el problema de transformar una distribución uniforme. <br/> [Distribución uniforme en la esfera](labs/sphere-uniform.pdf){:target="_blank"}
  L2      | 13.02.2021   |                                                                     |  **[Lista de ejercicios 2](listas/lista02.pdf){:target="_blank"}** <br/> [crimes.dat](listas/crimes.dat){:target="_blank"} [weather.csv](listas/weather.csv){:target="_blank"} <br/> **Fecha de entrega: Martes 23 de febrero.**
  12       | 15.02.2021   | PCA Robusto. Kernel PCA. <br/> [Aula 12](aulas/aula12.pdf){:target="_blank"} | Agregado ejemplo de KernelPCA.
  13       | 18.02.2021   | Variables latentes. ICA. <br/> [Aula 13](aulas/aula13.pdf){:target="_blank"} | Agregados ejemplos de ICA.
  14       | 22.02.2021   | Factoracion no-negativa de matrices <br/> [Aula 14](aulas/aula14.pdf){:target="_blank"} |  Agregados ejemplos de NNMF. <br/> **Obs!** El archivo no está completo. Me falta agregar el material sobre análisis semántico latente: LSA, LDA y FA y ejemplos (lo que vimos fuera de las diapositivas).
  15       | 25.02.2021   | Métodos locales I <br/> [Aula 15](aulas/aula15.pdf){:target="_blank"} | Agregados ejemplos de *manifold learning*. 
  L3       | 28.02.2021   |                                                                       | **[Lista de ejercicios 3](listas/lista03.pdf){:target="_blank"}** <br/> **Fecha de entrega: Jueves 11 de marzo.**
  16       | 01.03.2021   | Métodos locales II <br/> [Aula 16](aulas/aula16.pdf){:target="_blank"} | Faltan ejemplos de SOM.
  17       | 04.03.2021   | Funciones kernel. Construcción de distribuciones empíricas.            | Pendiente de agregar los ejemplos en Python. <br/> Estaré agregando las notas más adelante.
  L4       | 07.03.2021   |                                                                       | **[Lista de ejercicios 4](listas/lista04.pdf){:target="_blank"}** <br/> [hpi-data-2016.xlsx](listas/hpi-data-2'016.xlsx){:target="_blank"} <br/> **Fecha de entrega: Lunes 22 de marzo.**
  18       | 08.03.2021   | Agrupamiento jerárquico <br/> [Aula 18](aulas/aula18.pdf){:target="_blank"} | Ejemplos de visualización de dendrogramas: <br/> [Paper Covid19-1](lecturas/s41467-020-18854-2.pdf){:target="_blank"} [Paper Covid19-2](lecturas/eabe2555.full.pdf){:target="_blank"}
  19       | 11.03.2021   | K-medias, K-medianas, K-medioides, Fuzzy K-medias. <br/> [Aula 19](aulas/aula19.pdf){:target="_blank"} | Comentarios sobre la *maldición de la dimensionalidad* <br/> [Raúl Rojas dimensionality.pdf](https://www.inf.fu-berlin.de/inst/ag-ki/rojas_home/documents/tutorials/dimensionality.pdf){:target="_blank"} <br/> Ver también Cap. 1 libro de Giraud.
  20       | 18.03.2021   | Mezclas gaussianas. Algoritmo EM. <br/> [Aula 20](aulas/aula20.pdf){:target="_blank"} |   
  21       | 22.03.2021   | Agrupamiento espectral. <br/> [Aula 21](aulas/aula21.pdf){:target="_blank"} |    
  P1       | 22.03.2021   |                                                                       | **[Proyecto 1](listas/proyecto1.pdf){:target="_blank"}** <br/> **Fecha de entrega: Lunes 12 de abril.** <br/> **Presentaciones: Lunes 12 y Jueves 15 de abril.** <br/> Coordenadas estaciones: [stations.json](listas/stations.json){:target="_blank"}  [stations.csv](listas/stations.csv){:target="_blank"} 
  22       | 25.03.2021   | Métodos basados en densidades. <br/> [Aula 22](aulas/aula22.pdf){:target="_blank"} |   
  23       | 29.03.2021   | Métricas para métodos de agrupamiento. <br/> [Aula 23](aulas/aula23.pdf){:target="_blank"} | 
  24       | 05.04.2021  | Modelación predictiva. K vecinos más cercanos. <br/> [Aula 24](aulas/aula24.pdf){:target="_blank"} | Algunos demos interactivos <br/> [Demo1](http://vision.stanford.edu/teaching/cs231n-demos/knn/){:target="_blank"} [Demo2](https://martin-thoma.com/k-nearest-neighbor-classification-interactive-example/){:target="_blank"}
  L5       | 06.04.2021   |                                                                       | **[Lista de ejercicios 5](listas/lista05.pdf){:target="_blank"}** <br/> [heptatlon.csv](listas/heptatlon.csv){:target="_blank"} <br/> **Fecha de entrega: Viernes 23 de abril.**
  25       | 08.04.2021   | El clasificador bayesiano óptimo. <br/> [Aula 25](aulas/aula25.pdf){:target="_blank"} | 
  26       | 12.04.2021   | Ejemplos de clasificador bayesiano. Clasificador *Naive Bayes*. <br/> [Aula 26](aulas/aula26.pdf){:target="_blank"} | Algunos ejemplos <br/> [Ejemplo 1 (2 normales)](code/bayes_2normal_Example.ggb){:target="_blank"} <br/> [Ejemplo 2 (3 normales)](code/bayes_3normal_Example.ggb){:target="_blank"}
  27       | 15.04.2021   | Análisis discriminante (LDA y QDA). <br/> [Aula 27](aulas/aula27.pdf){:target="_blank"} | 
  S1       | 19.04.2021   | Presentación de seminarios.                                            | 
  S1       | 22.04.2021   | Presentación de seminarios.                                            | 
  28       | 26.04.2021   | Clasificadores lineales.                                               | 

# Material adicional (labs)
<div id='id-labs'/>

  **No.**  | **Fecha**    | **Tópicos**                                                         | **Material**
  -------- | ------------ | ------------------------------------------------------------------- |  -------------------------------------
  00       | 01.02.2021   | Instalación de librerías y ambiente de trabajo Python Anaconda, Jupyter-lab.  | [Anaconda+Tensorflow+Jupyter installation guide](otros/Anaconda+Tensorflow+Jupyter_installation_guide.pdf){:target="_blank"} <br/> *Archivos auxiliares:* [plotmatrix.py](otros/plotmatrix.py){:target="_blank"} [test.ipynb](otros/test.ipynb){:target="_blank"}
  .        | 04.02.2021   | Ejemplo de exploración de datos.                                    | [iris.ipynb](labs/iris.ipynb){:target="_blank"}
  01       | 06.02.2021   | Lectura archivo csv. Exploración de datos. Estandarización. Descomposición SVD. Análisis de componentes principales. | [lab01.ipynb](labs/Lab01.ipynb){:target="_blank"} <br/> [lab01_R.ipynb](labs/Lab01_R.ipynb){:target="_blank"} <br/> [deport.csv](labs/deport.csv){:target="_blank"}
  .        | 08.02.2021   | Errores comunes en PCA.                                              | [meteo-users.ipynb](labs/meteo-users.ipynb){:target="_blank"} <br/> [meteo-users.csv](labs/meteo-users.csv){:target="_blank"}
  02       | 13.02.2021   | Procesamiento de imágenes. RGB a escala de grises. Crop. Histogramas. Transformaciones básicas. | [lab02.ipynb](labs/Lab02.ipynb){:target="_blank"} <br/> [quetzal.png](labs/quetzal.png){:target="_blank"}
  .        | 18.02.2021   | Ejemplo de ICA.                                                      | [ICA_examples.ipynb](labs/ICA_examples.ipynb){:target="_blank"} <br/> [horse.jpg](labs/horse.jpg){:target="_blank"} [morro.jpg](labs/morro.jpg){:target="_blank"} [plane.jpg](labs/plane.jpg){:target="_blank"} [race.jpg](labs/race.jpg){:target="_blank"}
  .        | 22.02.2021   | Ejemplo de NNMF. Sistemas de recomendación.                          | [nnmf-recommender-system.ipynb](labs/nnmf-recommender-system.ipynb){:target="_blank"}
  .        | 01.03.2021   | Ejemplo de KernelPCA. Ejemplos de *manifold learning*.               | [manifold.ipynb](labs/manifold.ipynb){:target="_blank"}
  .        | 01.03.2021   | Ejemplo de SOM.                                                      | [DemocracyIndex.ipynb](labs/DemocracyIndex.ipynb){:target="_blank"} <br/> [democracy_index.csv](labs/democracy_index.csv){:target="_blank"}
  .        | 04.03.2021   | Funciones de base (kernel) radial.                                   | 
  03       | 13.03.2021   | Agrupamiento jerárquico. K-medias.                                   | [hierarchical.ipynb](labs/hierarchical.ipynb){:target="_blank"} <br/> [k-means.ipynb](labs/k-means.ipynb){:target="_blank"} <br/> [horse.jpg](labs/horse.jpg){:target="_blank"}
  .        | 18.03.2021   | Gaussian misture models. Algoritmo EM.                               | [gmm.ipynb](labs/gmm.ipynb){:target="_blank"}
  .        | 22.03.2021   | Agrupamiento espectral.                                              | [spectral1.ipynb](labs/spectral1.ipynb){:target="_blank"} <br/> [spectral2.ipynb](labs/spectral2.ipynb){:target="_blank"}
  .        | 25.03.2021   | Métodos basados en densidad. Comparación.                            | [density-based.ipynb](labs/density-based.ipynb){:target="_blank"} <br/> [comparison.ipynb](labs/comparison.ipynb){:target="_blank"} 
  .        | 25.03.2021   | Métricas de evaluación para agrupamiento.                            | [silhouette.ipynb](labs/silhouette.ipynb){:target="_blank"}
  04       | 17.04.2021   | Clasificador y regresor Knn. Clasificador Naive Bayes.               | [knn.ipynb](labs/knn.ipynb){:target="_blank"} <br/> [bayes.ipynb](labs/bayes.ipynb){:target="_blank"}
  

# Presentaciones del primer seminario (Datos Ecobici)
<div id='id-sem1'/>

  **No.**  | **Fecha**    | **Expositor**                                                          | **Tópicos**
  -------- | ------------ | ---------------------------------------------------------------------- | -------------------------------------
  01       | 19.04.2021   | Juan Lorthiois     <br/> [Presentación](seminario1/presentacion_Juan.pptx){:target="_blank"}  | Comparación de la demanda anterior/posterior de pandemia Covid 19. Perfilado o caracterización de un usuario típico. Determinación geográfica de estaciones con mayor demanda. Clusterización y diferenciación t-SNE por variable.
  02       | 19.04.2021   | José Ramos         <br/> [Presentación](seminario1/presentacion_JoseRamos.pdf){:target="_blank"}  | Modelo de decisión de velocidad media de los usuarios. Determinación de variables de mayor impacto en la predicción de la velocidad media de recorrido.  Clasificación *Naive Bayes* de velocidad del usuario: lento/rápido.
  03       | 19.04.2021   | Rodrigo Morales    <br/> [Presentación](seminario1/presentacion_Rodrigo.pdf){:target="_blank"}  | Modelos para localización óptima de nuevas estaciones. Uso de fuentes diversas para predicción: INEGI, población flotante, geolocalización, nivel socioeconómico. Comparación de criterios de localización óptima.
  04       | 19.04.2021   | Pablo Noack        <br/> [Presentación](seminario1/presentacion_Pablo.pdf){:target="_blank"}  | Distribuciones de tiempos de recorrido y desplazamientos. Relación geoespacial contra distribuciones de frecuencia de demanda. Análisis de la matriz de frecuencias. Clusterización t-SNE por frecuencia.
  05       | 22.04.2021   | José López         <br/> [Presentación](seminario1/presentacion_JoseLopez.pdf){:target="_blank"}  | 
  06       | 22.04.2021   | Javier Mejía       <br/> [Presentación](seminario1/presentacion_Javier.pptx){:target="_blank"}  | 
  07       | 24.04.2021   | José Menéndez      <br/> [Presentación](seminario1/s1.pdf){:target="_blank"}  | 
  08       | 24.04.2021   | Lorena Beltrán     <br/> [Presentación](seminario1/s.pdf){:target="_blank"}  | 
  

# Material sobre Python (textos, videos)
<div id='id-python'/>

* [R. Gonzáles Duque. *Python para todos*.](lecturas/Python_para_todos.pdf){:target="_blank"}

* [Theodore Petrou. *Pandas Cookbook*.](lecturas/Pandas_Cookbook.pdf){:target="_blank"}

* [*Curso Python (Youtube)*.](https://www.youtube.com/watch?v=G2FCfQj-9ig&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS){:target="_blank"}


# Referencias
<div id='id-ref'/>

### Textos:

* [R. Duda, P. Hart, D. Stork (2000). *Pattern classification*.](http://library.lol/main/5858DCFE63D714C5C42F433D5F821631){:target="_blank"}

* [C. Bishop (2000). *Pattern Recognition and Machine Learning*.](http://library.lol/main/B616EF565E2D48AE23EE2E19D7B0ADD2){:target="_blank"}

* [T. Hastie, R. Tibshirani, J. Friedman (2013). *The Elements of Statistical Learning*.](http://library.lol/main/5F88A9F135B7AB31FBCF1729412560DC){:target="_blank"}

* [K. Murphy (2012). *Machine Learning: a Probabilistic Perspective*.](http://library.lol/main/8ECFEEB2E1F9A19C770FBA1FF85FA566){:target="_blank"}

### Referencias adicionales:

* [G. James, D. Witten, T. Hastie, R. Tibshirani (2008). *An Introduction to Statistical Learning with Applications in R*.](http://library.lol/main/1E48B8220FEE4CD9D192F4ED5020F2DA){:target="_blank"}

* [A. Izenman (2008). *Modern Multivariate Statistical Techniques: Regression, Classification and Manifold Learning*.](http://library.lol/main/B5E1DA4CD9133B468CA730402BBC7117){:target="_blank"}

* [B. Everitt, T. Hothorn (2011). *An Introduction to Applied Multivariate Analysis with R*](http://library.lol/main/83BD38DABC018FE79C6AEEF726BF20D7){:target="_blank"}

* [K. Fukunaga (1990). *Introduction to Statistical Pattern Recognition*.](http://library.lol/main/F1FC9B38F5E9F245C7CDE3AFEDED4D06){:target="_blank"}

* [C. Giraud (2015). *Introduction to High-Dimensional Statistics*.](http://library.lol/main/38E216C9EFA26C09F5A2324BC3122F92){:target="_blank"}

* [L. Devroye, L. Györfi, G. Lugosi (1996). *A Probabilistic Theory of Pattern Recognition*.](http://library.lol/main/60F75D016A9C96D67D752536B9D1753A){:target="_blank"}

* [S. Shalev-Shwartz, S. Ben-David (2014). *Understanding Machine Learning: From Theory to Algorithms*.](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf){:target="_blank"}

* [P. Rigollet (2015). *Mathematics for Machine Learning*.](https://ocw.mit.edu/courses/mathematics/18-657-mathematics-of-machine-learning-fall-2015/lecture-notes/MIT18_657F15_LecNote.pdf){:target="_blank"}

### Artículos:

* [A. S. Bandeira (2016). *Ten Lectures and Forty-Two Open Problems in the Mathematics of Data Science*.](https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf){:target="_blank"}

---
