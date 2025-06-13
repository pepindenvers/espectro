import streamlit as st
from PIL import Image

st.set_page_config(page_title="Simulador Ka - Rojo de Metilo", layout="centered")

st.title("🎓 Simulador: Determinación espectrofotométrica de Ka del Rojo de Metilo")

# Etapa 1: Preparación de la solución madre
st.header("1️⃣ Preparación de solución madre")
img_balanza = Image.open("balanza.png")
st.image(img_balanza, caption="Balanza", width=300)

if st.button("Pesar 0.1 g de Rojo de Metilo"):
    peso = st.text_input("Ingrese la masa pesada:", key="peso")
    if peso == "0.1 g" or peso == "0.1":
        if st.button("Preparar solución estándar"):
            img_pipeta = Image.open("pipeta.png")
            st.image(img_pipeta, caption="Preparación de solución estándar", width=300)
            st.success("✅ Se pipetea 5 mL de la solución madre, se añade 50 mL de etanol al 95% y se afora con agua destilada.")
    elif peso:
        st.error("❌ Masa incorrecta. Intenta con 0.1 g.")

# Etapa 2: Preparación de soluciones ácida y básica
st.header("2️⃣ Preparación de soluciones ácida y básica")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Solución Ácida")
    img_hcl = Image.open("vaso_HCl.png")
    st.image(img_hcl, caption="HCl", width=200)
    if st.button("Usar HCl"):
        img_roja = Image.open("disolucion_roja.png")
        st.image(img_roja, caption="Solución roja-púrpura", width=300)
    if st.button("Usar Acetato (ácido)"):
        st.error("❌ Incorrecto. Esa es la base.")

with col2:
    st.subheader("Solución Básica")
    img_acetato = Image.open("vaso_acetato.png")
    st.image(img_acetato, caption="Acetato de sodio", width=200)
    if st.button("Usar Acetato (base)"):
        img_amarilla = Image.open("disolucion_amarilla.png")
        st.image(img_amarilla, caption="Solución amarilla", width=300)
    if st.button("Usar HCl (base)"):
        st.error("❌ Incorrecto. Esa es la solución ácida.")

# Etapa 3: Finalización
st.header("3️⃣ Espectrofotómetro")

if st.button("Finalizar preparación"):
    img_espectrofotometro = Image.open("espectrofotometro.png")
    st.image(img_espectrofotometro, caption="Espectrofotómetro", width=300)
    st.info("📥 Inserte la disolución ácida y básica.")
    st.warning("⚠️ Error: Falta paso previo.")

    respuesta = st.text_input("¿Qué paso hace falta?", key="blanco")

if st.button("Verificar respuesta"):
    if "blanco" in respuesta.lower():
        img_espectro = Image.open("espectro.png")
        st.image(img_espectro, caption="Espectro: Longitud de onda máxima", width=400)
        st.success("✅ ¡Simulación completada! Ahora puedes analizar el espectro.")
    else:
        st.error("❌ Respuesta incorrecta. Intenta de nuevo.")


