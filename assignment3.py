# prime num checker

# import math
# num=int(input('enter a num:'))
# def is_prime(num):
#     if num<=1 :
#         return False
#     for i in range(2,int(math.sqrt(num))+1):
#         if num%i==0:
#             return False
#         return True
# print(is_prime(num))
    

#recursive function to generate prime nos

start=int(input('enter start range:'))
end=int(input('enter stop range:'))

def is_prime(n,i=2):
    if n<=1:
        return False
    if n==i:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)

def range_prime(start,end,prime_list=None):
    if prime_list is None:
        prime_list=[]
    if start>end:
        return prime_list
    if is_prime(start):
        prime_list.append(start)
    return range_prime(start+1,end,prime_list)
prime_num=range_prime(start,end)
print(f'prime nums in range {start} and {end} is :{prime_num}')
    
