
#1. Якщо ми запишемо всі натуральні числа, що кратні 3 або 5, та менші 10, ми отримаємо 3, 5, 6 та 9. Сума цих чисел буде дорівнювати 23.
#2Знайти суму всіх чисел, що кратні 3 або 5, та менші 1000.

# sum_num = 0
# for num in range(1000):
# 	if num % 3 == 0 or num % 5 == 0:
# 		sum_num += num
# print(sum_num)

# 2. Для числа 13195 існують такі прості дільники (прості числа, на яке задане число ділиться без залишку):
# 5, 7, 13, 29. Знайти найбільший простий дільник числа 600851475143.


# def if_prime (num):
#     flag = True
#     for i in range(3, num//2+1):
#         temp = num%i
#         if temp == 0:
#             flag = False
#     return flag
# mine_number = 600851475143
# prime_number = 3
# for number in range(3, mine_number//2+1):
#     temp_prime = if_prime(number)
#     if temp_prime:
#         temp = mine_number%number
#         if temp==0:
#             prime_number = number
#             print(prime_number)
#         else:
#             continue
# 3. 2520 найменше число, що ділиться на будь-яке число від 1 до 10 без залишку.
# Яке найменше позитивне число ділиться без залишку на всі числа від 1 до 20?
i=2520
c=False
r=(3,4,6,7,8,9,11,12,13,14,15,16,17,18,19)
while c is False:
    str(i)
    for j in r:
        if i%j==0:
            c=True
            continue
        else:
            c=False
            break
    i+=10

print(i-10)


# 4. Триплет Піфагора - це набір з трьох натуральних чисел a < b < c, для якого a**2 + b**2 = c**2. Наприклад,  3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# Існує тільки один триплет Піфагора, для якого a + b + c = 1000. Знайти добуток a*b*c лдя цього триплету.

# def find_product(sum):
#     for a in range(1, sum):
#         for b in range(1, sum - a):
#             c = sum - a - b
#             if a ** 2 + b ** 2 == c ** 2:
#                 print
#                 a * b * c
#                 return a * b * c
#             else:
#                 pass
#
#     print
#     'No such triplet exists!'
#
#
# print(find_product(1000))

# 5. Сумою простих чисел менших 10 є 2 + 3 + 5 + 7 = 17. Знайти суму всіх простих чисел, менших за 2 мільйони.
# def primes(n):
#     """ Returns  a list of primes < n """
#     sieve = [True] * n
#     for i in range(3,int(n**0.5)+1,2):
#         if sieve[i]:
#             sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
#     return [2] + [i for i in range(3,n,2) if sieve[i]]
#
# print(sum(primes(2_000_000)))

# Примітка:
# Натуральні числа - всі цілі числа більші 0.
# Прості числа - такі натуральні числа, які мають тільки два натуальних дільники: 1 та саме це число.