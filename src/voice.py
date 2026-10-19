# -*- coding: utf-8 -*-
"""Textos con la voz de Saori: cercana, cálida, de tú a tú, con mimo por la piel.
Se aplican sobre data.py (hechos y datos técnicos no se tocan)."""

V = {
 "hifu-12d": dict(
  tagline="Un lifting sin cirugía ni incisiones, pensado para que te mires al espejo y te guste lo que ves. Ultrasonido que tensa tu piel desde las capas más profundas.",
  intro=["El HIFU 12D es nuestro Elixir de Firmeza: ultrasonido focalizado de alta intensidad que trabaja donde ningún cosmético llega, sin cirugía y sin incisiones.",
         "La energía se concentra en las capas profundas y despierta la producción de colágeno y elastina. Tu piel se va tensando poco a poco, y el cambio se nota de forma natural: más firmeza, más definición y más luz."],
  body_text="El HIFU no es solo cosa de la cara. En Saori también lo usamos para mimar el cuerpo cuando la piel pide un empujón de firmeza.",
  steps=[("Te escuchamos", "Empezamos con tu diagnóstico: miramos tu piel, tus zonas y qué es lo que quieres mejorar."),
         ("Preparamos tu piel", "Limpiamos la zona y aplicamos el gel que permite al ultrasonido hacer su trabajo."),
         ("Lifting profundo", "Aplicamos el cabezal con precisión en cada zona, trabajando las capas profundas."),
         ("Cuidamos el final", "Terminamos con calmante y protección, y te contamos cómo cuidarte los días siguientes.")]),
 "diatermia": dict(
  tagline="Calor profundo y agradable que despierta tus tejidos desde dentro. Piel más firme, más luminosa y con más vida, en el rostro y en el cuerpo.",
  intro=["La diatermia es un tratamiento no invasivo que genera calor profundo para estimular tus tejidos desde el interior y mejorar su función y su calidad.",
         "En el rostro activa la regeneración y rejuvenece de forma progresiva; en el cuerpo es un tratamiento profundo ideal para cuidar la salud del tejido. Además, potencia los resultados de otros tratamientos."],
  body_text="Sabemos lo que cuesta convivir con el lipedema. Por eso la diatermia también está aquí: como complemento que aporta bienestar y alivio.",
  steps=[("Te escuchamos", "Hablamos de tu objetivo: rostro, cuerpo o apoyo en lipedema. Lo adaptamos todo a ti."),
         ("Preparamos tu piel", "Preparamos la zona y aplicamos el producto para que el cabezal se deslice con suavidad."),
         ("Calor que transforma", "Trabajamos con movimientos suaves mientras el calor profundo activa el tejido."),
         ("Cuidamos el final", "Calmamos la piel y te damos pautas personalizadas para seguir cuidándote.")]),
 "kinesiolifting-facial": dict(
  tagline="Un lifting hecho con las manos. Sin aparatos ni productos químicos: solo técnica, cariño y mucha relajación para devolver armonía a tu rostro.",
  intro=["El kinesiolifting es un método manual de lifting y modelado facial que une kinesiología, neuroestética y masaje miolifting.",
         "Trabajamos con las manos sobre la fascia, el tejido conectivo, los músculos y las estructuras profundas del rostro y el cuello, para devolver el equilibrio a las tensiones, activar la circulación y dar armonía a tu contorno."],
  body_text="La neuroestética nos recuerda algo muy nuestro: cuidar la piel también es cuidarte a ti. Relajarte forma parte del resultado.",
  steps=[("Te escuchamos", "Observamos tu rostro, tus tensiones y lo que quieres conseguir."),
         ("Preparamos tu piel", "Preparamos la piel y el ambiente para que te dejes llevar."),
         ("Manos que modelan", "Maniobras de lifting y modelado sobre fascia y músculos, con ritmo pausado."),
         ("Cuidamos el final", "Cerramos con técnicas de calma y unas recomendaciones para ti.")]),
 "ipl-diatermia": dict(
  tagline="Dos tecnologías que se dan la mano: luz para la superficie y calor para la profundidad. Una piel más uniforme, firme y con ese efecto buena cara.",
  intro=["IPL facial + diatermia es nuestro tratamiento de rejuvenecimiento integral: actúa en la superficie y en lo más profundo de tu piel.",
         "La IPL ayuda con manchas, rojeces, acné, poro y tono apagado para una piel más uniforme y luminosa, mientras la diatermia estimula el colágeno desde dentro, activa la circulación y reafirma los tejidos."],
  body_text="Cuando sumamos IPL y diatermia trabajamos tu piel por capas, en una misma sesión, para un efecto buena cara que va a más.",
  steps=[("Te escuchamos", "Miramos tu tipo de piel, tus manchas y tu sensibilidad antes de decidir nada."),
         ("Preparamos tu piel", "Limpieza, protección ocular y ajuste de parámetros pensados para tu piel."),
         ("Luz y calor", "Aplicamos la luz pulsada y el calor profundo de forma ordenada."),
         ("Cuidamos el final", "Calmamos, hidratamos y protegemos tu piel antes de que te vayas.")]),
 "dermapen": dict(
  tagline="Despierta la capacidad de tu piel para regenerarse. Más colágeno, mejor textura y unos activos que se absorben como nunca.",
  intro=["El Dermapen es microneedling: un tratamiento que estimula la regeneración natural de tu piel y favorece la producción de colágeno y elastina.",
         "Mejora la textura, suaviza arrugas, manchas y líneas de expresión, y potencia la absorción de los principios activos. El resultado: una piel más firme, uniforme y luminosa."],
  body_text="Este protocolo exclusivo cuida todo tu rostro y también tus labios. Es una edición limitada y las plazas son reducidas: escríbenos y te contamos.",
  steps=[("Te escuchamos", "Valoramos tu piel y decidimos juntas la profundidad y los activos que más te convienen."),
         ("Preparamos tu piel", "Higienizamos la zona con material de un solo uso."),
         ("Microneedling", "Realizamos el pase con el dermapen junto con los activos elegidos."),
         ("Cuidamos el final", "Calmamos y protegemos tu piel y te damos pautas para los días siguientes.")]),
 "radiofrecuencia-fraccionada": dict(
  tagline="Para esas marcas de acné que te acompañan desde hace tiempo. Radiofrecuencia que regenera tu piel desde el interior.",
  intro=["La radiofrecuencia fraccionada es un tratamiento avanzado que actúa en profundidad estimulando colágeno y elastina.",
         "Es especialmente eficaz con las marcas y cicatrices de acné, porque regenera la piel desde dentro: mejora la textura, reduce el poro, suaviza irregularidades y deja una piel más firme, uniforme y renovada."],
  body_text="Si el acné se fue pero dejó marcas o textura irregular, la radiofrecuencia fraccionada actúa justo donde el cosmético no llega.",
  steps=[("Te escuchamos", "Miramos el tipo de cicatriz, tu piel y tu sensibilidad."),
         ("Preparamos tu piel", "Limpiamos y ajustamos los parámetros a tu caso."),
         ("Regeneración profunda", "Pasamos el cabezal de forma fraccionada por las zonas a tratar."),
         ("Cuidamos el final", "Calmamos y protegemos tu piel con cosmética específica.")]),
 "electroporacion": dict(
  tagline="Hidratación profunda sin agujas. Impulsos eléctricos que llevan los activos adonde tu piel los necesita para dejarla jugosa y luminosa.",
  intro=["La electroporación es un tratamiento no invasivo que utiliza impulsos eléctricos para que los activos penetren en profundidad, sin agujas.",
         "Ayuda a hidratar intensamente y mejora la luminosidad, la elasticidad y la firmeza. Además potencia otros tratamientos y deja la piel jugosa, revitalizada y uniforme."],
  body_text="Cada piel necesita su plan a medida, también en los activos. Los elegimos según tu diagnóstico: hidratación, luminosidad, firmeza o calma.",
  steps=[("Te escuchamos", "Valoramos tu piel y elegimos los activos que mejor le sientan."),
         ("Preparamos tu piel", "Limpiamos para que reciba bien los activos."),
         ("Activos en profundidad", "Aplicamos los impulsos con el cabezal junto a los activos."),
         ("Cuidamos el final", "Sellamos con una mascarilla calmante y protección.")]),
 "biopen-ems": dict(
  tagline="Firmeza en dos niveles: regeneramos tu piel con Biopen y activamos tu musculatura con EMS para redefinir el óvalo.",
  intro=["Biopen + EMS reafirmante combina dos tecnologías para mejorar la firmeza y el tono de tu piel, trabajando a dos niveles.",
         "El Biopen estimula la regeneración y la producción de colágeno, mejorando la textura y la calidad cutánea. La EMS activa la musculatura facial para reafirmar, redefinir el óvalo y dar efecto lifting."],
  body_text="Piel y músculo trabajando a la vez: así conseguimos una piel más firme, tersa y tonificada.",
  steps=[("Te escuchamos", "Valoramos tu firmeza, el tono muscular y la calidad de tu piel."),
         ("Regeneración con Biopen", "Trabajamos la regeneración y el colágeno."),
         ("Músculo activo con EMS", "Activamos la musculatura facial para reafirmar y definir."),
         ("Cuidamos el final", "Calmamos y protegemos tu piel.")]),
 "limpieza-saori": dict(
  tagline="El despertar de tu piel. Una limpieza de maniobras suaves que elimina lo que sobra para que tu piel respire y recupere su luz.",
  intro=["El despertar de la piel: una limpieza facial con maniobras suaves que elimina células muertas e impurezas, para que tu piel se oxigene y recupere su luminosidad.",
         "Es el mejor primer paso en Saori, y una forma preciosa de conocernos mientras hacemos tu diagnóstico facial."],
  body_text="Una limpieza profunda y respetuosa deja tu piel lista para recibir cualquier otro tratamiento. Y ella te lo agradece.",
  steps=[("Te escuchamos", "Charlamos y miramos tu tipo de piel y lo que necesita."),
         ("Preparamos tu piel", "Desmaquillado y limpieza profunda."),
         ("Maniobras suaves", "Eliminamos células muertas e impurezas con mimo."),
         ("Cuidamos el final", "Mascarilla, calmante y protección para sellar el momento.")]),
 "limpieza-zensy": dict(
  tagline="Frescura absoluta. Vibraciones ultrasónicas que llegan donde la limpieza manual no alcanza y dejan tus poros despejados.",
  intro=["Con vibraciones ultrasónicas de alta frecuencia, Zensy elimina impurezas, exceso de sebo y restos alojados en los poros.",
         "Actúa donde la limpieza manual no llega, y lo hace con una sensación de ligereza, calma y frescura absoluta."],
  body_text="Si tu piel tiene brillos, poros visibles o imperfecciones, Zensy se convierte en una de tus mejores aliadas.",
  steps=[("Te escuchamos", "Miramos tu piel y las zonas más congestionadas."),
         ("Preparamos tu piel", "Limpiamos e hidratamos antes de empezar."),
         ("Ultrasonidos", "Pasamos la espátula ultrasónica por todo el rostro."),
         ("Cuidamos el final", "Mascarilla y protección para terminar.")]),
 "punta-de-diamante": dict(
  tagline="Efecto piel nueva al instante. Tacto seda inmediato y un poro visiblemente más fino. Y además, potencia x2 tu siguiente tratamiento.",
  intro=["El despertar de la piel, versión diamante: efecto piel nueva al instante, con un tacto seda inmediato. Tu piel queda suave, fina y pulida.",
         "Mejora de forma visible el poro y potencia x2 los resultados del tratamiento que hagamos a continuación."],
  body_text="Al renovar la capa superficial, tu piel absorbe mejor los activos y la tecnología que apliquemos después.",
  steps=[("Te escuchamos", "Valoramos tu piel y la intensidad que necesita."),
         ("Preparamos tu piel", "Una limpieza previa para empezar con la piel despejada."),
         ("Punta de diamante", "Pulimos y renovamos la superficie con la punta."),
         ("Cuidamos el final", "Hidratación y protección para sellar el resultado.")]),
 "depilacion-ipl": dict(
  tagline="Dile adiós a las cuchillas y a la cera. Fotodepilación profesional con precios claros por zona, desde 10 €.",
  intro=["La depilación IPL es fotodepilación profesional con Luz Pulsada Intensa para reducir el vello de forma duradera y progresiva.",
         "La luz es absorbida por la melanina del vello y se convierte en calor, que debilita el folículo. Así, sesión a sesión, el pelo va creciendo cada vez menos."],
  body_text="Elige tus zonas, mira cuánto sale tu sesión y envíanos tu selección por WhatsApp. Te damos cita y listo.",
  steps=[("Te escuchamos", "Revisamos tu piel, tu vello y tu historial."),
         ("Preparamos tu piel", "Rasurado previo, limpieza y protección ocular."),
         ("Luz pulsada", "Aplicamos la IPL por zonas, de forma ordenada."),
         ("Cuidamos el final", "Calmante y recomendaciones para los días siguientes.")]),
}

def apply(services):
    for s in services:
        v = V.get(s["slug"])
        if v:
            s.update(v)
