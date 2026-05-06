"""
cat_emojis.py
──────────────────────────────────────────────────────
Un script de amor disfrazado de código.

Cómo usarlo:
    python cat_emojis.py

No necesita nada especial. Solo Python 3 y ganas.
──────────────────────────────────────────────────────
"""

import time
import random
import sys


# ──────────────────────────────────────────────────────
#  LOS GATITOS
# ──────────────────────────────────────────────────────

GATITOS = [
    r"""
    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)

  [ El Gatito de la Gratitud ]
""",
    r"""
    |\      _,,,---,,_
    /,`.-'`'    -.  ;-;;,_
   |,4-  ) )-,_..;\ (  `'-'
  '---''(_/--'  `-'\_)

  [ El Gatito del Perdón Rápido ]
""",
    r"""
   /\   /\
  (  o o  )
  =( Y )=
    )   (
   (_)-(_)

  [ El Gatito del Ronroneo Eterno ]
""",
    r"""
   ^~^  ,
  ('Y') )
  /   \/
 (\|||/)

  [ El Gatito Amasa-Disculpas™ ]
""",
    r"""
   /\_/\
  ( ^.^ ) ~♥
  (  >🐟< )
    vvvv

  [ El Gatito Ofrece Pescado de Paz ]
""",
    r"""
  /\   /\
 (  o_o  )
 (  >♥<  )
  \ === /
   '---'

  [ El Gatito que Te Quiere Mucho ]
"""
]


# ──────────────────────────────────────────────────────
#  LOS MENSAJES
# ──────────────────────────────────────────────────────

MENSAJES_DE_AMOR = [
    "Eres la persona más importante en mi mundo. Punto.",
    "No sé querer perfectamente, pero sí sé que te quiero a ti.",
    "Gracias por ayudarme, incluso cuando yo no lo pedí.",
    "Tu paciencia conmigo es un regalo que no siempre merezco.",
    "Me equivoqué. Lo reconozco. Y voy a hacerlo mejor.",
    "Cada vez que me ayudas, todo tiene más sentido.",
    "Eres más importante que cualquier mal momento que pueda tener.",
    "Perdóname por no haberlo dicho en el momento: gracias.",
    "Ser querido por ti es una de las mejores cosas de mi vida.",
    "No te merezco siempre, pero te elijo siempre.",
]

PROMESAS_CONCRETAS = [
    "🐾 Voy a decir gracias en el momento, no dos horas después.",
    "🐾 Voy a pausar antes de responder cuando esté estresado.",
    "🐾 No voy a asumir que 'ya sabes' que te lo agradezco — voy a decírtelo.",
    "🐾 Voy a pedir ayuda antes de llegar al límite.",
    "🐾 Cuando me ayudes, lo voy a mostrar. No solo sentirlo por dentro.",
    "🐾 Voy a nombrar las cosas buenas que haces, más seguido.",
    "🐾 Voy a dejar de dar por sentado lo que más importa.",
]


# ──────────────────────────────────────────────────────
#  LAS FUNCIONES
# ──────────────────────────────────────────────────────

def escribir_lento(texto, delay=0.03):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def linea(caracter="─", largo=55):
    print(caracter * largo)


def ronronear():
    print("\n  Iniciando ronroneo de disculpa...\n")
    for _ in range(2):
        for sonido in ["  prrr... ", "  PRRRRR... ", "  prrr... "]:
            sys.stdout.write(sonido)
            sys.stdout.flush()
            time.sleep(0.4)
    print("\n")


def arranque():
    linea("━")
    print("  🐾 repo-de-disculpas :: gatitos en acción")
    print("  Cargando amor...")
    linea("━")
    time.sleep(0.4)

    pasos = [
        "Desempolvando las gracias pendientes.........",
        "Activando modo ronroneo sincero..............",
        "Revisando promesas (sin errores)..............",
        "Midiendo cantidad de amor disponible..........",
        "Resultado: INFINITO. Continuando..............",
    ]

    for paso in pasos:
        sys.stdout.write(f"\n  🐱 {paso}")
        sys.stdout.flush()
        time.sleep(0.6)
        print(" ✅")

    print()
    time.sleep(0.4)


def mostrar_promesas():
    linea("═")
    print("  📋 Lo que voy a hacer diferente a partir de hoy")
    linea("═")
    time.sleep(0.4)
    for promesa in PROMESAS_CONCRETAS:
        escribir_lento(f"  {promesa}", delay=0.02)
        time.sleep(0.15)
    print()


def mensajes_de_amor():
    print("  💌 Cosas que quiero que sepas:\n")
    seleccion = random.sample(MENSAJES_DE_AMOR, k=4)
    for i, msg in enumerate(seleccion, 1):
        time.sleep(0.3)
        escribir_lento(f"  {i}. {msg}", delay=0.025)
    print()
    print(random.choice(GATITOS))


def mensaje_central():
    linea("★")
    print()
    escribir_lento("  Lo que este script realmente quiere decirte:", delay=0.04)
    print()
    time.sleep(0.7)

    print("""
  ┌───────────────────────────────────────────────────┐
  │                                                   │
  │   Me equivoqué. No valoré tu ayuda en el          │
  │   momento en que más debía haberlo hecho.         │
  │   Y lo siento.                                    │
  │                                                   │
  │   No como excusa.                                 │
  │   No como gesto rápido para que pase.             │
  │                                                   │
  │   Como alguien que te ve, que te quiere,          │
  │   y que está comprometido a hacerlo mejor.        │
  │                                                   │
  │   Gracias por ayudarme.                           │
  │   Gracias por existir.                            │
  │   Gracias por seguir aquí.                        │
  │                                                   │
  │              Con todo mi amor  🐾                 │
  │                                                   │
  └───────────────────────────────────────────────────┘
""")
    time.sleep(0.8)


def cierre():
    linea("━")
    print()
    escribir_lento("  ¿Sigue funcionando este amor?   ", delay=0.04)
    time.sleep(0.5)
    escribir_lento("  Sí. Siempre sí.", delay=0.06)
    print()
    print()
    escribir_lento('  "Lo siento. Te quiero. Gracias."', delay=0.05)
    print()
    linea("━")
    print()


# ──────────────────────────────────────────────────────
#  AQUÍ EMPIEZA TODO
# ──────────────────────────────────────────────────────

def main():
    try:
        arranque()
        mostrar_promesas()
        ronronear()
        mensajes_de_amor()
        mensaje_central()
        cierre()

    except KeyboardInterrupt:
        print("\n\n  (Se interrumpió... pero el amor no se interrumpe.)\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
