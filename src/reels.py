# -*- coding: utf-8 -*-
"""Reels reales de las redes del centro (Instagram @esteticasaori y TikTok @esteticarocioguti).
Visualizaciones tomadas de los perfiles. Los títulos y descripciones resumen el texto de cada publicación."""

IG = "https://www.instagram.com/reel/{}/"
TT = "https://www.tiktok.com/@esteticarocioguti/video/{}"

REELS = {
 "ig-diamante": dict(net="ig", id="Dc0zbEcuKp3", views="22,6 mil", title="Punta de diamante: el paso 1 tras el verano",
    desc="Exfoliación mecánica suave para retirar células muertas, afinar la textura y liberar el poro antes de cualquier otro tratamiento."),
 "tt-hifu": dict(net="tt", id="7506831992978165014", views="5,5 mil", title="HIFU 12D: reafirma sin cirugía",
    desc="Cómo funciona esta tecnología avanzada que trabaja en capas profundas de la piel."),
 "tt-acne": dict(net="tt", id="7601842837633748246", views="6,8 mil", title="Adiós a las cicatrices de acné",
    desc="Transforma tu piel y recupera tu confianza con radiofrecuencia fraccionada."),
 "tt-manchas": dict(net="tt", id="7620003087901674774", views="7,1 mil", title="¿Piel con manchas o tono apagado?",
    desc="Te enseñamos nuestro protocolo para uniformar el tono y recuperar la luminosidad."),
 "tt-kinesio": dict(net="tt", id="7504277072064384278", views="4,8 mil", title="Kinesiolifting: tensiones que no ves",
    desc="Muchas tensiones del rostro se acumulan dentro de la boca. Así las trabajamos."),
 "ig-diapasones": dict(net="ig", id="DdJDop4OPpt", views="1,3 mil", title="Neuroestética con diapasones",
    desc="Vibración acústica para relajar la musculatura facial, estimular la microcirculación y llevar tu piel a un estado de calma profunda."),
 "tt-antesdespues": dict(net="tt", id="7592923026014948611", views="2,8 mil", title="HIFU: transformación real en 6 meses",
    desc="Antes y después del tratamiento, explicado paso a paso."),
 "ig-hidrafacial": dict(net="ig", id="DdYfY8LuBi1", views="963", title="Hidrafacial + terapia de diapasones",
    desc="Limpieza profunda con hidrodermoabrasión y un momento de desconexión total en cabina."),
 "tt-limpieza": dict(net="tt", id="7500606931984272662", views="2,5 mil", title="Limpieza facial profesional paso a paso",
    desc="Así es una limpieza facial en Saori, desde la limpieza profunda hasta el final."),
 "ig-rf": dict(net="ig", id="DU3HqBPDNI4", views="2,3 mil", title="Radiofrecuencia fraccionada con microagujas",
    desc="Regeneración celular desde las capas profundas: flacidez, estrías y cicatrices. Resultados que mejoran con los meses."),
 "ig-coctel": dict(net="ig", id="Degxk2DAW_h", views="1 mil", title="Cóctel de juventud con dermapen",
    desc="ADN de salmón, silicio orgánico y multivitaminas, a medida de lo que necesita tu piel."),
 "ig-historia": dict(net="ig", id="DaOGJmekbXd", views="2 mil", title="Nuestra historia, sin filtros",
    desc="Detrás de este centro hay constancia, mucho esfuerzo y una decisión valiente: dedicarse solo a la estética avanzada."),
}

HOME = ["ig-diamante", "tt-acne", "ig-rf", "tt-manchas", "ig-diapasones", "tt-hifu", "ig-coctel", "tt-kinesio", "ig-hidrafacial", "tt-antesdespues", "tt-limpieza"]

# Reels que acompañan a cada página de tratamiento
BY_SERVICE = {
 "hifu-12d": ["tt-hifu", "tt-antesdespues"],
 "radiofrecuencia-fraccionada": ["tt-acne", "ig-rf"],
 "kinesiolifting-facial": ["tt-kinesio", "ig-diapasones"],
 "punta-de-diamante": ["ig-diamante"],
 "dermapen": ["ig-coctel"],
 "limpieza-saori": ["tt-limpieza", "ig-hidrafacial"],
 "ipl-diatermia": ["tt-manchas"],
}

def url(r):
    return (IG if r["net"] == "ig" else TT).format(r["id"])

def embed(r):
    if r["net"] == "ig":
        return f"https://www.instagram.com/reel/{r['id']}/embed/"
    return f"https://www.tiktok.com/embed/v2/{r['id']}"
