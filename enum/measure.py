class MeasureType:
        ONBEKEND = 0
        ALGEMENE_MAATREGEL = 1
        ONGEDEFINIEERD = 255

class SubMeasureType:
	EXTRA_VERVOER = '0'
	VERVALLEN_HALTE = '1'
	VERVANGENDE_HALTE = '2'
	RIJDEN_VIA_OMWEG = '3'
	GEEN_BUSINZET = '4_1'
	BEPERKTE_BUSINZET = '4_2'
	BUSINZET = '4_3'
	GEEN_TREINEN = '5_1'
	MINDER_TREINEN = '5_2'
	TREINEN_RIJDEN_VIA = '5_3'
	GEEN = '6'
	ROUTE_AANGEPAST = '7'
