# Proyecto de Automatización de Reservas de Hotel

## Contexto del Proyecto

En el competitivo mundo de la tecnología y los servicios en línea, la automatización de pruebas se ha convertido en una herramienta esencial para garantizar la calidad y eficiencia de las aplicaciones web. En este caso de estudio, la tarea consiste en automatizar el proceso de reserva de un hotel en una página de reservas de vuelos y hoteles. La aplicación principal utilizada será **Booking.com**, aunque, en caso de indisponibilidad, se podrá emplear otra plataforma similar.

## Objetivo del Caso de Estudio

El objetivo principal de este caso de estudio es desarrollar un **script de automatización** que pueda realizar las siguientes tareas:

- **Simular el inicio de sesión en la plataforma** (opcional, puede omitirse si el tiempo no lo permite).
- **Realizar una reserva de hotel aplicando varios filtros y criterios.**

## Criterios de Búsqueda y Reservación

Para llevar a cabo la automatización, se han definido los siguientes filtros para la búsqueda y selección del hotel:

- **Destino:** Selección del sitio de viaje.
- **Fechas:**
  - **Check-in:** 2 días a partir de la fecha actual.
  - **Check-out:** 7 días a partir de la fecha actual.
- **Número de habitaciones:** 2.
- **Número de adultos:** 3.
- **Número de niños:** 2.
- **Rango de precio:** Superior a **\$200 USD por noche**.
- **Número de estrellas:** 3 o más.

### Selección del Hotel

- Luego de aplicar los filtros, el script deberá **seleccionar el hotel más barato** disponible en los resultados de búsqueda.
- Se debe **guardar toda la información del hotel seleccionado**.

##
