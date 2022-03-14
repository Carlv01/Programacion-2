import modelo
import vista


class axiomaTerminalController:
    def __init__(self):
        self.model = modelo.axiomaModel()
        self.view = vista.vistaAxiomasPorTerminal()

    def run(self):
        vNroDeAxiomaEscogido = int(self.view.escojeAxioma())
        vAxioma = self.model.obtenerAxioma(vNroDeAxiomaEscogido)
        self.view.mostrar(vAxioma)
        