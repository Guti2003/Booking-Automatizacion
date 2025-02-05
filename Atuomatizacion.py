from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import tkinter as tk
from tkinter import simpledialog
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import locale
import time
import re
import pandas as pd
from bs4 import BeautifulSoup




service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://account.booking.com")

correo = "miguelguti2003@gmail.com"

time.sleep(5)


class Actor:

    #Constructor

    def __init__(self, driver):
        self.driver = driver

    #Inicio de sesion

    def popUp(self) :

        try:
            pop_Up = self.driver.find_element(By.XPATH, "//*[@id='b2indexPage']/div[45]/div/div/div/div[2]/div/a") 
            pop_Up.click()
            print("Funciono")
            return True
        except NoSuchElementException : 
            print("No se ejecuto")
            return False


    def Login(self):
        try:
            boton = self.driver.find_element(By.XPATH, "//*[@id='b2indexPage']/div[2]/div/div/header/div/nav[1]/div[2]/div")
            self.driver.execute_script("arguments[0].click();", boton)
        except NoSuchElementException:
            print("No se encontro boton de logeo")

    def Credenciales(self):

        root = tk.Tk()

        root.withdraw()

        Cod = simpledialog.askstring("Codigo", "Ingresalo Aqui")

        divPadre = self.driver.find_element(By.ID, "otp_input")

        divHijos = divPadre.find_elements(By.XPATH, ".//div//div//div//input")

        if len(divHijos) >= len(Cod):
    
            for campo, letra in zip(divHijos, Cod):
                campo.send_keys(letra)

    def ingresarCorreo(self, correo):
        campo = self.driver.find_element(By.XPATH, "//*[@id='username']")
        campo.send_keys(correo)
        boton = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/div/div/div/div/div/div/form/div[2]/button")
        boton.click()
    
    def botonIngresar(self) :

        boton = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/div/div/div/div/div/div/form/div/button[1]")
        boton.click()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #Cambiar a COP a USD

    def cambioDeMoneda(self):

        time.sleep(5)

        boton = self.driver.find_element(By.XPATH, "//*[@id='b2indexPage']/div[2]/div/div/header/div/nav[1]/div[2]/span[1]/button")

        boton.click()

        botonUsd = self.driver.find_element(By.XPATH, "//*[@id='header_currency_picker']/div/div/div[2]/div/div[2]/div/div/ul[1]/li[1]/button")

        botonUsd.click()

        time.sleep(3)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #Filtro


    def activarLista(self):

        time.sleep(3)
        barra = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/form/div/div[3]/div/button")
        barra.click()

    def adultos (self, numero) :

        for i in range(numero):

            sumar = self.driver.find_element(By.CSS_SELECTOR, ".a83ed08757.c21c56c305.f38b6daa18.d691166b09.ab98298258.bb803d8689.f4d78af12a") 
            sumar.click()

    def ninos (self, numero2):

        for i in range(numero2) :
            
            sumar = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/form/div/div[3]/div/div/div/div/div[2]/div[2]/button[2]")
            sumar.click()

    def edad1 (self,valor):

        listaDesplegable = self.driver.find_element(By.XPATH, "(//select[@class='ebf4591c8e'])")
        select = Select(listaDesplegable)
        select.select_by_value(valor)

        
            

    def edad2 (self,valor):

        try:
            popUp = self.driver.find_element(By.CLASS_NAME, "b067f3afe2 b3c059c742")

            if popUp :
                listaDesplegable = self.driver.find_element(By.XPATH, "(//select[@class='ebf4591c8e'])[2]")
                select = Select(listaDesplegable)
                select.select_by_value(valor)

        except NoSuchElementException:

            barra = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/form/div/div[3]/div/button")
            barra.click()

            listaDesplegable = self.driver.find_element(By.XPATH, "(//select[@class='ebf4591c8e'])[2]")
            select = Select(listaDesplegable)
            select.select_by_value(valor)

    def habitaciones (self, numero) :

        barra = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/form/div/div[3]/div/button")
        barra.click()

        for i in range(numero):
            dynamic_xpath = '//*[starts-with(@id, ":r")]/div/div[5]/div[2]/button[2]'
            sumar = self.driver.find_element(By.XPATH, dynamic_xpath)
            sumar.click()

    def botonListo(self):

        boton = self.driver.find_element(By.CSS_SELECTOR, ".a83ed08757.c21c56c305.bf0537ecb5.ab98298258.a2abacf76b.af7297d90d.c213355c26.b9fd3c6b3c")
        boton.click()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Validacion Check In y Check Auto

    def fechas(self):

        divBotonFecha = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/form/div/div[2]/div")

        divBotonFecha.click()

        divMes = self.driver.find_element(By.XPATH, "//*[@id='calendar-searchboxdatepicker']/div/div[1]/div/div[1]/h3")

        contenidoMes = divMes.text


        try:
            locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
        except locale.Error:
            locale.setlocale(locale.LC_TIME, "Spanish_Spain.1252")
    
        fechaActual = datetime.now()

        mes = fechaActual.strftime("%B/%Y").lower()

        mesRemplazado = mes.replace("/" , " ")

        dia = int(fechaActual.strftime("%d").lower())

        if contenidoMes == mesRemplazado :
            
            checkIn = dia + 2

            checkOut = dia + 7

            contenedorPadreTable = self.driver.find_element(By.XPATH, "//*[@id='calendar-searchboxdatepicker']/div/div[1]/div/div[1]/table/tbody")
            
            divHijos = contenedorPadreTable.find_elements(By.XPATH, ".//tr/td/span/span")

            for hijos in divHijos:

                if hijos.text.isdigit() and int(hijos.text) == checkIn:
                    self.driver.execute_script("arguments[0].click();", hijos)
                    break
            
            for hijos2 in divHijos:

                if hijos2.text.isdigit() and int(hijos2.text) == checkOut:
                    self.driver.execute_script("arguments[0].click();", hijos2)
                    break


        else:

            botonCambiarMes = self.driver.find_element(By.XPATH, "//*[@id=':R4ll1995:']/div/div/div/div/button[1]")
            botonCambiarMes.click()

            checkIn = dia + 2

            checkOut = dia + 7

            contenedorPadreTable = self.driver.find_element(By.XPATH, "//*[@id=':R4ll1995:']/div/div/div/div/div/div[1]/table/tbody")
            
            divHijos = contenedorPadreTable.find_elements(By.XPATH, ".//tr/td/span/span")

            for hijos in divHijos:

                if hijos.text.isdigit() and int(hijos.text) == checkIn:
                    self.driver.execute_script("arguments[0].click();", hijos)
                    break

            for hijos2 in divHijos:

                if hijos2.text.isdigit() and int(hijos2.text) == checkOut:
                    self.driver.execute_script("arguments[0].click();", hijos2)
                    break

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Destino

    def destino(self) :

        barraBusqueda = self.driver.find_element(By.CLASS_NAME, "eb46370fe1") 

        

        root = tk.Tk()

        root.withdraw()

        destino = ""

        destino = simpledialog.askstring("destino", "Escriba su destino")

        try :

            borrar = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/form/div/div[1]/div/div/div[1]/div/div/div[3]/button")

            borrar.click()
        except NoSuchElementException:
            print("No hay x")

        barraBusqueda.send_keys(destino)

        time.sleep(5)

        primeraOpcion = self.driver.find_element(By.ID, "autocomplete-result-0")

        boton = primeraOpcion.find_element(By.XPATH, ".//div")

        self.driver.execute_script("arguments[0].click();", boton)
    


    def buscar(self):

        boton = self.driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/form/div/div[4]/button")

        boton.click()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ultimo filtro
    
    def rangoPrecio(self):

        time.sleep(5)

        dynamic_xpath = '//*[starts-with(@id, "filter_group_price_")]/fieldset/div[2]/span/div'
        valor = driver.find_element(By.XPATH, dynamic_xpath)

        botonP = self.driver.find_element(By.CLASS_NAME, "f3c828a390")

        boton = botonP.find_element(By.XPATH, ".//div")

        primer_precio = valor.text

        primer_precio_Match = re.search(r"US\$\d+", primer_precio)

        actions = ActionChains(self.driver)

        
        if primer_precio_Match:
            resultado = primer_precio_Match.group()
            numero = int(resultado.replace("US$", ""))

            while True:
                if numero == 200:
                    break
                elif numero > 200:

                    actions.click_and_hold(boton).move_by_offset(-10, 0).release().perform()
                    time.sleep(0.2)

                else:
                    actions.click_and_hold(boton).move_by_offset(35, 0).release().perform()
                    time.sleep(0.05)
            
                dynamic_xpath = '//*[starts-with(@id, "filter_group_price_")]/fieldset/div[2]/span/div'
                valor = driver.find_element(By.XPATH, dynamic_xpath)
                primer_precio = valor.text
                primer_precio_Match = re.search(r"US\$\d+", primer_precio)
                resultado = primer_precio_Match.group()
                numero = int(resultado.replace("US$", ""))
                    
        else:
            print("No entro")
    

    def ordenarPor(self):
        # dynamic_xpath = '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/div/span/button'

        boton = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='sorters-dropdown-trigger']")
        boton.click()

        listaD = self.driver.find_element(By.CLASS_NAME, "ad7c39949a")

        hijosListaD = listaD.find_elements(By.XPATH, ".//li/button/div/div/span")

        for hijos in hijosListaD:

            textoHijos = hijos.text.lower()

            textoEncontrado = "Precio (más bajo primero)".lower()
            
            if textoHijos == textoEncontrado:
                hijos.click()
                break
    

    def agregarEstrellas(self):

        dynamic_xpath = '//*[starts-with(@id, "filter_group_class_:r")]/fieldset'

        Checks = self.driver.find_element(By.XPATH, dynamic_xpath) 

        ChecksHijo = Checks.find_elements(By.XPATH, ".//div")

        textoCheck3 = "3 estrellas".lower()
        textoCheck4 = "4 estrellas".lower()
        textoCheck5 = "5 estrellas".lower()


        for titulos in ChecksHijo:

            try:
                
                parrafo = titulos.find_element(By.XPATH, ".//label/span[3]/div/div/div/div/div")
                texto = parrafo.text.strip()  

                
                if texto == textoCheck3 or texto == textoCheck4 or texto == textoCheck5:
                    
                    self.driver.execute_script("arguments[0].click();", parrafo)

            except NoSuchElementException:
                print("Otro div")
        
        
        
        
        
        

    def primeroDeLaLista(self):

        

        divPrincipal = self.driver.find_elements(By.XPATH, "//*[@class='d4924c9e74' and @role='list']")

        for hijo in divPrincipal:

            

            try:
                
                titulo = hijo.find_element(By.XPATH, ".//*[contains(@data-testid, 'title-link')]")
                
                time.sleep(5)
                titulo.click()
                
                break
            except NoSuchElementException:
                print("Otro div no se encontro")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pandas

    def crearExcel(self):
        ventana_original = self.driver.current_window_handle

        for ventana in self.driver.window_handles:
            if ventana != ventana_original:
                self.driver.switch_to.window(ventana)
                break

        contenedorTitulo = self.driver.find_element(By.XPATH, '//*[@id="hp_hotel_name"]/div/h2')

        tableHTML = self.driver.find_element(By.CLASS_NAME, "hp-group_recommendation__table")

        titulo = contenedorTitulo.text

        filas = tableHTML.find_elements(By.TAG_NAME, "tr")

        informacion_habitacion = []

        for fila in filas:
            columnas = fila.find_elements(By.TAG_NAME, "td")
            fila_datos = [columna.text for columna in columnas]

            texto_limpio = [BeautifulSoup(texto, 'html.parser').get_text().strip() for texto in fila_datos]

            texto_limpio = [texto for texto in texto_limpio if texto and texto != "Reserva tu selección"]

            texto_limpio = [texto.replace("\n", " ").replace("['", "").replace("']", "") for texto in texto_limpio]


            if texto_limpio:
                informacion_habitacion.append(texto_limpio)

        datos = {
            titulo: informacion_habitacion  
        }

        tabla = pd.DataFrame(datos)

        tabla.to_excel('informacion_hotel.xlsx', index=False)

        print("¡Archivo Excel creado exitosamente con los datos del hotel!")  




actor = Actor(driver)

# if actor.popUp():
#     print("Se manejo el popUp")
# else:
#     actor.Login()

# actor.ingresarCorreo(correo)

# actor.Credenciales()

# actor.botonIngresar()

# time.sleep(5)

# actor.cambioDeMoneda()

driver.get("https://www.booking.com/index.es.html?aid=304142&label=gen173bo-1DCA8oggI46AdIMVgDaDKIAQGYAQq4ARfIAQzYAQPoAQH4AQaIAgGYAiGoAgO4Asu3l7wGwAIB0gIkZmY4NjhjNmEtMTI3ZC00OTUwLWJlZGUtODNmNDcxM2E0NjJk2AIE4AIB&sid=e74477c0446132edda06d241bfe071e3&auth_success=1&selected_currency=USD")

time.sleep(5)

actor.activarLista() 

actor.adultos(1)

actor.ninos(2)

actor.edad1("3")

actor.edad2("6")

actor.habitaciones(1)

actor.botonListo()

actor.fechas()


actor.destino()

actor.buscar()

actor.rangoPrecio()

time.sleep(1)

actor.ordenarPor()

actor.agregarEstrellas()

time.sleep(10)

actor.primeroDeLaLista()

time.sleep(5)

actor.crearExcel()

driver.quit()



