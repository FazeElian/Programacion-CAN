import groups #Importación archivo groups

#Definición de formulario y/o variables del mismo (características o items)
def form(nombre, apodo, nacionalidad, dorsal, equipo, goles, asistencias = "Stable"): #Definición Variables de características de cada ítem (jugador)

    #Definición de variables (tipo de variable: entero, cadena de texto, decimal, etc)
        nombre = str("nombre")
        apodo = str("apodo")
        nacionalidad = str("-nacionalidad")
        dorsal = str("dorsal")
        equipo = str("equipo")
        goles = str("goles")
        asistencias = str("asistencias")  
          
        #Result de cada variable tipo característica
        result = "\nnombre:{} \napodo:{} \ndorsal:{} \nequipo:{} \ngoles:{} \nasistencias:{}".format(nombre, apodo, equipo, dorsal, goles, asistencias)
        return result

#Elementos: Información de cada ítem puesto al principio antes del "form"
#Los elementos están  según la posición del result y el formulario
Elements = { #Jugadores
            "1. Cristiano Ronaldo":
             form("Cristiano Ronaldo Dos Santos Aveiro", "El Bicho", "Portugués", "7", "577", "251"),
            "2. Lionel Messi":
             form("Lionel Andrés Messi Cuccittini", "La Pulga", "Argentino", "10", "800", "328"),
            "3. Pelé":
             form("Edson Arantes do Nascimento", "Rey", "Brasileño", "10", "757", "30"),
            "4. Maradona":
             form("Diego Armando Maradona", "Pelusa", "Argentino", "10", "345", "262"),
            "5. Cruyff":
             form("Hendrik Johannes Cruijff", "El Tulipán de Oro", "Holandés", "14", "371", "40"),
            "6. Zidane":
             form("Zinédine Yazid Zidane", "Zizou", "Francés", "5", "151", "28"),
            "7. Beckenbauer":
             form("Franz Anton Albert Beckenbauer", "El Káiser","Aleman", "6", "103", "19"),
            "8. Di Stéfano":
             form("Alfredo Stéfano Di Stéfano Laulhé", "La Saeta Rubia","Argentino", "9", "308", "34"),
            "9. Ronaldo Nazário":
             form("Ronaldo Luís Nazário de Lima", "El Fenómeno","brasileño", "9", "715", "35"),
            "10. George Best":
             form("Ronald Samuel", "El Chico de Belfast","norirlandés", "7", "36", "12"),
    }