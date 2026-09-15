import pygame

class Cell:
    def __init__(self, screen: pygame.Surface, field: list[list[int]]):
        self.screen = screen
        self.field = field
        self.neightbour = 0
        self.to_update = []
        self.to_update2 = []

    def draw(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 255, 0), ((self.screen.get_height()/len(self.field[i])) * j, 
                                                                (self.screen.get_height()/len(self.field)) * i,
                                                                  self.screen.get_height()/len(self.field[i]),
                                                                  self.screen.get_height()/len(self.field[i])))

    def update_field(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if i-1 >= 0:
                    if self.field[i-1][j] == 1:
                        self.neightbour+=1
                if i+1 < len(self.field):
                    if self.field[i+1][j] == 1:
                        self.neightbour+=1
                if j-1 >= 0:
                    if self.field[i][j-1] == 1:
                        self.neightbour+=1
                if j+1 < len(self.field[i]):
                    if self.field[i][j+1] == 1:
                        self.neightbour+=1
                if i-1 >= 0 and j-1 >= 0:
                    if self.field[i-1][j-1] == 1:
                        self.neightbour+=1
                if i-1 >= 0 and j+1 < len(self.field[i]):
                    if self.field[i-1][j+1] == 1:
                        self.neightbour+=1
                if i+1 < len(self.field) and j-1 >= 0:
                    if self.field[i+1][j-1] == 1:
                        self.neightbour+=1
                if i+1 < len(self.field) and j+1 < len(self.field[i]):
                    if self.field[i+1][j+1] == 1:
                        self.neightbour+=1
                if (self.neightbour < 2 or self.neightbour > 3) and self.field[i][j] == 1:
                    self.to_update.append((i, j, 0))
                elif self.neightbour == 3 and self.field[i][j] == 0:
                    self.to_update.append((i, j, 1))
                self.neightbour = 0

        for i, j, value in self.to_update:
            self.field[i][j] = value
        self.to_update.clear()