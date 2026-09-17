import pygame

class Cell:
    def __init__(self, screen: pygame.Surface, field: list[list[int]]):
        self.screen = screen
        self.field = field
        self.neightbour = 0
        self.to_update = []

    def draw(self):
        heigth = self.screen.get_height()/len(self.field)
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 1:
                    width = self.screen.get_height()/len(self.field[i])
                    pygame.draw.rect(self.screen, (0, 255, 0), (width * j, 
                                                                heigth * i,
                                                                  width,
                                                                  width))
                    pygame.draw.rect(self.screen, (155, 0, 0),(width * j, 
                                                                (heigth * i),
                                                                  width/2,
                                                                  width/2))
                    pygame.draw.rect(self.screen, (0, 0, 155),  (width * j + width/2, 
                                                                (heigth * i + width/2),
                                                                    width/2,
                                                                    width/2)) 

    def update_field(self):
        field_len_row = len(self.field)
        field_len_col = len(self.field[0]) if field_len_row > 0 else 0

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if i-1 >= 0:
                    if self.field[i-1][j] == 1:
                        self.neightbour += 1

                if i+1 < field_len_row:
                    if self.field[i+1][j] == 1:
                        self.neightbour += 1

                if j-1 >= 0:
                    if self.field[i][j-1] == 1:
                        self.neightbour += 1

                if j+1 < field_len_col:
                    if self.field[i][j+1] == 1:
                        self.neightbour += 1

                if i-1 >= 0 and j-1 >= 0:
                    if self.field[i-1][j-1] == 1:
                        self.neightbour += 1

                if i-1 >= 0 and j+1 < field_len_col:
                    if self.field[i-1][j+1] == 1:
                        self.neightbour += 1

                if i+1 < field_len_row and j-1 >= 0:
                    if self.field[i+1][j-1] == 1:
                        self.neightbour += 1

                if i+1 < field_len_row and j+1 < field_len_col:
                    if self.field[i+1][j+1] == 1:
                        self.neightbour += 1

                if (self.neightbour < 2 or self.neightbour > 3) and self.field[i][j] == 1:
                    self.to_update.append((i, j, 0))
                elif self.neightbour == 3 and self.field[i][j] == 0:
                    self.to_update.append((i, j, 1))
                self.neightbour = 0

        for i, j, value in self.to_update:
            self.field[i][j] = value
        self.to_update.clear()