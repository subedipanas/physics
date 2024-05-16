from unit import Unit

class Units:
    m = Unit("m")
    s = Unit("s")
    kg = Unit("kg")
    N = Unit(symbol="N", components=[Unit("kg"), Unit("m"), Unit("s", -2)])