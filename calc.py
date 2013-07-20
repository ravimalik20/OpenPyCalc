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
#
###########################################################################################

from copy import deepcopy
from copy import deepcopy
from math import *
bchar=["*","/","+","-","(",")","^"]
ops=["*","/","+","-","^","sin","cos","tan","cosec","sec","cot","sqrt","fact","abs","log","ln"]
unary=["sin","cos","tan","cosec","sec","cot","sqrt","fact","abs","log","ln"]
def preeval(a):
	t=a
	i=0
	stack=[]
	while i!=len(t):
		if t[i] in unary:
			stack.append(i)
		i=i+1
	while len(stack)!=0:
		a=stack.pop()
		b=-1		
		exp=[]
		c=1
		i=a+2
		while c!=0:
			if t[i]=="(":
				c=c+1
			elif t[i]==")":
				c=c-1
			exp.append(deepcopy(t[i]))
			i=i+1
		del(exp[len(exp)-1])		
		b=i-1
		post=convert(exp)
		val=evaluate(post)
		if t[a]=="sin":
			val=radians(float(val))
			val=sin(float(val))
		elif t[a]=="cos":
			val=radians(float(val))
			val=cos(float(val))
		elif t[a]=="tan":
			val=radians(float(val))
			val=tan(float(val))
		elif t[a]=="cosec":
			val=radians(float(val))
			val=1/sin(float(val))
		elif t[a]=="sec":
			val=radians(float(val))
			val=1/cos(float(val))
		elif t[a]=="cot":
			val=radians(float(val))
			val=1/tan(float(val))		
		elif t[a]=="sqrt":
			val=sqrt(float(val))
		elif t[a]=="log":
			val=log10(float(val))
		elif t[a]=="ln":
			val=log1p(float(val))
		elif t[a]=="fact":
			val=factorial(int(val))
		elif t[a]=="abs":
			val=fabs(float(val))
		
		while b!=a:
			del(t[a])
			b=b-1
		t[a]=str(val)		
	return t	

def parse(a):
	infix=[]	
	n=len(a)
	token=""
	if a[0]=="-":
		a="0"+a
	n=len(a)
	for i in range(0,n):		
		if a[i] in bchar:
			if a[i]=="-":
				if a[i+1].isalpha():
					if len(token)!=0:
						infix.append(deepcopy(token))
						token="" 
					infix.append(deepcopy(a[i]))	
				elif a[i-1] in bchar:
					token=token+a[i]
				else:
					if len(token)!=0:
						infix.append(deepcopy(token))
						token=""
					infix.append(deepcopy(a[i]))
			else:
				if len(token)!=0:
					infix.append(deepcopy(token))
					token=""
				infix.append(deepcopy(a[i]))			
		else:
			token=token+a[i] 
	if len(token)!=0:
		infix.append(deepcopy(token))
	return infix

def convert(infix):
	postfix=[]	
	stack=[]
	stack.append("(")
	infix.append(")")
	sttop=0
	n=len(infix)
	for i in range(0,n):
		if not infix[i] in bchar:
			postfix.append(deepcopy(infix[i]))
		elif infix[i]=="(":
			stack.append(deepcopy(infix[i]))
			sttop=sttop+1
		elif infix[i] in ops:
			if infix[i]=="-":
				while stack[sttop] in ops:
					postfix.append(deepcopy(stack.pop()))
					sttop=sttop-1
			elif infix[i]=="+":
				while stack[sttop] in ops:
					postfix.append(deepcopy(stack.pop()))
					sttop=sttop-1	
			elif infix[i]=="*":
				while stack[sttop] in ops and stack[sttop]!="-" and stack[sttop]!="+":
					postfix.append(deepcopy(stack.pop()))
					sttop=sttop-1
			elif infix[i]=="/":
				while stack[sttop] in ops and stack[sttop]!="-" and stack[sttop]!="+" and stack[sttop]!="*":
					postfix.append(deepcopy(stack.pop()))
					sttop=sttop-1
			elif infix[i]=="^":
				while stack[sttop] in ops and stack[sttop]!="-" and stack[sttop]!="+" and stack[sttop]!="*" and stack[sttop]!="/":
					postfix.append(deepcopy(stack.pop()))
					sttop=sttop-1
			elif infix[i] in unary:
				while stack[sttop] in ops and stack[sttop]!="-" and stack[sttop]!="+" and stack[sttop]!="*" and stack[sttop]!="/" and stack[sttop]!="^":
					postfix.append(deepcopy(stack.pop()))
					sttop=sttop-1
			stack.append(deepcopy(infix[i]))
			sttop=sttop+1
		elif infix[i]==")":
			while stack[sttop]!="(":
				postfix.append(deepcopy(stack.pop()))
				sttop=sttop-1
			del(stack[sttop])
			sttop=sttop-1
	return postfix

def evaluate(postfix):
	temp=deepcopy(postfix)	
	stack=[]
	sttop=-1
	temp.append(")")
	n=len(temp)
	i=0
	while temp[i]!=")":
		if not temp[i] in bchar:
			stack.append(deepcopy(temp[i]))
			sttop=sttop+1
		else:
			a=stack.pop()
			b=stack.pop()
			sttop=sttop-2
			c=0
			if temp[i]=="+":
				c=float(b)+float(a)
			elif temp[i]=="-":
				c=float(b)-float(a)
			elif temp[i]=="*":
				c=float(b)*float(a)
			elif temp[i]=="/":
				c=float(b)/float(a)
			elif temp[i]=="^":
				a=float(a)
				b=float(b)
				c=float(pow(b,a))
			stack.append(deepcopy(c))
			sttop=sttop+1
		i=i+1	
	return stack[sttop]
