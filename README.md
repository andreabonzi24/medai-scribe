# 🩺 MedAI Scribe - Assistente AI per Cartelle Cliniche

**Trasforma documenti medici caotici in dati strutturati con AI open-source**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://medai-scribe.streamlit.app/)

## 🚀 Come Iniziare

```bash
# Clona il repository
git clone https://github.com/andreabonzi24/medai-scribe.git
cd medai-scribe

# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'applicazione
streamlit run src/streamlit_app.py
```

## 💡 Funzionalità Principali
- Estrazione automatica di diagnosi, farmaci e allergie da testo clinico
- Rilevamento base di potenziali interazioni farmacologiche
- Interfaccia semplice e intuitiva per medici

## 🛠 Roadmap di Sviluppo
- [x] Analisi di testi clinici in italiano
- [ ] Supporto per PDF scannerizzati (OCR)
- [ ] Integrazione con database farmaceutici italiani
- [ ] Riconoscimento di note vocali

## 🤝 Come Contribuire
1. Segnala bug o richieste funzionali [aprendo una issue]https://github.com/andreabonzi24/medai-scribe.git)
2. Migliora il database farmaci: modifica `data/drug_database.csv`
3. Aggiungi nuove funzionalità tramite pull request

## 📜 Licenza
Questo progetto è rilasciato sotto licenza [Apache 2.0](LICENSE)
