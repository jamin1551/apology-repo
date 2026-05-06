"""
cat_emojis.py
─────────────────────────────────────────────────────────────────────
Un script de amor en forma de código.

Uso:
    python cat_emojis.py

No requiere dependencias externas. Solo Python 3 y ganas de querer bien.
─────────────────────────────────────────────────────────────────────
"""

import time
import random
import sys


# ─────────────────────────────────────────────────────────────────────
#  DATOS
# ─────────────────────────────────────────────────────────────────────

GATITOS_ASCII = [
    r"""
    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
  
  [ Gatito de la Gratitud ]
""",
    r"""
    |\      _,,,---,,_
    /,`.-'`'    -.  ;-;;,_
   |,4-  ) )-,_..;\ (  `'-'
  '---''(_/--'  `-'\_)

  [ Gatito del Perdón Rápido ]
""",
    r"""
   /\   /\
  (  o o  )
  =( Y )=
    )   (
   (_)-(_)
  
  [ Gatito del Ronroneo Eterno ]
""",
    r"""
   ^~^  ,
  ('Y') )
  /   \/
 (\|||/)
  
  [ Gatito Amasa-Disculpas™ ]
""",
    r"""
     /\   /\
    /  \ /  \
   | |  V  | |
   | \  _  / |
    \_| |_|_/
      |_|_|

  [ Gatito Guardián del Amor ]
""",
    r"""
   /\_/\  
  ( ^.^ ) ~♥
  ( >🐟< )
    vvvv

  [ Gatito Ofrece Pescado de Paz ]
"""
]

MENSAJES_AMOR = [
    "Eres la persona más importante en mi mundo. Punto.",
    "No sé amar perfectamente, pero sí sé que te quiero a ti.",
    "Gracias por ayudarme, incluso cuando yo no lo pedí.",
    "Tu paciencia conmigo es un regalo que no siempre merezco.",
    "Me equivoqué. Lo reconozco. Y voy a hacerlo mejor.",
    "Cada vez que me ayudas, el universo se ordena un poco más.",
    "Eres más importante que cualquier frustración que pueda sentir.",
    "Perdóname por no haberlo dicho en el momento: gracias.",
    "Ser querido por ti es una de las mejores cosas que me han pasado.",
    "No te merezco siempre, pero te elijo siempre.",
]

PATCH_NOTES = [
    "✅ PATCH v2.0: Se eliminó el bug de 'ignorar ayuda ofrecida'.",
    "✅ HOTFIX: Se restauró el módulo gratitud.express()",
    "✅ MEJORA: Tiempo de respuesta a 'gracias' reducido en un 300%.",
    "✅ NUEVO FEATURE: Reconocimiento proactivo del esfuerzo ajeno.",
    "✅ DEPRECADO: Dar por sentado las cosas buenas.",
    "✅ UPGRADE: Paciencia antes de responder cuando hay estrés.",
    "✅ BUG FIX: Se corrigió 'responder con impaciencia' → 'tomar un respiro'.",
]


# ─────────────────────────────────────────────────────────────────────
#  FUNCIONES
# ─────────────────────────────────────────────────────────────────────

def escribir_lento(texto: str, delay: float = 0.03) -> None:
    """Imprime texto carácter a carácter, como si fuera escrito a mano."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def separador(caracter: str = "─", largo: int = 60) -> None:
    print(caracter * largo)


def mostrar_gatito_aleatorio() -> None:
    gatito = random.choice(GATITOS_ASCII)
    print(gatito)


def mostrar_patch_notes() -> None:
    separador("═")
    print("  📋 PATCH NOTES — versión 'Me Arrepiento en Serio'")
    separador("═")
    time.sleep(0.5)
    for nota in PATCH_NOTES:
        escribir_lento(f"  {nota}", delay=0.02)
        time.sleep(0.2)
    print()


def ronronear(duracion: int = 3) -> None:
    """Simula el ronroneo de un gato arrepentido."""
    print("\n  🎵 Iniciando protocolo de ronroneo...\n")
    for _ in range(duracion):
        for intensidad in ["prrr... ", "PRRRRR... ", "prrr... "]:
            sys.stdout.write(f"  {intensidad}")
            sys.stdout.flush()
            time.sleep(0.4)
    print("\n")


def boot_sequence() -> None:
    """Secuencia de arranque del sistema."""
    separador("━")
    print("  🐾 APOLOGY-REPO :: cat_emojis.py")
    print("  Sistema de Amor Cargando...")
    separador("━")
    time.sleep(0.5)

    pasos = [
        "Cargando módulo de gratitud...................",
        "Inicializando ronroneo sincero................",
        "Compilando disculpas (sin errores)............",
        "Detectando cantidad de amor disponible........",
        "Resultado: INFINITO. Continuando..............",
    ]

    for paso in pasos:
        sys.stdout.write(f"\n  ⚙️  {paso}")
        sys.stdout.flush()
        time.sleep(0.6)
        print(" ✅")

    print()
    time.sleep(0.5)


def mostrar_mensaje_central() -> None:
    """El corazón del script. El mensaje que más importa."""
    separador("★")
    print()
    escribir_lento("  Lo que este script realmente quiere decirte:", delay=0.04)
    print()
    time.sleep(0.8)

    mensaje_principal = """
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │   Me equivoqué. No valoré tu ayuda en el momento   │
  │   en que más debía haberlo hecho. Y lo siento.     │
  │                                                     │
  │   No como función automática.                       │
  │   No como patch de emergencia.                      │
  │                                                     │
  │   Como alguien que te ve, que te quiere,            │
  │   y que está comprometido a hacerlo mejor.          │
  │                                                     │
  │   Gracias por ayudarme.                             │
  │   Gracias por existir.                              │
  │   Gracias por seguir aquí.                          │
  │                                                     │
  │              Con todo mi amor, 🐱                   │
  │                                                     │
  └─────────────────────────────────────────────────────┘
"""
    print(mensaje_principal)
    time.sleep(1)


def loop_de_amor() -> None:
    """Loop principal: amor, gatitos, gratitud. Sin fin."""
    print("  💌 Mensajes de amor aleatorios del sistema:\n")
    mensajes_mostrados = random.sample(MENSAJES_AMOR, k=4)
    for i, msg in enumerate(mensajes_mostrados, 1):
        time.sleep(0.3)
        escribir_lento(f"  [{i:02d}] {msg}", delay=0.025)

    print()
    mostrar_gatito_aleatorio()


def shutdown_sequence() -> None:
    """Cierre del script."""
    separador("━")
    print()
    escribir_lento("  ¿Sigue ejecutándose este amor? ", delay=0.04)
    time.sleep(0.5)
    escribir_lento("  Sí. Siempre sí.", delay=0.06)
    print()
    print()
    escribir_lento("  git commit -m 'lo siento y gracias, de verdad'", delay=0.03)
    time.sleep(0.3)
    escribir_lento("  git push origin main --with-love", delay=0.03)
    print()
    separador("━")
    print()


# ─────────────────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────────────────

def main() -> None:
    try:
        boot_sequence()
        mostrar_patch_notes()
        ronronear(duracion=2)
        loop_de_amor()
        mostrar_mensaje_central()
        shutdown_sequence()

    except KeyboardInterrupt:
        print("\n\n  (Interrumpido... pero el amor no se puede interrumpir.)\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
