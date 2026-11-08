# n=int(input())
# i=1
# while i<=n:
#     print(i)
#     i+=1
# a, b, c = map(int, input().split())

# for i in range(a, b-1, c):
#     if i % 2 == 0:
#         print(i, end=" ")
# sum = 0
# n = int(input())
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# n=int(input())
# i=1
# for i in range(1, n + 1):
#     if i%2==0:
#         print(i, end=" ")

# n=int(input())
# i=1
# for i in range(1, n+1):
#     if i%2!=0:
#         print(i, end=" ")

# n= int (input())
# for i in range(1, 11):
#     print(n, '*', i, '=', n*i)

# n= int(input())
# i=1
# sum=0
# for i in range(1, n+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# n= int(input())
# i=1
# sum=0
# for i in range(1, n+1):
#     if i%2!=0:
#         sum+=i
# print(sum)
# lst=list(map(int, input().split()))

# print(len(lst))
# cnt=0

# for i in range(0, len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i], end=" ")
#         cnt+=1


#  vazifai xonagi motable i miytable


# 1  lst=list(map(int, input().split()))
# cnt=0
# for i in range(0, len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i], end=" ")
#         cnt+=1
# print(cnt)

# 2  numbers = list(map(int, input().split()))
# total = sum(numbers)
# size = len(numbers)
# minimum = min(numbers)
# maximum = max(numbers)

# print("Sum:", total)
# print("Size:", size)
# print("Min:", minimum)
# print("Max:", maximum)

#3  numbers = list(map(int, input().split()))

# average = sum(numbers) / len(numbers)

# print("Average:", average)

# for n in numbers:
#     if n > average:
#         print(n)

# 4  numbers = list(map(int, input().split()))

# numbers.sort()

# print("Sort:", numbers)
# print("Reverse:", numbers[::-1])


# 5 numbers = list(map(int, input().split()))
# positive = 0
# negative = 0
# zero = 0

# for n in numbers:
#     if n > 0:
#         positive += 1
#     elif n < 0:
#         negative += 1
#     else:
#         zero += 1

# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)

# 6 numbers = list(map(int, input().split()))

# unique = list(set(numbers))

# unique.sort()

# print(unique)

# 7 numbers = list(map(int, input().split()))

# for n in numbers:
#     print(n, ":", numbers.count(n))


# 8 numbers = list(map(int, input().split()))

# numbers.append(100)
# numbers.insert(0, 50)
# numbers.extend([200, 300])

# print(numbers)


# 9 numbers = list(map(int, input().split()))

# result = []

# for n in numbers:
#     if n % 2 != 0:
#         result.append(n)

# print(result)


# 10 numbers = list(map(int, input().split()))

# print("First:", numbers[0])
# print("Last:", numbers[-1])
# print("Middle:", numbers[len(numbers) // 2])
# print("Index 30:", numbers.index(30))


# 11 numbers = list(map(int, input().split()))

# unique = list(set(numbers))

# unique.sort()

# print(unique[-2])


# 12 numbers = list(map(int, input().split()))

# numbers[0], numbers[-1] = numbers[-1], numbers[0]

# print(numbers)


# 13 numbers = list(map(int, input().split()))

# if numbers == numbers[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# 14 numbers = list(map(int, input().split()))

# numbers.pop(2)

# print(numbers)


# 15 numbers = list(map(int, input().split()))

# for i in range(len(numbers) - 1):
#     if numbers[i] + numbers[i + 1] == 10:
#         print(numbers[i], numbers[i + 1])


# 16 numbers = list(map(int, input().split()))

# first = numbers[:3]
# second = numbers[3:]

# print("First:", first)
# print("Second:", second)


# 17 numbers = list(map(int, input().split()))

# for n in numbers:
#     if numbers.count(n) == 1:
#         print(n)


# 18 numbers1 = list(map(int, input().split()))
# numbers2 = list(map(int, input().split()))

# numbers = numbers1 + numbers2

# numbers.sort()

# total = sum(numbers)

# print("List:", numbers)
# print("Sum:", total)


# 19 numbers = list(map(int, input().split()))

# count = 1
# maximum = 1

# for i in range(1, len(numbers)):
#     if numbers[i] == numbers[i - 1]:
#         count += 1
#     else:
#         count = 1

#     if count > maximum:
#         maximum = count

# print(maximum)