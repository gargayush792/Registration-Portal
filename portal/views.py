from django.shortcuts import render, redirect, render_to_response
from portal.models import *
from django.http import *
from django.template import Context, loader
from django.contrib.auth import authenticate, login

y=""
z=0
u=""
username=""
password=""
s=0
i=0
na=""

def login(request):
	return render(request, 'login.html')

def log(request):
	global username
	global password
	username = request.POST['user']
	password = request.POST['pass']
	if (username=='robotix2014') and (password=='pbotixMMXIV'):
		return redirect(root)
	else:
		return HttpResponse("Wrong details entered.Please login again.")

def data(request):
	if (request.GET['team_name']!="") and (request.GET["name1"]!=""):
		x=1
		for ind_det in Details.objects.all():
			if ind_det.event == request.GET['event']:
				x=x+1
		Details(
			name1=request.GET['name1'],
			email1=request.GET['email1'],
			phone1=request.GET['phone1'],
			college1=request.GET['college1'],
			name2=request.GET['name2'],
			email2=request.GET['email2'],
			phone2=request.GET['phone2'],
			college2=request.GET['college2'],
			name3=request.GET['name3'],
			email3=request.GET['email3'],
			phone3=request.GET['phone3'],
			college3=request.GET['college3'],
			name4=request.GET['name4'],
			email4=request.GET['email4'],
			phone4=request.GET['phone4'],
			college4=request.GET['college4'],
			team_name=request.GET['team_name'],
			event=request.GET['event'],
			address=request.GET['address'],
			team_id=x,
			present_round=1,
			).save()		
		message="Please report to the help desk now.Your team ID is "+request.GET['event']+str(x)
	else:
		message='You submitted an invalid form.'
	return HttpResponse(message)

def root(request):
	if (username=='robotix2014') and (password=='pbotixMMXIV'):
		return render(request, 'main.html')
	else:
		return HttpResponse("Wrong")

def register(request):
	return render(request, 'form.html')

def scoring(request):
	if (username=='robotix2014') and (password=='pbotixMMXIV'):
		return render(request, 'scoreinitial.html')
	else:
		return HttpResponse("wrong")

def scoreinitial(request):
	global y
	global z
	global u
	global na
	na=request.GET['name']
	eve=request.GET['event']
	rou=request.GET['round']
	y=eve+str(rou)
	z=int(rou)
	u=eve
	det=eve+str(rou)+'.html'
	if z==3:
		det='round3.html'
	return render_to_response(det,{'filtered': Details.objects.filter(event=u)})

def certi(request):
	return render_to_response('certi.html',{'teamlist': Details.objects.all()})

def certiprocess(request):
	r7=request.GET['event']
	r8=int(request.GET['id'])
	yi= Details.objects.filter(event=r7, team_id=r8)
	for r6 in yi: 
		r6.certificate="given"
		r6.save()
	return HttpResponse("certificate given for the forementioned team recorded.")

def scoreprocess(request):
	global y
	global z
	global u
	global s
	global i
	i=int(request.GET['id'])
	if y == "IN1":
		s=int(request.GET['gcheckpoints'])*100+int(request.GET['corks'])*(150)+int(request.GET['botfalling'])*(-100)+int(request.GET['timeouts'])*(-100)+int(request.GET['restarts'])*(-200) + int(request.GET['runtimetaken'])
	if y == "IN2":
		s=int(request.GET['gcheckpoints'])*100+int(request.GET['corks'])*(150)-int(request.GET['botfalling'])*(100)-int(request.GET['timeouts'])*(100)-int(request.GET['restarts'])*(200)-int(request.GET['redf'])*(75) +  int(request.GET['runtimetaken'])
	if y == "CR1":
		s=int(request.GET['objpick'])*75+int(request.GET['objsafe'])*100  -int(request.GET['restarts'])*100-int(request.GET['timeouts'])*50-int(request.GET['objfallen'])*50-int(request.GET['botfallen'])*100 - ((int)(request.GET['runtimetaken'])/3)
	if y == "CR2":
		s=int(request.GET['objplatpick'])*75+int(request.GET['objwaterpick'])*100+int(request.GET['objsafe'])*100-int(request.GET['restarts'])*100-int(request.GET['timeouts'])*50-int(request.GET['objfallen'])*50-int(request.GET['botfallen'])*100 - ((int)(request.GET['runtimetaken'])/3)	
	if (y == "TR1"):
		s=1000 + int(request.GET['saved'])*100+int(request.GET['solshits'])*(-25)+int(request.GET['wallhits'])*(-20)+int(request.GET['enteredic'])*(-75)+int(request.GET['hitsecondc'])*(-50)+int(request.GET['hitthirdc'])*(-25)+int(request.GET['crossover'])*(-25)+int(request.GET['timeouts'])*(-25)+int(request.GET['restarts'])*(-80) + ((int(request.GET['allotedruntime']) - ((int)(request.GET['runtimetaken'])))/2)
	if ( y == "TR2"):
		s=1000 + int(request.GET['saved'])*100+int(request.GET['solshits'])*(-25)+int(request.GET['wallhits'])*(-20)+int(request.GET['enteredic'])*(-75)+int(request.GET['hitsecondc'])*(-50)+int(request.GET['hitthirdc'])*(-25)+int(request.GET['crossover'])*(-25)+int(request.GET['timeouts'])*(-25)+int(request.GET['restarts'])*(-80) + ((int(request.GET['allotedruntime']) - ((int)(request.GET['runtimetaken'])))/2)
	if (y == "GA1") or (y == "GA2"):
		s=int(request.GET['correctturn'])*50+int(request.GET['stopcorrect'])*(100)+int(request.GET['rtzone'])*(75)+int(request.GET['walltouch'])*(-20)+int(request.GET['timeouts'])*(-30)+int(request.GET['restarts'])*(-50)
	if (y == "TP1"):
		s=500 + int(request.GET['voidsfwe'])*100 + int(request.GET['voidsfe']) * 40 +int(request.GET['steps'])*(-20)+int(request.GET['voidsc'])*(-30)+int(request.GET['timeouts'])*(-25)+int(request.GET['restarts'])*(-80) + ((int(request.GET['allotedruntime']) - ((int)(request.GET['runtimetaken'])))/3)
	if (y == "TP2"):
		s=500 + int(request.GET['voidsfwe'])*100 + int(request.GET['voidsfe']) * 40+int(request.GET['steps'])*(-20)+int(request.GET['voidsc'])*(-30)+int(request.GET['timeouts'])*(-25)+int(request.GET['restarts'])*(-80) + ((int(request.GET['allotedruntime']) - ((int)(request.GET['runtimetaken'])))/3)
			
	if (z==3):
		s=request.GET['score']
	c = Context({
		"team": request.GET['id'],
		"score": s,
		"event": u,
		})
	t=loader.get_template('verifyscore.html')
	return HttpResponse(t.render(c))

def scorefinal(request):
	global s
	global z
	global i
	global u
	if request.GET['yes'] == 'y':
		if z==1:
			te=Details.objects.filter(team_id=i, event=u).update(round1 = s, score_person=na)
		if z==2:
			te=Details.objects.filter(team_id=i, event=u).update(round2 = s, score_person=na)
		if z==3:
			te=Details.objects.filter(team_id=i, event=u).update(round3 = s, score_person=na)
		return HttpResponse("The score has been added to the database")
#	elif request.GET['no'] == 'n':
#		return HttpRespone("No score is added")
	else:
		return redirect(scoring)

def printev(request):
	return render(request, 'teamsregd.html')


def printrequest(request):
	query_results = Details.objects.filter(event=request.GET['event'])
	r3 = loader.get_template('printevent.html')
	r4 = Context({
        'query_results': query_results,
    })
	return HttpResponse(r3.render(r4))

def promote(request):
	return render(request, 'promote.html')

def promote_process(request):
	te=Details.objects.filter(team_id=request.GET['id'], event=request.GET['event'])
	for oi in te:
		oi.present_round = oi.present_round+1
		oi.save()
	return HttpResponse("Team promoted")





	


	
