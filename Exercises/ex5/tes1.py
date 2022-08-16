T =" * "
for i in range(1,5):
    print( i*T)
for i in range(1,5):
    j = 6-i
    print(j*T)
print(T)


from PIL import Image
img = Image.open('./fib.png').convert('LA')
#img.save('greyscale.png')
