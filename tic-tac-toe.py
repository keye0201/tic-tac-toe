from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
            winner()
      else :
            player = "X"
            button["bg"] = "lightgreen"
            winner()

def winner():
      if list[0]["text"]==list[1]["text"]==list[2]["text"] != "     ":
            winnerShow()
      elif list[0]["text"]==list[3]["text"]==list[6]["text"] != "     ":
            winnerShow()
      elif list[0]["text"]==list[4]["text"]==list[8]["text"] != "     ":
            winnerShow()
      elif list[1]["text"]==list[4]["text"]==list[7]["text"] != "     ":
            winnerShow()
      elif list[2]["text"]==list[4]["text"]==list[6]["text"] != "     ":
            winnerShow()
      elif list[2]["text"]==list[5]["text"]==list[8]["text"] != "     ":
            winnerShow()
      elif list[3]["text"]==list[4]["text"]==list[5]["text"] != "     ":
            winnerShow()
      elif list[6]["text"]==list[7]["text"]==list[8]["text"] != "     ":
            winnerShow()

def winnerShow():
      if player == "X" :
            m = Message(window, text="O is win")
            m.grid(row=3, column=0)
            
      else :
            m = Message(window, text="X is win")
            m.grid(row=3, column=0)

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


