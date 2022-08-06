from hifini_download import downloadMusic

if __name__ == '__main__':
    while 1:
        
        flag = int(input("Input 0 to exit process, input other number to continue this process!"))
        if flag == 0 :
            exit()

        else:
            downloadMusic()