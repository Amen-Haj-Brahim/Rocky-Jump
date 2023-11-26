while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("yellow")
    #pygame.draw.circle(screen, "red", player_pos, 40)
    screen.blit(pygame_icon,player_pos)
    screen.blit(ground,(0,1030))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt*3
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt*3
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()