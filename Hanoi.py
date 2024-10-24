def move_disk(src,dist):
    print(f"Move disk from {src} to {dist}")


def solve_hanoi(n,src,aux,dest):
    if n==1:
        move_disk(src,dest)
        return
    solve_hanoi(n-1,src,dest,aux)
    move_disk(src,dest)
    solve_hanoi(n-1,aux,src,dest)
    

def main():
    n = int(input("Enter the no of disks: "))
    solve_hanoi(n,"A","B","C")
    
main()