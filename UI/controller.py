import flet as ft

class Controller:
    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Il grafo è stato creato."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))
        self._view._txtIdOggetto.disabled = False
        self._view._btnCompConnessa.disabled = False
        self._view.update_page()

    def handleCompConnessa(self,e):
        txtInput = self._view._txtIdOggetto.value
        if txtInput == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un ID per usare questa funzione!",
                                                          color="red"))
            self._view.update_page()
            return
        try:
            idInput = int(txtInput)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un numero!"))
            self._view.update_page()
            return
        if not self._model.hasNode(idInput):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("L'ID inserito non corrisponde a nessun oggetto del database!"))
            self._view.update_page()
            return
        sizeCompConnessa = self._model.getInfoConnessa(idInput)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa, che contiene il nodo {self._model.getObjectFromId(idInput)}, ha dimensione pari a {sizeCompConnessa}."))
        self._view.update_page()