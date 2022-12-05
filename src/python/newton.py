# skończone
def dwumian(n, k):
    if k < 0 or n < 0 or n < k:
        return None
    if k == 0 or k == n:
        return 1
    
    return dwumian(n - 1, k - 1) + dwumian(n - 1, k)

def main():
    print(dwumian(8, 3))
    print(dwumian(-3, 5))
    print(dwumian(3, 5))
    print(dwumian(4, -5))

if __name__ == "__main__":
    main()