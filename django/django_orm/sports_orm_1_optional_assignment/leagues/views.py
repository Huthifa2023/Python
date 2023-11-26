from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"1_baseball" : League.objects.filter(sport = "Baseball"),
		"2_womens" : League.objects.filter(name__contains="wom"),
		"3_hockey" : League.objects.filter(sport__contains="Hockey"),
		"4_NotFootball" : League.objects.exclude(sport__contains="Football"),
		"5_conferences" : League.objects.filter(name__contains="Conference"),
		"6_Atlantic_region" : League.objects.filter(name__contains="Atlantic"),
		"7_Dallas" : Team.objects.filter(location="Dallas"),
		"8_Raptors" : Team.objects.filter(team_name__contains="Raptors"),
		"9_city" : Team.objects.filter(location__contains="City"),
		"10_begin_t" : Team.objects.filter(team_name__startswith="T"),
		"11_teams_alpha" : Team.objects.all().order_by("location"),
		"12_reverse_team" : Team.objects.all().order_by("-team_name"),
		"13_last_cooper" : Player.objects.filter(last_name="Cooper"),
		"14_first_joshua" : Player.objects.filter(first_name= "Joshua"),
		"15_last_Cooper_not_first_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name= "Joshua"),
		"16_first_alexander_or_wyatt": Player.objects.filter(first_name__in=["Alexander","Wyatt"]),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")