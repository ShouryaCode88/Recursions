def reverse(a,a_size,n):
    temp = 0
    while (temp<a_size):
        start = temp

        end = min(temp + n-1,a_size-1)
        while (start<end):
          a[start],a[end] = a[end],a[start]
          start += 1
          end -= 1

        temp += n

a = [1,4,11,5,6,1]

a_size = len(a)

n = 2

reverse(a,a_size,n)

for i in range(0,a_size):
   print(a[i], end=' ')