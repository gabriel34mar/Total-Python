
def count_primes(numbers):
    secuence=range(2, numbers+1)
    count=0
    for i in secuence:
        for j in range(2, int(i**.5)+1):
            if i%j==0:
                break
        else:
            count +=1
    print(f"Found {count} prime numbers")
    return count        
count_primes(10)
