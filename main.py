import pygame
import sys
import dot as d
import statistics
from threading import Timer


class Game:
    print(statistics.read_record())

    new_record = False

    pygame.init()
    pygame.display.set_caption('Guess where game')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_resolution = (screen.get_width(), screen.get_height() - 50)

    main_clock = pygame.time.Clock()

    dot = d.Dot(screen_resolution)
    print(dot.task)
    screen_mgr = "Menu"

    last_click = False

    def draw_text(self, text, color, x, y, center, font_size):
        font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        x_margin = textrect.width / 2 if center else 0
        y_margin = textrect.height / 2 if center else 0
        textrect.topleft = (x - x_margin, y - y_margin)
        self.screen.blit(textobj, textrect)

    def draw_point(self, color, coordinates, radius, empty):
        pygame.draw.circle(self.screen, color, coordinates, radius)
        pygame.draw.circle(self.screen, (83, 92, 104), coordinates, empty)

    def draw_rect(self, color, coordinates, size, center):
        x_margin = size[0] / 2 if center else 0
        y_margin = size[1] / 2 if center else 0
        pygame.draw.rect(self.screen, color, (coordinates[0] - x_margin, coordinates[1] - y_margin, size[0], size[1]))

    def draw_top_menu(self):
        # top menu
        self.draw_rect((149, 175, 192), (0, 0), (self.screen.get_width(), 50), False)
        self.draw_text(f"Round {statistics.round_of_game}/10", (19, 15, 64), 100, 30, True, 30)
        if self.screen_mgr == "Game":
            self.draw_text(f"Task: {self.dot.task} px", (19, 15, 64), 0.5 * self.screen.get_width(), 30, True, 30)
        elif self.screen_mgr == "Show_correct":
            self.draw_text(f"Last task: {self.dot.task}, you got {new_points} points, Click LMB to continue...", (19, 15, 64), 0.5 * self.screen.get_width(), 30, True, 30)
        self.draw_text(f"{statistics.points}", (19, 15, 64), self.screen.get_width() - 60, 30, True, 30)

    def start(self):
        global clicked_position
        global new_points
        while True:
            # exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # rest
            self.screen.fill((83, 92, 104))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]

            if self.screen_mgr == "Menu":
                # let's play button
                lets_play_button = Button(game=self, button_color=(186, 220, 88), text_color=(19, 15, 64), x=0.5*self.screen.get_width(), y=0.3*self.screen.get_height(), text="Let's play")
                if lets_play_button.onclick_method(click, mouse):
                    self.screen_mgr = "Game"

                # quit game button
                quit_play_button = Button(game=self, button_color=(235, 77, 75), text_color=(19, 15, 64), x=0.5*self.screen.get_width(), y=0.5*self.screen.get_height(), text="Quit the game")
                if quit_play_button.onclick_method(click, mouse):
                    pygame.quit()
                    sys.exit()

                # record
                self.draw_text(f'Record: {str(statistics.read_record())}', (68, 189, 50), 0.5 * self.screen.get_width(),
                                   0.65 * self.screen.get_height(), True, int(0.05 * self.screen.get_height()))

            elif self.screen_mgr == "Game":
                # circle, which change radius during mouse move
                self.draw_point((235, 77, 75), self.dot.coordinates, int(d.distance(mouse, self.dot.coordinates)),
                                int(d.distance(mouse, self.dot.coordinates)) - 3)

                # top menu
                self.draw_top_menu()

                # our static point
                self.draw_point((186, 220, 88), self.dot.coordinates, 18, 4)

                if click and self.last_click == False:
                    clicked_position = mouse
                    new_points = self.dot.add_points(mouse)
                    self.screen_mgr = "Show_correct"

            elif self.screen_mgr == "Show_correct":
                # correct circle
                pygame.draw.circle(self.screen, (106, 176, 76), self.dot.coordinates, self.dot.task, width=3)

                # clicked circle
                pygame.draw.circle(self.screen, (235, 77, 75), self.dot.coordinates, d.distance(clicked_position, self.dot.coordinates), width=3)

                # clicked point
                pygame.draw.circle(self.screen, (235, 77, 75), clicked_position, 18, width=0)

                # our static point
                self.draw_point((186, 220, 88), self.dot.coordinates, 18, 4)

                # top menu
                self.draw_top_menu()

                if click and self.last_click == False:
                    self.dot.__del__()

                    if statistics.round_of_game < 10:
                        self.screen_mgr = "Game"
                        self.dot = d.Dot(self.screen_resolution)
                    else:
                        self.screen_mgr = "End of the game"
                        if statistics.read_record() < statistics.points:
                            statistics.new_record(statistics.points)
                            self.new_record = True

            elif self.screen_mgr == "End of the game":
                self.draw_text(str(statistics.points), (186, 220, 88), 0.5 * self.screen.get_width(),
                               0.35 * self.screen.get_height(), True, int(0.15 * self.screen.get_height()))

                # Play again button
                play_again_button = Button(game=self, button_color=(186, 220, 88), text_color=(19, 15, 64), x=0.5*self.screen.get_width(), y=0.6*self.screen.get_height(), text="Play again")
                if play_again_button.onclick_method(click, mouse):
                    self.screen_mgr = "Game"
                    self.new_record = False
                    statistics.points = 0
                    statistics.round_of_game = 1

                # quit game button
                quit_play_button = Button(game=self, button_color=(235, 77, 75), text_color=(19, 15, 64),
                                              x=0.5 * self.screen.get_width(), y=0.75 * self.screen.get_height(),
                                              text="Quit the game")

                if self.new_record:
                    self.draw_text(f"New record", (186, 220, 88), 0.5 * self.screen.get_width(),
                                   0.15 * self.screen.get_height(), True, int(0.15 * self.screen.get_height()))

                if quit_play_button.onclick_method(click, mouse):
                    pygame.quit()
                    sys.exit()

            if click:
                self.last_click = True
            else:
                self.last_click = False

            pygame.display.update()
            self.main_clock.tick(60)


class Button:
    def __init__(self, game, button_color, text_color, x, y, text):
        self.game = game
        self.x = x
        self.y = y
        game.draw_rect(button_color, (x, y),
                       (0.25 * game.screen.get_width(), 0.08 * game.screen.get_height()), True)
        game.draw_text(text, text_color, x,
                       y, True, int(0.045 * game.screen.get_height()))

    def onclick_method(self, click, mouse):
        if click and self.x - 0.125 * self.game.screen.get_width() <= mouse[0] <= self.x + 0.125 * self.game.screen.get_width() and self.y - 0.04 * self.game.screen.get_height() <= mouse[1] <= self.y + 0.04 * self.game.screen.get_height():
            return True
        return False


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
