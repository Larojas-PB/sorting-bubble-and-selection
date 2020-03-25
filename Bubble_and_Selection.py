import time

def mainmenu():
    print("1. Selection Sort")
    print("2. Bubble sort")
    print("3. Quit")
    select=int(input("Pilih nomor: "))
    if select==1:
        selection()
    elif select==2:
        bubble()
    elif select==3:
        quit()
    else:
        print("Error. Pilih 1-3")
        input("Enter untuk mengulang")


def selection():
    print("pisahkan angka dengan koma(,)")
    inp = input('masukan angka: ')
    nums = inp.split(',')
    start=time.time()
    for i in range(len(nums)):
        minpos=i
        for j in range(i+1,len(nums)):
            if int(nums[j]) < int(nums[minpos]):
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print (nums)

    print(nums)
    end=time.time()
    print("selesai dalam")
    print(end-start)
    print("second")
    input("Enter untuk melanjutkan")


def bubble():
    print("pisahkan angka dengan koma(,)")
    inp = input('masukan angka: ')
    y = inp.split(',')
    start=time.time()
    for i in range (len(y)-1,0,-1):
        for j in range (i):
            if int(y[j]) > int(y[j+1]):
                temp = y[j]
                y[j] = y[j+1]
                y[j+1] = temp

                print (y)
    print(y)
    end=time.time()
    print("selesai dalam")
    print(end-start)
    print("second")
    input("Enter untuk melanjutkan")

while True:
    mainmenu()


                 
