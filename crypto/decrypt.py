import base64
n = 8589869170 - 1000
i = 5
cipher_b64 = b"MTE0LDg0LDQzNyw4MDk1LDMzNTUwNDM0LDg1ODk4NjkxNzAsMTM3NDM4NjkxMzc2LDIzMDU4NDMwMDgxMzk5NTIyMzUsMjY1ODQ1NTk5MTU2OTgzMTc0NDY1NDY5MjYxNTk1Mzg0MjI0NSwxOTE1NjE5NDI2MDgyMzYxMDcyOTQ3OTMzNzgwODQzMDM2MzgxMzA5OTczMjE1NDgxNjkyOTQsMTMxNjQwMzY0NTg1Njk2NDgzMzcyMzk3NTM0NjA0NTg3MjI5MTAyMjM0NzIzMTgzODY5NDMxMTc3ODM3MjgyMjMsMTQ0NzQwMTExNTQ2NjQ1MjQ0Mjc5NDYzNzMxMjYwODU5ODg0ODE1NzM2Nzc0OTE0NzQ4MzU4ODkwNjYzNTQzNDkxMzExOTkxNTIyMTYsMjM1NjI3MjM0NTcyNjczNDcwNjU3ODk1NDg5OTY3MDk5MDQ5ODg0Nzc1NDc4NTgzOTI2MDA3MTAxNDMwMjc1OTc1MDYzMzcyODMxNzg2MjIyMzk3MzAzNjU1Mzk2MDI2MDA1NjEzNjAyNTU1NjY0NjI1MDMyNzAxNzUwNTI4OTI1NzgwNDMyMTU1NDMzODI0OTg0Mjg3NzcxNTI0MjcwMTAzOTQ0OTY5MTg2NjQwMjg2NDQ1MzQxMjgwMzM4MzE0Mzk3OTAyMzY4Mzg2MjQwMzMxNzE0MzU5MjIzNTY2NDMyMTk3MDMxMDE3MjA3MTMxNjM1Mjc0ODcyOTg3NDc0MDA2NDc4MDE5Mzk1ODcxNjU5MzY0MDEwODc0MTkzNzU2NDkwNTc5MTg1NDk0OTIxNjA1NTU2NDcwODcsMTQxMDUzNzgzNzA2NzEyMDY5MDYzMjA3OTU4MDg2MDYzMTg5ODgxNDg2NzQzNTE0NzE1NjY3ODM4ODM4Njc1OTk5OTU0ODY3NzQyNjUyMzgwMTE0MTA0MTkzMzI5MDM3NjkwMjUxNTYxOTUwNTY4NzA5ODI5MzI3MTY0MDg3NzI0MzY2MzcwMDg3MTE2NzMxMjY4MTU5MzEzNjUyNDg3NDUwNjUyNDM5ODA1ODc3Mjk2MjA3Mjk3NDQ2NzIzMjk1MTY2NjU4MjI4ODQ2OTI2ODA3Nzg2NjUyODcwMTg4OTIwODY3ODc5NDUxNDc4MzY0NTY5MzEzOTIyMDYwMzcwNjk1MDY0NzM2MDczNTcyMzc4Njk1MTc2NDczMDU1MjY2ODI2MjUzMjg0ODg2MzgzNzE1MDcyOTc0MzI0NDYzODM1MzAwMDUzMTM4NDI5NDYwMjk2NTc1MTQzMzY4MDY1NTcwNzU5NTM3MzI4MjQy"

def a(n):
    # print("------")
    b = n - 1000
    for i in range(1, n):
        if(n % i == 0):
            b += i
        print(b, i, n)
        if b > n:
            return False
    return b == n


print("flag{", end='', flush=True)
cipher = base64.b64decode(cipher_b64).decode().split(",")
print(cipher)
while(i < len(cipher)):
    if (a(n)):
        # print(chr(int(cipher[i]) ^ n), end='', flush=True)
        print(cipher[i], n, int(cipher[i]) ^ n, i, chr(int(cipher[i]) ^ n))
        i += 1
    n+=1
    # print(n, 8589871170)
    if n == (8589869170 + 1000):
        print("i is {}".format(i))
        break

print("}")

#
# currnt i -> 5, 8589869670


# flag[8095] = "tHE_b"
