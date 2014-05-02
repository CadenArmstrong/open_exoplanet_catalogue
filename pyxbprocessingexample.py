import oecbinding

xml = open("systems/Kepler-20.xml").read()
obj = oecbinding.CreateFromDocument(xml)

# obj is the entire system object
print("System properties------------")
print("System name:" + obj.name[0])
print("Distance:" + str(obj.distance[0].value()))
print("Right ascension:" + obj.rightascension[0])
print("Declination:" + obj.declination[0])
for star in obj.star:
    # star is a new obj
    print("Star--------")
    print("Name:"+ star.name[0])
    print("Temperature:"+ str(star.temperature[0].value()))
    for planet in star.planet:
        print("     planet-------")
        print("     Name:"+ planet.name[0])
        try:
            print("     Mass:" + str(planet.mass[0].value()))
        except:
            pass
