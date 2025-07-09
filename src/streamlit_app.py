import streamlit as st
from clinical_parser import ClinicalParser

st.set_page_config(page_title="MedAI Scribe", layout="wide")
st.title("🩺 MedAI Scribe - Assistente AI per Cartelle Cliniche")
st.markdown("""
Carica una cartella clinica in formato **testo, PDF o audio** per estrarre automaticamente:
- 🧬 **Diagnosi principali**  
- 💊 **Farmaci assunti**  
- ⚠️ **Allergie e interazioni pericolose**  
""")

uploaded_file = st.file_uploader("Scegli un file", type=["txt", "pdf", "mp3", "wav"])

if uploaded_file:
    st.subheader("Risultati Analisi")
    parser = ClinicalParser()
    
    # Per ora processiamo solo file di testo
    if uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
        results = parser.parse_text(text)
        
        # Visualizzazione medicale intuitiva
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Riepilogo Clinico")
            if results["diagnosi"]:
                st.success(f"**Diagnosi rilevate**: {', '.join(results['diagnosi'])}")
            else:
                st.info("Nessuna diagnosi rilevata")
                
            if results["farmaci"]:
                st.warning(f"**Farmaci identificati**: {', '.join([d['nome'] for d in results['farmaci']])}")
            
            if results["allergie"]:
                st.error(f"**Allergie segnalate**: {', '.join(results['allergie'])}")
        
        with col2:
            st.subheader("⚠️ Avvertenze Importanti")
            # Controllo interazioni farmacologiche (esempio base)
            if len(results.get("farmaci", [])) > 1:
                st.warning("Possibili interazioni farmacologiche - verificare con farmacista")
            else:
                st.info("Nessuna interazione farmacologica critica rilevata")
    else:
        st.warning("Formato file non ancora supportato! Usa un file .txt per i test iniziali")

st.markdown("---")
st.caption("Progetto open-source - [Contribuisci su GitHub](https://github.com/andreabonzi24/medai-scribe.git)")