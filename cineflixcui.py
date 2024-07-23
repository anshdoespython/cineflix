import tkinter as tk
import csv
from tkinter import messagebox



def on_button_click():
    messagebox.showinfo('ready to watch')

def printlis(mo_li):
    print(len(mo_li))
    for i in mo_li:
        print(i)

field = ['name','tag','image','rating']
   
movie_list = [
['oppenheimer','#drama','oppenheimer.com.png',3],
['battleship','#action','battleship.com.png',2],
['inception','#suspense','inception.com.png',2],
['cars','#thriller','cars.com.png',1],
['cars 2','#thriller','cars2.com.png',2],
['cars 3','#thriller','cars.com.png',1],
['angel has fallen down','#suspense','ahfd.com.png',2],
['incredibles 2','#action','incredibles2.com.png',2],
['john wick 4','#action','jw4.com.png',3],
['batman : the dark knight','#action','batmantdk.com.png',3],
['12th fail','#drama','12fail.com.png',1],
['final destination 4','#horror','fd4.com.png',3],
['barbie','#adventure','barbie.com.png',2],
['interstellar','#scifi','interstellar.com.png',2],
['momento','#suspense','momento.com.png',2]
]
             

        
filename = 'movie.csv'
with open('movie.csv','w+',newline='') as f:
    csv_w= csv.writer(f,delimiter = ',')
    csv_w.writerow(field)
    csv_w.writerows(movie_list)
    print('All rows written')
    
#[name,genre,image,rating(u,ua,a)]
movie_info_list = []
watchlist = []
thriller = [i for i in movie_list if i[1]=='#thriller']
adventure = [i for i in movie_list if i[1]=='#adventure']
action = [i for i in movie_list if i[1]=='#action']
drama = [i for i in movie_list if i[1]=='#drama']
suspense = [i for i in movie_list if i[1]=='#suspense']
scifi = [i for i in movie_list if i[1]=='#scifi']
horror = [i for i in movie_list if i[1]=='#horror']

u_r = [i for i in movie_list if i[3]==1]
ua_r = [i for i in movie_list if i[3]==2]
a_r = [i for i in movie_list if i[3]==3]

print('(1) home')
print('(2) add movie')
print('(3) search a movie')
print('(4) profile')
print('(5) watch a movie')
print('(6) show watchlist')
print('(7) search by genre')
print('(8) search by rating (U,U/A,A)')

print('welcome to cineflix')

name = input('enter name to start : ')
print("welcome",name)
while True:
   
    prompt1 = int(input("So what's up : "))

    if prompt1 == 1:
        n = len(movie_list)
        print(n)
        for k in range(n):
            print(movie_list[k])
       
    elif prompt1 == 2:
        password = input('enter password : ')
        if password == 'ottcisgood':
            movie_name_append = input("enter name of movie : ")
            movie_tag_append = input("enter tag : ")
            movie_image_append = input("enter image address : ")
            movie_rating_append = input("enter rating : ")
            movie_info_list.append(movie_name_append)
            movie_info_list.append(movie_tag_append)
            movie_info_list.append(movie_image_append)
            movie_info_list.append(movie_rating_append)
            movie_list.append(movie_info_list)
            print(movie_info_list,"is added")
            
            #with open('movie.csv','w+',newline='') as f:
             #   csv_w= csv.writer(f,delimiter = ',')
              #  csv_w.writerow(field)
               # for i in movie_info_list:
                #    csv_w.writerow(i)
                 #   print('All rows written')
            n = len(movie_list)
            for k in range(n):
                print(movie_list[k])
        else:
            print('wrong password! Try again')
           

    elif prompt1 == 3:
        search_movie = input('search movie : ')
        for i in movie_list:
           
            for j in i:
               
                if j == search_movie:
                    print('your movie',i,'is available, Watch!')
                    ask_user = input('add to watchlist or watch : ')
                    if ask_user == 'watch':
                        root = tk.Tk()
                        root.title(search_movie)

                        button = tk.Button(root, text='watch', command=on_button_click)
                        button.pack(padx=50, pady=50)

                        root.mainloop()

                    if ask_user == 'add to watchlist':
                        watchlist.append(j)
                        print(watchlist,' is added to your watchlist')
                break
           

    elif prompt1 == 4:
        print('name : ',name)

    elif prompt1 == 5:
        search_movie = input('search movie a to watch : ')
        for i in movie_list:
           
            for j in i:
               
                if j == search_movie:
                    print('your movie',i,'is available, Watch!')
                    root = tk.Tk()
                    root.title(search_movie)

                    button = tk.Button(root, text='watch', command=on_button_click)
                    button.pack(padx=50, pady=50)

                    root.mainloop()
                   
    elif prompt1 == 6:
        print('your watchlist ',watchlist)
       
    elif prompt1 == 7:
        print("(1) #action")
        print("(2) #adventure")
        print("(3) #drama")
        print("(4) #horror")
        print("(5) #scifi")
        print("(6) #suspense")
        print("(7) #thriller")
        prompt2 = int(input("enter genre : "))
        if prompt2 == 1:
            printlis(action)
        elif prompt2 == 2:
            printlis(adventure)
        elif prompt2 == 3:
            printlis(drama)
        elif prompt2 == 4:
            printlis(horror)
        elif prompt2 == 5:
            printlis(scifi)
        elif prompt2 == 6:
            printlis(suspense)
        elif prompt2 == 7:
            printlis(thriller)
        else:
            print('wrong choice !!')
    elif prompt1 == 8:
        print("(1) U")
        print("(2) U/A")
        print("(3) A")
        prompt3 = int(input("enter rateing : "))
        if prompt3 == 1:
            printlis(u_r)
        elif prompt3 == 2:
            printlis(ua_r)
        elif prompt3 == 3:
            printlis(a_r)
           
    else:
        print("Wrong Choice !! ")

    
                    
    
        
        
                
        
        



