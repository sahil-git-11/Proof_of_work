import hashlib
import time

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros  
    nonce = 0  
    
    while True:
        text = f"{block_number}{transactions}{previous_hash}{nonce}"  
        new_hash = hashlib.sha256(text.encode()).hexdigest()  
        
        if new_hash.startswith(prefix_str):  
            print(f"Successfully mined with nonce: {nonce}, Hash: {new_hash}")
            return new_hash, nonce  
        
        nonce += 1  

block_number = 1
transactions = "Sahil sends 1 BTC to Alice, Alice sends 0.5 BTC to Bob"
previous_hash = "0" * 10
difficulty = 4

start_time = time.time()  
new_hash, nonce = mine(block_number, transactions, previous_hash, difficulty)
end_time = time.time()  

print(f"Mining completed in {end_time - start_time:.2f} seconds with difficulty {difficulty}.")
