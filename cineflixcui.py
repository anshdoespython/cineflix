import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo('ready to watch')
    
movie_list = [['oppenheimer','#drama','oppenheimer.com.png'],
              ['battleship','#action','battleship.com.png'],
              ['inception','#suspense','inception.com.png']
              
]
movie_info_list = []
watchlist = []

print('home')
print('add movie')
print('search')
print('profile')
print('watch a movie')
print('show watchlist')

print('welcome to cineflix')

name = input('enter name to start : ')
while True:
    
    prompt1 = input("So what's up : ")

    if prompt1 == 'home':
        n = len(movie_list)
        print(n)
        for k in range(n):
            print(movie_list[k])
        
    if prompt1 == 'add movie':
        password = input('enter password : ')
        if password == 'ottcisgood':
            movie_name_append = input("enter name of movie : ")
            movie_tag_append = input("enter tage : ")
            movie_image_append = input("enter image address : ")
            movie_info_list.append(movie_name_append)
            movie_info_list.append(movie_tag_append)
            movie_info_list.append(movie_image_append)
            movie_list.append(movie_info_list)
            print(movie_info_list,"is added")
            n = len(movie_list)
            for k in range(n):
                print(movie_list[k])

    if prompt1 == 'search':
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
            

    if prompt1 == 'profile':
        print('name : ',name)

    if prompt1 == 'watch a movie':
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
    if prompt1 == 'show watchlist':
        print('your watchlist ',watchlist)

    
                    
    
        
        
                
        
        



