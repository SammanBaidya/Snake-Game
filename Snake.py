import tkinter as tk #tkinter moduler for GUI
import random 
import pygame # type: ignore #Fix the pygame import!!!!!
#Grid and window sizing
ROWS = 25 
COLS = 25
TILE_SIZE = 25 
WINDOW_WIDTH = TILE_SIZE * COLS #25 * 25 = 625
WINDOW_HEIGHT = TILE_SIZE * COLS #25 * 25 = 625


#[[[[[[[[[[[[[[[[[[[ONE PIECE IS REAL]]]]]]]]]]]]]]]]]]]

class Tile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

#game window []
window = tk.Tk()
window.title("Snake Fever") #Game TITLE 
window.resizable(False, False) #To stop the window resizing
canvas = tk.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack() #canvas add to the winow

window.update()

# Center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()        

def init_game():
    global snake, food, velocityX, velocityY, snake_body, game_over, score
    snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5) #single tile for snake
    food = Tile(TILE_SIZE * 10, TILE_SIZE * 10) #single tile for food
    velocityX, velocityY = 0, 0 
    snake_body = [] 
    game_over = False #Game over check
    score = 0 

def change_direction(e): #here e = event print(e) (e.keysym) !
    global velocityX, velocityY, game_over
    if game_over:
        init_game() #Resets the game after you lose :V
        return #edit code to reset game variable to play again..
    
    #Change direction based on pressed keys
    if (e.keysym == "Up" and velocityY != 1): 
        velocityX = 0
        velocityY = -1
    
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
        
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0    
    
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0


#Function to check for collision with walls and snake             
def check_collisions():
    global game_over
    #Check for wall collison
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True #ENd the game if snake hits the wall
        return

#Check for self collision
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True #End if self collision

            return


def check_food_collision():
    global score
    if snake.x == food.x and snake.y == food.y:#Checks if snake head is on the food
        snake_body.append(Tile(snake.x, snake.y)) #adds a new segment to snake
        food.x = random.randint(0, COLS - 1) * TILE_SIZE #randomly place food again
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1 #score update 
        

def move_snake(): #function to move the snake 
    if game_over:
        return

    check_collisions() 
    if game_over:
        return

    check_food_collision()

    if len(snake_body) > 0:#moves the snake's body
        snake_body.insert(0, Tile(snake.x, snake.y)) #add the head position to body
        snake_body.pop() #last segment remove

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw(): 
    global snake, food, snake_body, game_over, score
    move_snake() #move the snake 
    canvas.delete("all")
    
    #making food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill='red')
    for tile in [snake] + snake_body:
        #making snake 
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill='lime green')
    if game_over:
        canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, font="Arial 20", text = f"Game Over HUMAN: {score}", fill="white")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f"Score: {score}", fill="white")
    window.after(100, draw) #call draw again every 100ms (1/10 of a sec) which is 10 frames per second.




init_game()
window.bind("<KeyRelease>", change_direction) #when you press direction key and let go
draw()
window.mainloop()#window events listener for key presses 

#Plan 14: next add music and graphics 

