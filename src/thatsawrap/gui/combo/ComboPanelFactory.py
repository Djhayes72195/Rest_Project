from src.thatsawrap.data.order.ComboBuilder import ComboBuilder
from src.thatsawrap.gui.combo.ComboPanel import ComboPanel


class ComboPanelFactory:


    @staticmethod
    def get_panel(window, str_name: str) -> object:
        return ComboPanel(master=window, item=ComboBuilder().build_combo(str_name))
