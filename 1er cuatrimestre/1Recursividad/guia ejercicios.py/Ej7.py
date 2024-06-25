def serie(num):
    if num == 0:
        return num
    else:
        return 1/num + serie(num-1)
print