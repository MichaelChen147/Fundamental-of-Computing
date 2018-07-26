# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
x = 0
y = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D
    t = counter
    if (t % 600) < 10:
        D = str(t % 600)[0]
        C = str(0)
        B = str(0)
    elif 10 <= (t % 600) < 100:
        D = str(t % 600)[1]
        C = str(t % 600)[0]
        B = str(0)
    else:
        D = str(t % 600)[2]
        C = str(t % 600)[1]
        B = str(t % 600)[0]    
    A = str(t / 600)
    return A + ":" + B + C + "." + D
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
    
def Stop():
    timer.stop()
    global x, y, D

    if D == "0":
        x += 1
    y += 1
    
def Reset():
    global counter, x, y
    timer.stop()
    counter = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    

# define draw handler
def draw(canvas):
    global counter, x, y
    if counter <= 6000:
        canvas.draw_text(format(counter), [80,150], 40, "Red")                        
    canvas.draw_text(str(x) + "/" + str(y), 
                    [250,25], 30, "Red")  
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", Start)
frame.add_button("Stop", Stop)
frame.add_button("Reset", Reset)

# start frame
frame.start()

# Please remember to review the grading rubric
