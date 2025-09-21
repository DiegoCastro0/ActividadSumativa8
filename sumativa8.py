#importamos todo lo necesario para la interfaz
#import PyQt5
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox,QComboBox,QCheckBox)
import sys
from PyQt5.QtGui import QPixmap

#creamos una lista para mostrar en el historial
resultados = []

"""
Creamos la funcion mensaje en la cual haremos todo el proceso para ingresar notas, calcular promedio y
muestra el resultado en el "historial"
"""
def mensaje():
    #Entrada de dato del nombre
    nombre = nombre2.text()
    #Entrada de dato del grupo
    gruposelec = grupo.currentText()
    try:
        #Ingreso de datos
        n1 = float(nota1.text())
        n2 = float(nota2.text())
        n3 = float(nota3.text())
        #calcular promedio
        promedio = (n1 + n2 + n3) / 3
        
        #Validación
        if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
             QMessageBox.warning(ventana, "Error", "Por favor ingresa solo números válidos.")
        else:
            #Asignación de estado
            if promedio >= 7:
                estado = " Aprobado"
            elif promedio >= 5:
                estado = " En riesgo"
            else:
                estado = " Reprobado"

            #Mostrar el resultado en el "Historial"
            resultados.append(f"{nombre} ({gruposelec}): {promedio:.2f} - {estado}")
            historial.setText("Historial de promedios:\n" + "\n".join(resultados))


            #Ventana emergente para confirmar que si se cumplio el proceso
            QMessageBox.information(ventana, "Resultado",
                                    f"El promedio del estudiante {nombre} ({gruposelec}) es: {promedio:.2f}")
    #Excepción por si todo falla
    except ValueError:
        QMessageBox.warning(ventana, "Error", "Por favor ingresa solo números válidos.")


#Funcion para el uso del primer filtro (Aprobado)
def actualizar():
    #Verificar si el checkboz esta marcado
    if filtro.isChecked():
        #Nos aseguramos que si este checkbox esta marcado los otros 2 no
        filtro2.setChecked(False)
        filtro3.setChecked(False)
        #Busqueda por filtro
        filtrados = [r for r in resultados if " Aprobado" in r]
        #Agregamos el resultado al "Historial"
        historial.setText("Historial de promedios (solo aprobados):\n" + "\n".join(filtrados))
    #Si no esta marcado que muestre todos los tipos de notas (aprobadas,reprobadas u en riesgo)
    else:
        historial.setText("Historial de promedios:\n" + "\n".join(resultados))
#función para el uso del filtro 2 (Reprobado)
def actualizar2():
    #Lo mismo que la funcion actualizar pero cambiando que filtros se desactivan XDXDXDXD
    if filtro2.isChecked():
        filtro.setChecked(False)
        filtro3.setChecked(False)
        filtrados = [r for r in resultados if " Reprobado" in r]
        historial.setText("Historial de promedios (solo Reprobados):\n" + "\n".join(filtrados))

    else:
        historial.setText("Historial de promedios:\n" + "\n".join(resultados))
    
#función para el uso del filtro 3 (En riesgo)
def actualizar3():
    #Lo mismo que la funcion actualizar pero cambiando que filtros se desactivan XDXDXDXD
    if filtro3.isChecked():
        filtro.setChecked(False)
        filtro2.setChecked(False)
        filtrados = [r for r in resultados if " En riesgo" in r]
        historial.setText("Historial de promedios (solo En riesgo):\n" + "\n".join(filtrados))

    else:
        historial.setText("Historial de promedios:\n" + "\n".join(resultados))

#Iniciar interfaz
app = QApplication(sys.argv)
ventana = QWidget()
#Propiedades de una ventana
ventana.setWindowTitle("Calculadora de promedio")
ventana.setGeometry(100,100,700,300)
layout = QVBoxLayout()

#Creamos los widgets que necesitamos
#label de informacion
info = QLabel("Esta es una calculadora de promedio de 3 actividades/notas para estudiantes")
#label de informacion
nombre = QLabel("Nombre del alumno")
#Entrada de texto de nombre de alumno
nombre2 = QLineEdit()

#label de informacion
GLs = QLabel("Selecciona el grupo")
#Crear la combobox donde se elige el grupo
grupo = QComboBox()
#Asignamos las opciónes que el usuario puede elegir
grupo.addItems(["Grupo A1", "Grupo A2", "Grupo A3"])


#label de informacion
info2 = QLabel("Ingresa las 3 notas")
#Entrada de la primera nota
nota1 = QLineEdit()
#Entrada de la segundaa nota
nota2 = QLineEdit()
#Entrada de la tercera nota
nota3 = QLineEdit()
#Boton para calcular el promedio
boton = QPushButton("Calcular promedio")
#Conectar el boton con la función mensaje
boton.clicked.connect(mensaje)
#Checkbox para el filtro
filtro = QCheckBox("Mostrar solo aprobados")
#Le asignamos la función al checkbox llamada filtro
filtro.stateChanged.connect(actualizar)
#Checkbox para el filtro2
filtro2 = QCheckBox("Mostrar solo reprobados")
#Le asignamos la función al checkbox llamada filtro2
filtro2.stateChanged.connect(actualizar2)
#Checkbox para el filtro3
filtro3 = QCheckBox("Mostrar solo En riesgo")
#Le asignamos la función al checkbox llamada filtro3
filtro3.stateChanged.connect(actualizar3)

#label de informacion
imagen = QLabel()
#Cargar y escalar la imagen
pixmap = QPixmap("promedio.jpg")
pixmap = pixmap.scaled(300, 300, aspectRatioMode=1)  
#Asignar la imagen al label
imagen.setPixmap(pixmap) 
  
#label de informacion
historial = QLabel("Historial de promedios:")

#Widgets que usamos en el layout
widgets = [info,nombre,nombre2,GLs, grupo,info2,nota1,nota2,nota3, boton,filtro,filtro2,filtro3, imagen,historial]
for w in widgets:
    layout.addWidget(w)

#Asignamos el layout a la ventana
ventana.setLayout(layout)
#Mostramos la ventana
ventana.show()
#Ejecutamos la app
sys.exit(app.exec_())