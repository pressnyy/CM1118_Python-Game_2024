import pygame

class Timer():
    def __init__(self):
        # Colors
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

        # Font settings
        self.font = pygame.font.Font(None, 36)
        self.timer_text = self.font.render("", True, self.RED)
        self.timer_rect = self.timer_text.get_rect(topleft=(10, 10))

        self.startTimer()

    def startTimer(self):
        # Start time for measuring elapsed time
        self.start_time = pygame.time.get_ticks() / 1000

    def countUp(self, screen):
        # Calculate elapsed time
        self.elapsed_time = pygame.time.get_ticks() / 1000 - self.start_time

        # Update timer text
        self.timer_text = self.font.render(f"Elapsed Time: {self.elapsed_time:.2f} seconds", True, self.BLACK)
        
        # Draw timer text
        screen.blit(self.timer_text, self.timer_rect)

    def getTime(self):
        return self.elapsed_time