from math import log2

from flet.core.types import Number

from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNMax(self):
        return self._model._NMax

    def getTMax(self):
        return self._model._TMax

    def reset(self,e ):
        self._model.reset()
        self._view._txtOutT.value = self._model._T
        self._view._lv.controls.clear()
        self._view._lv.controls.append(ft.Text("Indovina a quale numero sto pensando!"))
        self._view._btnReset.disabled = False
        self._view._btnPlay.disabled = False
        self._view._txtIn.disabled = False
        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txtIn.value
        self._view._txtIn.value = ""
        self._view._txtOutT.value = self._model._T -1
        self._view.update()
        if tentativoStr == "":
            self._view._lv.controls.append(ft.Text("Attenzione, inserisci un valore numero da testare"), color="red")
            self._view.update()
            return
        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Attenziome, l valore inserito non è un intero", color="red"))
            return

        res = self._model.play(tentativoInt)
        if res == 0: #Ho vinto
            self._view._lv.controls.append(ft.Text(f"Hai vinto! Il segreto era {tentativoInt}",color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == 2: #Ho finito tutte le vite
            self._view._lv.controls.append(ft.Text(f"Mi dispiace hai finito le vite, il segreto era{self._model._segreto}"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
        elif res == -1: #il mio segreto è più piccolo
            self._view._lv.controls.append(ft.Text(f"Il segreto è più piccolo di {tentativoInt}"))
            self._view.update()
        else:
            self._view._lv.controls.append(ft.Text(f"Il segreto è più grande di {tentativoInt}"))
            self._view.update()

