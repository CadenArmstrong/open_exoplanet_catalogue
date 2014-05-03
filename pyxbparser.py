import oecbinding

def get_pyxb(filepath):
	return oecbinding.CreateFromDocument(open(filepath).read())

def print_system(pyxb):

	print("System name: " + pyxb.name[0])
	print("Distance: " + str(pyxb.distance[0].value()))
	print("Right ascension: " + pyxb.rightascension[0])
	print("Declination: " + pyxb.declination[0])
	for star in pyxb.star:
	    # star is a subobject of pyxb
            for names in star.name:
                print("Star Name: "+ names)
	    try:	
	    	print("Temperature: "+ str(star.temperature[0].value()))
            except:
                pass
	    try:	
	    	print("Semimajor axis: "+ str(star.semimajoraxis[0].value()))
            except:
                pass
	    try:	
	    	print("Eccentricity: "+ str(star.eccentricity[0].value()))
            except:
                pass
	    try:	
	    	print("Periastron: "+ str(star.periastron[0].value()))
            except:
                pass
	    try:	
	    	print("Longitude: "+ str(star.longitude[0].value()))
            except:
                pass
	    try:	
	    	print("Ascending node: "+ str(star.ascendingnode[0].value()))
            except:
                pass
	    try:	
	    	print("Inclination: "+ str(star.inclination[0].value()))
            except:
                pass
	    try:	
	    	print("Period: "+ str(star.period[0].value()))
            except:
                pass
	    try:	
	    	print("transittime: "+ str(star.transittime[0].value()))
            except:
                pass
	    try:	
	    	print("magB: "+ str(star.magB[0].value()))
            except:
                pass
	    try:	
	    	print("magV: "+ str(star.magV[0].value()))
            except:
                pass
	    try:	
	    	print("magI: "+ str(star.magI[0].value()))
            except:
                pass
	    try:	
	    	print("magJ: "+ str(star.magJ[0].value()))
            except:
                pass
	    try:	
	    	print("magH: "+ str(star.magH[0].value()))
            except:
                pass
	    try:	
	    	print("magK: "+ str(star.magK[0].value()))
            except:
                pass
	    try:	
	    	print("magR: "+ str(star.magR[0].value()))
            except:
                pass
	    try:	
	    	print("metallicity: "+ str(star.metallicity[0].value()))
            except:
                pass
	    try:	
	    	print("Spectral type: "+ str(star.spectraltype[0]))
            except:
                pass
	    try:	
	    	print("Age: "+ str(star.age[0].value()))
            except:
                pass
	    try:	
	    	print("Radius: "+ str(star.radius[0].value()))
            except:
                pass
	    try:	
	    	print("Mass: "+ str(star.mass[0].value()))
            except:
                pass

	    for planet in star.planet:
                for names in planet.name:
                    print("    Planet Name: "+ names)
		try:
		    print("        Mass:" + str(planet.mass[0].value()))
		except:
		    pass
                try:	
                    print("        Temperature: "+ str(planet.temperature[0].value()))
                except:
                    pass
                try:	
                    print("        Semimajor axis: "+ str(planet.semimajoraxis[0].value()))
                except:
                    pass
                try:	
                    print("        Eccentricity: "+ str(planet.eccentricity[0].value()))
                except:
                    pass
                try:	
                    print("        Periastron: "+ str(planet.periastron[0].value()))
                except:
                    pass
                try:	
                    print("        Longitude: "+ str(planet.longitude[0].value()))
                except:
                    pass
                try:	
                    print("        Ascending node: "+ str(planet.ascendingnode[0].value()))
                except:
                    pass
                try:	
                    print("        Inclination: "+ str(planet.inclination[0].value()))
                except:
                    pass
                try:	
                    print("        Period: "+ str(planet.period[0].value()))
                except:
                    pass
                try:	
                    print("        transittime: "+ str(planet.transittime[0].value()))
                except:
                    pass
                try:	
                    print("        metallicity: "+ str(planet.metallicity[0].value()))
                except:
                    pass
                try:	
                    print("        Spectral type: "+ str(planet.spectraltype[0]))
                except:
                    pass
                try:	
                    print("        Age: "+ str(planet.age[0].value()))
                except:
                    pass
                try:	
                    print("        Radius: "+ str(planet.radius[0].value()))
                except:
                    pass

print_system(get_pyxb("systems/Kepler-20.xml"))
