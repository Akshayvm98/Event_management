'''StartPage displays Buttons  to navigate to Add_Events,Add_participants,View_participants'''

import tkinter as tk
import csv

LARGE_FONT=("Verdana",20)

class EventManagement(tk.Tk):

	def __init__(self,*args,**kwargs):

		tk.Tk.__init__(self,*args,**kwargs)

		container=tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_columnconfigure(0,weight=1)
		container.grid_rowconfigure(0,weight=1)
		self.geometry("390x200+10+10")
		self.frames={}
		#initialization of frames in the dictionary with key as the frame name and object returned as the value
		for F in (StartPage,Add_Events,Add_Participants,View_Participants):
			frame=F(parent=container,controller=self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(StartPage)
		#code to display the frame required 
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()
#start page frame contains buttons to navigate to Add_participants,add_events and view participants.
class StartPage(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		self.controller=controller
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(padx=10,pady=10)
		button1=tk.Button(self,text="add events",command=lambda:controller.show_frame(Add_Events))
		button2=tk.Button(self,text="add participants",command=lambda:controller.show_frame(Add_Participants))
		button3=tk.Button(self,text="view participants",command=lambda:controller.show_frame(View_Participants))
		
		button1.grid(row =4, column = 0, padx=20, pady =20)
		button2.grid(row = 4, column = 3, padx=20, pady =20)
		button3.grid(row = 8,column =1,padx=20, pady =20 )
		
#Add_Events lets you add new events to the contest with name of the event and the price of the event.
class Add_Events(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame(self,parent)
		self.controller  = controller
		self.name_label=tk.Label(self,text="Name of Event")
		self.price_label=tk.Label(self,text="Price for the event")
		self.name_text=tk.Text(self,height=2,width=30)#text box to add event name
		self.price_text=tk.Text(self,height=2,width=30)#text box to add the price of event

		self.name_label.grid(row=0,column=0,padx=20,pady=20)
		self.name_text.grid(row=0,column=1,padx=20,pady=20)
		self.price_label.grid(row=1,column=0,padx=20,pady=20)
		self.price_text.grid(row=1,column=1,padx=20,pady=20)

		self.back_button=tk.Button(self,text="Back",command=lambda:controller.show_frame(StartPage))#button when pressed, moves back to the startPage
		self.submit_button=tk.Button(self,text="submit",command=add_events)#button when pressed adds the new event to the events.csv file
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		self.submit_button.grid(row=2,column=4,padx=20,pady=20)

	def add_events(self):
		self.ename=self.name_text.get("1.0","end-1c")
		self.eprice=self.price_text.get("1.0","end-1c")
		self.name_text.delete("1.0","end")
		self.price_text.delete("1.0" ,"end")	
		print(self.ename, self.eprice)

		with open('events.csv','a',newline="\n") as f:
			wr=csv.writer(f, dialect='excel')
			wr.writerow([self.ename,self.eprice])

#to add new participants to the events, with name,college name and the list of events displayed in the optionmenu
class Add_Participants(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		self.controller=controller
		self.participant_name_label=tk.Label(self,text="Name of participant")
		self.college_name_label=tk.Label(self,text="Name of college")
		self.event_name_label=tk.Label(self,text="event name")
		self.participant_name_text=tk.Text(0,height=1,width=50)#adds name of the participant
		self.college_name_text=tk.Text(0,height=1,width=50)#college of the participant
		self.participant_name_label.grid(row=0,column=0,padx=10,pady=10)
		self.participant_name_text.grid(row=0,column=1,padx=10,pady=10)
		self.college_name_label.grid(row=1,column=0,padx=10,pady=10)
		self.college_name_text.grid(row=1,column=1,padx=10,pady=10)
		self.event_name_label.grid(row=2,column=0,padx=10,pady=10)

		self.submit_button=tk.Button(self,text="submit",command=self.add_participants)#adds the details to participant.csv file
		self.back_button=tk.Button(self,text="Back",command=lambda:controller.show_frame(StartPage))#moves back to startpage
		self.submit_button.grid(row=4,column=0,padx=10,pady=10)
		self.back_button.grid(row=4,column=1,padx=10,pady=10)
#file opened to display the events 
		with open('events.csv', 'r') as eventfile:
			r = csv.reader(eventfile)
			option = []                # To store the event name
			for line in r:
				option.append(line[0]) 
		options = list(set(option))		#to obtain only unique events 
		variable = tk.StringVar(self)
		variable.set(options[0])		#Setting the default event
		self.select = tk.OptionMenu(self, variable,*options).grid(row =2,column =1,padx=10,pady=10)
		self.event = variable.get()

	def add_participants(self):
		self.participant_name=self.participant_name_text.get("1.0","end-1c")
		self.college_name=self.college_name_text.get("1.0","end-1c")
		self.participant_name_text.delete("1.0","end")
		self.college_name_text.delete("1.0","end")
		print(self.participant_name,self.college_name)

		with open('participants.csv','a',newline="") as f:
			wr=csv.writer(f, dialect='excel')
			wr.writerow([self.ename, self.eprice, self.event])
	
#to view participants of the events enrolled
class View_Participants(tk.Frame):
	''' textbox for text
		back and view are buttons'''
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.textbox = tk.Text(self,width=45,height=7)
		self.back = tk.Button(self, text="Back",command=lambda: controller.show_frame(StartPage))
		self.view = tk.Button(self, text = " View", command =self.view_participant).grid(row =0,column=0,padx=5,pady=5)
		self.textbox.grid(rowspan = 5,padx=10, pady =5)
		self.back.grid(row=7, padx=5, pady =5)
	
	def view_participant(self):
		with open("participants.csv","r") as myfile:
			rd=csv.reader(myfile)
			for i,line in enumerate(rd) :
				print(f"{line[0]} - {line[1]}")
				self.textbox.insert("0.0",f"{line[0]}\t  {line[1]}\t  {line[2]}\n")



app=EventManagement()
app.mainloop()

