standard_months = [31,28,31,30,31,30,31,31,30,31,30,31]
leapyear_months = [31,29,31,30,31,30,31,31,30,31,30,31]

sundays = 0

leap_year = False

overall_days = 0
day = 0
month = 0
year = 1900


while year < 2001:
	day += 1
	overall_days += 1

	if day == 1 and overall_days % 7 == 0:
		sundays += 1

	if leap_year:
		months = leapyear_months
	else:
		months = standard_months

	print(day,month+1,year,overall_days,sundays-2)

	if day == months[month]:
		day = 0
		month+=1

	if month == 12:
		year+=1
		month = 0

	leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


