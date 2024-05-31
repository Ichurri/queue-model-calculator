# Aplicacion de Calculo de Modelos de Lineas de Espera
Este programa permite calcular diferentes parámetros de modelos de colas mediante una interfaz gráfica desarrollada en Tkinter. Se incluyen varios modelos de colas como M/M/1, M/M/k, M/G/1, M/M/k con fuente finita y M/D/1.

## Requisitos
- Python 3.x
- Paquetes de Python: tkinter, math

## Instalacion
1. Clona este repositorio o descarga los archivos necesarios.
   
2. Asegúrate de tener Python instalado en tu sistema.
   
3. Instala Tkinter si no lo tienes ya instalado. Para instalar Tkinter en Debian/Ubuntu, usa el siguiente comando:
```sh
sudo apt-get install python3-tk
```
## Uso
1. Ejecuta el script `queueing_models_calculator.py`:
```sh
python queueing_models_calculator.py
```
2. Se abrirá una ventana con el título "Cálculo de Líneas de Espera".

### Selección del Modelo
En la parte superior de la ventana, selecciona el modelo de cola que deseas calcular:

- M/M/1
- M/M/k
- M/G/1
- M/M/k (fuente finita)
- M/M/1 (fuente finita)
- M/D/1

### Ingreso de Parametros
Dependiendo del modelo seleccionado, ingresa los siguientes parámetros:

- λ (tasa de llegadas): Tasa de llegadas por unidad de tiempo.
- μ (tasa de servicios): Tasa de servicios por unidad de tiempo.
- k (número de canales): (Solo para modelos M/M/k) Número de canales de servicio.
- N (tamaño de la fuente): (Solo para M/M/k con fuente finita y M/M/1 con fuente finita) Tamaño de la población.
- σ (desviación estándar): (Solo para M/G/1) Desviación estándar del tiempo de servicio.
- n (número de unidades en el sistema): (No aplicable para M/D/1).

### Ejecucion del Calculo

1. Una vez ingresados los parámetros correspondientes, haz clic en el botón "Calcular".
2. Los resultados se mostrarán en la parte inferior de la ventana, incluyendo:
- P0: Probabilidad de que no haya unidades en el sistema.
- Lq: Número promedio de unidades en la línea de espera.
- L: Número promedio de unidades en el sistema.
- Wq: Tiempo promedio que una unidad pasa en la línea de espera.
- W: Tiempo promedio que una unidad pasa en el sistema.
- Pw: Probabilidad de que una unidad que llega tenga que esperar para ser atendida.
- Pn: Probabilidad de que haya n unidades en el sistema (cuando sea aplicable).

### Ejemplo de Uso
1. Selecciona el modelo "M/M/1".
2. Ingresa λ = 5 y μ = 10.
3. Haz clic en "Calcular".
4. Los resultados aparecerán en la parte inferior de la ventana.

## Notas
- Asegúrate de que los valores de los parámetros sean numéricos y válidos según el contexto del modelo seleccionado.
- El programa mostrará un mensaje de error si los valores ingresados no son válidos.
