#! /usr/bin/python
#########################################################################################
#	
#	Copyright (C) 2011-2013  Ravi Malik
#	
#	This program is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License
#	as published by the Free Software Foundation; either version 2
#	of the License, or (at your option) any later version.
#	
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#	You may contact the author by:
#		E-Mail: ravimalik2364@gmail.com
#	
#
###########################################################################################

from calc import *
from Tkinter import *
import tkMessageBox as message
class interface:
	def __init__(self,parent):
		self.records=[]
		self.res=StringVar()
		root=self.root=parent
		root.title("The Calculator")
		Label(root,text="The Calculator",fg="Blue").pack()
		menu=Menu(root)
		root.config(menu=menu)
		filemenu=Menu(menu)
		
		menu.add_cascade(label="File",menu=filemenu)
		filemenu.add_command(label="Quit",command=self.quit)
		
		aboutmenu=Menu(menu)
		menu.add_cascade(label="About",menu=aboutmenu)
		aboutmenu.add_command(label="Help",command=self.help)
		aboutmenu.add_command(label="About",command=self.about)		
		
		Label(root,text="Enter the expression to evaluate").pack()
		self.e=Entry(root)
		self.e.pack(padx=5)
		self.e.focus_set()
		b=Button(root,text="Evaluate",command=self.send)
		b.pack(pady=5)
		Label(root,textvariable=self.res).pack()
		Button(root,text="Show Previous Results",command=self.showrecords).pack()
		Button(root,text="Clear Previous Records",command=self.clearrecords).pack()
		Button(root,text="Export Previous Results to Text File",command=self.exportrecords).pack()
	def send(self):
		exp=self.e.get()
		value=""
		val=""
		try:
			infix=parse(exp)
			infix=preeval(infix)		
			postfix=convert(infix)
			value=str(evaluate(postfix))
			val="Value is : "+value
		except ZeroDivisionError:
			val="Division by Zero not allowed."
		except ValueError:
			val="Domain of a Function out of bound"
		self.res.set(val)
		r=record(exp,value)
		self.records.append(r)
	def showrecords(self):
		rec=Toplevel(root)
		if len(self.records)==0:
			Label(rec,text="No Records in the Buffer.").grid()
		else:
			Label(rec,text="Expression:").grid(row=0,column=0)
			Label(rec,text="Result:").grid(row=0,column=1)
			cr=1			
			for i in self.records:
				Label(rec,text=i.expression).grid(row=cr,column=0)
				Label(rec,text=i.result).grid(row=cr,column=1)
				cr=cr+1
		root.wait_window(rec)
	def clearrecords(self):
		self.records=[]
	def exportrecords(self):
		exp=Toplevel(root)
		self.fname=StringVar()
		res=StringVar()
		Label(exp,text="Enter the filename to save:").grid(row=0,column=0)
		Entry(exp,textvariable=self.fname).grid(row=0,column=1)
		Button(exp,text="Export",command=self.export).grid(row=1,column=0,columnspan=2)
		root.wait_window(exp)
	def export(self):
		fn=self.fname.get()
		f=open(fn,"w")
		c=1
		for i in self.records:
			f.write("%d.\nExpression:%s\nResult:%s\n\n"%(c,i.expression,i.result))
			c=c+1
		f.close()
		message.showinfo("Information","Export Complete")
	def quit(self):
		root.quit()	
	def help(self):
		top=Toplevel(root)
		top.title("Help")
		Label(top,text='''Welcome to Help.
Enter the expression to evaluate . You can give the following operators:
1. Addition:		+
2. Subtraction:		-
3. Multiplication:	*
4. Division:		/
5. Power:		^
6. Sine :		sin()
7. Cosine:		cos()
8. Tangent:		tan()
9. Cosecant:		cosec()
10. Secant:		sec()
11. Cotangent:		cot()
12. Log base 10:	log()
13. Natural Log:	ln()
14. Factorial:		fact()
15. Absolute Value:	abs()
16. Square Root:	sqrt() 
After entering the expression click on evaluate to get the result of the expression.''').pack()
		root.wait_window(top)
	def about(self):
		top=Toplevel(root)
		top.title("About")
		Label(top,text="Developed by Ravi Malik using Python 2.7 and Tkinter GUI").pack()
		root.wait_window(top)
class record:
	def __init__(self,exp,res):
		self.expression=exp
		self.result=res
root=Tk()
d=interface(root)
root.mainloop()
