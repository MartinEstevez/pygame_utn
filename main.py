import pygame

pygame.init()

# DIMENSIONES DE LA PANTALLA
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# COLORES
COLOR_TEXTO = (230, 230, 230)
COLOR_FONDO_BOTON = (10, 40, 90)

# RUTAS
RUTA_IMAGEN_MENU = "menu.png"
RUTA_IMAGEN_FONDO_JUEGO = "fondo.png"
RUTA_FAVICON = "favicon.png"
TITULO_JUEGO = "¿Quién quiere ser millonario?"

# CONFIGURACIÓN DE LA PANTALLA
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.RESIZABLE)
pygame.display.set_caption(TITULO_JUEGO)
pygame.display.set_icon(pygame.image.load(RUTA_FAVICON))

# FUENTES
fuente_titulo = pygame.font.Font(None, 64)
fuente_boton = pygame.font.Font(None, 32)

# FUNCIÓN PARA LOS BOTONES
def dibujar_boton(pantalla, rect_boton, texto, color_fondo, color_texto):
    pygame.draw.rect(pantalla, color_fondo, rect_boton)
    texto_render = fuente_boton.render(texto, True, color_texto)
    rect_texto = texto_render.get_rect(center=rect_boton.center) # PARA CENTRAR EL TEXTO EN EL RECTANGULO
    pantalla.blit(texto_render, rect_texto)
    return rect_boton

# MENU PRINCIPAL
pantalla_actual = "MENU"
botones_menu = ["NUEVA PARTIDA", "OPCIONES", "SALIR"]
ancho_boton = 300
alto_boton = 50
espacio_entre_botones = 20
y_botones = 220

# BUCLE PRINCIPAL
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # DETECTA EL CLIC
            mouse_pos = pygame.mouse.get_pos()
            if pantalla_actual == "MENU":
                for i in range(len(botones_menu)):
                    x = (ANCHO_PANTALLA - ancho_boton) / 2
                    y = y_botones + i * (alto_boton + espacio_entre_botones)
                    rect_boton = pygame.Rect(x, y, ancho_boton, alto_boton)

                    if rect_boton.collidepoint(mouse_pos):
                        if botones_menu[i] == "SALIR":
                            corriendo = False # CIERRA EL JUEGO AL HACER CLIC EN EL BOTON SALIR
                        elif botones_menu[i] == "NUEVA PARTIDA":
                            pantalla_actual = "EN_JUEGO" # PANTALLA DE JUEGO
                        else:
                            print("PROBLEMAS TECNICOS, FALTA CODEAR!!")

    # PANTALLA MENÚ
    if pantalla_actual == "MENU":
        fondo = pygame.image.load(RUTA_IMAGEN_MENU) # CARGAR IMAGEN
        fondo = pygame.transform.scale(fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
        pantalla.blit(fondo, (0, 0))

        # TÍTULO
        titulo_render = fuente_titulo.render("MENÚ PRINCIPAL", True, COLOR_TEXTO)
        ancho_titulo = titulo_render.get_width()
        x_titulo = (ANCHO_PANTALLA - ancho_titulo) / 2
        y_titulo = 120
        pantalla.blit(titulo_render, (x_titulo, y_titulo))

        # BOTONES
        for i in range(len(botones_menu)): # RECORREMOS LA LISTA DE BOTONES
            x = (ANCHO_PANTALLA - ancho_boton) / 2 # CALCULAMOS POSICIÓN HORIZONTAL
            y = y_botones + i * (alto_boton + espacio_entre_botones) # CALCULAMOS POSICIÓN VERTICAL
            rect_boton = pygame.Rect(x, y, ancho_boton, alto_boton)
            dibujar_boton(pantalla, rect_boton, botones_menu[i], COLOR_FONDO_BOTON, COLOR_TEXTO)

    # PANTALLA DE JUEGO
    elif pantalla_actual == "EN_JUEGO":
        fondo_juego = pygame.image.load(RUTA_IMAGEN_FONDO_JUEGO)
        fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO_PANTALLA, ALTO_PANTALLA))
        pantalla.blit(fondo_juego, (0, 0))

    pygame.display.update()

pygame.quit()
