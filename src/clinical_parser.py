from transformers import pipeline
import re

class ClinicalParser:
    def __init__(self):
        self.ner_model = pipeline("ner", model="dbmdz/bert-base-italian-xxl-cased")
        self.drug_db = self.load_drug_db()
    
    def load_drug_db(self):
        # Database farmaci semplificato (da espandere)
        return {
            "lisinopril": {"classe": "ACE-inibitore", "interazioni": ["potassio", "fans"]},
            "aspirina": {"classe": "Antiplastrinico", "interazioni": ["fans", "anticoagulanti"]}
        }
    
    def parse_text(self, text):
        # Analisi base del testo
        entities = self.ner_model(text)
        
        # Estrazioni specifiche per contesto medico
        findings = {
            "diagnosi": self.extract_pattern(text, r'diagno[s|stica]\s+di\s+(.+?)[\.\n]'),
            "farmaci": self.extract_drugs(text),
            "allergie": self.extract_pattern(text, r'allergi[co|a]\s+a\s+(.+?)[\.\n]')
        }
        return findings
    
    def extract_drugs(self, text):
        drugs = []
        for drug_name in self.drug_db.keys():
            if drug_name in text.lower():
                drug_data = self.drug_db[drug_name].copy()
                drug_data["nome"] = drug_name
                drugs.append(drug_data)
        return drugs
    
    def extract_pattern(self, text, pattern):
        matches = re.findall(pattern, text, re.IGNORECASE)
        return matches if matches else []

# Esempio di utilizzo
if __name__ == "__main__":
    parser = ClinicalParser()
    sample_text = "Paziente con diagnosi di ipertensione essenziale. Assume Lisinopril 20mg. Allergico alla penicillina."
    print(parser.parse_text(sample_text))