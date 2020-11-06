import pygame
import sys
import dot as d


class Game:
    pygame.init()
    pygame.display.set_caption('Guess where game')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_resolution = (screen.get_width(), screen.get_height())

    main_clock = pygame.time.Clock()

    dot = d.Dot(screen_resolution)
    print(dot.task)
    screen_mgr = "Menu"

    def draw_text(self, text, color, x, y, center, font_size):
        font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        x_margin = textrect.width/2 if center else 0
        y_margin = textrect.height/2 if center else 0
        textrect.topleft = (x - x_margin, y - y_margin)
        self.screen.blit(textobj, textrect)

    def draw_point(self, color, coordinates, radius):
        pygame.draw.circle(self.screen, color, coordinates, radius)
        pygame.draw.circle(self.screen, (83, 92, 104), coordinates, 4)

    def draw_button(self, color, coordinates, size, center):
        x_margin = size[0] / 2 if center else 0
        y_margin = size[1] / 2 if center else 0
        pygame.draw.rect(self.screen, color, (coordinates[0]-x_margin, coordinates[1]-y_margin, size[0], size[1]))

    def start(self):
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
                self.draw_button((186, 220, 88), (0.5 * self.screen.get_width(), 0.5 * self.screen.get_height()), (0.25 * self.screen.get_width(), 0.08 * self.screen.get_height()), True)
                self.draw_text("Let's play", (19, 15, 64), 0.5 * self.screen.get_width(), 0.5 * self.screen.get_height(), True, int(0.045 * self.screen.get_height()))
                if click and 0.375 * self.screen.get_width() <= mouse[0] <= 0.625 * self.screen.get_width() and 0.46 * self.screen.get_height() <= mouse[1] <= 0.54 * self.screen.get_height():
                    self.screen_mgr = "Game"
            elif self.screen_mgr == "Game":

                self.draw_point((186, 220, 88), self.dot.coordinates, 18)
                if click:
                    print(self.dot.add_points(mouse, 100))

            pygame.display.update()
            self.main_clock.tick(60)


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()
