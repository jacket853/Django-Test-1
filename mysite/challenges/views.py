from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

monthlyGoals = {
    "january":"Hello January! Happy New Year",
    "february":"Hello February! Brrr it's cold",
    "march":"Is it spring <i>yet</i>",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "august":"august",
    "september":"september",
    "october":"october",
    "november":"november",
    "december":"december",
    "vacationer":"take a chill pill big dawg"
}

def index(request):
    # dataToReturn = ""
    months = list(monthlyGoals.keys()) # get us jan, feb, etc. from keys from dict
    # for month in months: # iterate through list
    #     monthPath = "/challenges/" + month
    #     dataToReturn += f"<li style='color:blue; font-size:30px;'><a href='{monthPath}'>{month.capitalize()}</li>\n"
    # responseData = f"<ul>{dataToReturn}</ul>"
    # return HttpResponse(responseData)
    return render(request, "challenges/index.html", {
        "months_key":months
    })

def monthly_goal_by_num(request, month):
    #just testing that we are handling ints
    # return HttpResponse(f"<h1>numeric month entered: {month}</h1>")

    # use dictionary to help with our redirect
    months = list(monthlyGoals.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("You entered an invalid numeric month")
    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_goal(request, month):
    strToReturn = ""

    try:
        # strToReturn = "<h1>" + monthlyGoals[month] + "</h1>"
        strToReturn = monthlyGoals[month]
        # return HttpResponse(strToReturn)
        return render(request, "challenges/challenge.html", {
            "text":strToReturn,
            "month_name":month.capitalize()

        })
    except:
        return HttpResponseNotFound("<strong>ERROR!!! ERROR!!!</strong> month")

"""
    if month == "january":
        strToReturn = "<h1>Hello January! Happy New Year</h1>"
    elif month == "february":
        strToReturn = "<h1>Hello February! Brrr it's cold</h1>"
    elif month == "march":
        strToReturn = "<h1>Is it spring <i>yet</i></h1>"
    else:
        return HttpResponseNotFound("<h1>ERROR !!!! BZZZZT not found</h1>")
    return HttpResponse(strToReturn)
"""
