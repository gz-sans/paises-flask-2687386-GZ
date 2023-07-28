from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hola')
def index():
    return 'hola 2687386'

@app.route('/paises')
def paises():
    '''Lista en python'''
    continentes = [
                { 
                     
                    "nombre":"America",
                    "paises":[
                    {
                        "nombre":"Colombia",
                        "capital":"Bogota",
                        "moneda":"Peso",                                     
                       "poblacion":60,
                       "superficie":1000000

                    },
                    { 
                        "nombre":"Peru",
                        "capital":"Lima",
                        "moneda":"Sol",
                       "poblacion":60,
                       "superficie":1000000

                    }    
                    ]
                },
                {
                   "nombre":"Europa",
                    "paises":[
                    { 
                            "nombre":"Reino Unido",
                            "capital":"Londres",
                            "moneda":"Libra",
                           "poblacion":60,
                       "superficie":1000000


                    },
                    { 
                            "nombre":"Francia",
                            "capital":"Londres",
                            "moneda":"Euros",
                           "poblacion":60,
                       "superficie":1000000


                    }   
                    ]

                },
                {
                    "nombre":"Asia",
                     "paises":[
                        { 
                            "nombre":"China",
                            "capital":"shangay",
                            "moneda":"yuan",
                           "poblacion":60,
                       "superficie":1000000


                        },
                        {
                            "nombre":"Japon",
                            "capital":"Pekin",
                            "moneda":"yen",
                           "poblacion":60,
                       "superficie":1000000

                        }

                     ]
                }
         ]
    
    for continente in continentes:
       longitud=len(continente["nombre"])
    
    print(longitud)
    user = 'kevin luis'
    return render_template('paises_listas.html',
                           dato = user,
                           continentes=continentes,
                           tamaño=longitud
                           
                           ) 