# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
integer = 0
x = 0
y = 0 
bool = False 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = int(t%10)
    t = t / 10
    C = int(t%10)
    t = t / 10
    B = int(t % 6)
    A = int(t/6)
    return str(A)+':'+str(B)+str(C)+'.'+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global bool
    bool = True
def stop():
    timer.stop() 
    global x,y,bool
    if bool == True:
        y = y + 1
        if integer%10 == 0:
            x = x + 1
    bool = False
def reset():
    timer.stop()
    global integer,x,y
    integer = 0 
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global integer
    integer = integer + 1
    #print integer
    

# define draw handler
def draw_handler(canvas):
    global integer,x,y
    canvas.draw_text(format(integer), [80,80], 26, "RED")
    canvas.draw_text(str(x)+'/'+str(y), [160,20], 20, "RED")
    #canvas.draw_text(str(y), [190,16], 26, "RED")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

#create timer
timer = simplegui.create_timer(100,timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
# start frame
frame.start()


# Please remember to review the grading rubric
