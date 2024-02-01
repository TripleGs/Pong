from player import Player
from ball import Ball

import pygame
import sys
import os

#Manages the game
class Pong():
    def __init__(self, window_name = "Pong", window_width = 900, window_height = 400):
        pygame.init()
        pygame.display.set_caption(window_name)

        self.game_font = pygame.font.SysFont('Verdana', 60)
        self.font_color = (255,255,255)

        self.window = pygame.display.set_mode((window_width, window_height))

        self.player1 = Player(5, 195)
        self.player2 = Player(880, 195)

        self.ball = Ball(450, 195)

        self.speed = 2
        
        self.running = True

    def draw_background(self):
        self.window.fill((100,100,100))
        pygame.draw.lines(self.window, (255,255,255), True, [(450,0),(450,400)], 2)

    def draw_score(self):
        self.window.blit(self.game_font.render(str(self.player2.score), True, self.font_color), (675,20))
        self.window.blit(self.game_font.render(str(self.player1.score), True, self.font_color), (225,20))

    def draw_players(self):
        self.player1.rect = pygame.draw.rect(self.window, self.player1.color, [(self.player1.x, self.player1.y),self.player1.size])
        self.player2.rect = pygame.draw.rect(self.window, self.player2.color, [(self.player2.x, self.player2.y),self.player2.size])

    def draw_ball(self):
        self.ball.rect = pygame.draw.circle(self.window, self.ball.color, (self.ball.x,self.ball.y), self.ball.size)
        
    def update_window(self):
        self.draw_background()
        self.draw_score()
        self.draw_players()
        self.draw_ball()

    def check_ball_paddle_collision(self, player):
        if self.ball.rect.colliderect(player.rect):
            self.ball.modx *= -1
            if self.ball.y <= player.y+30:
                self.ball.mody = self.speed
            if self.ball.y > player.y +30 and self.ball.y < player.y+60:
                self.ball.mody = -self.speed
            self.speed +=.1

    def check_if_window_closed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def check_key_presses(self):
        key_presses = pygame.key.get_pressed()
        if key_presses[pygame.K_LEFT]:
            if self.player2.y > 0:
                self.player2.y -= 5
        if key_presses[pygame.K_RIGHT]:
            if self.player2.y < 340:
                self.player2.y += 5
        if key_presses[pygame.K_a]:
            if self.player1.y > 0:
                self.player1.y -= 5
        if key_presses[pygame.K_d]:
            if self.player1.y < 340:
                self.player1.y +=5

    def check_if_hit_wall(self):
        if self.ball.y <= 0:
            self.ball.mody *=-1
        if self.ball.y >= 400:
            self.ball.mody *=-1
        self.ball.x -= self.ball.modx
        self.ball.y -= self.ball.mody
        
    def check_if_pass_wall(self):
        if self.ball.x < 0:
            self.ball.x = 450
            self.ball.y = 200
            self.ball.mody = 0
            self.player2.score = self.player2.score+1
            self.speed = 2
        if self.ball.x > 900:
            self.ball.x = 450
            self.ball.y=200
            self.ball.mody = 0
            self.player1.score = self.player1.score+1
            self.speed=2
        
    def check_events(self):
        self.check_if_window_closed()
        self.check_key_presses()
        self.check_ball_paddle_collision(self.player1)
        self.check_ball_paddle_collision(self.player2)
        self.check_if_hit_wall()
        self.check_if_pass_wall()
            
    def run(self):
        while self.running:
            self.update_window()
            self.check_events()
            pygame.display.flip()
        pygame.quit()
