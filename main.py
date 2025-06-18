import pygame

pygame.init()

# DIMENSIONES DE LA PANTALLA
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# COLORES
COLOR_TEXTO = (230, 230, 230)
COLOR_BORDE_BOTON = (0, 156, 222)
COLOR_FONDO_BOTON = (0, 0, 0, 0)

# RUTAS
RUTA_IMAGEN_MENU = "menu.png"
RUTA_IMAGEN_FONDO_JUEGO = "fondo.png"
RUTA_FAVICON = "favicon.png"
TITULO_JUEGO = "¿Quién quiere ser millonario?"

# TITULO - FAVICON - PANTALLA
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.RESIZABLE)
pygame.display.set_caption(TITULO_JUEGO)
pygame.display.set_icon(pygame.image.load(RUTA_FAVICON))

# FUENTES
fuente_titulo = pygame.font.Font(None, 64)
fuente_boton = pygame.font.Font(None, 32)

# FUNCIONES

def dibujar_boton(pantalla, x, y, ancho, alto, texto, color_borde, color_texto):
    rect_boton = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, color_borde, rect_boton, border_radius=20, width=2)
    
    texto_render = fuente_boton.render(texto, True, color_texto)
    rect_texto = texto_render.get_rect(center=rect_boton.center)
    pantalla.blit(texto_render, rect_texto)
    
    return rect_boton

# DATOS

pantalla_actual = "MENU"
botones_menu = ["NUEVA PARTIDA", "CARGAR PARTIDA", "OPCIONES", "SALIR"]
ancho_boton = 300
alto_boton = 50
x_boton = 20  # ESPACIO X ENTRE LOS BOTONES
y_boton = 220  # ESPACIO Y INICIAL

# BUCLE PRINCIPAL
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if pantalla_actual == "MENU":
                for i in range(len(botones_menu)):
                    x = (ANCHO_PANTALLA - ancho_boton) // 2
                    y = y_boton + i * (alto_boton + x_boton)
                    rect_boton = pygame.Rect(x, y, ancho_boton, alto_boton)
                    if rect_boton.collidepoint(mouse_pos):
                        if botones_menu[i] == "SALIR":
                            corriendo = False
                        elif botones_menu[i] == "NUEVA PARTIDA":
                            pantalla_actual = "EN_JUEGO"
                        else:
                            print(f"Se seleccionó la opción: {botones_menu[i]}")

    # CARGA DE PANTALLAS
    if pantalla_actual == "MENU":
        fondo = pygame.image.load(RUTA_IMAGEN_MENU)
        fondo = pygame.transform.scale(fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
        pantalla.blit(fondo, (0, 0))

        # Título
        titulo_render = fuente_titulo.render("MENÚ PRINCIPAL", True, COLOR_TEXTO)
        rect_titulo = titulo_render.get_rect(center=(ANCHO_PANTALLA // 2, 120))
        pantalla.blit(titulo_render, rect_titulo)

        # Botones
        for i in range(len(botones_menu)):
            x = (ANCHO_PANTALLA - ancho_boton) // 2
            y = y_boton + i * (alto_boton + x_boton)
            dibujar_boton(pantalla, x, y, ancho_boton, alto_boton, botones_menu[i], COLOR_BORDE_BOTON, COLOR_TEXTO)

    elif pantalla_actual == "EN_JUEGO":
        fondo_juego = pygame.image.load(RUTA_IMAGEN_FONDO_JUEGO)
        fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO_PANTALLA, ALTO_PANTALLA))
        pantalla.blit(fondo_juego, (0, 0))

    pygame.display.flip()

pygame.quit()
