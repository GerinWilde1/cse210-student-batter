import random
from game import constants
from game.action import Action
import sys
from game.point import Point
class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        bricks = cast["brick"]
        ball = cast["ball"][0]#one ball
        paddle = cast["paddle"]
        walls = cast["wall"]
        
        for brick in bricks:#for look tp manage brick collison
            
            if brick.get_position().equals(ball.get_position()) and brick.get_text() !="":
                x = -(ball.get_velocity().get_x())
                y = -(ball.get_velocity().get_y())
                
                velocity = Point(x ,y) 
                ball.set_velocity(velocity)
                brick.set_text("")  
                break
        
        for wall in walls: #for loop to manage walls collision

            if (wall.get_position().get_x()-1) == (ball.get_position().get_x()) or (wall.get_position().get_x()+1) == (ball.get_position().get_x()):
                x = -(ball.get_velocity().get_x())
                ball.set_velocity(Point(x, ball.get_velocity().get_y()))
        
        if (ball.get_position().get_y() == 1):
            y = -(ball.get_velocity().get_y())
            ball.set_velocity(Point(ball.get_velocity().get_x(), y))
        

        P = 0
        for section in paddle: #for loop to manage pattle collison
            if section.get_position().equals(ball.get_position()):
                rando = random.randint(0,2)
                part  = section.get_velocity().get_x()
                
                if section.get_velocity().get_x() < 0:
                    x = section.get_velocity().get_x() - rando
                else:
                    x = section.get_velocity().get_x() + rando

                velocity = Point(x, -1)
                ball.set_velocity(velocity)
                P += 1
                break
            elif (ball.get_position().get_y() == constants.MAX_Y - 1) and P == len(paddle)-1:
                sys.exit()
            else:
                P += 1