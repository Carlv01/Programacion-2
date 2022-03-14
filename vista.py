class vistaAxiomas:
    
    def mostrar(self):
        pass
    
    def escojeAxioma(self):
        vResult = None
        vResult = int(input("Tipee el nro. de axioma que quiere ver: "))
        if vResult >= 1 and vResult <= 6:
         return vResult
        else:
             return "El número del axioma escogido, no está dentro de los permitidos que van desde (1-6) "
    
    
class vistaAxiomasPorTerminal(vistaAxiomas):
    
    def mostrar(self, vAxioma):
        print("y el axioma es: ", vAxioma)
        

class vistaAxiomasHTML(vistaAxiomas):
   
   def mostrar(self, vAxioma):
        vArchivoHtml = open('vistaMVC.html', 'w')

        vPlantilla = """
        <html>
        <head>
        <title> Telematica - Prog2 </title>
        </head>
        <body> 
        <h1>Modelo-Vista-Controlador (MVC)</h1>
        <h2>Vista html</h2>
        <table border="1">
        <tbody>
        <tr>
        <td>y el Axioma es: </td>
        </tr>
        <tr>
        <td>        
        """
        vPlantilla += vAxioma
        vPlantilla += """
        </td>
        </tr>
        </tbody>
        </table>
        </body>
        </html>
        """

        vArchivoHtml.write(vPlantilla)
        vArchivoHtml.close()