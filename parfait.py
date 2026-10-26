class Crypto:
    def encrypt(self, clear_text: str, key_stream: str) -> str:
        """Chiffre un message en clair à l'aide d'un masque jetable (addition modulaire)."""
        cipher_chars = []
        for c, k in zip(clear_text, key_stream):
            # Conversion lettre -> nombre (A=1, B=2, ..., Z=26)
            p_val = ord(c.upper()) - ord('A') + 1
            k_val = ord(k.upper()) - ord('A') + 1
            
            # Addition modulaire modulo 26 (ramené dans l'intervalle 1..26)
            c_val = (p_val + k_val - 1) % 26 + 1
            
            # Reconversion nombre -> lettre
            cipher_chars.append(chr(c_val + ord('A') - 1))
            
        return "".join(cipher_chars)

    def decrypt(self, cipher_text: str, key_stream: str) -> str:
        """Déchiffre un message chiffré à l'aide du masque jetable (soustraction modulaire)."""
        clear_chars = []
        for c, k in zip(cipher_text, key_stream):
            # Conversion lettre -> nombre (A=1, B=2, ..., Z=26)
            c_val = ord(c.upper()) - ord('A') + 1
            k_val = ord(k.upper()) - ord('A') + 1
            
            # Soustraction modulaire modulo 26
            p_val = (c_val - k_val) % 26
            if p_val == 0:
                p_val = 26
            
            # Reconversion nombre -> lettre
            clear_chars.append(chr(p_val + ord('A') - 1))
            
        return "".join(clear_chars)


# --- Résolution directe de l'exercice du TP ---
if __name__ == "__main__":
    crypto = Crypto()
    
    # Données du TP
    cipher_msg = "CUFNFLRQMLWBLARVJDALMURNGSHILXXMVDUMFPYG"
    key = "ACWZYRJYHGVNHUCARNVXJPUIFACBWOJFBOTIEBVBBZHANSLYOP"
    
    # Déchiffrement
    message_clair = crypto.decrypt(cipher_msg, key)
    print("Message en clair d'origine :")
    print(message_clair)