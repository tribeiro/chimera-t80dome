# This is an example of an simple instrument.

from chimera_astelco.instruments.astelcodome import AstelcoDome
from chimera_commander.instruments.skdomefan import SKDomeFan

class T80Dome(AstelcoDome,SKDomeFan):
    __config__ = {"param1": "a string parameter"}

    def __init__(self):
        AstelcoDome.__init__()

