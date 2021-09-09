from tkinter import *
import PIL.ImageTk as itk
from game import *
gameover = False
juego =Game()
window = Tk()

pixel = PhotoImage(width=1,height=1)
#o = PIL.Image.open('x.png')
oimg = itk.PhotoImage(file='o2.png')
ximg = itk.PhotoImage(file='x2.png')


turn = 'O'
def change():
    global turn
    if(turn=='O'):
        turn ='X'
    else:
        turn ='O'
def play(button,x,y):
    global turn
    global gameover
    global juego
    if not gameover:    
        if(turn =='O'):
            button.config(image=oimg)
        elif(turn=='X'):
            button.config(image=ximg)
        
        juego.play(turn,x-1,y-1)
        
        gameover = juego.check_column(y-1) or juego.check_row(x-1) or juego.check_diagonales()
        print(juego.check_column(y-1))
        print(juego.check_row(x-1))
        print(juego.check_diagonales())
         
        change()
    if gameover:
        print("Game is over")
        buttons = [button11,button12,button13,button21,button22,button23,button31,button32,button33]    
        for i in buttons:
            i.config(image=pixel)
        gameover = False
        juego = Game()
    print(juego.board)
game = Frame(window, bg="black",width=300, height=300)

window.geometry("500x500")
game.place(relx=.5,rely=.5,anchor="center")

button11 =Button(game,image=pixel,text="Juega",command = lambda: play(button11,1,1),height=50,width=50)
button11.config(height=80,width=80)
button11.place(x=0,y=0)

button12=Button(game,image=pixel,text="Juega",command = lambda: play(button12,1,2),height=80,width=80)
button12.place(x=106,y=0)


button13 =Button(game,image=pixel,text="Juega",command = lambda: play(button13,1,3),height=80,width=80)
button13.place(x=212,y=0)

button21 =Button(game,image=pixel,text="Juega",command = lambda: play(button21,2,1),height=50,width=50)
button21.config(height=80,width=80)
button21.place(x=0,y=105)

button22=Button(game,image=pixel,text="Juega",command = lambda: play(button22,2,2),height=80,width=80)
button22.place(x=106,y=105)


button23 =Button(game,image=pixel,text="Juega",command = lambda: play(button23,2,3),height=80,width=80)
button23.place(x=212,y=105)

button31 =Button(game,image=pixel,text="Juega",command = lambda: play(button31,3,1),height=50,width=50)
button31.config(height=80,width=80)
button31.place(x=0,y=210)

button32=Button(game,image=pixel,text="Juega",command = lambda: play(button32,3,2),height=80,width=80)
button32.place(x=106,y=210)


button33 =Button(game,image=pixel,text="Juega",command = lambda: play(button33,3,3),height=80,width=80)
button33.place(x=212,y=210)




    
    
window.mainloop()