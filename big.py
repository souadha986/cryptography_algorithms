class ResultatEuclide:
    def __init__(self, d, x, y):
        self.d = d  # Le PGCD
        self.x = x  # Le coefficient u
        self.y = y  # Le coefficient v

def euclide_etendu(a: int, b: int) -> ResultatEuclide:
    r, r_prime = a, b
    u, u_prime = 1, 0
    v, v_prime = 0, 1

    while r_prime != 0:
        q = r // r_prime  # Division entière
        
        # Mise à jour simultanée correcte
        r, r_prime = r_prime, r - q * r_prime
        u, u_prime = u_prime, u - q * u_prime
        v, v_prime = v_prime, v - q * v_prime

    return ResultatEuclide(r, u, v)

def inverse_mod(a: int, n: int) -> int:
    res = euclide_etendu(a, n)
    
    if res.d != 1:
        print(f"Erreur : L'inverse de {a} modulo {n} n'existe pas (PGCD != 1).")
        return -1

    return (res.x % n + n) % n

# --- Test avec tes valeurs ---
if __name__ == "__main__":
    a =   26334555 
    n =  11345678
    inv = inverse_mod(a, n)
    print(f"L'inverse de {a} modulo {n} est : {inv}")