import time

science_txt = "{:.2E} in scientific notation"
comma_txt = "{:,}"
curr_time = time.time()
timestruct = time.localtime(curr_time)
print("Seconds since January 1, 1970:", comma_txt.format(curr_time), "or", science_txt.format(curr_time))
print(time.strftime("%b %a %Y", timestruct))