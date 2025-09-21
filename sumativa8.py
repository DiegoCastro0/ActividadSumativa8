#import PyQt5
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox,QComboBox,QCheckBox)
import sys
from PyQt5.QtGui import QPixmap

resultados = []


def mensaje():
    nombre = nombre2.text()
    gruposelec = grupo.currentText()
    try:
        n1 = float(nota1.text())
        n2 = float(nota2.text())
        n3 = float(nota3.text())
        promedio = (n1 + n2 + n3) / 3
        
        
        if promedio >= 7:
            estado = " Aprobado"
        elif promedio >= 5:
            estado = " En riesgo"
        else:
            estado = " Reprobado"

        resultados.append(f"{nombre} ({gruposelec}): {promedio:.2f} - {estado}")
        historial.setText("Historial de promedios:\n" + "\n".join(resultados))



        QMessageBox.information(ventana, "Resultado",
                                f"El promedio del estudiante {nombre} ({gruposelec}) es: {promedio:.2f}")
    except ValueError:
        QMessageBox.warning(ventana, "Error", "Por favor ingresa solo números válidos.")



def actualizar():
    if filtro.isChecked():
        filtrados = [r for r in resultados if "Aprobado" in r]
        historial.setText("Historial de promedios (solo aprobados):\n" + "\n".join(filtrados))
    else:
        historial.setText("Historial de promedios:\n" + "\n".join(resultados))


app = QApplication(sys.argv)
ventana = QWidget()
#Propiedades de una ventana
ventana.setWindowTitle("Calculadora de promedio")
ventana.setGeometry(100,100,700,300)
layout = QVBoxLayout()


info = QLabel("Esta es una calculadora de promedio de 3 actividades/notas para estudiantes")
nombre = QLabel("Nombre del alumno")
nombre2 = QLineEdit()

GLs = QLabel("Selecciona el grupo")
grupo = QComboBox()
grupo.addItems(["Grupo A1", "Grupo A2", "Grupo A3"])


nota1 = QLineEdit()
info2 = QLabel("Ingresa las 3 notas")
nota1 = QLineEdit()
nota2 = QLineEdit()
nota3 = QLineEdit()
boton = QPushButton("Calcular promedio")
boton.clicked.connect(mensaje)
filtro = QCheckBox("Mostrar solo aprobados")
filtro.stateChanged.connect(actualizar)

imagen = QLabel()
pixmap = QPixmap("promedio.jpg")
pixmap = pixmap.scaled(300, 300, aspectRatioMode=1)  
imagen.setPixmap(pixmap) 
  
historial = QLabel("Historial de promedios:")


widgets = [info,nombre,nombre2,GLs, grupo,info2,nota1,nota2,nota3, boton,filtro, imagen,historial]
for w in widgets:
    layout.addWidget(w)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())