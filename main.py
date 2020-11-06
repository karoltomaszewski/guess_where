import pygame
import sys


class Game:
    pygame.init()
    pygame.display.set_caption('Guess where game')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    main_clock = pygame.time.Clock()

    font = pygame.font.Font(pygame.font.get_default_font(), 20)

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

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
            self.screen.fill((0, 0, 0))
            self.draw_text("Hello world", (255, 255, 255), 0.5 * self.screen.get_width(), 0.3 * self.screen.get_height())

            pygame.display.update()
            self.main_clock.tick(60)


def main():
    s = Game()
    s.start()


if __name__ == '__main__':
    main()