for i in range(20):
    if i % 2==0:
        continue

    print(i)

#Output: prints all odd numbers within the range 20
#i%2 == 0, here checks if i is even.
#continue - This keyword usage causes the skipping of the current block if the condition specified is satisfied and jumps to the "for" or "while" statement.
