class Navigation:
    SCREENS = {}
    LAST = ''

    def addScreen(self, screen_name, screen_inst):
        screen = screen_inst()
        self.SCREENS[screen_name] = screen

    def showScreen(self, screen_name):
        self.SCREENS[screen_name].show()
        self.LAST = screen_name

    def changeScreen(self, screen, hiden=True):
        if hiden:
            self.SCREENS[self.LAST].hide()
        self.showScreen(screen)