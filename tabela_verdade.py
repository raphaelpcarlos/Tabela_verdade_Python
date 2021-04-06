from PyQt5 import QtCore, QtGui, QtWidgets
import conversoes
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(593, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_dois = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_dois.setObjectName("rd_dois")
        self.horizontalLayout.addWidget(self.rd_dois)
        self.rd_hum = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_hum.setObjectName("rd_hum")
        self.horizontalLayout.addWidget(self.rd_hum)
        self.rd_tres = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_tres.setObjectName("rd_tres")
        self.horizontalLayout.addWidget(self.rd_tres)
        self.rd_quatro = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_quatro.setObjectName("rd_quatro")
        self.horizontalLayout.addWidget(self.rd_quatro)
        self.rd_cinco = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_cinco.setObjectName("rd_cinco")
        self.horizontalLayout.addWidget(self.rd_cinco)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.area_texto = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.area_texto.setFont(font)
        self.area_texto.setMouseTracking(False)
        self.area_texto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.area_texto.setAutoFillBackground(False)
        self.area_texto.setObjectName("area_texto")
        self.gridLayout.addWidget(self.area_texto, 1, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_a = QtWidgets.QPushButton(self.centralwidget)
        self.btn_a.setObjectName("btn_a")
        self.verticalLayout_2.addWidget(self.btn_a)
        self.btn_b = QtWidgets.QPushButton(self.centralwidget)
        self.btn_b.setObjectName("btn_b")
        self.verticalLayout_2.addWidget(self.btn_b)
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setObjectName("btn_c")
        self.verticalLayout_2.addWidget(self.btn_c)
        self.btn_d = QtWidgets.QPushButton(self.centralwidget)
        self.btn_d.setObjectName("btn_d")
        self.verticalLayout_2.addWidget(self.btn_d)
        self.btn_e = QtWidgets.QPushButton(self.centralwidget)
        self.btn_e.setObjectName("btn_e")
        self.verticalLayout_2.addWidget(self.btn_e)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_and = QtWidgets.QPushButton(self.centralwidget)
        self.btn_and.setObjectName("btn_and")
        self.verticalLayout.addWidget(self.btn_and)
        self.btn_or = QtWidgets.QPushButton(self.centralwidget)
        self.btn_or.setObjectName("btn_or")
        self.verticalLayout.addWidget(self.btn_or)
        self.btn_not = QtWidgets.QPushButton(self.centralwidget)
        self.btn_not.setObjectName("btn_not")
        self.verticalLayout.addWidget(self.btn_not)
        self.btn_abre = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abre.setObjectName("btn_abre")
        self.verticalLayout.addWidget(self.btn_abre)
        self.btn_fechar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fechar.setObjectName("btn_fechar")
        self.verticalLayout.addWidget(self.btn_fechar)
        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)
        self.edt_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_valor.setObjectName("edt_valor")
        self.gridLayout.addWidget(self.edt_valor, 2, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_converter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_converter.setObjectName("btn_converter")
        self.horizontalLayout_2.addWidget(self.btn_converter)
        self.btn_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpar.setObjectName("btn_limpar")
        self.horizontalLayout_2.addWidget(self.btn_limpar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_limpar.clicked.connect(self.area_texto.clear)
        self.btn_limpar.clicked.connect(self.edt_valor.clear)
        self.btn_limpar.clicked.connect(self.label_3.clear)
        self.btn_limpar.clicked.connect(self.limpeza)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tabela Verdade"))
        self.rd_dois.setText(_translate("MainWindow", "Hum"))
        self.rd_hum.setText(_translate("MainWindow", "Dois"))
        #self.rd_dois.setChecked(True)
        self.rd_tres.setText(_translate("MainWindow", "Três"))
        self.rd_quatro.setText(_translate("MainWindow", "Quatro"))
        self.rd_cinco.setText(_translate("MainWindow", "Cinco"))
        self.label.setText(_translate("MainWindow", "Conversões"))
        self.btn_a.setText(_translate("MainWindow", "A"))
        self.btn_b.setText(_translate("MainWindow", "B"))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.btn_d.setText(_translate("MainWindow", "D"))
        self.btn_e.setText(_translate("MainWindow", "E"))
        self.btn_and.setText(_translate("MainWindow", "And ( ^ )"))
        self.btn_or.setText(_translate("MainWindow", "OR ( v )"))
        self.btn_not.setText(_translate("MainWindow", "NOT ( ~ )"))
        self.btn_abre.setText(_translate("MainWindow", "("))
        self.btn_fechar.setText(_translate("MainWindow", ")"))
        self.label_2.setText(_translate("MainWindow", "(A,B,C,D OU E) Ex: not a or ( b or not c ) "))
        self.btn_converter.setText(_translate("MainWindow", "Converter"))
        self.btn_limpar.setText(_translate("MainWindow", "Limpar"))

        self.btn_converter.clicked.connect(self.convert)

        self.btn_a.clicked.connect(self._a)
        self.btn_b.clicked.connect(self._b)
        self.btn_c.clicked.connect(self._c)
        self.btn_d.clicked.connect(self._d)
        self.btn_e.clicked.connect(self._e)
        self.btn_and.clicked.connect(self._and)
        self.btn_or.clicked.connect(self._or)
        self.btn_not.clicked.connect(self._not)
        self.btn_abre.clicked.connect(self._abre)
        self.btn_fechar.clicked.connect(self._fechar)

    entrada_texto = ' '

    def _a(self):
        self.entrada_texto = self.entrada_texto + 'a '
        self.edt_valor.setText(self.entrada_texto)
    def _b(self):
        self.entrada_texto = self.entrada_texto + 'b '
        self.edt_valor.setText(self.entrada_texto)
    def _c(self):
        self.entrada_texto = self.entrada_texto + 'c '
        self.edt_valor.setText(self.entrada_texto)
    def _d(self):
        self.entrada_texto = self.entrada_texto + 'd '
        self.edt_valor.setText(self.entrada_texto)
    def _e(self):
        self.entrada_texto = self.entrada_texto + 'e '
        self.edt_valor.setText(self.entrada_texto)
    def _and(self):
        self.entrada_texto = self.entrada_texto + 'and '
        self.edt_valor.setText(self.entrada_texto)

    def _or(self):
        self.entrada_texto = self.entrada_texto + 'or '
        self.edt_valor.setText(self.entrada_texto)

    def _not(self):
        self.entrada_texto = self.entrada_texto + 'not '
        self.edt_valor.setText(self.entrada_texto)

    def _abre(self):
        self.entrada_texto = self.entrada_texto + '( '
        self.edt_valor.setText(self.entrada_texto)

    def _fechar(self):
        self.entrada_texto = self.entrada_texto + ') '
        self.edt_valor.setText(self.entrada_texto)

    """Função para limpar os dados da tela"""
    def limpeza(self):

        self.entrada_texto = ''

    saida_tabela = ''

    """Função para realizar a conversão"""
    def convert(self):

        try:
            self.entrada_texto = self.edt_valor.text()

            self.teste()

            time.sleep(1)

            """Realiza a chamada da função entrada valor do pacote conversoes, informando nos parametros de entrada
               o valor digitado, convertendo em String e a quantidade de caracter digitado"""
            self.saida_tabela = str(conversoes.entrada_valor(str(self.entrada_texto), self.validacao_qtd()))

            self.area_texto.setText(self.saida_tabela)

            self.validacao_qtd()
            self.label_3.clear()
            self.edt_valor.clear()
            self.limpeza()

        except:

            self.label_3.setText("Erro de entrada. Informe um valor! ")

    """Função para retornar a quantidade de entradas do parametros. Este retorno se faz necessário para determinar os 
    valores de que serão informados para gerar a tabela"""
    def validacao_qtd(self):

        if self.rd_hum.isChecked():
            return 2
        if self.rd_dois.isChecked():
            return 1
        if self.rd_tres.isChecked():
            return 3
        if self.rd_quatro.isChecked():
            return 4
        if self.rd_cinco.isChecked():
            return 5

        """ Função para selecionar o radiobutton de acordo com a entrada de parametros. (até 5 entradas)"""
    def teste(self):
        teste = 'a','b','c','d','e'
        entrada_valor = self.entrada_texto.split()
        self.total = 0
        for letra in entrada_valor:

            if letra in teste:
                self.total = self.total+1

                if self.total == 1:
                    self.rd_dois.setChecked(True)
                if self.total == 2:
                    self.rd_hum.setChecked(True)
                if self.total == 3:
                    self.rd_tres.setChecked(True)
                if self.total == 4:
                    self.rd_quatro.setChecked(True)
                if self.total == 5:
                    self.rd_cinco.setChecked(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
